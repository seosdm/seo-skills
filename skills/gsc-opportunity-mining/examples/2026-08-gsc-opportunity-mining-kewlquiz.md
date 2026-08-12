# GSC Opportunity Mining — kewlquiz.com

**Data:** Google Search Console export, Web search, last 3 months vs prior 3 months
**Date:** August 2026
**Companion:** the CTR-decay teardown for the same property covers *why clicks fell*.
This document covers *what to do next*.

---

## Coverage — read this before the numbers

`Pages.csv` covers **100%** of site clicks. `Queries.csv` covers **39%** — GSC anonymizes
long-tail queries, and nothing in the export UI warns you.

Every query-level figure below therefore describes 39% of traffic. That is enough to find
opportunities but not enough to size them. Anyone presenting a query-level GSC analysis as
site-wide is overstating by roughly two and a half times.

---

## 1. Striking distance — and why the textbook read is wrong here

**Standard method:** find queries at positions 4–15 with real impression volume, push them
into the top 3.

**Result:** 17 queries, **6,207 impressions, 419 clicks.**

| Query | Impr | Pos | Prev pos | Clicks | CTR |
|---|---|---|---|---|---|
| tmkoc quiz | 2,209 | 6.2 | 4.4 ▼ | 209 | 9.5% |
| bahubali quiz | 459 | 5.3 | 5.7 ▲ | 10 | 2.2% |
| taarak mehta ka ooltah chashmah quiz | 412 | 4.1 | 2.7 ▼ | 49 | 11.9% |
| tmkoc quiz questions | 400 | 7.1 | 7.2 ▲ | 19 | 4.8% |
| tmkoc quiz game | 376 | 6.8 | 3.5 ▼ | 13 | 3.5% |
| who is masterji in paatal lok | 360 | 8.1 | 10.4 ▲ | **0** | 0.0% |
| taarak mehta quiz | 347 | 4.8 | 2.8 ▼ | 42 | 12.1% |
| tarak mehta ulta chashma quiz | 219 | 4.8 | 2.4 ▼ | 28 | 12.8% |
| most loved character in mirzapur | 192 | 6.4 | 7.9 ▲ | 1 | 0.5% |
| tarak mehta quiz | 176 | 3.7 | 2.9 ▼ | 33 | 18.8% |

**Two things a naive striking-distance list gets wrong on this data.**

**These queries are not climbing toward the top 3 — they're falling away from it.** Every
high-value quiz query in the set moved *down*: 4.4→6.2, 3.5→6.8, 2.8→4.8, 2.4→4.8. They
were already top-3 and lost ground. That inverts the work. "Optimize the page to push it
up" is the wrong prescription for a page that was recently higher — the question is what
changed, not what to add.

**Several entries can never convert regardless of position.** "who is masterji in paatal
lok" *improved* from 10.4 to 8.1 and still earned **zero clicks** on 360 impressions. Same
for "old song emoji" (165 impressions, position 8.3, zero clicks) and "most loved character
in mirzapur" (192 impressions, one click). These are factual one-line-answer queries
resolved in the SERP. Better ranking produces more zero-click impressions.

**Filtered list — actual opportunity:** strip the informational zero-click cluster and the
real striking-distance set is the six quiz queries, worth roughly **3,700 impressions**
currently earning 374 clicks. The work is recovery of lost position on existing top-3
terms, not new optimization.

---

## 2. Cannibalization — one confirmed pair

| Page | Pos | Impressions | Clicks |
|---|---|---|---|
| `/quiz/taarak-mehta-ka-ooltah-chashmah-quiz/` | 6.5 | 10,819 | 734 |
| `/quiz/taarak-mehta-ka-ooltah-chashmah-quiz-to-find-out/` | 12.8 | 441 | 33 |

Two pages, same show, same quiz intent, near-identical slugs. The second is a duplicate
competing with the site's single most valuable page — which is itself down from position
5.83 and has lost half its CTR.

