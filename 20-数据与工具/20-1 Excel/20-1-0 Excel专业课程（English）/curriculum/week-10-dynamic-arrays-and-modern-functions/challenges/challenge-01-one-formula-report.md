# Challenge 1 — Whole Report in One Formula

**Time:** ~90 minutes. **Difficulty:** Hard. **One formula. No helper cells.**

## The scenario

Your manager wants a **Regional Performance Report**: for every region that has at least one Shipped order, show the region name, how many Shipped orders it has, its total Shipped revenue, and its average Shipped order value — sorted so the highest-revenue region is on top. You could build this the "old" way: a `UNIQUE` list of regions in one column, four `SUMIFS`/`COUNTIFS` formulas dragged down next to it, then a manual sort. That's five to eight cells wired together, and if the source data changes shape, several of them need re-checking.

This challenge is the other way: **build the entire report from one anchor cell, using `LET`, with zero cells anywhere else in the workbook feeding into it.**

## Requirements

Your single formula must, in this order:

1. Find the **distinct regions that have at least one Shipped order** — not all 4 regions, only the ones actually represented among Shipped orders. *(Hint: `UNIQUE` of a `FILTER`, not `UNIQUE` of the raw column.)*
2. For each of those regions, compute: the **count** of Shipped orders, the **total revenue** (sum of `Total`) from Shipped orders, and the **average order value** for Shipped orders in that region. *(Hint: `MAP` a `LAMBDA` over your regions array for each metric — or one `LAMBDA` that returns multiple values via `HSTACK`, if you want to combine the three metrics in a single `MAP` pass.)*
3. Combine region name + the three metrics into one array with columns in the order: `Region, OrderCount, TotalRevenue, AvgOrderValue`. *(Hint: `HSTACK`.)*
4. **Sort** the combined result by `TotalRevenue` descending.
5. Wrap every intermediate step in `LET`, with a clear, honest name for each — no single-letter names.

## Expected result

Three regions qualify (one of the four regions has **zero** Shipped orders — figure out which one and why before you start building; it's a direct consequence of this dataset, not a bug in your formula). Sorted by revenue descending, your report should read approximately:

| Region | OrderCount | TotalRevenue | AvgOrderValue |
|--------|-----------:|-------------:|---------------:|
| South | 4 | 903.00 | 225.75 |
| North | 8 | 533.00 | 66.63 |
| East | 7 | 402.00 | 57.43 |

All three revenue figures must sum to **1838.00** — the company-wide Shipped total you already verified in Exercise 1. If your three numbers don't add up to that, a region's `FILTER` condition is wrong somewhere.

## Constraints

- **One cell, one formula.** No cell outside your `LET` formula may feed into it — not a helper `UNIQUE`, not a scratch `SUMIFS`, nothing. If you find yourself wanting a helper cell, that's a sign you need another named step inside `LET`, not a new cell.
- Every `LET`-named value must have a real, self-explanatory name (`shipped_regions`, not `sr`; `region_totals`, not `t`).
- Your formula must **recompute correctly** if the source data changes — don't hard-code the three region names, the count `3`, or any dollar figure anywhere in the formula.

## Hints

<details>
<summary>On step 2 — computing three metrics per region without three separate MAPs</summary>

You *can* just write three separate `MAP` calls (one for counts, one for revenue, one for the average, reusing the first two) inside the same `LET` — that's a completely valid solution and often the most readable one. If you want a single-pass version instead, a `LAMBDA` inside `MAP` can return more than one value per call by building a small `HSTACK` for each region and then stacking those with `VSTACK` — but this is meaningfully harder to get right and isn't required for a strong submission.

</details>

<details>
<summary>On figuring out which region is missing</summary>

Don't guess — build `UNIQUE(Orders!D2:D31)` (all 4 regions) in a scratch cell first, compare it against `UNIQUE(FILTER(Orders!D2:D31, Orders!J2:J31="Shipped"))` (only regions with a Shipped order), and see which name is in the first list but not the second. Delete the scratch cells once you've confirmed it — the final submission has zero helper cells, but there's nothing wrong with a scratch cell while you're investigating.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|---------------|
| Cell count | Report is built from 3+ linked cells | Exactly one anchor cell, everything inside `LET` |
| Correctness | Revenue figures don't sum to 1838.00 | All three regions' totals sum exactly to the company Shipped total |
| Robustness | Region names or counts are hard-coded | Formula would still work correctly if a new region appeared in the data |
| Naming | `LET` names are single letters or abbreviations | Every name reads as a clear English phrase |

## Submission

Commit `challenge-01.md` (your formula as text, copy-pasted from the formula bar, plus a two-sentence note on your design) to your portfolio under `c41-week-10/challenge-01/`.
