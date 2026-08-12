---
name: seo-content-brief
description: Produce a writer-ready SEO content brief for a target keyword — search intent, SERP analysis, required subtopics, internal links, entities to cover, and a word-count target grounded in what actually ranks. Use whenever the user mentions a content brief, article outline, blog brief, "what should I write about [keyword]", writing brief, content spec, or hands over a keyword and expects content direction. Also use before drafting any SEO article, even if the user just asks you to "write a post about X".
---

# SEO Content Brief

A brief is a contract with the writer. If it doesn't constrain them, it isn't a
brief — it's a suggestion. Every section below must be specific enough that two
different writers would produce structurally similar articles.

## Inputs

- Target keyword (required)
- Domain (required — needed for internal links and to judge realistic difficulty)
- Secondary keywords, if the user has them
- Business goal for the page: rank, convert, or support (default: ask)

## Step 1 — Read the SERP, don't assume it

Search the target keyword. Record for the top 8 results:

- Page type (guide, listicle, tool, product, forum, video)
- Title format
- Approximate depth and structure
- Publish/update date
- Domain type (does a small site rank? if not, say so)

**Then classify intent** into one of: informational, commercial investigation,
transactional, or navigational. If the SERP is mixed, say which mix and pick the
dominant format. Never write a brief that fights the SERP — if every result is a
listicle, a narrative essay will not rank, regardless of quality.

**Also check:** is there an AI Overview? What does it cite? That tells you the
extractable answer format to build for.

## Step 2 — Assess whether this page should exist

Before briefing, answer honestly:

- Does the site already have a page targeting this? → recommend update, not new
- Can this site realistically compete for this term? → if not, propose a
  longer-tail entry point and say why
- Does this serve the business goal, or just traffic?

A brief that talks the client out of a bad page is worth more than one that
doesn't. Include this as a short "Recommendation" block at the top.

## Step 3 — Build the brief

```
# Content Brief: [Keyword]

## Recommendation
New page / update existing / don't build. One paragraph of reasoning.

## Target & intent
Primary keyword, secondaries, intent classification, SERP format to match.

## Angle
One sentence: why this page deserves to outrank the current #1.
Not "more comprehensive". A real differentiator — original data, practitioner
experience, a tool, a contrarian position, better specificity.

## Audience & stage
Who reads this and what they do next.

## Outline
H1, then every H2 and H3 with a 1–2 line note on what belongs under it.
Mark which section answers the query directly (put it above the fold —
this is what gets extracted into AI answers and featured snippets).

## Must-cover entities & subtopics
Concepts, tools, people, and terms that appear across ranking pages. A page
missing these reads as topically incomplete to both readers and retrieval systems.

## Questions to answer
From People Also Ask, Reddit, and forums. Verbatim phrasing.

## Internal links
3–6 specific URLs from the site, with suggested anchor text and where in the
outline each belongs. Include at least one link *to* a money page.

## External references
Sources worth citing. Prefer primary data and original research.

## Specs
Word count (derived from the ranking set, with the range stated), title tag
(under 60 chars), meta description (under 155), URL slug, schema type.

## What would make this fail
2–3 sentences of honest risk. Thin differentiation, wrong intent, no authority.
```

## Rules

- Word counts come from the SERP, never from a default. State the observed range.
- Every internal link must be a real URL you verified exists on the domain.
- Don't pad the "must-cover" list with obvious terms. If it's in the keyword, it's
  not an insight.
- Never write "write engaging, high-quality content". Say what the section must contain.

---

Built by [Semil Shah](https://semilshah.me) — SEO consultant, Toronto.
→ [Coaching for teams who want to run this themselves](https://semilshah.me/seo-coaching.html)