**Action:** consolidate. Redirect the `-to-find-out` variant into the primary, or merge its
questions in. This is the highest-confidence, lowest-effort item in this document.

**Method caveat that matters.** The standard GSC UI export does **not** include the
query × page dimension — `Queries.csv` and `Pages.csv` are separate tables with no join
key. So this is a *candidate* identified from slug similarity plus overlapping position and
impression profiles, not proof. Confirming true cannibalization requires the Search Console
API, or filtering by page in the UI and comparing query sets.

The clustering also produces false positives, and saying so is part of the method: a token
match on "find" grouped 71 unrelated pages purely because the site's URL convention is
`...take-this-quiz-to-find-out`. Automated cannibalization detection needs a human pass.

---

## 3. CTR underperformance

Covered in depth in the companion teardown. In summary: CTR collapsed at positions 3–5 and
held or improved at 6–10 — the signature of something occupying the top of the SERP rather
than a general ranking decline. Site-wide CTR fell 6.57% → 4.88% while impressions rose
34.5%.

The relevant point for opportunity mining: **title and description testing on the top five
quiz pages is the highest-leverage remaining lever.** When an answer surface sits above
you, the snippet has to earn the click on its own merits.

---

## 4. Page decay

| Page | Impr prior → now | Clicks prior → now | CTR |
|---|---|---|---|
| `/quiz/taarak-mehta-ka-ooltah-chashmah-quiz/` | 5,646 → 10,819 | 757 → **734** | 13.4% → 6.8% |
| `/quiz/doraemon-quiz-which-character-are-you/` | 480 → 459 | 10 → 7 | 2.1% → 1.5% |
| `/quiz/how-well-do-you-know-the-world-of-dark...` | 318 → 289 | 47 → 40 | 14.8% → 13.8% |

The flagship is the decay story: impressions nearly doubled, clicks fell, CTR exactly
halved, position moved only 5.83 → 6.49. Position explains a fraction of a halving, not
the whole of it.

Note the counter-example in the same table — the "Dark" quiz holds 13.8% CTR at position
8.9, better than the flagship manages at 6.5. Whatever is suppressing the flagship's SERP
is not affecting every page equally, which is itself diagnostic and worth a manual SERP
check on both.

---

## 5. Intent mismatch

**33% of query-level impressions sit in a permanently zero-click cluster** — 343 of 603
query rows, 3,198 impressions, zero clicks.

The pattern is consistent: factual entity questions about TV shows ("who is masterji in
paatal lok", "cast of paatal lok masterji", "masterji paatal lok") ranking at positions
8–10 for a quiz site.

The page ranks because it contains the entity. The searcher wants a fact and gets offered a
quiz. No CTR work fixes that — the intent is wrong at the root.

**Action: stop measuring these pages on clicks.** They have a structural ceiling near zero.
Either accept them as brand-surface impressions and report them separately, or rebuild them
to answer the question first and offer the quiz second. What you cannot do is keep counting
their impressions as growth — which is exactly what the site-wide "+34.5% impressions"
headline does.

---

## Prioritized actions

1. **Consolidate the duplicate TMKOC quiz pages.** Highest confidence, lowest effort, and
   it's diluting the site's most valuable asset.
2. **Manual SERP check on the top five quiz queries.** Record what sits above position 3.
   Everything else here is inference until that's done.
3. **Title and description testing on the flagship.** CTR halved at near-constant position;
   the snippet is the remaining lever.
4. **Re-segment reporting** so the zero-click informational cluster is separated from quiz
   pages. Currently it drags the site-wide CTR average down and hides that quiz delivery is
   healthier than the headline suggests.
5. **Do not chase the informational cluster.** 33% of impressions, structurally unwinnable.

---

## What would change these conclusions

A year-over-year comparison instead of quarter-over-quarter. The current window is roughly
May–August against February–May, and a TV-quiz site plausibly tracks broadcast cycles.
Seasonality is not ruled out and every trend statement here inherits that caveat.
