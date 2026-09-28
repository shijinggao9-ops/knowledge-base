# Exercise 1 — Build a Conversion Funnel Query

**Goal:** Turn Loopline's raw `events` table into the full 6-step onboarding funnel — total-visitor counts, step-to-step conversion rates, and one cut by acquisition channel — writing it the honest way (distinct users, no accidental drop of unconverted visitors).

**Estimated time:** 1–1.5 hours. Practices Lecture 2.

## Setup

Confirm your seed data loaded (see the [week README](../README.md)):

```sql
SELECT COUNT(*) FROM users;    -- must print 59
SELECT COUNT(*) FROM events;   -- must print 669
```

Create `solutions.sql` and put each answer under a `-- Task N` comment.

## Tasks

1. **Top of funnel.** Write a query that counts total distinct visitors — everyone who ever fired a `landing_page_view` — with **no join to `users`**. *(Expected: 168.)*

2. **The trap, on purpose.** Now write the same count, but this time `JOIN` to `users` first. Run it, note the number, and in a one-sentence comment above the query explain *why* it's wrong and what question it actually answers instead. *(You're reproducing the Lecture 2 §2 mistake deliberately — this is the query you must never accidentally ship.)*

3. **Full funnel, distinct users per step.** Write one query that returns all six steps (`landing_page_view`, `signup_started`, `signup_completed`, `workspace_created`, `task_created`, `task_completed`) with `COUNT(DISTINCT user_id)` for each, in funnel order. *(Expected: 168 / 86 / 59 / 49 / 34 / 29.)*

4. **Step-to-step conversion.** Extend Task 3 so each row also shows the conversion rate **relative to the immediately preceding step** (not relative to total visitors). Round to 1 decimal place. *(Expected, e.g.: `signup_started → signup_completed` = 68.6%; `signup_completed → workspace_created` = 83.1%.)*

5. **Overall conversion.** Add a column showing each step's conversion **relative to total visitors** (step 1). *(Expected: `task_completed` = 17.3% of all visitors.)*

6. **Where do people actually drop?** Using the numbers from Tasks 4 and 5, write one sentence in `answers.md` naming the single *worst* step-to-step conversion in the funnel, and one sentence naming the step responsible for the *biggest absolute loss* of users (these are not necessarily the same step — explain why).

7. **First-touch timestamps with a window function.** Using `MIN(event_time)` grouped by `user_id` and `event_name` (Lecture 2 §4), write a query returning the **five earliest** `signup_completed` timestamps in the dataset, with the `user_id` attached. *(Expected first row: user 12, `2025-01-06 18:15:41`.)*

8. **Never completed.** Write a query counting users who reached `signup_started` but **never** reached `signup_completed` — the users who abandoned mid-signup. *(Expected: 27.)*

9. **Time-to-convert.** Compute the average number of minutes between a user's first `signup_started` and first `signup_completed`, for users who did both. *(Expected: roughly 8.1 minutes. Hint: `julianday()` on SQLite, `EXTRACT(EPOCH FROM ...)` on Postgres.)*

10. **Funnel by acquisition channel.** `users.signup_channel` tells you how each *registered* user arrived (`organic_search`, `paid_search`, `referral`, `social`, `direct`). Write a query showing, for each channel, how many registered users came from it, sorted highest to lowest. *(Expected top channel: `paid_search` with 16.)* In one sentence in `answers.md`, note the limit of this cut: `signup_channel` only exists for people who *finished* signing up — you cannot use it to measure channel performance further up the funnel (landing → signup_started) without additional tracking this dataset doesn't have. Say what you'd need to fix that.

## Expected result (spot checks)

- Task 1 → 168.
- Task 3 → 168 / 86 / 59 / 49 / 34 / 29.
- Task 8 → 27.
- Task 9 → ≈ 8.1 minutes.
- Task 10 → `paid_search` leads with 16 registered users.

## Done when…

- [ ] `solutions.sql` has all 10 queries under numbered `-- Task N` comments, and every count matches the spot checks.
- [ ] `answers.md` has your one-sentence answers for Tasks 6 and 10.
- [ ] Task 2's query runs, and its comment correctly names the wrong question it answers.
- [ ] Every funnel-step query uses `COUNT(DISTINCT user_id)`, never bare `COUNT(*)`.
- [ ] You can explain out loud why `events.user_id` having no foreign key to `users` is a *feature* of this schema, not a mistake.

## Stretch

- Rebuild Task 3 using the strict-ordering pivot pattern from Lecture 2 §4 (`FILTER`/`CASE` on pivoted first-touch timestamps) instead of the simple `COUNT(DISTINCT)` version. Confirm you get the same six numbers — then explain in one sentence why they matched here but might not on messier real-world event data.
- Add a `session_id` count to Task 3: for the `signup_completed` step, how many *distinct sessions* reached it versus distinct users? Are they ever different, and what would it mean if a user completed signup across two different sessions?

## Submission

Commit `solutions.sql` and `answers.md` to your portfolio under `c44-week-06/exercise-01/`.
