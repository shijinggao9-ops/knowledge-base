# Week 6 — Homework

Five problems, ~4.75 hours total, spread across the week. These reinforce the lectures with a mix of SQL practice, a pandas trend hunt, and structured product judgment. Commit each.

---

## Problem 1 — Add a step to the funnel, then undo it cleanly (60 min)

Loopline's product team is considering a "share a task with a teammate" feature (`task_shared`). Before it ships, they want to know: if the six existing Activated users (Lecture 3 §4 — user_ids `68, 52, 88, 118, 153, 155`) had used it, what would the resulting funnel look like?

In `funnel-extension.sql`:

1. `INSERT` five to eight `task_shared` events into `events`, timestamped shortly after each Activated user's first `task_completed` (invent plausible timestamps — state your assumption in a comment). Not every Activated user needs one.
2. Write a query showing the `task_completed → task_shared` conversion rate among Activated users only.
3. Write one sentence: does this small sample tell you anything trustworthy about whether `task_shared` would be a popular feature? Why or why not?
4. **Undo cleanly:** `DELETE FROM events WHERE event_name = 'task_shared';` and confirm with `SELECT COUNT(*) FROM events;` that you're back to 669.

**Deliver** `funnel-extension.sql` with the inserts, the query, the sentence (as a comment), and the cleanup + confirmation.

---

## Problem 2 — North Star audit of three products you actually use (45 min)

Pick three real products you use regularly (not Loopline) — ideally from different categories (e.g., one social app, one productivity tool, one e-commerce or media app).

For each, in `nsm-audit.md`:

1. Guess what you believe is (or should be) its North Star Metric, stated in the "count/rate of X per time window" phrasing from Lecture 1 §1–2.
2. Name one vanity metric that product could report instead that would make its numbers look better without reflecting real health.
3. Name one metric that product likely tracks internally that's gameable, and describe the specific gaming behavior a team under growth pressure might resort to.

**Deliver** `nsm-audit.md` — three products × three answers each, one to two sentences per answer.

---

## Problem 3 — Build the full retention grid, six cohorts deep (75 min)

Extend Exercise 2's retention query to build the **complete** grid: all 8 cohorts × weeks 0 through 6, with an observability flag on every cell (Lecture 3 §3).

In `full-retention-grid.sql`:

1. Write the single query (or small set of CTEs) that produces one row per (cohort_week, week_number) with columns: `cohort_size`, `active_users`, `pct_active`, `is_observable`.
2. Paste the output (as a Markdown table) into `retention-grid.md`.
3. Below the table, write two to three sentences: which cohorts have the most complete (least censored) picture, and — looking only at the observable cells — does retention appear to be getting better, worse, or staying flat as cohort week increases (i.e., are later cohorts retaining better or worse than earlier ones, among the weeks you can actually compare)?

**Deliver** `full-retention-grid.sql` and `retention-grid.md`.

---

## Problem 4 — Hunt the stickiest and weakest days (60 min, SQL + pandas)

Using the pandas pattern from Lecture 3 §6 (or a SQL loop over every date in the data if you prefer), compute DAU/MAU stickiness for **every day** that appears in `events`.

In `stickiness-hunt.py` (or `.sql` if you go the SQL route):

1. Find the 3 highest-stickiness days and the 3 lowest-stickiness days (excluding the first 29 days of the dataset, where MAU is still ramping up and the ratio is unreliable — start from 2025-02-04 onward).
2. For each of the 6 days, pull the day's raw `event_name` counts (a simple `GROUP BY`) and note anything visible in the mix — e.g. a day with unusually many `login`/`task_completed` events from returning users, versus a quiet day.
3. Write two to three sentences: does the pattern look like it's driven by a handful of highly active users, or broad-based activity across many users that day? (Hint: compare `COUNT(*)` to `COUNT(DISTINCT user_id)` for that day's engaged events.)

**Deliver** `stickiness-hunt.py` (or `.sql`) plus `stickiness-notes.md` with your findings.

---

## Problem 5 — Vanity/gameable metric audit at work or school (45 min)

Think of a real number you've seen tracked at a job, internship, club, or school project — not a tech product this time (a sales quota, a "posts per week" content calendar, an attendance count, a GPA, a "tickets closed" support metric — anything with a target attached).

In `real-world-metric-audit.md`:

1. Name the metric and who was accountable for it.
2. Was it vanity (could go up with zero real improvement), gameable (could be moved via a change a reasonable person would call a regression), both, or neither? Defend your answer in 2–3 sentences.
3. If it was vanity or gameable, propose the guardrail metric that should have been paired with it, in the style of Lecture 1 §4's `task_created` / `% completed within 14 days` pairing.

**Deliver** `real-world-metric-audit.md`.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 60 min |
| 2 | 45 min |
| 3 | 75 min |
| 4 | 60 min |
| 5 | 45 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
