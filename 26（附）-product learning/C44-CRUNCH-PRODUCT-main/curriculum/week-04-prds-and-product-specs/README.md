# Week 4 — PRDs & Product Specs

> **Goal:** by Sunday you can write a PRD for a real feature — goals, non-goals, user stories with acceptance criteria, edge cases, and the event schema it must emit — precise enough that an engineer can build every line without booking a meeting to ask you what you meant.

Welcome back to **C44 · Crunch Product**. Weeks 1–3 built the judgment: what a PM owns, who the user is and what job they hire your product for, and how to size and frame a problem before anyone writes a line of code. This week you turn that judgment into the single artifact that actually ships software — the **PRD** (product requirements document). A PRD is not a Word-doc ritual. It's a contract: it tells engineering what to build, tells design what constraints to work inside, tells data what to instrument, and tells your future self what "done" was supposed to mean when a stakeholder asks "wait, was this ever supposed to handle refunds?" six months from now.

We keep working the same running example from Weeks 1–3: **Loopline**, the fictional team task-management app. In Week 1's value-proposition table, we promised engineering managers a "stuck items" view that surfaces anything untouched for more than 48 hours, and a Slack integration that "surfaces blockers in the channel the manager already reads." This week we write the actual PRD that turns that promise into a shippable feature: **Stuck Task Alerts** — proactively pushing a Slack message the moment a task crosses the 48-hour stuck threshold, instead of making the manager remember to open a view. Every lecture, exercise, and challenge below builds toward the mini-project: a complete, shippable PRD for that one feature.

## Learning objectives

By the end of this week, you will be able to:

- **Structure** a PRD with context, goals, non-goals, requirements, success metrics, and open questions — and explain why the non-goals section is the one stakeholders fight you on and the one that saves the project.
- **Slice** a feature into user stories that follow **INVEST**, and write acceptance criteria in **Given/When/Then** form that leaves no room for "well, I built *a* version of it."
- **Enumerate** a feature's edge cases systematically — empty states, error states, loading states, permission boundaries, and the "what happens at 2am when nobody's watching" cases — *before* a single line of code is written, not after a bug report.
- **Specify** the exact events a feature must emit for measurement, in a SQL-queryable schema (never a spreadsheet), so the feature's success or failure is provable, not asserted.
- **Write** a spec detailed enough that an engineer can build from it without a clarifying meeting per line — the actual bar this whole week is aimed at.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 4930` — translate validated needs into a product requirements document: context, goals and non-goals, user stories, acceptance criteria, success measures and open questions. |
| Industry | Write the spec an engineer builds from on Monday without booking a meeting per line — including the edge cases nobody asked about and the events the feature must emit to be measurable at all. |
| Beyond the bar | The spec is not finished until the measurement exists: the event schema is written as runnable `CREATE` / `INSERT` statements and queried, so the feature's success is provable rather than asserted — `exercises/exercise-03-spec-the-event-schema.md` |

## Prerequisites

- Week 1 (PM foundations), Week 2 (user research), and Week 3 (problem & opportunity framing) — this week assumes you can read a JTBD statement and a validated problem brief without re-explanation.
- You can write plain, structured English. No prior spec-writing experience assumed — most PMs learn this on the job, badly, by shipping ambiguous specs and cleaning up the fallout. This week teaches it directly.
- PostgreSQL 16+ **or** SQLite 3.35+ installed, for Lecture 3 and Exercise 3, where you design and query an events table. If you only install one, SQLite is zero-setup and everything here runs on either engine unchanged. Install steps are in [`resources.md`](./resources.md).
- **No spreadsheets as a data store.** Wherever this week needs to store or query structured data — an event schema, a feature backlog, a QA matrix — you use SQL and/or Python (pandas), never Excel/Sheets as the system of record. Spreadsheets are a presentation surface only, and are taught separately in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/).

## Set up the seed events table

Lecture 3 and Exercise 3 both use one small seed table representing Loopline's existing event log — the events the app already emits, before Stuck Task Alerts adds new ones. Create it once.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_events.db
```

**PostgreSQL:**

```bash
createdb loopline_events
psql loopline_events
```

Then paste this into the shell (unchanged on both engines):

