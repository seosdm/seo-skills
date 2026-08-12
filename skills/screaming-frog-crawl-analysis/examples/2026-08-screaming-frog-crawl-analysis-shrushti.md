# Technical SEO Audit — shrushti.com

**Crawl:** Screaming Frog, 5 August 2026, 33m 45s
**Scope:** 1,495 URLs encountered · 642 internal · 425 indexable · 531 internal HTML
**Companion:** [AI Visibility Audit — Shrushti Digital](../../ai-visibility-audit/examples/2026-08-shrushti-ai-visibility-audit.md)

---

## Start here: the biggest number in this crawl is wrong

Screaming Frog's top finding, flagged **High** priority:

> **Response Codes: Internal No Response — 38 URLs**

38 internal URLs returned `Connection Timeout`, with **40,603 internal inlinks**
pointing at them. And they are not obscure pages:

| Inlinks | URL |
|---|---|
| 2,886 | `/local-seo-packages/` |
| 2,585 | `/glossary/` |
| 2,490 | `/gbp-audit-services/` |
| 2,480 | `/outsource-keyword-research/` |
| 2,473 | `/ppc/` |
| 2,467 | `/link-audit/` |
| 2,459 | `/google-penalty-removal-recovery/` |
| 2,074 | `/white-label-link-building-services/` |

Every commercial page on the site, apparently dead. It would be reasonable to send
that to a client as a P0 emergency.

**It isn't real.** Three of those URLs were fetched independently, live:

| URL | Result |
|---|---|
| `/white-label-link-building-services/` | 200, full page — "White Label Link Building Services For Agencies and Resellers" |
| `/local-seo-packages/` | 200, full page — pricing tiers at $329 / $499 / $699 |
| `/link-audit/` | 200, full page — "Link Audit Service", $399 |

The pages are fine. The server throttled the crawler.

### Why this matters more than the finding itself

A crawler hitting a site with multiple threads for 33 minutes gets rate-limited. The
timeouts are a property of *how the crawl was run*, not of the site. Report them as
outages and you burn credibility permanently — and the client goes and pays a developer
to investigate pages that were never broken.

**Two real consequences follow, and they're worth acting on:**

1. **The crawl data for those 38 URLs is missing, not clean.** No titles, no headings,
   no schema, no word counts. Roughly 7% of internal URLs — and disproportionately the
   commercial ones — were never actually audited. Anything below is silent on them.
2. **The server does drop connections under load, and Googlebot also crawls in
   parallel.** Not proven harmful here, but worth checking Search Console's Crawl Stats
   for host-status errors. If Googlebot is seeing the same throttling, that's a genuine
   crawl-budget problem.

**Action:** re-crawl at 1–2 threads with a 0.5s delay to get clean data on those 38
URLs. Until then, treat this audit as covering 604 of 642 internal URLs.

There's a knock-on artifact too: *Sitemaps: Non-Indexable URLs in Sitemap — 33 URLs* is
the same 38 pages seen a second way. Both counts collapse together on a clean re-crawl.

---

## What is actually broken

### P1 — Two pages have malformed HTML document structure

`/answer-engine-optimization/` and `/generative-engine-optimization-services/` are the
only two pages on the site flagged for **all three** of:

- Multiple `<head>` tags
- Multiple `<body>` tags
- Page title outside `<head>`

Independently verified: both pages render their **entire navigation menu twice**, and
the footer link blocks repeat. The document is being emitted twice inside one response —
a template or page-builder bug, not a content issue.

**Why it's P1:** a `<title>` outside `<head>` may be ignored by parsers entirely. Two
`<head>` sections means whatever canonical, meta description, and JSON-LD sit in the
second one are in undefined territory. Both pages are also flagged **Structured Data:
Missing**, which is likely a *consequence* of the malformed structure rather than a
separate problem.

These are Shrushti's AI-search service pages — GEO packages listed at $1,500–$3,000+/mo.
The pages selling AI-search optimization are the two pages on the site that AI parsers
will struggle with. Fixing them is a template fix, probably an hour, and it's the
highest-value hour on this list.

### P1 — Redirect loop

`/glossary/above-the-fold/` returns 301 → `/glossary/above-the-fold/`. It redirects to
itself. The page is unreachable by any crawler or user, and has 3 internal links
pointing into it.

### P1 — Internal links to 404s

11 internal 4xx. After removing false positives, the real ones are commercial:

| URL | Inlinks |
|---|---|
| `/content-marketing/` | 5 |
| `/technical-seo-consultant/` | 4 |
| `/ecommerce-consultant` | 1 |

Note `/ecommerce-consultant` has no trailing slash while the site's convention is
trailing-slash — likely a typo'd link rather than a deleted page. Also
`/hire-our-technical-seo-experts//hire-our-technical-seo-experts/` returns 403 — a
doubled path, another malformed link.

### P2 — The glossary is the most valuable asset on the site and it's buried

129 glossary URLs are missing structured data. The glossary also contains the deepest
pages in the crawl:

| Depth | URL |
|---|---|
| 13 | `/glossary/query-fan-out/` |
| 12 | `/glossary/automated-internal-linking/` |
| 11 | `/glossary/canonical-urls/` |
| 10 | `/glossary/few-shot-learning/` |

