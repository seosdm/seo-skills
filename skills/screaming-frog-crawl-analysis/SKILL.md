---
name: screaming-frog-crawl-analysis
description: Analyze a Screaming Frog crawl export (internal_all.csv, and optionally the response codes, page titles, canonicals, directives, and inlinks exports) to produce a technical SEO diagnosis — indexability logic, crawl-depth and orphan analysis, redirect-chain resolution, internal link equity distribution, and a prioritized fix list. Use whenever the user mentions Screaming Frog, a site crawl, a crawl export, "internal_all.csv", technical SEO audit, crawl depth, orphan pages, redirect chains, indexability, or hands over any CSV/export from a crawler and wants technical findings. Also use before any technical audit even if the tool isn't named.
---

# Screaming Frog Crawl Analysis

Screaming Frog gives you 40 columns and 50,000 rows. The skill is knowing which
six columns answer which question, and how to cross-reference exports so the
findings are causal, not just descriptive. A list of "pages with missing titles"
is a filter, not an audit.

## Inputs

Ask which exports the user has. Minimum viable is `internal_all.csv`. The
analysis gets sharper with each additional export:

| Export | Unlocks |
|---|---|
| `internal_all.csv` | Everything below at baseline |
| `all_inlinks.csv` | Real internal link equity + true orphan detection |
| `redirect_chains.csv` | Chain length and loop resolution |
| `canonicals` report | Canonical conflict logic |
| GSC / GA export or a sitemap | Orphan confirmation (crawled-not-in-GSC vs in-GSC-not-crawled) |
| Ahrefs export | Which technical issues sit on pages that actually have links/traffic |

Prioritization is only credible when you can weight issues by whether the
affected page has traffic or links. If the user has GSC or Ahrefs data, get it —
a broken canonical on a zero-traffic page is not a priority and saying so builds trust.

## Step 1 — Run the parser

Use `scripts/analyze_crawl.py` to compute the metrics rather than eyeballing the
CSV. It handles the export's quirks (mixed encodings, the header row, the
Address column as key) and outputs a structured summary. Read the summary, then
reason about it — don't dump the raw table at the user.

```
python scripts/analyze_crawl.py internal_all.csv --inlinks all_inlinks.csv
```

## Step 2 — Indexability, as a logic tree not a checklist

For every URL, resolve indexability in this order. The *first* failing gate is
the real problem; downstream flags are noise.

1. Status 200? → if not, it's a status problem, stop here
2. Indexable per robots directive (not noindex)?
3. Canonical points to self (or intentionally elsewhere)?
4. Not blocked by robots.txt?
5. Reachable by internal links (not orphaned)?
6. In the XML sitemap?

Report indexability as "fails at gate N", not as a pile of independent flags.
A noindexed page with a missing title tag does not have a title-tag problem.

## Step 3 — The five analyses that matter

**Crawl depth.** Bucket pages by click depth from home. Anything past depth 4 is
effectively invisible to crawlers and users. Flag high-value pages (traffic,
links, conversion) sitting deep. The fix is internal linking, not more content.

**Orphans, done properly.** A true orphan = has organic traffic or backlinks but
zero internal inlinks. Cross-reference `all_inlinks` against GSC/Ahrefs. Pages
with no inlinks *and* no traffic aren't orphans, they're dead weight — a
different recommendation (consolidate or remove).

**Redirect chains.** Resolve every chain to its final destination. Flag chains
>1 hop, loops, and redirects that land on 4xx/5xx. Output the find-and-replace
list: source → final 200 destination, so links get repointed at the end target.

**Internal link equity.** From `all_inlinks`, compute inlink count per URL.
Surface the mismatch: money pages with few inlinks, thin/utility pages hoarding
them. This is usually the highest-ROI finding in the whole audit and nobody looks
at it because it requires the inlinks export.

**Duplicate & near-duplicate clusters.** Group by identical/near-identical titles
and H1s. Duplicate titles at scale usually mean a templating or faceted-URL
problem — diagnose the pattern, don't list 400 URLs.

## Step 4 — Output

```
# Technical Crawl Analysis — [domain]
## Verdict
Crawl size, indexable ratio, the one structural problem if there is one.

## Indexability breakdown
Pages by first-failing gate. The number that matters: indexable ÷ total.

## Prioritized findings
Each: what, scale (how many URLs), evidence, business weight (traffic/links
on affected pages), fix, effort. Ranked by (impact × confidence) ÷ effort.

## Redirect remediation list
source → final destination, ready to hand to a dev.

## Internal linking actions
Specific: link [these money pages] from [these high-authority pages].

## Watchlist
Issues that aren't worth fixing now but will grow.
```

## Rules

- Weight every finding by traffic or links when that data exists. An unweighted
  technical audit is a list of chores, not a strategy.
- Diagnose patterns, never paste 400 rows. "Faceted navigation is generating
  duplicate titles across /shop/*" beats 400 duplicate-title URLs.
- Distinguish "crawled but shouldn't be indexed" (correct) from "should be
  indexed but isn't" (the actual problem). They look identical in a filter.
- If a "problem" sits entirely on zero-value pages, say it's not a priority.

---

Built by [Semil Shah](https://semilshah.me) — technical SEO consultant, Toronto.
→ [Fractional SEO engagements](https://semilshah.me/fractional-seo-manager.html)
