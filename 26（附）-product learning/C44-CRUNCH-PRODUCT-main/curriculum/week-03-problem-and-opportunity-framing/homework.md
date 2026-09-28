# Week 3 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of writing, SQL, and a bit of research outside Loopline. Commit each.

All SQL problems run against the `signup_cohort` seed from the [README](./README.md) unless a problem says otherwise.

---

## Problem 1 — Five Whys on your own life (30 min)

Pick a genuine, mildly annoying recurring problem from your own life — not work, not this course (e.g., "I keep missing the bus," "my inbox is always at 4,000 unread"). In `five-whys.md`:

1. State the symptom in one sentence.
2. Run a real Five Whys chain (3–5 steps is fine) — actually think through each "why," don't invent a chain that just sounds good.
3. Write the resulting problem statement using the who/what/why/impact structure from Lecture 1 (yes, "who" can be just you — be specific about the circumstance anyway).
4. Note one solution you'd have jumped to *before* doing this exercise, and whether the root cause you found changes what you'd actually try.

---

## Problem 2 — Ten SQL warm-ups on `signup_cohort` (75 min)

Write and run each. Put them in `warmups.sql` with a `-- N` comment and the result beneath each.

1. How many teams signed up in the second half of November (Nov 16–30)?
2. What is the largest team (by `seats`) in the whole cohort, and did it convert?
3. Of teams with 5 or more seats, what fraction converted to paid?
4. What is the total MRR currently on the books from this cohort (sum of `mrr` across all 30 teams)?
5. List every team that contacted support about their import but did **not** end up converting — team_id and seats only.
6. What is the average `import_row_count` for teams whose import succeeded, versus teams whose import failed? *(Hint: `AVG(import_row_count)` grouped by `import_succeeded`, only over rows where `import_attempted` is true.)*
7. Which single team had the highest `import_row_count` among **failed** imports, and what was its `import_error_type`?
8. How many teams never attempted an import **and** never converted? *(These are the ones who quietly used the product with no data migration and no purchase — a third distinct segment worth naming, separate from the import-friction story.)*
9. Rank all 30 teams by `mrr` descending, and show the top 5 with their `team_id`, `seats`, and whether they attempted an import.
10. Using `CASE WHEN`, add a computed column `segment` to a `SELECT * FROM signup_cohort` that labels each row `'no import'`, `'import ok'`, or `'import failed'` — confirm the three counts sum to 30.

---

## Problem 3 — Explain the confound, in writing (45 min)

In `confound-writeup.md`, no more than 400 words total:

1. In your own words, explain what a "confounding variable" is, using the seats/conversion/import example from this week.
2. Design (in prose, not SQL — just describe it) one additional piece of data Loopline could collect that would let you test the confound more rigorously than the seat-bucket cut in Exercise 2, Task 5.
3. Give one real-world example (not from this course) of a metric you've seen — at work, in the news, anywhere — that was probably confounded, and explain what the hidden variable likely was.

---

## Problem 4 — Practice TAM/SAM/SOM on a product you use (60 min)

Pick any real product you personally use (not Loopline). In `sizing-practice.md`, build a top-down TAM/SAM/SOM chain for one specific, plausible feature opportunity for that product (invented by you — you don't have real access to their data, and that's fine, this is practice with the *method*, not real research):

1. State the feature opportunity as a proper problem statement first (Lecture 1) — resist jumping straight to sizing.
2. Build the TAM → SAM → SOM chain with each assumption labeled.
3. Compute a final SOM revenue estimate.
4. Rate each of your own assumptions Solid/Soft/Unfounded, same as Challenge 2's audit structure, and be honest — most of them will be Soft or Unfounded, since you don't have the company's real data, and that's the point of the exercise.

---

## Problem 5 — Extend the tree (60 min)

Return to your Exercise 3 opportunity-solution tree (or Lecture 3's, if you want a fresh start). Add a **fifth** opportunity you didn't include before — one you have to invent evidence for (label it clearly as invented/hypothetical practice data, not real). Then:

1. Add at least one solution under it.
2. Re-run the scoring pass from Lecture 3 (evidence strength, sized or not, cost to explore further, how directly it serves the outcome) across all five opportunities now on the tree.
3. State whether adding this fifth opportunity changes your prioritization call from Exercise 3, and why or why not.

**Deliver** `tree-extended.md` with the updated tree and your reasoning.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 30 min |
| 2 | 75 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 60 min |
| **Total** | **~4.5 h** |

After homework, take the [quiz](./quiz.md) and ship the [mini-project](./mini-project/README.md).
