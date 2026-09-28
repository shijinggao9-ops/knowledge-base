# Exercise 2 — Bottom-Up Size an Opportunity in SQL

**Goal:** Reproduce and extend Lecture 2's bottom-up sizing of Loopline's import-friction opportunity, using SQL you write yourself — including a check for whether team size (seats), not the import outcome itself, might be doing the real work behind the conversion gap.

**Estimated time:** 2 hours.

## Setup

You already loaded `signup_cohort` (see the [week README](../README.md#set-up-this-weeks-seed-dataset)). Confirm it:

```sql
SELECT COUNT(*) FROM signup_cohort;   -- must print 30
```

Create a file `sizing.sql` and put each answer under a `-- Task N` comment. Where a task asks for interpretation, add it as a SQL comment (`--`) directly beneath the query's expected output, or in a companion `sizing-notes.md` — your choice, but be consistent.

**Portability note:** the `FILTER` clause used in the lectures (`COUNT(*) FILTER (WHERE ...)`) works on PostgreSQL and on SQLite 3.30+. If your SQLite is older, or you just want the more universally portable form, use `SUM(CASE WHEN condition THEN 1 ELSE 0 END)` instead — it's equivalent and works everywhere. Both forms are shown in Task 1.

## Tasks

1. **Baseline rates, two ways.** Reproduce Lecture 2's Step 1 query — the share of all 30 signups that attempted an import, and the share of attempts that failed. Write it once using `FILTER`, and once using `CASE WHEN` + `SUM`, and confirm they return the same numbers. *(Expected: 14 attempted = 46.7%; 6 of 14 attempts failed = 42.9%.)*

2. **Chain the two rates by hand** (not in SQL — just arithmetic in a comment) to get "percent of **all** signups that end up as a failed import." Then write a single SQL query that computes this directly from the table (i.e., without going through the two intermediate percentages) and confirm it matches your hand calculation. *(Expected: 6 of 30 = 20.0%.)*

3. **Break the failed-import group down by `import_error_type`.** For each of the three error types, show the count of teams, how many converted, and total `mrr` from that group. *(Expected: `row_limit_exceeded` → 2 teams, 0 converted, $0 mrr. `duplicate_emails` → 2 teams, 0 converted, $0 mrr. `encoding_error` → 2 teams, 1 converted, $45 mrr.)* In a comment, note which error type looks most "recoverable" based on this data, and which two look closer to a dead end.

4. **Reproduce Lecture 2's Step 2 table** — conversion rate and average MRR-if-converted, grouped by `never attempted` / `succeeded` / `failed`. *(Expected: as in the lecture — 75.0% / 50.0% / 16.7% conversion; $70.00 / $25.00 / $45.00 avg MRR.)*

5. **The confound check.** Team size (`seats`) could be driving both "whether the import succeeds" (bigger teams may have cleaner data hygiene) and "whether the team converts" (bigger teams may just be more serious buyers) — which would mean fixing the import wouldn't close as much of the conversion gap as Task 4 suggests. Bucket teams into `small (2-4 seats)`, `mid (5-7 seats)`, and `large (8+ seats)`, and within **each bucket**, compute the conversion rate for `succeeded` vs. `failed` vs. `never attempted` (where a cell has any rows). *(Expected cells you should be able to reproduce: mid-bucket succeeded = 80.0% [4 of 5] vs. mid-bucket failed = 33.3% [1 of 3]; small-bucket failed = 0.0% [0 of 3].)* In a comment: does the gap between succeeded and failed survive within a seat bucket, or does it disappear once you control for team size?

6. **Build your own ranged annual estimate.** Pick a monthly company-wide signup assumption between 200 and 400 (state your choice and why — e.g., "300, a round number roughly matching the November cohort's daily pace of 1/day extrapolated to a 30-day month at typical scale"). Using the 20.0% failed-import rate from Task 2 and the conversion gap from Task 4, compute: failed-import teams/month → incremental conversions/month → conservative and optimistic incremental MRR/month → annualized low and high. Show your work as commented arithmetic in `sizing.sql`, the same way the lecture did.

## Expected results (spot checks)

- Task 1 → 46.7% attempted, 42.9% of attempts failed, both query forms agree.
- Task 2 → 20.0% of all signups.
- Task 3 → `encoding_error` is the only error type with any conversions.
- Task 4 → 75.0% / 50.0% / 16.7%.
- Task 5 → the succeeded-vs-failed gap is present in every bucket where both cells have data, though sample sizes per cell are small (3–5 rows) — flag that explicitly, don't overstate confidence.
- Task 6 → your own numbers, but if you use 300/month the lecture's own worked range ($18,900–$29,400/year) is what you should land near.

## Done when…

- [ ] `sizing.sql` has all 6 tasks, each runnable and matching (or explaining any deviation from) the expected results above.
- [ ] Task 1's two query forms (`FILTER` and `CASE WHEN`) return identical numbers.
- [ ] Task 5 states, in a comment, whether the seat-size confound meaningfully explains away the conversion gap or not — with a specific number as evidence, not just a hunch.
- [ ] Task 6's assumption (monthly signups) is stated explicitly, not buried in the arithmetic.

## Stretch

Loopline's actual company-wide monthly signup count is unknown to you — that's realistic; PMs constantly work with numbers owned by another team. Write two sentences on where you'd actually go to get that number in a real company (which team, which dashboard/table), and what you'd do differently about this whole exercise if the real number turned out to be 50/month instead of 300/month.

## Submission

Commit `sizing.sql` (and `sizing-notes.md` if you used one) to your portfolio under `c44-week-03/exercise-02/`.
