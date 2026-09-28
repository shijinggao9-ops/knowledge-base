# Week 6 Exercises

Three exercises, meant to be done in order — each builds directly on the last. All three run against the single `users` + `events` seed dataset set up in the [week README](../README.md). Budget ~1–1.5 hours each.

| # | Exercise | Practices | Uses |
|--:|----------|-----------|------|
| 1 | [Build a Conversion Funnel Query](./exercise-01-build-a-funnel-query.md) | Step-by-step funnel counts, conversion rates (Lecture 2) | `events` |
| 2 | [Write a Retention Cohort Query](./exercise-02-write-a-retention-cohort.md) | Weekly cohort table, right-censoring (Lecture 3) | `users` + `events` |
| 3 | [Compute DAU/WAU/MAU and Stickiness](./exercise-03-compute-dau-wau-mau.md) | Rolling active-user windows, stickiness, a pandas cross-check (Lecture 3) | `events` |

## How to work them

1. Read the linked lecture first — each exercise assumes you've done the reading, not just skimmed it. All the SQL patterns you need (window functions, cohort grids, trailing windows) were built and explained there; the exercises ask you to apply them to a new slice of the same data, not invent new techniques from scratch.
2. You already have `users` and `events` loaded from the [week README](../README.md) setup. If you're not sure they loaded correctly, re-run the two sanity checks there (`SELECT COUNT(*) FROM users;` → `59`, `SELECT COUNT(*) FROM events;` → `669`).
3. Write your SQL into a `solutions.sql` file per exercise, one query per numbered task, each under a `-- Task N` comment. Where a written interpretation is asked for, put it in a matching `answers.md`.
4. Every exercise gives you an "Expected result" section — use it to check your own work before moving on. If your count doesn't match, the bug is almost always in the `WHERE` clause (wrong event names) or the join (accidentally dropping unconverted visitors) — re-read Lecture 2 §2 before assuming the seed data is wrong.
5. Commit each exercise's output to your portfolio, in a folder named for the exercise (see the **Submission** section at the bottom of each file).

## Why data lives in SQL here, not a spreadsheet

Every dataset this week is stored and queried as a real table (SQLite or PostgreSQL), never a spreadsheet standing in as a database — and this week makes the reason viscerally obvious. Try building an 8-week retention cohort triangle by hand in a grid: you'd need one column per week-since-signup, one row per cohort, and a manual `COUNTIF`-style formula per cell that correctly excludes cells that haven't happened yet (right-censoring). One typo in a cell range and the whole triangle silently reports the wrong week for half your cohorts, with no error, ever. The SQL version is twelve lines, runs in milliseconds, and is exactly as correct on 700 rows as it would be on 700 million. Spreadsheets have a place — as a presentation or export surface for a finished analysis — and that's taught on its own in [C41 Crunch Excel](../../../../C41-CRUNCH-EXCEL/). In this course, if it's a system of record or anything gets *computed* from it, it's SQL (or pandas).
