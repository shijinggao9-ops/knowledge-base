# Week 1 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of writing, structured judgment, and one small SQL query set. Commit each.

---

## Problem 1 — Own vs. influence, audited against a real team (45 min)

Think of a team you've been part of — a job, a class group project, a club, a sports team, a household. It doesn't need to be a software team.

1. List 5 recurring decisions that team made.
2. For each, classify it as something the nominal "leader" (manager, captain, project lead) **owned** outright, **influenced but didn't decide alone**, or that **nobody clearly owned** (and describe what went wrong because of that gap, if anything did).
3. Write two sentences connecting this back to Lecture 1's own/influence framework — where did your team's structure match the PM pattern, and where did it differ?

**Deliver** `ownership-audit.md`.

---

## Problem 2 — Ten JTBD statements, ten feature requests (75 min)

Fluency comes from reps. For each feature request below, write a full JTBD statement (situation / functional job / outcome) and confirm it passes the disguised-feature-request test from Exercise 1 — no product or feature name inside the statement itself.

1. "Add a 'snooze' button to notifications."
2. "Let me undo a delete."
3. "I want push notifications, not just email."
4. "Add a search bar."
5. "Let me share a read-only link."
6. "I want an offline mode."
7. "Add keyboard shortcuts."
8. "Let me set a custom reminder time."
9. "I want a way to see everything due today, across all my projects."
10. "Add a 'recently viewed' list."

**Deliver** `jtbd-drills.md` — 10 statements, each followed by one clause naming the functional/emotional/social layer(s) present.

---

## Problem 3 — Explain the lifecycle stage mismatch (45 min)

In `stage-mismatch.md`, answer in prose (no more than 500 words total):

1. Describe, from your own experience or observation, a product or feature that seemed to be optimizing for the *wrong* stage's metric — e.g., chasing new signups while an existing user base was quietly churning, or obsessing over "polish" on a feature nobody had validated wanted to exist yet.
2. Which lifecycle stage (Lecture 3) do you think that team *thought* they were in, and which stage do you think the evidence actually supported?
3. What's the risk of a team misdiagnosing its own stage — name one concrete way it wastes effort or money.
4. If you were advising that team, what's the one metric you'd ask them to look at first?

---

## Problem 4 — VVF+U speed drills (45 min)

For each idea below, give a quick VVF+U call (1–5 on each lens, one clause of reasoning per lens — you're aiming for fast, defensible judgment, not an essay):

1. A grocery delivery app adds a feature letting users video-call a personal shopper while they're in the store.
2. A budgeting app adds a leaderboard showing how your savings rate compares to friends.
3. A B2B analytics tool adds a fully custom, drag-and-drop dashboard builder.
4. A fitness app starts requiring a $2/month fee for a feature that used to be free.
5. A note-taking app adds end-to-end encryption, with no visible UI change otherwise.

**Deliver** `vvfu-drills.md` — 5 ideas × 4 scores + 4 one-clause reasons each.

---

## Problem 5 — Query the Loopline metrics table, extended (60 min)

Reuse the `product_metrics` table you built in Exercise 3. In `metrics-extension.sql`:

1. Write `INSERT` statements adding **4 more weeks** (weeks 13–16) of your own invention, continuing whatever trend you believe is most likely given weeks 1–12 (accelerating decline, a recovery after an intervention — your call, but state your assumption in a comment).
2. Write a query using `AVG()` and `GROUP BY` to compare the average `activation_rate`-equivalent (`activated_users / new_signups`) between weeks 1–6 and weeks 7–16 as two periods. *(Hint: a `CASE WHEN week_number <= 6 THEN 'early' ELSE 'late' END` column, grouped.)*
3. Then **undo** it cleanly: `DELETE FROM product_metrics WHERE week_number >= 13;` and confirm you're back to 12 rows.

**Deliver** `metrics-extension.sql` (the inserts, the comparison query with its output, and the cleanup) plus one sentence on what your invented weeks 13–16 would mean for the strategic bet you wrote in Exercise 3.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 45 min |
| 2 | 75 min |
| 3 | 45 min |
| 4 | 45 min |
| 5 | 60 min |
| **Total** | **~4.5 h** |

After homework, take the [quiz](26-product%20learning（附）/curriculum/week-01-product-management-foundations/quiz.md) and ship the [mini-project](26-product%20learning（附）/curriculum/week-01-product-management-foundations/mini-project/README.md).
