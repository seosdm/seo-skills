# seo-skills

The core SEO operating stack I run for clients, as Claude skills. Six skills
across the stages of an SEO cadence, plus the orchestration layer that runs them
on a schedule.

| Skill | Stage | What it does |
|---|---|---|
| [`screaming-frog-crawl-analysis`](skills/screaming-frog-crawl-analysis) | Technical | Indexability logic tree, crawl depth, orphans, redirect chains, internal link equity. Ships with a runnable Python parser. |
| [`gsc-opportunity-mining`](skills/gsc-opportunity-mining) | Find | Striking-distance queries, CTR gaps, cannibalization, page decay. Cheapest win first. |
| [`backlink-keyword-gap`](skills/backlink-keyword-gap) | Links | Backlink profile + competitor keyword gap via Ahrefs. Conservative on disavow. |
| [`seo-content-brief`](skills/seo-content-brief) | Ship | Writer-ready briefs grounded in the live SERP, not a template. |
| [`local-seo-gbp-audit`](skills/local-seo-gbp-audit) | Local | Google Business Profile audit, category-first, grid-aware. |
| [`seo-operating-cadence`](skills/seo-operating-cadence) | Track | The conductor — schedules the others, keeps runs read-only, writes the weekly narrative. |

## How to use
Each folder under [`skills/`](skills/) has a `SKILL.md`. Copy any into a Claude
Project, or clone the whole repo to run the full cadence. The GSC and backlink
skills connect to live data (a GSC connector and Ahrefs); the crawl skill reads
a Screaming Frog export.

> **Note:** never commit a real client's GSC or Ahrefs export to a public repo.
> Anonymize or synthesize every example.

## Who made this
[Semil Shah](https://semilshah.me) — SEO consultant, Toronto. 15 years of search.
→ [SEO Coaching](https://semilshah.me/seo-coaching.html) · [SEMrush & Ahrefs Coaching](https://semilshah.me/semrush-ahrefs-coaching.html)

MIT licensed.
