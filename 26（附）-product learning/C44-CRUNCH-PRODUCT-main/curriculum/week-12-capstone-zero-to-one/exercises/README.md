# Week 12 — Exercises

Three exercises, in strict order, each one a piece of your capstone. Unlike most prior weeks, these don't warm up a shared skill against shared seed data and then release you — they **build the actual capstone deliverable**, file by file. By the time you finish Exercise 3, you should have three real files in your portfolio that Saturday's mini-project assembles and finishes, not three disposable practice exercises.

## How these fit together

| Exercise | Produces | Feeds into |
|----------|----------|-------------|
| 1 — Capstone Discovery Brief | `discovery-brief.md` — your validated problem, JTBD, evidence, opportunity size, risk assessment | Exercise 2's PRD must cite this brief directly |
| 2 — Capstone PRD and Roadmap | `prd.md` and `roadmap.md` — your MVP spec and a RICE/WSJF-scored Now/Next/Later roadmap | Exercise 3's dashboard must measure the PRD's stated success metric |
| 3 — Capstone Metrics Dashboard | `dashboard-schema.sql`, `dashboard-queries.sql`, `dashboard-seed-data.sql` — your own event schema, synthetic seed data, and the queries that would tell you if the MVP worked | Challenge 1's experiment and the mini-project's launch narrative both reference these queries |

If you find yourself changing your capstone idea between exercises, stop and go back — Lecture 1 named this "drift" as the single fastest way to end up with an orphaned Act 2. One idea, committed on Monday, carried through all three exercises and both challenges.

## Before you start

- You should already have a one-sentence capstone idea from Lecture 1, Section 4, saved at `c44-week-12/00-capstone-idea.md`.
- The `mvp_users` / `mvp_launch_events` seed data from the [week README](../README.md) is only needed for Exercise 3's Part A warm-up — it has nothing to do with Exercises 1–2, which are about *your* idea from the start.
- PostgreSQL or SQLite, plus Python with pandas, should already be installed from prior weeks.

## Submission

Commit each exercise's files to your portfolio under `c44-week-12/exercise-01/`, `exercise-02/`, and `exercise-03/` respectively. Keep them — the mini-project explicitly re-uses (not re-writes) these files.

## Getting unstuck

If you're stuck on *which idea to pick*, re-read Lecture 1 Section 4's three constraints (right-sized, evidence-able, has a real metric) before asking for help — most stalls here come from an idea that's too broad, not from a lack of creativity. If you're stuck on the SQL in Exercise 3, the [week README](../README.md)'s seed data and Lecture 2's five queries are a complete worked template — adapt their structure to your own event names and columns rather than starting from a blank query.
