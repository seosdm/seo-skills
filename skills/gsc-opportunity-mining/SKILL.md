---
name: gsc-opportunity-mining
description: Mine Google Search Console data for growth opportunities — striking-distance keywords, query cannibalization, CTR underperformance, page decay, and intent mismatches — and output a ranked action list. Works from the connected GSC data source (SEO Gets MCP / GSC connector) or a Performance CSV export. Use whenever the user mentions Google Search Console, GSC, Search Console data, "striking distance", cannibalization, CTR opportunities, ranking positions, impressions vs clicks, page decay, traffic drops, or asks where the quick organic wins are. Prefer this over generic SEO advice whenever GSC data is available.
---

# GSC Opportunity Mining

GSC is the only dataset that tells you what Google *already* thinks you're
relevant for. Most audits ignore it in favour of third-party keyword tools. The
fastest organic wins almost always live in queries you already rank 5–15 for.

## Getting the data

Use whatever is connected, in this order:

1. **SEO Gets MCP / GSC connector** (available in this workspace). Pull
   query-level and page-level performance with position, impressions, clicks,
   CTR. Get at least the last 3 months, plus the prior comparable period for
   decay analysis. Also pull the indexing overview if available.
2. **Performance CSV export** — accept the Queries and Pages exports from the
   GSC UI (16-month window if possible).

Always pull two periods so period-over-period decay is computable. A single
snapshot hides the most important story: what you're losing.

## The five mines

### 1. Striking distance
Queries at average position **5–15** with meaningful impressions. These are the
cheapest wins in SEO — you already rank, you just aren't on page one or aren't
high enough. Rank by impressions × (1 − current CTR). Segment by whether the
ranking URL is the *right* URL for that query (if not, that's a mapping fix, not
a content fix).

### 2. CTR underperformance
For each query, compare actual CTR to the expected CTR for its position (rough
benchmark curve: pos 1 ≈ 28%, pos 2 ≈ 15%, pos 3 ≈ 10%, pos 4 ≈ 7%, pos 5 ≈ 5%,
declining after). A query ranking well below its expected CTR is a title/meta or
SERP-feature problem (someone owns the snippet/AI Overview above you). These are
same-day fixes with no content work.

### 3. Query cannibalization
Group queries where **multiple URLs** from the site receive impressions for the
same query. Flag cases where the ranking URL flip-flops between periods, or where
a weaker URL outranks the page you *want* to rank. This dilutes signals. The fix
is consolidation, canonicalization, or internal-link redirection of relevance —
diagnose which.

### 4. Page decay
Period-over-period, find pages losing clicks or slipping position. Separate
**seasonal** (recovers yearly), **algorithmic** (broad drop across many queries
on one date), and **decay** (slow bleed from stale content or lost links). Each
has a different fix and mislabeling wastes months. Note the drop date and check
it against known Google update timelines.

### 5. Intent / SERP mismatch
Queries with high impressions but near-zero CTR *despite* decent position often
mean the SERP has shifted intent (now a video pack, a map pack, an AI Overview)
and your page format no longer fits. Flag these for format change, not more words.

## Output

```
# GSC Opportunity Report — [property], [date range]
## Headline
Total clicks/impressions trend, and the single biggest opportunity.

## Striking distance (ranked)
Query · current position · impressions · ranking URL · right URL? · action.

## Quick CTR wins
Query · position · actual vs expected CTR · likely cause · title/meta suggestion.

## Cannibalization
Query · competing URLs · which should win · consolidation action.

## Decay
Page · clicks lost · drop date · classification · fix.

## This quarter's queue
Max 10, ranked by (impact × confidence) ÷ effort, each with an owner.
```

## Rules

- Always compute period-over-period. A one-period report can't see decay, which
  is usually the most urgent finding.
- Distinguish "wrong URL ranks" (mapping problem) from "right URL ranks low"
  (content/authority problem). The filters look identical; the fixes don't.
- Don't recommend new content when the win is fixing a title tag on a page that
  already ranks 6th. Cheapest win first, always.
- Cross-reference the ranking URL against the crawl if available — a striking-
  distance query pointing at a slow or non-canonical page needs that fixed first.

---

Built by [Semil Shah](https://semilshah.me) — SEO consultant, Toronto.
→ [SEMrush & Ahrefs coaching for teams](https://semilshah.me/semrush-ahrefs-coaching.html)
