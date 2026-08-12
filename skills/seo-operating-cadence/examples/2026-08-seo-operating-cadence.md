# SEO Operating Cadence — worked example

**Account:** the operating rhythm actually run at Shrushti Digital Marketing
**Date:** August 2026
**Scale:** ~50 client folders across four agency spaces in ClickUp

---

## What this documents

A real cadence, not a proposed one. Six recurring activities the agency already runs,
mapped to data sources, cadences, owners and destinations — and then the honest audit of
where the rhythm has gaps.

The value of writing a cadence down is rarely the schedule. It's discovering which
activities have no data source wired to them, and which produce output nobody routes
anywhere.

---

## The stated rhythm

As described by the practitioner, unedited:

1. Weekly comparison crawl
2. Monthly GSC review
3. Monthly competitor review — presence and content strategy
4. Conversion data from Google Analytics, plus KPIs from GSC
5. Branded search tracking in GSC
6. Prompt visibility from various external tools

Six activities. Two weekly-or-monthly cycles. Below, each is wired up.

---

## The cadence, wired

| # | Activity | Cadence | Skill | Data source | Mode | Output goes to |
|---|---|---|---|---|---|---|
| 1 | Comparison crawl | **Weekly** · Mon | `screaming-frog-crawl-analysis` | Screaming Frog, crawl-over-crawl diff | read-only | Dev tickets → ClickUp `TS - [client]` |
| 2 | GSC review | **Monthly** | `gsc-opportunity-mining` | GSC / SEO Gets MCP | read-only | Content briefs → `CO - [client]`; quick wins → `TS -` |
| 3 | Competitor presence & content | **Monthly** | *(no skill yet — gap)* | Manual + SERP | read-only | Strategy note → account plan |
| 4 | GA conversions + GSC KPIs | **Monthly** | *(no skill yet — gap)* | GA4 + GSC | read-only | Client report → `RE - [client]` |
| 5 | Branded search tracking | **Monthly** | `gsc-opportunity-mining` (branded filter) | GSC, brand-term regex | read-only | Trend line in client report |
| 6 | AI prompt visibility | **Monthly** | `ai-visibility-audit` | External tools + manual engine runs | read-only | Visibility section of client report |
| — | **Weekly narrator** | **Weekly** · Mon 08:00 | this skill | all of the above | read-only | Email / Slack, per account |

**Why the crawl is weekly and everything else is monthly.** Technical state changes on
deploy — a botched release can noindex a template on a Tuesday, and a monthly crawl finds
it three weeks late. Ranking, conversion and competitor signals move on a scale of weeks;
sampling them weekly produces noise that trains people to ignore the report. Cadence should
match how fast the underlying signal actually moves, and these six activities do not move
at the same speed.

---

## Gaps this exercise surfaced

Writing the rhythm down exposed three things the rhythm doesn't currently have.

**Activities 3 and 4 have no skill behind them.** Competitor review and the GA+GSC KPI roll-up
are done manually every month across ~50 accounts. They are the two most repetitive items
in the list and the two with no automation — which is the usual pattern, because manual
work doesn't announce itself the way a missing tool does.

**No skill owns backlinks in the stated rhythm.** `backlink-keyword-gap` exists in the
stack but appears nowhere in the six activities. Either it runs and wasn't mentioned, or a
build-out asset is going unused. Worth resolving explicitly rather than leaving ambiguous.

**Activity 6 depends on external tools and manual engine runs.** Prompt visibility is the
newest and least systematized item. The AI visibility audit for one brand needed 28 prompts
across four engines to produce a defensible answer; at 50 accounts that does not scale
manually. This is the highest-value automation target in the list, and also the one where
"we check it sometimes" most easily masquerades as a process.

---

## Read-only by default

Every scheduled run above is marked **read-only**, and that is a deliberate constraint
rather than a limitation.

A report that recommends a redirect is safe to generate unattended. A task that *ships* a
redirect is not. The write step stays manual and reviewed — an unattended process that
edits canonicals on a live client site is how an agency loses an account and a reputation
in the same week.

Where a connector can write — ClickUp task creation, for instance — the prompt names the
write action explicitly and a human approves before it lands.

---

## The weekly narrator

The keystone. Every Monday, before anyone asks:

```
# [Client] — SEO, week of [date]

## The one thing
Single most important change. One sentence.

## What moved
Position, impression and click deltas vs last week. Material only.
The *why* behind the top three moves, not just the numbers.

## What the cadence surfaced
Whatever this week's scheduled runs flagged, filtered to what matters.

## Next week's three priorities
Ranked, each with an owner. No more than three.
```

**Three priorities, never thirty.** The narrator's product is judgment — deciding what to
ignore. A report listing everything is operationally identical to no report, because the
reader has to do the triage the report was supposed to do.

An honest quiet week says "nothing material this week." Manufactured urgency destroys the
credibility that makes the report worth sending.

---

## Routing — matching destination to reader

Output goes where the reader already works, never to a dashboard they must remember to open.

| Output | Destination | Why |
|---|---|---|
| Client narrative | Email or Slack | The client reads it without logging in |
| Dev tickets from crawl findings | ClickUp `TS - [client]` | Where the dev already looks |
| Content briefs from GSC gaps | ClickUp `CO - [client]` | Writer's queue |
| Link opportunities | ClickUp `LB - [client]` | Outreach queue |
| Internal exec view | `agency-ops-clickup` weekly report | Rolls across all accounts |

The workspace already uses a `TS / LB / CO / RE / OP / OB / WD` list-prefix convention per
client folder, which makes routing mechanical rather than a judgment call each time. That
convention is doing more work than it looks like — it's what lets a cadence scale past a
handful of accounts.

---

## Scaling honesty — the part most cadence documents omit

This cadence is documented for ~50 client folders. Six activities × 50 accounts is 300
monthly runs plus 50 weekly crawls plus 50 weekly narrators.

**That does not run manually, and pretending otherwise is how cadences quietly die.**

Three implications worth stating rather than discovering:

**Tier the accounts.** Not every client earns the full rhythm. A stable site with no
publishing needs a quarterly crawl, not a weekly one. Reserve the full cadence for accounts
where the retainer justifies it, and say which tier each account sits in.

**Stagger the schedule.** Fifty crawls firing Monday at 08:00 will exhaust API quota and
produce fifty reports nobody reads by Wednesday. Spread them across the week.

**Scheduled tasks fire while the machine is awake.** For genuine always-on cadence this
needs an always-on machine. Better to say that than let someone discover it via a missed
Monday report.

---

## Rules

- Cadence matches signal speed. Weekly for deploy-sensitive technical state; monthly for
  everything that moves on a scale of weeks.
- Read-only unless a human promotes the task. Mode stated on every scheduled run.
- The narrator filters, it does not list. Judgment is the product.
- Never schedule an unattended write to a client's live site.
- A quiet week is reported as a quiet week.
- If an activity has no data source wired to it, it is not part of the cadence — it is an
  intention. Write it in the gaps section, not the schedule.