239 pages sit at crawl depth 4+. Thirteen clicks from the homepage is functionally
invisible — it gets crawled rarely and passes almost no internal authority.

**This connects directly to the AI visibility finding.** Definitional content is the
single most citable asset type for AI answer engines. Shrushti has 129 definitional
pages, with no `DefinedTerm` schema, buried up to 13 clicks deep. That is a large
latent asset being wasted.

Two other glossary problems: `/glossary/canonical-url/` and `/glossary/canonical-urls/`
are duplicate-title near-duplicates of each other (consolidate), and `/glossary/blog/`
contains **Lorem Ipsum placeholder text** — an unfinished page live in production.

### P2 — Organization schema has a `foundingDate` error

Flagged under Google Organization validation.

This is small and specific and matters more than it looks. The AI visibility audit
called out *factual drift* — models getting founder, location or founding year wrong —
as a root cause to watch, and prompt N3 tests exactly that. `foundingDate` is one of the
primary signals that defines the entity. A validation error there means the one
machine-readable statement of when the company started is broken.

Also broken: 4 rich-result validation errors across `/service-page-seo/` and three
`/career/` pages, mostly JobPosting fields (`validThrough`, `employmentType`,
`applicantLocationRequirements`).

### P2 — Orphan pages, including pages that earn traffic

456 orphan URLs. Most are noise — UTM-tagged variants, career listings — but **7 have
Search Console traffic and zero internal links**:

- `/white-label-seo-canada/` ← a commercial geo page, earning clicks, orphaned
- `/seoblog/web-2-0-sites/`
- `/seoblog/how-to-outsource-local-seo/`
- plus 4 `/career/` pages

A page ranking with no internal links is ranking despite the site, not because of it.
`/white-label-seo-canada/` is the one to fix first.

### P3 — Titles, and a note on the content flags

64 titles over 561px, 54 over 60 characters, 14 under 30. Standard housekeeping —
but see the CTR argument in the companion GSC teardown: when an answer surface sits
above you, the snippet is what earns the click. Title work is worth more than it used
to be.

---

## What to ignore

Half the value of an audit is refusing to bill for the noise.

| Flagged | Reality |
|---|---|
| **Internal Blocked by Robots.txt — 18** | All `/wp-includes/` and `/wp-admin/` assets, **0 inlinks each**. Standard WordPress. Ignore. |
| **`/cdn-cgi/l/email-protection` 404, 438 inlinks** | Cloudflare email obfuscation. Never a real URL. The scariest-looking 404 in the crawl and a complete false positive. |
| **Directives: Noindex — 147** | 106 are `/ss-admin/`, plus author archives, blog pagination, sitemap XML. Correct behavior, not a problem. |
| **Spelling 517 / Grammar 411** | Screaming Frog's dictionary flags SEO jargon as misspellings. Sample 20 before touching. |
| **Reduce Unused JS 394 / CSS 105** | Real but generic WordPress theme bloat. Not the constraint on this site. |

That's roughly 1,600 flagged "issues" that need no action. The real list is about a
dozen items.

---

## How this fits with the other two audits

Three data sources, one story:

**AI visibility** — absent from all 32 results across four unbranded discovery prompts;
present in 5 of 9 branded results.

**This crawl** — the definitional content that AI engines cite most readily (129
glossary pages) has no schema and sits up to 13 clicks deep. The entity's own
`foundingDate` fails validation. The two pages selling AI-search services have
malformed HTML.

**GSC (kewlquiz, separate property)** — the CTR-decay pattern showing what happens to
clicks when answer surfaces expand above organic results.

The technical work here doesn't fix the AI visibility problem — that was diagnosed as a
*placement* problem, and it still is. Being in the cited listicles is what moves the
unbranded number.

But the glossary and the schema are the part Shrushti *does* control. Right now the
site's most citable asset is unschema'd and buried, and the entity definition has a
validation error. Placement gets you cited; a clean, well-defined entity is what
determines whether the citation says the right thing about you.

---

## Priority order

1. Fix the duplicated document structure on the two AEO/GEO pages — template bug, ~1hr
2. Fix the `/glossary/above-the-fold/` self-redirect
3. Repoint the 3 internal links hitting 404s; fix the doubled-path 403
4. Fix `foundingDate` in Organization schema
5. Internally link `/white-label-seo-canada/`
6. Add `DefinedTerm` schema to the glossary and raise it out of depth 10+
7. Delete or finish `/glossary/blog/` (Lorem Ipsum in production)
8. Consolidate `/glossary/canonical-url/` and `/glossary/canonical-urls/`
9. Re-crawl at 1–2 threads to get clean data on the 38 unaudited URLs
10. Check Search Console Crawl Stats for Googlebot host errors

Items 1–5 are a single afternoon.

---

## Method note

This audit covers 604 of 642 internal URLs. The 38 that timed out are unaudited, not
clean — and they are disproportionately the commercial pages. Any claim in this document
is silent on them until the re-crawl.

Stating that plainly is the point. An audit that reports 1,600 issues and doesn't
mention that 7% of the site went unfetched is worse than one that reports a dozen and
says what it couldn't see.
