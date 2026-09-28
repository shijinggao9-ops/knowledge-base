# Exercise 2 — Group Dates & Show % of Total

**Goal:** Practice grouping a date field into months/quarters, grouping a numeric field into bins, and using Show Values As to turn raw sums into percentages and running totals — without writing a single formula.

**Estimated time:** 45 minutes.

## Setup

Continue in `crunch-week7`. Create a new sheet named `Ex2-Grouping` for this exercise's work.

## Tasks

1. **Group by month.** Build a pivot: `OrderDate` in Rows, grouped by **Month**; `TotalRevenue` (Sum) in Values. *(Expected 6 rows, Jan through Jun. Feb should be the lowest month; May should be the highest.)*

2. **Group by quarter.** On a fresh pivot, group `OrderDate` by **Quarter** instead. *(Expected: 2 rows — Q1 = 11,108.09, Q2 = 16,386.90. These two should sum to the same 27,494.99 grand total as every other pivot this week — if they don't, something about your source range is wrong.)*

3. **Bin a number.** Build a pivot: `Units` in Rows, grouped into bins of size **2** starting at 1 (so bins read roughly `1-2`, `3-4`, `5-6`); `OrderID` (Count) in Values. *(Expected: 3 bins, counts summing to 86.)*

4. **% of Grand Total.** Build a pivot: `Category` in Rows, `TotalRevenue` (Sum) in Values, Show Values As → **% of Grand Total**. *(Expected: Camping ≈ 31.0%, Electronics ≈ 24.7%, Footwear ≈ 21.0%, Apparel ≈ 16.7%, Accessories ≈ 6.6% — should sum to ~100%.)*

5. **% of Row Total.** Build a pivot: `Region` in Rows, `Channel` in Columns, `TotalRevenue` (Sum) in Values, Show Values As → **% of Row Total**. *(Expected: within North's row specifically, Online should be the clear majority — around 64%.)*

6. **Running total.** Build a pivot: `OrderDate` grouped by Month in Rows, `TotalRevenue` (Sum) in Values, Show Values As → **Running Total In** (by the Month field). *(Expected: the running total's last row, June, equals the grand total 27,494.99 — this is your built-in check that the running total is configured correctly.)*

7. **Rank.** Build a pivot: `SalesRep` in Rows, `TotalRevenue` (Sum) in Values twice — once plain, once Show Values As → **Rank Largest to Smallest**. *(Expected: Jack Rivera ranks #1; Nadia Osei ranks #8, last.)*

## Expected result (spot checks)

- Task 2 → Q1 = 11,108.09, Q2 = 16,386.90, sum = 27,494.99.
- Task 4 → percentages sum to (approximately) 100%.
- Task 6 → June's running total = 27,494.99, matching every other pivot's grand total this week.
- Task 7 → Jack Rivera is rank 1; Nadia Osei is rank 8.

## Done when…

- [ ] All 7 pivots exist on `Ex2-Grouping` (or clearly separated sheets/pivots), each labeled with the question it answers.
- [ ] You can explain, without looking it up, the difference between % of Row Total and % of Column Total.
- [ ] Your Task 6 running total's final value matches the grand total — if it doesn't, you've found and fixed the bug before moving on.
- [ ] All spot-check numbers match.

## Stretch

- Add a calculated field `RevenuePerUnit = TotalRevenue/Units` to any pivot from this exercise and put it in Values. Compare its value for Camping vs. Accessories — which category commands a higher revenue per unit sold?
- Group `OrderDate` by **Month-Year** (or Month + Year together in Excel's Group dialog) even though this dataset only spans one year — confirm it produces the same 6 rows as plain Month grouping, and explain in one sentence why that would stop being true on a 2-year dataset.

## Submission

Keep `Ex2-Grouping` in your `crunch-week7` workbook — no separate file needed, but be ready to walk through your pivots if asked in review.
