# Exercise 3 — Spec the Event Schema for a Feature

**Goal:** Design the exact new events Stuck Task Alerts needs, insert realistic sample data into the seed `events` table, and write the SQL queries that would answer this week's success metrics — proving the feature's success is provable, not asserted.

**Estimated time:** 75–90 minutes.

## Setup

You already ran the seed from the [week README](26-product%20learning（附）/curriculum/week-04-prds-and-product-specs/README.md). Confirm you're connected and the table is there:

```sql
SELECT COUNT(*) FROM events;   -- must print 10
```

Create a file `event-schema.sql` for your `INSERT` statements and a file `metric-queries.sql` for your analysis queries.

## Tasks

1. **List the new event names Stuck Task Alerts needs**, beyond the six named in Lecture 3 — is there anything Lecture 3 missed? Consider: what event captures a manager *viewing* the passive Stuck Items view, which you'd need to compare "pull" behavior (Week 1's baseline) against "push" behavior (this week's feature) in the same table. Add it to your list with a one-sentence justification, or explain why you think the six from the lecture are already sufficient.

2. **Write `INSERT` statements** simulating one full stuck-task lifecycle, in `event-schema.sql`, continuing the `event_id` sequence from 11:
   - Task 502 (already `in_progress` per the seed data) goes quiet and crosses the 48-hour threshold two days after its last `task_status_changed` event.
   - A `task_stuck_detected` event fires.
   - A `stuck_alert_sent` event fires 3 minutes later.
   - The manager snoozes it 10 minutes after that (`stuck_alert_snoozed`).
   - 20 hours later, the assignee finally updates the task (`task_status_changed`) and a `task_unstuck` event fires, referencing how many hours had elapsed since detection.

   Use realistic, consistent timestamps — each event's `occurred_at` must be chronologically consistent with the story you're telling (an alert can't be sent before detection, etc.).

3. **Write three queries** in `metric-queries.sql`, adapted from Lecture 3's examples but run against **your actual inserted data** (not just copy-pasted):
   - The number of hours between `task_stuck_detected` and `stuck_alert_sent` for task 502 (this is your alert-delivery latency for one instance).
   - The number of hours between `stuck_alert_sent` and `task_unstuck` for task 502 (this is your "time to resolution after alert" for one instance).
   - A query that would return **zero rows** right now but is *structured correctly* to catch a real problem: tasks where a `stuck_alert_sent` event exists but **no** `task_unstuck` event follows within 7 days — i.e., alerts that were sent and apparently ignored. Explain in a comment why this query returning rows in production would be a warning sign worth investigating, even before you know *why* those tasks stalled.

4. **Write one sentence per new event** (from Task 1's list plus Lecture 3's six) stating which PRD success metric or guardrail (from Lecture 1's example, or one you'd add) it exists to support. If an event doesn't clearly support any metric, cut it — instrumentation that doesn't answer a real question is clutter, not rigor.

## Expected outcome (self-check)

- `SELECT COUNT(*) FROM events;` after your inserts returns **15 or 16** (10 seed rows + 5 or 6 of yours, depending on whether you added the extra event from Task 1).
- Your latency query (Task 3, first bullet) returns a small number of minutes, not hours or days — alert delivery should be fast per the PRD's "within 5 minutes" acceptance criterion from Lecture 2.
- Your "sent but never unstuck within 7 days" query (Task 3, third bullet) runs without error and returns 0 rows against your current data — but you could point to exactly which row it *would* catch if you inserted a stalled example.

## Done when…

- [ ] `event-schema.sql` has all inserts for the full task-502 lifecycle, chronologically consistent.
- [ ] `metric-queries.sql` has all three queries, each with a comment explaining what it answers.
- [ ] Task 1's extra-event analysis and Task 4's one-sentence-per-event justification are written out (can live in a `notes.md` or as comments).
- [ ] You can explain, out loud, why the third query (alerts sent but not resolved) matters even though it currently returns zero rows.

## Stretch

- Add a `SELECT` that computes, across **all** stuck-task lifecycles in the table (not just task 502), the average time from `stuck_alert_sent` to `task_unstuck`, using `AVG()` and the JSON `properties` field for the timestamps or elapsed-hours values you stored.
- Loopline's `properties` column is a loosely-typed JSON blob for portability. Write two sentences on the trade-off: what do you gain by keeping events generic this way, and what would you gain instead from adding dedicated typed columns (e.g., a real `hours_stuck INTEGER` column) once this feature's event volume is large enough to matter for query performance?

## Submission

Commit `event-schema.sql`, `metric-queries.sql`, and your notes to your portfolio under `c44-week-04/exercise-03/`.
