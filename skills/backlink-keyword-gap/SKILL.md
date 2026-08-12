---
name: backlink-keyword-gap
description: Run a backlink profile audit and competitor keyword-gap analysis using Ahrefs (or SEMrush / a CSV export) — link velocity and quality, anchor-text risk, lost/broken link reclamation, referring-domain gap vs competitors, and a keyword-gap-to-content roadmap. Use whenever the user mentions backlinks, link building, Ahrefs, SEMrush, referring domains, anchor text, toxic/spam links, link gap, keyword gap, competitor keywords, "what are competitors ranking for that we aren't", domain authority, or link reclamation. Prefer this over generic link advice whenever link/keyword data is available.
---

# Backlink Profile & Keyword Gap

Two analyses that share a data source and a purpose: find where competitors are
beating you on authority and coverage, and turn it into a prioritized roadmap.
"Build more links" is not a strategy. "These 12 referring domains link to all
three competitors and none to you" is.

## Getting the data

1. **Ahrefs MCP** (connected in this workspace). Pull for the client and each
   competitor: referring domains, backlink profile, anchor-text distribution,
   organic keywords, and the content/keyword gap. Use the tool's own gap
   endpoints where available rather than re-deriving them.
2. **SEMrush / Ahrefs CSV exports** — accept exported referring domains, anchors,
   and keyword-gap files.

Always run competitors through the *same* pull so comparisons are apples-to-apples.

## Part A — Backlink profile audit

**Link velocity & trend.** New vs lost referring domains over time. A rising
lost-link trend is often the hidden cause of a slow traffic decline — pair this
with the GSC decay analysis if available. Sudden spikes in new links can signal a
negative-SEO attack or a low-quality campaign; investigate before celebrating.

**Quality distribution, not count.** Bucket referring domains by authority tier
and topical relevance. 500 links from irrelevant low-authority domains are worth
less than 20 relevant editorial ones. Report the shape of the profile, not the
headline number.

**Anchor-text risk.** Distribution across branded / naked-URL / generic /
exact-match / partial-match. An over-concentration of exact-match commercial
anchors is a footprint that invites a penalty. Flag the ratio and whether it
looks organic.

**Toxic / spam review.** Identify genuinely manipulative or spam links (PBN
footprints, link-farm patterns, irrelevant foreign-language bulk links). Be
conservative: most "toxic link" panic is unwarranted and disavowing good links
does real harm. Recommend disavow only for clear, deliberate manipulation, and
say so explicitly. Google mostly ignores junk links on its own.

**Reclamation opportunities.** Two fast wins: (1) *lost links* worth winning back
(a chase email or a fixed redirect), and (2) *unlinked brand mentions* — sites
that name the brand without linking. Both convert faster than cold outreach.
Draft the outreach for the top opportunities.

## Part B — Keyword & content gap

**Referring-domain gap.** Domains linking to 2+ competitors but not the client.
These are pre-qualified, reachable link targets — they already link within the
niche. This is the single most actionable link-building output; rank by how many
competitors each links to.

**Keyword gap.** Terms where competitors rank in the top 10–20 and the client
doesn't rank at all (or ranks past 20). Filter to commercially or topically
relevant terms — don't drown the roadmap in irrelevant head terms nobody will win.

**Cluster into a roadmap.** Group gap keywords by topic into content clusters,
each with: the pillar page, supporting articles, the competitor(s) currently
winning it, and realistic difficulty given the client's authority. Sequence by
(traffic potential × relevance) ÷ difficulty. This is the bridge from data to a
quarter of content work.

## Output

```
# Backlink & Gap Analysis — [domain] vs [competitors]
## Verdict
Authority position vs competitor set; the single biggest lever.

## Backlink profile
Velocity trend · quality distribution · anchor risk · toxic assessment (with
an explicit "disavow / don't disavow" call and reasoning).

## Reclamation (fast wins)
Lost links + unlinked mentions, with drafted outreach for the top targets.

## Referring-domain gap
Ranked list of domains linking to competitors but not the client.

## Keyword gap → content roadmap
Clusters, ranked, each with pillar + supporting pieces and difficulty.

## Sequenced plan
What to do in months 1–3, links and content interleaved.
```

## Rules

- Report link profiles by quality and relevance, never by raw count.
- Be conservative on disavow. State "do not disavow" plainly when that's correct
  — reflexive disavowing is a common, damaging mistake.
- The referring-domain gap is usually the highest-value output. Lead with it for
  link-building engagements.
- Filter keyword gaps for relevance and winnability. A roadmap the client can't
  realistically rank for is worse than a shorter honest one.
- When GSC decay data exists, connect lost links to the pages that lost traffic.
  Causation beats two separate reports.

---

Built by [Semil Shah](https://semilshah.me) — SEO consultant, Toronto.
→ [SEMrush & Ahrefs coaching](https://semilshah.me/semrush-ahrefs-coaching.html)
