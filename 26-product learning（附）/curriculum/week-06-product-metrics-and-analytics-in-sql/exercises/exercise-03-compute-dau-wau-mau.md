# Exercise 3 — Compute DAU/WAU/MAU and Stickiness

**Goal:** Compute Loopline's DAU, WAU, and MAU for specific dates in SQL, find the dataset's peak activity day, and cross-check one of your numbers in pandas.

**Estimated time:** 1–1.5 hours. Practices Lecture 3 §5–6.

## Setup

Confirm your seed data loaded (see the [week README](26-product%20learning（附）/curriculum/week-06-product-metrics-and-analytics-in-sql/README.md)):

```sql
SELECT COUNT(*) FROM users;    -- must print 59
SELECT COUNT(*) FROM events;   -- must print 669
```

Create `solutions.sql` for the SQL and `solutions.py` for the pandas part. Remember: `login`, `task_created`, `task_completed`, and `workspace_created` count as "engaged" events for this exercise — `landing_page_view`, `signup_started`, and `signup_completed` do **not** (Lecture 3 §5 explains why in detail; re-read it if Task 1 gives you a suspiciously large number).

## Tasks

1. **DAU on a single day.** Compute DAU (distinct engaged users) for **2025-01-20**. *(Expected: 3.)*

2. **WAU on the same day.** Compute WAU (trailing 7-day window ending 2025-01-20, inclusive) for the same date. *(Expected: 15.)*

3. **MAU on the same day.** Compute MAU (trailing 30-day window ending 2025-01-20, inclusive) for the same date. *(Expected: 25.)*

4. **Stickiness.** Using your Task 1 and Task 3 results, compute the DAU/MAU stickiness percentage for 2025-01-20, rounded to 1 decimal. *(Expected: 12.0%.)*

5. **Repeat for a busier day.** Run Tasks 1–4 again for **2025-02-14**. *(Expected: DAU 8, WAU 16, MAU 37, stickiness 21.6%.)*

6. **Find the peak day.** Write one query that computes DAU for **every** distinct day that appears in `events`, and returns the top 5 busiest days sorted descending. *(Expected #1: 2025-02-14 with DAU 8.)*

7. **One query, all three numbers, any date.** Refactor Tasks 1–3 into a single query (a CTE or three scalar subqueries, per Lecture 3 §5) that takes one date and returns `dau`, `wau`, `mau`, and `stickiness_pct` as four columns in one row. Parameterize it by editing a literal date at the top rather than copy-pasting three separate queries — this is the version you'd actually reuse.

8. **The mistake, on purpose.** Recompute MAU for 2025-02-14, but this time **without** the `event_name IN (...)` filter (i.e., count every event type, including `landing_page_view`). Note the new number in `answers.md`, compute how many percentage points lower the *real* stickiness ratio looks with this inflated MAU, and explain in one sentence why a marketing traffic spike would make this wrong version look like "engagement is crashing" even if nothing in the product changed.

9. **Total reach.** Across the *entire* dataset (Jan 6 – Mar 16), how many distinct users ever fired at least one engaged event? *(Expected: 49 — compare this to `SELECT COUNT(*) FROM users` (59) and explain the gap in one sentence: who are the 10 registered users who never engaged?)*

## Expected result (spot checks)

- Task 1 → DAU 3.
- Task 2 → WAU 15.
- Task 3 → MAU 25.
- Task 4 → 12.0%.
- Task 5 → DAU 8, WAU 16, MAU 37, 21.6%.
- Task 6 → 2025-02-14 is the peak day.
- Task 9 → 49.

## Done when…

- [ ] `solutions.sql` has all 9 tasks under numbered comments, and all spot checks match.
- [ ] `answers.md` has your Task 8 write-up (the inflated-MAU comparison) and Task 9's one-sentence explanation.
- [ ] Task 7 is a single reusable query, not three queries pasted together.
- [ ] You can say, without checking notes, which four event names belong in an "engaged" DAU/MAU calculation for this dataset, and which three do not.

## Stretch — the pandas cross-check

Load `events` into pandas and independently recompute Task 5 (DAU/WAU/MAU for 2025-02-14). This is the "trust but verify" habit real analysts use before shipping a number into a deck: if your SQL and your pandas agree, you've caught most classes of query bugs.

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("loopline_events.db")   # adjust path/engine as needed
events = pd.read_sql(
    "SELECT user_id, event_name, event_time FROM events "
    "WHERE event_name IN ('login','task_created','task_completed','workspace_created')",
    conn, parse_dates=["event_time"],
)
events["date"] = events["event_time"].dt.date

target = pd.Timestamp("2025-02-14").date()
dau = events.loc[events["date"] == target, "user_id"].nunique()
wau = events.loc[
    (events["date"] > target - pd.Timedelta(days=6)) & (events["date"] <= target), "user_id"
].nunique()
mau = events.loc[
    (events["date"] > target - pd.Timedelta(days=29)) & (events["date"] <= target), "user_id"
].nunique()

print(f"DAU={dau} WAU={wau} MAU={mau} stickiness={100*dau/mau:.1f}%")
# Expect: DAU=8 WAU=16 MAU=37 stickiness=21.6%
```

If your numbers don't match, the usual culprit is an inclusive/exclusive boundary mismatch (`>` vs `>=`) between your SQL date range and pandas' — walk both queries' date boundaries side by side until you find the off-by-one.

## Submission

Commit `solutions.sql`, `solutions.py`, and `answers.md` to your portfolio under `c44-week-06/exercise-03/`.
