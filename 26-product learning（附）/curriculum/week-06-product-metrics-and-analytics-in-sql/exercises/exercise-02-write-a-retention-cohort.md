# Exercise 2 — Write a Retention Cohort Query

**Goal:** Build a weekly retention cohort table for all eight of Loopline's signup cohorts, and correctly separate real weak retention from right-censored "not enough time has passed yet" cells.

**Estimated time:** 1–1.5 hours. Practices Lecture 3 §2–3.

## Setup

Confirm your seed data loaded (see the [week README](26-product%20learning（附）/curriculum/week-06-product-metrics-and-analytics-in-sql/README.md)):

```sql
SELECT COUNT(*) FROM users;    -- must print 59
SELECT COUNT(*) FROM events;   -- must print 669
```

Create `solutions.sql` for the queries and `answers.md` for the written parts. Remember the dataset's as-of date: **2025-03-16**.

## Tasks

1. **Cohort sizes.** Write a query grouping `users` into weekly signup cohorts (Monday-start weeks) and counting each cohort's size. *(Expected 8 cohorts, sizes: 12, 11, 10, 5, 5, 5, 6, 5 for weeks starting 01-06 through 02-24.)*

2. **"Active" definition.** Before writing any retention SQL, write one sentence in `answers.md` defining which `event_name` values count as "active" for this exercise, and explain why `landing_page_view` does **not** belong in that list (Lecture 3 §5 covers exactly this trap for DAU/MAU — the same logic applies here).

3. **Week 1 retention.** For each cohort, compute the count and percentage of users with at least one qualifying "active" event in days 7–13 after their `signup_date`. *(Expected, cohort `2025-01-06`: 3 of 12 = 25.0%. Cohort `2025-02-24`: 3 of 5 = 60.0%.)*

4. **Week 2 retention.** Same as Task 3, but for days 14–20 after signup. *(Expected, cohort `2025-01-13`: 4 of 11 = 36.4%.)*

5. **The censoring trap.** Run Task 4's query for cohort `2025-02-24` specifically. You should get **0 of 5 (0.0%)**. Before you write that number down as "this cohort's week-2 retention is zero," check: has enough time passed since `2025-02-24` for week 2 (days 14–20) to have fully happened, given the dataset's as-of date of `2025-03-16`? Show your arithmetic in `answers.md` and state whether this 0.0% is a real measurement or a right-censored artifact.

6. **Build the observability flag.** Write a query that, for every (cohort_week, week_number) pair from week 0 through week 4, computes whether that cell is fully observable as of `2025-03-16` — i.e., whether `cohort_week + (week_number + 1) * 7 days <= 2025-03-16`. *(Hint: Lecture 3 §3. Expected: cohort `2025-02-24` is unobservable from week 2 onward; cohort `2025-02-17` is unobservable from week 3 onward; cohort `2025-02-10` is unobservable at week 4.)*

7. **A censoring-safe report.** Combine Tasks 3–6 into one query that shows week 1 and week 2 retention **only for cells flagged observable**, and shows `NULL` (or omits the row) for cells that aren't. This is the version you'd actually be allowed to put in front of a VP.

8. **Compare two cohorts, honestly.** In `answers.md`, compare cohort `2025-01-06` (12 users, oldest, fully observable through week 4+) against cohort `2025-02-24` (5 users, newest). Which one looks "worse" if you naively compare raw week-2 percentages? Which comparison is actually fair, and why?

## Expected result (spot checks)

- Task 1 → 8 cohorts; sizes 12, 11, 10, 5, 5, 5, 6, 5.
- Task 3 → cohort `2025-01-06`: 25.0%; cohort `2025-02-24`: 60.0%.
- Task 4 → cohort `2025-01-13`: 36.4%.
- Task 5 → 0.0%, and it is **right-censored**, not a real zero (as of 2025-03-16, cohort `2025-02-24`'s week-2 window — days 14–20 after 2025-02-24 — extends to 2025-03-16, so it's only just barely closing; check your exact boundary math).
- Task 6 → cohort `2025-02-17` unobservable from week 3; cohort `2025-02-10` unobservable at week 4.

## Done when…

- [ ] `solutions.sql` has all queries under numbered `-- Task N` comments.
- [ ] `answers.md` states the active-event definition (Task 2), the censoring analysis (Task 5), and the cohort comparison (Task 8).
- [ ] Task 7's query never presents an unobservable cell as if it were a measured zero.
- [ ] You can explain, without looking at the lecture, why the *newest* cohort in any retention table is always the one most at risk of being misread.

## Stretch

- Extend the cohort table out to week 8 and render it as a small pandas `DataFrame.pivot_table` (`index="cohort_week", columns="week_number", values="pct_active"`) so you can see the full triangle shape at once — the unobservable cells should show up as `NaN`, not `0.0`.
- For the one cohort with a full 8+ weeks of observable history (`2025-01-06`), plot (or just print, in order) its retention percentage by week. Does it decay smoothly, or does it flatten out at some point? A curve that flattens rather than continuing to zero is the classic signature of a "retained core" — the users for whom the product truly stuck.

## Submission

Commit `solutions.sql` and `answers.md` to your portfolio under `c44-week-06/exercise-02/`.
