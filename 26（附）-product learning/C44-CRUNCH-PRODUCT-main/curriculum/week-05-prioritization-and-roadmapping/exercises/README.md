# Week 5 — Exercises

Three guided exercises, ~1–1.5 hours each. Each one builds a piece you'll reuse directly in the mini-project's full prioritization and roadmap — don't skip ahead, the mini-project assumes you already have working output from all three.

1. **[Exercise 1 — Score a Backlog with RICE](exercise-01-score-a-backlog-with-rice.md)** — compute RICE scores for the full 14-item backlog in SQL, plus a weighted-scoring alternative, and compare the two rankings.
2. **[Exercise 2 — Kano-Classify a Feature Set](exercise-02-kano-classify-features.md)** — classify a fourth feature (`guest_external_access`) from raw, messier survey data than the lecture's clean walkthrough — by hand first, then in SQL.
3. **[Exercise 3 — Build a Now/Next/Later Roadmap](exercise-03-build-a-now-next-later.md)** — run the full capacity-constrained, dependency-respecting sequencing pipeline in pandas and produce a real roadmap table.

## Before you start

- You've completed all three lectures.
- You ran the seed from the [week README](../README.md): `SELECT COUNT(*) FROM backlog_items;` returns **14**, `backlog_dependencies` returns **2**, `kano_survey_responses` returns **60**.
- You have a shell open (`psql loopline_backlog` or `sqlite3 loopline_backlog.db`) and a Python virtual environment with `pandas` and `sqlalchemy` installed.

## Suggested workflow

- Write and run real SQL/Python for every task — don't just describe what a query "would" return. The point of this week is fluency with the arithmetic, not familiarity with the concept.
- Save each exercise's output (a `.sql` file, a `.md` writeup, a `.py` script and its printed output) — you'll fold the strongest pieces directly into the mini-project.
- Where an exercise asks for a judgment call (a Reach estimate, a tie-break), write the one-sentence justification down. An unexplained number is not a finished answer this week.

## Note on the running example

All three exercises work against **Loopline**'s Q3 backlog — the same fictional team task-management app from Weeks 1–4. Exercise 2 deliberately uses a feature (`guest_external_access`) that wasn't part of Lecture 1's worked Kano walkthrough, so you're applying the method fresh rather than recalling the lecture's answer.
