# Exercise 3 — Model a Pricing Change in SQL

**Goal:** Run Lecture 3's tier-migration and risk-adjustment workflow yourself against the seeded `subscriptions` table, and defend the churn-risk assumptions in your own words. This exercise uses a specific, canonical three-tier proposal (Starter $9 / Team $15 / Business $18) — not necessarily the tiers you designed in Exercise 1 — so everyone's SQL numbers match and can be checked against the same expected outcome.

**Estimated time:** 60–90 minutes.

## Setup

You should already have `subscriptions` seeded from Lecture 3 ([lecture-notes/03-modeling-pricing-and-growth.md](03-modeling-pricing-and-growth.md), Section 1). If not, run that `CREATE TABLE`/`INSERT` block first.

Sanity check:

```sql
SELECT COUNT(*) FROM subscriptions;                       -- 30
SELECT COUNT(*) FROM subscriptions WHERE status='active';  -- 26
```

**The canonical tier rule** (use this exact mapping for every query below):

- `segment = 'Enterprise'` → **Business** tier, **$18.00**/seat
- `segment != 'Enterprise'` and `seats <= 10` → **Starter** tier, **$9.00**/seat
- everything else → **Team** tier, **$15.00**/seat

## Tasks

1. **Baseline.** Write the MRR/ARPU query from Lecture 3, Section 2. Record `active_accounts`, `total_seats`, `mrr`, and `blended_arpu` in `pricing-model.md`.

2. **Tier assignment.** Write the `CASE`-based tier-migration query from Lecture 3, Section 3 (the one producing `new_tier`, `new_price_per_seat`, and `new_mrr` per account). Run it and paste the full 26-row output into `pricing-model.md` under a heading **"Tier assignment."**

3. **Naive projection.** Sum `old_mrr` and sum `new_mrr` across all 26 active accounts. Record both totals and the percent change in `pricing-model.md` under **"Naive projection."**

4. **Risk-adjust it.** Write the full risk-adjustment query from Lecture 3, Section 4 (the one with the `churn_risk` and `expected_mrr` columns). Sum `expected_mrr` across all rows. Record the risk-adjusted total and its percent change vs. the old MRR baseline, under **"Risk-adjusted projection."**

5. **Explain the gap, in your own words.** In 3–4 sentences in `pricing-model.md`, explain *why* the naive and risk-adjusted numbers differ as much as they do, and name which segment is driving most of that gap. Don't just restate the lecture's numbers — say it as if you were explaining it to a CFO who has never seen this table.

6. **Defend or revise the risk table.** Lecture 3's churn-risk assumptions (22% risk at ≥40% price increase, 10% at 10–39%, 4% at 0–9%, 1% at any decrease) were stated, not derived from real data — this is a real-world constraint you'll hit constantly: you often have to price-change *before* you have historical price-elasticity data on your own product. In `pricing-model.md`, either (a) defend why you'd keep these exact numbers for Loopline specifically, citing something in the `subscriptions` data (a churn reason, an NPS score, a segment concentration) that supports them, or (b) propose one specific change to the risk table and rerun the risk-adjusted query with your revised numbers, reporting the new total.

## Expected outcome (self-check)

- **Baseline:** 26 active accounts, 906 seats, **$9,344.40 MRR**, **$10.31 blended ARPU**.
- **Naive projection:** new MRR **$12,830.85** → **+37.3%** vs. baseline.
- **Risk-adjusted projection:** expected MRR **$10,547.52** → **+12.9%** vs. baseline.
- **The gap** between naive and risk-adjusted is **$2,283.33/month** (~$27,400/year), and **Business tier (the 5 Enterprise accounts) drives almost all of it** — their naive new MRR of $8,666.10 risk-adjusts down to $6,759.56, a swing of $1,906.54/month by itself, because every Enterprise account faces the full 50% price increase and lands in the highest risk bracket.
- If your numbers don't match, the most common cause is applying `discount_pct` inconsistently between the `old_mrr` and `new_mrr` calculations — the negotiated discount should apply to **both** the old and new price, not just one.

## Done when…

- [ ] `pricing-model.md` has all four sections (baseline, tier assignment, naive projection, risk-adjusted projection) with real query output.
- [ ] Your baseline and projection totals match the expected outcome above (or you've found and explained a specific discrepancy).
- [ ] The gap-explanation paragraph names the driving segment and states the mechanism (price-increase size → risk bracket → dollars), not just the numbers.
- [ ] Task 6 is answered — either a defense of the existing risk table or a revised one with a rerun total.

## Stretch

- Rerun the risk-adjusted query with **Business tier priced at $15/seat instead of $18** (i.e., Enterprise accounts get the Team price, not a distinct Business price). How much revenue upside does the $18 price point buy you, after risk-adjustment, compared to just putting Enterprise on the Team tier? Is the compliance-gated Business tier worth the added churn risk, in dollars?
- Using the two real churned accounts in the table (Silverpine AI and Vantage Manufacturing, both already churned *before* this repricing), would either of them have been retained under the new tier structure had they still been active customers? Justify with the actual tier and price they'd have landed on.

## Submission

Commit `pricing-model.md` (and, if you did the stretch, `pricing-model-stretch.md`) to your portfolio under `c44-week-10/exercise-03/`.
