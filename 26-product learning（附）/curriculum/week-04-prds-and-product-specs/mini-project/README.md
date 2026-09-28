# Mini-Project — The Stuck Task Alerts PRD

> Write a complete, shippable PRD for Loopline's Stuck Task Alerts feature — context, goals, non-goals, user stories with acceptance criteria, an edge-case table, an instrumentation plan, success metrics, and open questions. This is the document; everything this week built toward it.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and unlike most weeks' mini-projects, it isn't a set of separate questions — it's **one deliverable**, assembled from the pieces you've already built. Exercise 1 gave you acceptance criteria technique. Exercise 2 gave you edge-case technique. Exercise 3 gave you event-schema technique. The two challenges gave you scope discipline and ambiguity-handling. Now you put all of it into a single PRD that could genuinely go to an engineering team on Monday morning.

---

## Deliverable

A directory in your portfolio `c44-week-04/mini-project/` containing:

1. `PRD-stuck-task-alerts.md` — the full PRD, following the seven-section skeleton from Lecture 1.
2. `event-schema.sql` — the `CREATE`/`INSERT` statements for every new event your PRD's instrumentation section specifies, extending the seed `events` table from the week README.
3. `metric-queries.sql` — the SQL queries that answer your PRD's success metrics and guardrail, runnable against the schema in `event-schema.sql`.
4. `notes.md` — a short reflection (see the end).

---

## Required sections of `PRD-stuck-task-alerts.md`

Use this as your checklist. Every section is required; none is optional filler.

### 1. Context (3–6 sentences)

Ground it in Week 1's value-proposition evidence (the "stuck items" pain reliever and the 22%-of-managers-open-the-passive-view gap referenced in the week README). Name the specific gap this feature closes.

### 2. Goals (2–4, each falsifiable)

At minimum, cover: reduced time-to-manager-awareness, and increased rate of tasks getting unstuck after an alert. You may add a third goal if you can state it as falsifiably as the first two.

### 3. Non-goals (at least 4)

Each with a one-clause reason. At minimum, address: configurable thresholds, alerting the assignee (vs. only the manager), digest mode, and non-team workspaces — you may keep, adapt, or replace the four from Lecture 1's example, but you must reason about each yourself, not just copy the lecture text.

### 4. Requirements — at least 3 user stories

Each story:
- Full `As a / I want / so that` form.
- One-line INVEST check (which letters does it clearly pass; if any is borderline, say so).
- **At least 3 acceptance criteria per story**, in Given/When/Then form. At least one story must include a boundary-timing criterion (mirroring Lecture 2's "47 hours 55 minutes" precision) and at least one must include a "does NOT happen" criterion.

Minimum story set: (1) core stuck-detection-and-alert, (2) snooze, (3) opt-out. You may add a 4th (e.g., deep-link content) if you want to be thorough, but 3 fully spec'd stories done well beats 5 done thinly.

### 5. Edge cases — a table of at least 8 rows

Use Lecture 3's five categories (empty, error, loading, permission, timing/concurrency) — you don't need exactly 8 categories represented equally, but you must show you applied the checklist, not just brainstormed randomly. At least one row must be an honest open question (you don't know the right behavior yet) rather than a confident guess for every single row.

### 6. Instrumentation + success metrics

- List every new event, its trigger condition, and its key properties (table form, like Lecture 3's example).
- State explicitly which events already exist in the seed schema (from the week README) versus which are new.
- Write out the actual success-metric queries (these should match what's in your `metric-queries.sql`, not just be described in prose).
- Include one **guardrail metric** — something that would tell you the feature is doing *harm*, not just whether it's "working" (Lecture 1's opt-out-rate example, or one of your own).

### 7. Open questions (2–4, each with an owner and a resolve-by point)

No question with no owner. If you genuinely can't think of an honest open question, you haven't looked hard enough — go back to the edge-case table and find the row you were least sure about.

---

## `event-schema.sql` and `metric-queries.sql` requirements

- Extend the seed `events` table from the week README (no redesign needed — reuse its shape).
- Insert enough sample rows to demonstrate **at least two full lifecycles**: one where a stuck task gets resolved after an alert (a "success" case for your primary metric), and one where an alert is sent but the task is *never* resolved within a reasonable window (a case your guardrail or your "alerts sent but not acted on" query, from Exercise 3, would catch).
- Every success metric and guardrail named in your PRD must have a corresponding, runnable query in `metric-queries.sql` — if a metric in your PRD has no query, that's a real gap; fix one or the other.

---

## Milestones

Pace yourself; don't try to write the whole PRD in one sitting.

- **Milestone 1 (45 min):** Sections 1–3 (context, goals, non-goals). Get the frame right before writing a single story.
- **Milestone 2 (60 min):** Section 4 (all 3 stories, full acceptance criteria). This is the largest section — budget accordingly.
- **Milestone 3 (30 min):** Section 5 (edge-case table).
- **Milestone 4 (30 min):** Section 6 (instrumentation + metrics) plus writing `event-schema.sql` and `metric-queries.sql` together, so the two stay honest against each other.
- **Milestone 5 (15 min):** Section 7 (open questions) plus `notes.md` reflection.

---

## Rules

- **No spreadsheets anywhere in this deliverable.** Event data lives in SQL; if you want a scratch view of your data while working, use a SQL query or a pandas DataFrame, never an Excel/Sheets file as the record of truth.
- **Every goal, non-goal, and success metric must be falsifiable** — a stranger reading your PRD in six weeks should be able to check whether each one happened.
- **Every acceptance criterion must contain a checkable number, duration, or exact condition** — no criterion that only a feeling could pass or fail.
- **The instrumentation section and the SQL files must match.** If you mention a metric in the PRD, there's a query for it. If you have an event in the SQL, it's documented in the PRD.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Structure & completeness | 20% | All 7 sections present, in order, nothing left as a stub |
| Non-goals quality | 15% | Specific, varied reasons; visibly prevents real scope creep |
| Acceptance criteria | 25% | Given/When/Then throughout; boundary + "does NOT happen" cases present; no criterion just restates its story |
| Edge cases | 15% | 8+ rows, checklist-driven, at least one honest open question |
| Instrumentation & metrics | 20% | Events documented, queries actually runnable, guardrail present, PRD and SQL match |
| Open questions | 5% | Each has a real owner and a resolve-by point |

---

## Reflection (`notes.md`, ~200 words)

1. Which section was hardest to write, and why — was it a knowledge gap or a judgment call you kept avoiding?
2. Pick one non-goal you wrote. If a stakeholder pushed back and said "no, we actually need that in v1," what evidence would change your mind?
3. Which acceptance criterion in your PRD do you think an engineer is *most* likely to misread or disagree with, even after your best effort at precision? What would you add to close that gap?
4. Look at your guardrail metric. If it started trending in the bad direction two weeks after launch, what's the very first thing you'd check — the metric itself, or something upstream of it?

---

## Why this matters

This is the artifact that actually gets built from. Every technique this week taught — non-goals that prevent scope creep, acceptance criteria precise enough to build without a meeting, edge cases enumerated before they become bug reports, instrumentation specified before launch instead of bolted on after — exists because a PM's real leverage isn't having good ideas, it's writing them down precisely enough that a whole team can execute without you in the room. Keep this PRD; Week 5's prioritization work assumes you can size and sequence work like this, and later weeks (6, 7, 11) will query and extend exactly this kind of event schema.

When done: push, then take the [quiz](26-product%20learning（附）/curriculum/week-04-prds-and-product-specs/quiz.md) and start [Week 5 — Prioritization & roadmapping](../../week-05-prioritization-and-roadmapping/).
