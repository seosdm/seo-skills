#!/usr/bin/env python3
"""
analyze_crawl.py — Parse a Screaming Frog internal_all.csv export and compute
the metrics that actually drive a technical audit.

Handles the common export quirks: BOM/encoding, the 'Address' column as the key,
mixed status types, and the optional all_inlinks export for link-equity analysis.

Usage:
    python analyze_crawl.py internal_all.csv
    python analyze_crawl.py internal_all.csv --inlinks all_inlinks.csv
    python analyze_crawl.py internal_all.csv --inlinks all_inlinks.csv --json out.json

Built by Semil Shah — semilshah.me
"""
import argparse
import json
import sys
from collections import Counter, defaultdict


def read_csv(path):
    """Read a Screaming Frog CSV, tolerating encoding issues."""
    import csv
    for enc in ("utf-8-sig", "utf-16", "latin-1"):
        try:
            with open(path, newline="", encoding=enc) as f:
                rows = list(csv.DictReader(f))
            if rows:
                return rows
        except (UnicodeDecodeError, UnicodeError):
            continue
    raise SystemExit(f"Could not read {path} with common encodings.")


def col(row, *names):
    """Return the first matching column value; SF column names vary by version."""
    for n in names:
        for k in row:
            if k.strip().lower() == n.lower():
                return (row[k] or "").strip()
    return ""


def to_int(v, default=0):
    try:
        return int(float(v))
    except (ValueError, TypeError):
        return default


def analyze(rows, inlinks=None):
    total = len(rows)
    out = {"total_urls": total}

    # --- Status codes ---
    status = Counter(col(r, "Status Code") for r in rows)
    out["status_codes"] = dict(status.most_common())

    # --- Indexability logic tree: first failing gate wins ---
    gates = Counter()
    indexable = 0
    for r in rows:
        sc = to_int(col(r, "Status Code"))
        indexability = col(r, "Indexability").lower()
        canonical = col(r, "Canonical Link Element 1", "Canonical")
        address = col(r, "Address")
        if sc != 200:
            gates["1_non_200"] += 1
        elif "non-indexable" in indexability or "noindex" in col(r, "Meta Robots 1").lower():
            gates["2_noindex_directive"] += 1
        elif canonical and address and canonical.rstrip("/") != address.rstrip("/"):
            gates["3_canonicalised_away"] += 1
        else:
            indexable += 1
    out["indexable"] = indexable
    out["indexable_ratio"] = round(indexable / total, 3) if total else 0
    out["first_failing_gate"] = dict(gates)

    # --- Crawl depth ---
    depth = Counter()
    deep_pages = []
    for r in rows:
        d = to_int(col(r, "Crawl Depth"), default=-1)
        if d >= 0:
            bucket = str(d) if d <= 4 else "5+"
            depth[bucket] += 1
            if d >= 5:
                deep_pages.append(col(r, "Address"))
    out["crawl_depth"] = dict(sorted(depth.items()))
    out["pages_depth_5plus"] = len(deep_pages)
    out["sample_deep_pages"] = deep_pages[:15]

    # --- Duplicate titles / H1s ---
    def dupes(field_names):
        seen = defaultdict(list)
        for r in rows:
            v = col(r, *field_names)
            addr = col(r, "Address")
            if v:
                seen[v].append(addr)
        return {v: urls for v, urls in seen.items() if len(urls) > 1}

    dup_titles = dupes(["Title 1", "Title"])
    dup_h1 = dupes(["H1-1", "H1"])
    out["duplicate_title_groups"] = len(dup_titles)
    out["urls_with_duplicate_titles"] = sum(len(v) for v in dup_titles.values())
    out["duplicate_h1_groups"] = len(dup_h1)
    out["sample_duplicate_titles"] = dict(list(dup_titles.items())[:5])

    # --- Missing/weak metadata (indexable pages only) ---
    missing_title = missing_meta = missing_h1 = 0
    for r in rows:
        if to_int(col(r, "Status Code")) != 200:
            continue
        if "non-indexable" in col(r, "Indexability").lower():
            continue
        if not col(r, "Title 1", "Title"):
            missing_title += 1
        if not col(r, "Meta Description 1", "Meta Description"):
            missing_meta += 1
        if not col(r, "H1-1", "H1"):
            missing_h1 += 1
    out["indexable_missing_title"] = missing_title
    out["indexable_missing_meta_description"] = missing_meta
    out["indexable_missing_h1"] = missing_h1

    # --- Internal link equity (needs inlinks export) ---
    if inlinks:
        inlink_count = Counter()
        for r in inlinks:
            dest = col(r, "Destination")
            if dest:
                inlink_count[dest] += 1
        counts = [inlink_count.get(col(r, "Address"), 0) for r in rows]
        orphans = [col(r, "Address") for r in rows
                   if inlink_count.get(col(r, "Address"), 0) == 0
                   and to_int(col(r, "Status Code")) == 200]
        out["internal_links"] = {
            "pages_with_zero_inlinks": len(orphans),
            "sample_zero_inlink_pages": orphans[:15],
            "max_inlinks": max(counts) if counts else 0,
            "median_inlinks": sorted(counts)[len(counts) // 2] if counts else 0,
            "note": "Cross-reference zero-inlink pages against GSC/Ahrefs to "
                    "separate true orphans (have traffic/links) from dead weight.",
        }
    else:
        out["internal_links"] = {"note": "Pass --inlinks all_inlinks.csv for link-equity analysis."}

    return out


def main():
    ap = argparse.ArgumentParser(description="Screaming Frog crawl analyzer")
    ap.add_argument("internal", help="Path to internal_all.csv")
    ap.add_argument("--inlinks", help="Path to all_inlinks.csv (optional)")
    ap.add_argument("--json", help="Write full results to this JSON path")
    args = ap.parse_args()

    rows = read_csv(args.internal)
    inlinks = read_csv(args.inlinks) if args.inlinks else None
    result = analyze(rows, inlinks)

    if args.json:
        with open(args.json, "w") as f:
            json.dump(result, f, indent=2)
        print(f"Wrote {args.json}")

    # Human-readable summary to stdout
    print(f"\n=== Crawl summary: {args.internal} ===")
    print(f"Total URLs crawled:        {result['total_urls']}")
    print(f"Indexable:                 {result['indexable']} "
          f"({result['indexable_ratio']*100:.1f}%)")
    print(f"Status codes:              {result['status_codes']}")
    print(f"First failing gate:        {result['first_failing_gate']}")
    print(f"Crawl depth distribution:  {result['crawl_depth']}")
    print(f"Pages at depth 5+:         {result['pages_depth_5plus']}")
    print(f"Duplicate title groups:    {result['duplicate_title_groups']} "
          f"({result['urls_with_duplicate_titles']} URLs)")
    print(f"Indexable missing title:   {result['indexable_missing_title']}")
    print(f"Indexable missing meta:    {result['indexable_missing_meta_description']}")
    print(f"Indexable missing H1:      {result['indexable_missing_h1']}")
    il = result["internal_links"]
    if "pages_with_zero_inlinks" in il:
        print(f"Pages with 0 inlinks:      {il['pages_with_zero_inlinks']} "
              f"(median inlinks: {il['median_inlinks']})")
    print()


if __name__ == "__main__":
    main()
