# Exercise 3 — Infer Strategy from a Product's Metrics

**Goal:** Query 12 weeks of Loopline's real metrics table and diagnose, with evidence — not vibes — what lifecycle stage the product is in and what strategic bet its team should be making next.

**Estimated time:** 60–90 minutes.

## Setup — seed the metrics table

You do **not** need prior SQL experience — every query in this exercise is given to you, ready to run. Open `sqlite3 loopline.db` (or `psql loopline`) and run:

```sql
CREATE TABLE product_metrics (
    week_number     INTEGER PRIMARY KEY,
    week_start      DATE    NOT NULL,
    new_signups     INTEGER NOT NULL,
    activated_users INTEGER NOT NULL,  -- of new_signups, how many completed onboarding + first task
    dau             INTEGER NOT NULL,  -- daily active users, week's average
    wau             INTEGER NOT NULL,  -- weekly active users
    mau             INTEGER NOT NULL,  -- monthly active users (trailing 30 days)
    churned_accounts INTEGER NOT NULL, -- paying accounts that cancelled this week
    nps             INTEGER,           -- net promoter score, -100 to 100; NULL = not surveyed that week
    mrr             NUMERIC NOT NULL   -- monthly recurring revenue, USD, end of week
);

INSERT INTO product_metrics VALUES
(1, '2026-01-05', 380, 258, 3100, 5400, 14200, 6, 42, 118000),
(2, '2026-01-12', 402, 265, 3180, 5550, 14650, 7, 41, 121500),
(3, '2026-01-19', 415, 261, 3240, 5700, 15100, 8, NULL, 124800),
(4, '2026-01-26', 430, 255, 3300, 5820, 15600, 9, 39, 128200),
(5, '2026-02-02', 448, 246, 3350, 5900, 16050, 11, 38, 131300),
(6, '2026-02-09', 460, 235, 3390, 5960, 16480, 13, NULL, 134100),
(7, '2026-02-16', 475, 222, 3410, 6000, 16900, 16, 34, 136600),
(8, '2026-02-23', 490, 211, 3420, 6020, 17280, 19, 32, 138700),
(9, '2026-03-02', 505, 199, 3400, 6010, 17600, 23, NULL, 140200),
(10, '2026-03-09', 518, 187, 3380, 5980, 17880, 27, 28, 141100),
(11, '2026-03-16', 530, 176, 3350, 5930, 18100, 31, 26, 141600),
(12, '2026-03-23', 542, 165, 3300, 5860, 18280, 36, 22, 141800);
```

Sanity check — this should print `12`:

```sql
SELECT COUNT(*) FROM product_metrics;
```

## Tasks

Run each query, record the actual output, and answer the interpretation question that follows it in a file `diagnosis.md`.

1. **Top-of-funnel trend.**

   ```sql
   SELECT week_number, new_signups FROM product_metrics ORDER BY week_number;
   ```

   Is new-signup growth accelerating, steady, or decelerating over the 12 weeks? Compute the percent change from week 1 to week 12.

2. **Activation rate — the number nobody put in the table directly.**

   ```sql
   SELECT
       week_number,
       new_signups,
       activated_users,
       ROUND(100.0 * activated_users / new_signups, 1) AS activation_rate_pct
   FROM product_metrics
   ORDER BY week_number;
   ```

   Describe the trend in activation rate across the 12 weeks in one sentence. Is it moving the same direction as `new_signups`?

3. **Stickiness — WAU/MAU ratio.**

   ```sql
   SELECT
       week_number,
       ROUND(1.0 * wau / mau, 3) AS wau_mau_ratio
   FROM product_metrics
   ORDER BY week_number;
   ```

   A WAU/MAU ratio near 1.0 means almost every monthly user is active weekly (very sticky); a ratio well under 0.5 means many monthly users only show up occasionally. What's the trend here, and what does it suggest about how *engaged* the growing user base actually is?

4. **Churn and revenue together.**

   ```sql
   SELECT
       week_number,
       churned_accounts,
       mrr,
       mrr - LAG(mrr) OVER (ORDER BY week_number) AS mrr_change_from_prior_week
   FROM product_metrics
   ORDER BY week_number;
   ```

   *(This one query uses a window function, `LAG`, a Week-9 topic — you're not expected to write this yourself yet, just read its output. It shows each week's MRR change from the week before.)* Is churn rising, flat, or falling? Is MRR growth still positive by week 12 — and if so, is it growing at the same rate it was in week 1–4?

5. **NPS — read it with its gaps.**

   ```sql
   SELECT week_number, nps FROM product_metrics WHERE nps IS NOT NULL ORDER BY week_number;
   ```

   NPS wasn't surveyed every week (`NULL` in weeks 3, 6, 9 — Loopline surveys roughly every third week). Using only the real values, what's the trend? Would averaging with `NULL`s treated as `0` distort the picture — and why does `AVG(nps)` in SQL already handle this correctly? *(Revisit C33 Week 1's `NULL`-and-aggregates lesson if this is fuzzy — `AVG` ignores `NULL`s automatically; it does not need special handling.)*

6. **Put it together — diagnose the stage.** Using Lecture 3's five-stage table, which stage is Loopline in, and which stage is it *drifting toward* if these trends continue unchanged? Cite at least **three** of the five queries above as evidence — a diagnosis with one metric cited is not yet a diagnosis, it's a guess.

7. **Write the strategic bet.** Using the claim / reason / bet / falsification-condition shape from Lecture 3, write one strategic bet Loopline's PM should make in response to what you found. Name the specific metric and threshold that would tell them, in 4–6 weeks, whether the bet worked.

## Expected outcome (self-check)

- Task 1: signups grow from 380 to 542 — roughly **+43%** over 12 weeks. On its own this reads as unambiguous good news.
- Task 2: activation rate falls from **68%** (week 1) to **30%** (week 12) — a steep, steady decline that runs in the *opposite* direction from signups.
- Task 3: WAU/MAU drifts down from about **0.380** to **0.321** — engagement per monthly user is softening, not just activation.
- Task 4: churned accounts rise from 6 to 36 (a 6x increase); weekly MRR growth is still positive every week but is shrinking — compare the week 2 vs. week 12 `mrr_change_from_prior_week` values.
- Task 6: this is a growth-stage product where the acquisition engine is working but the product/onboarding experience is degrading under its own growth — the exact pattern from Lecture 3, Section 2, just with twice the data and a revenue signal added.

## Done when…

- [ ] `diagnosis.md` has all 7 tasks answered with the actual query output referenced (not just a vibe).
- [ ] Task 6's diagnosis cites at least three separate metrics as evidence.
- [ ] Task 7's strategic bet names a specific number and a specific deadline — "improve retention" is not a falsification condition, "activation rate ≥55% within 6 weeks" is.

## Stretch

- Write (or ask a worker model to help draft, then verify by hand) a query that computes **net new MRR** per week (`mrr_change_from_prior_week` is gross change; try isolating how much of it is new signups' revenue vs. offset by churn, using the `churned_accounts` column as a rough proxy).
- In Python/pandas, load this table (`pd.read_sql` against SQLite or Postgres) and plot `activation_rate_pct` and `new_signups` on the same chart with two y-axes. Does the visual make the divergence more obvious than the table did?

## Submission

Commit `diagnosis.md` to your portfolio under `c44-week-01/exercise-03/`.
