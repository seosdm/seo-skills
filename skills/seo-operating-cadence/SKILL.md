---
name: seo-operating-cadence
description: Orchestrate a full SEO operating rhythm — decide which audit/analysis skill runs on which cadence, wire each to its data source, route the output to the right destination, and produce a single weekly narrative that ties it together. Use whenever the user wants a recurring SEO cadence, a "set it and forget it" workflow, scheduled audits, a weekly SEO report that writes itself, an SEO command center, or to chain multiple SEO skills into one operating system rather than running them ad hoc. Also use when someone asks how to automate or schedule their SEO work.
---

# SEO Operating Cadence

The individual skills in this stack each answer one question well. This one
decides *when* each runs, *what data* it reads, *where the output goes*, and how
it all rolls up into one narrative a client or a founder will actually read.

The point isn't automation for its own sake. It's that SEO is a rhythm, not a
project — and the failure mode at an agency is a skill that exists but never gets
run because nobody scheduled it.

## The rhythm

Four stages, mapped to the deep skills in this repo, each on its natural cadence.
Don't run everything weekly — that produces noise nobody reads and burns data
quota. Cadence is chosen to match how fast each signal actually moves.

| Stage | Skill | Cadence | Data source | Mode |
|---|---|---|---|---|
| **Find** | `gsc-opportunity-mining` | Weekly · Mon | GSC (SEO Gets MCP) | read-only |
| **Find** | `backlink-keyword-gap` (gap half) | Quarterly + on-demand | Ahrefs MCP | read-only |
| **Ship** | `seo-content-brief` | Weekly · Tue (from GSC gaps) | GSC + SERP | read-only |
| **Ship** | `screaming-frog-crawl-analysis` | Monthly (fresh crawl) | SF export | read-only |
| **Links** | `screaming-frog` (internal-link half) | Monthly | SF inlinks export | read-only |
| **Links** | `backlink-keyword-gap` (profile half) | Monthly | Ahrefs MCP | read-only |
| **Local** | `local-seo-gbp-audit` | Monthly (local clients) | GBP + Maps | read-only |
| **Visibility** | `ai-visibility-audit` | Monthly | web + AI engines | read-only |
| **Track** | *this skill's narrator* | Weekly · Mon 8am | all of the above | read-only |

Adjust to the account. A stable enterprise site needs less frequency than a
site actively publishing. State the cadence you chose and why.

## Read-only by default — and why the discipline matters

Every scheduled run is **read-only** unless a human explicitly promotes it. A
report that recommends a redirect is safe to run unattended; a task that *ships*
a redirect is not. Keep the write step manual and reviewed. If a connector is
write-capable (e.g., a CMS MCP), the prompt must name the write action
explicitly and the human approves before it lands. Publishing "SEO that ships
fixes autonomously" and then breaking a client's canonicals unattended is how you
lose the account and the reputation. Recommend, review, then ship.

## Scheduling it (the mechanics)

Claude's scheduled-task feature is the scheduler; the connectors are the data.
For each skill above:

1. Create a scheduled task named for the skill and the account
   (e.g., "GSC quick wins — ClientX — weekly").
2. The task prompt says: "Run the `[skill-name]` skill for [account], read data
   from [connector], deliver the output as [format] to [destination]."
3. Pick the cadence from the table. Stagger start times so they don't all fire
   at once.

Scheduled tasks fire while the machine is awake — for genuine always-on cadence,
run on an always-on machine. Say this to the user rather than letting them
discover a missed Monday report.

## The weekly narrator (the keystone)

This is the report that makes the whole cadence stick, because it lands before
anyone asks for it. Every Monday, read the week's data across sources and write a
short executive narrative — not a dashboard:

```
# [Account] — SEO, week of [date]
## The one thing
Single most important change this week. One sentence.

## What moved
Position / impression / click deltas vs last week. Only what's material —
skip noise. Explain the *why* behind the top 3 moves, not just the numbers.

## What the cadence surfaced
New striking-distance queries, a decaying page, a broken canonical on a
traffic page, a lost link worth reclaiming — whatever this week's scheduled
skills flagged, filtered to what matters.

## Next week's 3 priorities
Ranked, each with an owner. No more than three.
```

Three priorities, not thirty. The narrator's value is judgment — deciding what
to ignore. A report that lists everything is the same as no report.

## Routing output

Match the destination to the reader: exec/client narrative → email or Slack;
dev tickets from the tech-debt findings → the issue tracker or ClickUp
(`agency-pipeline-report` can absorb these); content briefs → the writer's
workspace. Deliver where the reader already works, not to a dashboard they have
to remember to open.

## Rules

- Cadence matches signal speed. Don't run quarterly analyses weekly.
- Read-only unless a human promotes the task. State the mode on every task.
- The narrator filters; it does not list. Judgment is the product.
- Never schedule an unattended write to a client's live site.
- If a scheduled run has no meaningful finding, the narrator says "nothing
  material this week" — an honest quiet week beats manufactured urgency.

---

Built by [Semil Shah](https://semilshah.me) — SEO consultant & ClickUp systems, Toronto.
This is the operating layer I set up for fractional and coaching clients.
→ [Fractional SEO](https://semilshah.me/fractional-seo-manager.html) · [Coaching](https://semilshah.me/seo-coaching.html)