```sql
CREATE TABLE events (
    event_id     INTEGER PRIMARY KEY,
    event_name   TEXT    NOT NULL,
    task_id      INTEGER,
    user_id      INTEGER NOT NULL,
    team_id      INTEGER NOT NULL,
    occurred_at  TIMESTAMP NOT NULL,
    properties   TEXT      -- JSON blob of event-specific fields, kept as text for portability
);

INSERT INTO events (event_id, event_name, task_id, user_id, team_id, occurred_at, properties) VALUES
(1, 'task_created',        501, 12, 3, '2026-06-01 09:02:00', '{"title":"Fix billing webhook"}'),
(2, 'task_assigned',       501, 12, 3, '2026-06-01 09:03:00', '{"assignee_id":18}'),
(3, 'task_status_changed', 501, 18, 3, '2026-06-01 14:20:00', '{"from":"todo","to":"in_progress"}'),
(4, 'task_created',        502, 12, 3, '2026-06-02 10:00:00', '{"title":"Update onboarding copy"}'),
(5, 'task_assigned',       502, 12, 3, '2026-06-02 10:01:00', '{"assignee_id":19}'),
(6, 'task_status_changed', 502, 19, 3, '2026-06-02 10:05:00', '{"from":"todo","to":"in_progress"}'),
(7, 'task_status_changed', 501, 18, 3, '2026-06-05 11:00:00', '{"from":"in_progress","to":"done"}'),
(8, 'task_created',        503, 15, 3, '2026-06-03 08:30:00', '{"title":"Investigate flaky test suite"}'),
(9, 'task_assigned',       503, 15, 3, '2026-06-03 08:31:00', '{"assignee_id":20}'),
(10,'task_status_changed', 503, 20, 3, '2026-06-03 09:00:00', '{"from":"todo","to":"in_progress"}');
```

Sanity check — this should print `10`:

```sql
SELECT COUNT(*) FROM events;
```

Note what's already here: `task_created`, `task_assigned`, `task_status_changed`. Notice there is **no** event for "a task went 48 hours without an update." That gap is exactly what this week's PRD has to close — you can't build a feature on data the app doesn't yet collect, and this week teaches you to specify that data *before* asking engineering to build the feature that depends on it.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Anatomy of a PRD; goals vs. non-goals | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | User stories, INVEST, acceptance criteria | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Edge cases and instrumentation | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Practice: acceptance criteria + edge cases | 0h | 1.5h | 1h | 0.5h | 1h | 1h | 5h |
| Friday | Challenges: trim a PRD, spec an ambiguous ask | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (full Stuck Task Alerts PRD) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-anatomy-of-a-prd.md](./lecture-notes/01-anatomy-of-a-prd.md) | Context, goals, non-goals, requirements, success metrics, open questions; why non-goals prevent scope creep | 2h |
| 2 | [lecture-notes/02-user-stories-and-acceptance-criteria.md](./lecture-notes/02-user-stories-and-acceptance-criteria.md) | Story slicing, INVEST, Given/When/Then acceptance criteria, definition of done | 2h |
| 3 | [lecture-notes/03-edge-cases-and-instrumentation.md](./lecture-notes/03-edge-cases-and-instrumentation.md) | Enumerating failure states, empty/error/loading states, specifying events the feature must log to SQL | 2h |
| 4 | [exercises/exercise-01-write-acceptance-criteria.md](./exercises/exercise-01-write-acceptance-criteria.md) | Write acceptance criteria for a real story | 1.5h |
| 5 | [exercises/exercise-02-enumerate-edge-cases.md](./exercises/exercise-02-enumerate-edge-cases.md) | Enumerate a feature's edge cases systematically | 1h |
| 6 | [exercises/exercise-03-spec-the-event-schema.md](./exercises/exercise-03-spec-the-event-schema.md) | Design and query a SQL event schema for a feature | 1.5h |
| 7 | [challenges/challenge-01-trim-a-bloated-prd.md](./challenges/challenge-01-trim-a-bloated-prd.md) | Cut a real, bloated 6-goal PRD down to its true non-goals | 1.5h |
| 8 | [challenges/challenge-02-spec-an-ambiguous-request.md](./challenges/challenge-02-spec-an-ambiguous-request.md) | Turn a one-line Slack ask from an exec into a buildable spec | 1.5h |
| 9 | [mini-project/README.md](./mini-project/README.md) | Write the full Stuck Task Alerts PRD: stories, acceptance criteria, edge cases, event schema | 2.5h |
| 10 | [homework.md](./homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](./quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](./resources.md) | Official docs, canonical spec-writing reading, and install steps | — |

## By the end of this week you can…

- Open a blank page and structure a PRD that a skeptical engineering lead would call "actually useful" instead of "another doc nobody reads."
- Write a non-goals section that kills scope creep before it starts a fight in sprint planning.
- Slice a feature into stories that are independently shippable, and write acceptance criteria precise enough that QA and engineering read them the same way.
- Look at a feature idea and produce a real edge-case list — empty, error, loading, permission, concurrency, and "it's 2am and nobody's watching" — before it ships with a gap.
- Specify a SQL event schema for a feature, and write the first queries that would prove (or disprove) that it's working.

## Up next

[Week 5 — Prioritization & roadmapping](../week-05-prioritization-and-roadmapping/) — once you can write a spec anyone can build from, the next skill is deciding which specs are worth building first.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
