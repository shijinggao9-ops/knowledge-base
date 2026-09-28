# Exercise 2 — Run a Five-User Usability Test

**Goal:** Write goal-based tasks with real success criteria, run 5 think-aloud sessions on a real flow, log every result into the SQL table from the week README, and pull a prioritized fix list out with queries — not a spreadsheet tally.

**Estimated time:** 2 hours (roughly 15 min × 5 sessions, plus setup and analysis).

## Setup

You need:

1. The `usability_sessions` table from the [week README](../README.md#set-up-the-usability-log-table) — confirm it exists: `SELECT COUNT(*) FROM usability_sessions;` should run without error (it's fine if it returns 0).
2. Five participants, 10–15 minutes each. They do not need to know anything about product management or Loopline.
3. **A real flow to test.** Two options — pick one:
   - **Option A (recommended if you're short on time):** a real sign-up, checkout, or settings flow from a product you use daily (your bank's app, a food delivery app, a SaaS tool at work). Real interfaces produce more honest struggle than a described one.
   - **Option B:** Loopline's checkout flow from [Exercise 1](./exercise-01-map-a-flow-and-friction.md), acted out as a **paper/verbal prototype** — you read each screen's contents aloud or show the ASCII wireframe, and the participant tells you what they'd tap and why. Slower to run, but works if you can't recruit around a live product.

## Part 1 — Write your tasks (20 min)

Write 3–4 goal-based tasks (Lecture 2, Section 2) for your chosen flow. For each, write the success criterion **before** your first session — not after, and not while a participant is mid-task.

Template:

```
Task N: <goal, in the user's language, no UI instructions>
Success criterion: <exactly what "done" looks like, observable, unambiguous>
Failure: <what counts as not completing it>
```

Save this as `test-script.md`, along with your think-aloud opener (adapt the script from Lecture 2, Section 3 — say it out loud to yourself once before session 1).

## Part 2 — Run 5 sessions (60–75 min)

For each participant:

1. Read the think-aloud instructions verbatim.
2. Give one task at a time. Stay quiet. Let struggle happen.
3. For each task, record: did they succeed unassisted (per your written criterion), how long it took (start the clock when you finish reading the task), how many wrong turns/errors they made, and any quote worth keeping verbatim.
4. If you spot a heuristic violation causing the struggle, note which one and a rough severity guess — you'll firm this up during analysis.
5. Debrief for 1 minute at the end: "what was the most confusing part?"

Keep rough notes per session as you go — you'll formalize them into SQL rows next, and memory fades fast.

## Part 3 — Log results to SQL (20 min)

Insert every task result from every session into `usability_sessions`. Use a consistent `flow_name` (e.g., `'my_test_flow'`), pseudonyms for participants (`'P1'`–`'P5'`, never real names), and `NULL` for `time_seconds` on any task nobody finished.

```sql
INSERT INTO usability_sessions
    (participant, flow_name, task_number, task_label, success, time_seconds, error_count, severity_hint, notable_quote)
VALUES
('P1', 'my_test_flow', 1, 'Task 1 label here', TRUE, 28, 0, NULL, NULL);
-- ... one row per participant per task (5 participants x N tasks)
```

Confirm your row count matches: 5 participants × your number of tasks.

```sql
SELECT COUNT(*) FROM usability_sessions WHERE flow_name = 'my_test_flow';
```

## Part 4 — Summarize with SQL (20 min)

Run and save the output of these three queries (adapt `flow_name` to yours):

```sql
-- 1. Success rate per task
SELECT task_number, task_label,
       COUNT(*) AS attempts,
       SUM(CASE WHEN success THEN 1 ELSE 0 END) AS successes,
       ROUND(100.0 * SUM(CASE WHEN success THEN 1 ELSE 0 END) / COUNT(*), 0) AS success_pct
FROM usability_sessions
WHERE flow_name = 'my_test_flow'
GROUP BY task_number, task_label
ORDER BY task_number;

-- 2. Average completion time per task (successes only)
SELECT task_number, task_label, ROUND(AVG(time_seconds), 0) AS avg_seconds
FROM usability_sessions
WHERE flow_name = 'my_test_flow' AND success = TRUE
GROUP BY task_number, task_label
ORDER BY task_number;

-- 3. Every task with an error, ranked by how often it happened
SELECT task_number, task_label, SUM(error_count) AS total_errors
FROM usability_sessions
WHERE flow_name = 'my_test_flow'
GROUP BY task_number, task_label
HAVING SUM(error_count) > 0
ORDER BY total_errors DESC;
```

Paste the three result sets into `results-summary.md`.

## Part 5 — Prioritized fix list (15 min)

From your logged data (not vibes), write a severity × frequency table like the one in [Lecture 2, Section 6](../lecture-notes/02-running-usability-tests.md#6-from-observations-to-a-prioritized-fix-list), listing every real issue you observed, its severity (0–4), how many of your 5 sessions hit it, and a priority call (fix before ship / high / medium / low). Save as `findings.md`.

## Done when…

- [ ] `test-script.md` has 3–4 goal-based tasks, each with a written success criterion, dated *before* session 1.
- [ ] `usability_sessions` has 15–20 rows (5 participants × 3–4 tasks) for your `flow_name`.
- [ ] `results-summary.md` has the output of all three queries, actually run — not hand-typed guesses.
- [ ] `findings.md` has at least 3 issues ranked by severity × frequency, each traceable to at least one specific session.
- [ ] You can name one thing a real participant did that surprised you — if nothing surprised you, you were probably leading them.

## Submission

Commit `test-script.md`, `results-summary.md`, and `findings.md` (plus your raw `INSERT` statements as `sessions.sql`) to your portfolio under `c44-week-08/exercise-02/`.
