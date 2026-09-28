# Week 4 — Exercises

Three guided exercises, ~60–90 min each. Each one builds a piece you'll reuse directly in the mini-project's full PRD — don't skip ahead, the mini-project assumes you already have working drafts from all three.

1. **[Exercise 1 — Write Acceptance Criteria for a Story](exercise-01-write-acceptance-criteria.md)** — take one Stuck Task Alerts story and write Given/When/Then acceptance criteria precise enough to build from.
2. **[Exercise 2 — Enumerate a Feature's Edge Cases](exercise-02-enumerate-edge-cases.md)** — run the five-category checklist against a *different* Loopline feature to prove the method generalizes.
3. **[Exercise 3 — Spec the Event Schema for a Feature](exercise-03-spec-the-event-schema.md)** — design and query the SQL events a feature needs, using the seed `events` table from the week README.

## Before you start

- You've completed all three lectures.
- You ran the seed from the [week README](../README.md) and `SELECT COUNT(*) FROM events;` returns **10**.
- You have a shell open: `psql loopline_events` (PostgreSQL) or `sqlite3 loopline_events.db` (SQLite).

## Suggested workflow

- Open the exercise file beside a blank Markdown file — you're producing real spec text, not just answering questions.
- Write acceptance criteria and edge cases in full Given/When/Then / table form, not bullet fragments — the discipline of the exact phrasing is the point.
- For Exercise 3, write and run the SQL — don't just describe what a query "would" do.
- Save each exercise's output in its own file; you'll fold the strongest pieces into the mini-project's PRD.

## Note on the running example

All three exercises work against **Loopline**, the same fictional team task-management app from Weeks 1–3. Exercise 1 and 3 use **Stuck Task Alerts** (this week's running feature). Exercise 2 deliberately uses a *different* Loopline feature so you practice applying the edge-case method fresh, rather than just recalling the lecture's worked example.
