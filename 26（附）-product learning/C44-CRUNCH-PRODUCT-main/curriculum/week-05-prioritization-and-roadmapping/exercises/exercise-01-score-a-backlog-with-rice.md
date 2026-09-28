# Exercise 1 — Score a Backlog with RICE

**Goal:** Get RICE into your fingers — compute it in SQL for a full real backlog, build a weighted-scoring alternative, and see exactly where the two rankings disagree and why.

**Estimated time:** 90 minutes.

## Setup

You already ran the seed (see the [week README](../README.md)). Confirm you're connected and the tables are there:

```sql
SELECT COUNT(*) FROM backlog_items;   -- must print 14
```

Create a file `solutions.sql` and put each answer under a `-- Task N` comment.

## Tasks

### Task 1 — RICE, full backlog

Write a `SELECT` that returns `item_key`, `title`, `requested_by`, and a computed `rice_score` (rounded to 2 decimals) for all 14 items, ordered highest score first.

*(Expected: `recurring_tasks` is #1 at 190.0, `public_api_webhooks` is #14 at 2.77.)*

### Task 2 — Top 5 and bottom 5, named

From Task 1's output, list the top 5 and bottom 5 item titles in a short table in `solutions.sql` as a comment block. For each of the bottom 5, write **one sentence** on which RICE input (Reach, Impact, Confidence, or Effort) is doing the most damage to its score.

### Task 3 — Build a weighted-scoring model

RICE has exactly one formula. Weighted scoring lets *you* pick the criteria. Design a 3-criterion weighted model for Loopline's backlog using columns already in `backlog_items` (you may reuse `user_business_value`, `time_criticality`, `risk_reduction_opp_enable`, `job_size_points`, or invent a derived expression from `reach`/`impact`/`confidence`/`effort_weeks`). Pick weights that sum to something sensible (they don't have to sum to 1 or 100 — just be consistent) and write **one sentence justifying each weight** as a comment above your query.

Write the query, ordered by your weighted score descending.

### Task 4 — Where do RICE and your weighted model disagree?

Compare Task 1's ranking to Task 3's ranking. Find **at least 2 items** whose rank differs by 4 or more positions between the two models. For each, write 2–3 sentences: *which model do you trust more for this specific item, and why?*

### Task 5 — A stakeholder pushback, in writing

Imagine the Support lead sees that `stuck_alert_digest_mode` (the fix for the alert-fatigue tickets they've been filing) ranks 5th on RICE, not 1st. Write a 3–4 sentence response, grounded in the actual numbers, explaining why it's ranked where it is and what would have to change about the inputs — not the ranking rule — to move it up.

## Expected results (spot checks)

- Task 1 → `recurring_tasks` = 190.0 (highest), `public_api_webhooks` = 2.77 (lowest).
- Task 1 → `dark_mode` = 150.0 (2nd highest) — flag this one; you'll need it again in Exercise 2 and the challenges.
- Task 1 → `guest_external_access` = 12.0 — low despite being tied to 3 signed deals. This gap is the whole subject of Lecture 2.

## Done when…

- [ ] `solutions.sql` has all 5 tasks, each under a `-- Task N` comment.
- [ ] Task 1's RICE scores match the spot checks above.
- [ ] Task 3's weighted model has a written, one-sentence justification for every weight — not just numbers.
- [ ] Task 4 names two real items with a large rank shift and a stated reason.
- [ ] Task 5's response cites specific numbers, not just "it's ranked lower."

## Stretch

- Add a `rice_rank` and `weighted_rank` column to a single combined query (window function: `RANK() OVER (ORDER BY rice_score DESC)`), and a computed `rank_shift` column, so the disagreements from Task 4 surface automatically instead of by eyeballing two separate lists.
- Recompute RICE for `ai_task_summaries` assuming its Confidence were honestly raised to 0.5 (after a validation spike) instead of 0.2. By how much does its score move, and does it change its position relative to its neighbors?

## Submission

Commit `solutions.sql` to your portfolio under `c44-week-05/exercise-01/`.
