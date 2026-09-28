# Exercise 3 — Summarize With SUMIFS/COUNTIFS

**Goal:** Build the Region × Category summary matrix from Lecture 3 yourself, from a blank `Summary` sheet, using `SUMIFS` and `COUNTIFS` against structured references — then extend it with a rep breakdown.

**Estimated time:** 1.5 hours.

## Setup

Before starting, confirm your `Orders` Table is back to a clean **24 data rows**, `SUM(Orders[Total])` = **5240.60**. If you kept Exercise 2's Task 6 test row, delete it now (or complete Exercise 2's Stretch step) — this exercise's expected numbers assume the original 24 rows only.

Add a new sheet tab `Summary` (or clear the one from Lecture 3 if you still have it — build this one fresh either way, typing every formula yourself).

## Tasks

1. **Lay out the matrix skeleton.** In `A1:E1`, type: *(blank)*, `Electronics`, `Furniture`, `Office Supplies`, `Software`. In `A2:A5`, type: `North`, `South`, `East`, `West`.

2. **Write one `SUMIFS` formula in `B2`** that will work correctly filled across and down the whole grid:
   ```
   =SUMIFS(Orders[Total], Orders[Region], $A2, Orders[Category], B$1)
   ```
   Fill `B2` right through `E2`, then fill `B2:E2` down through row 5.

3. **Verify against these spot checks:**
   - `North`/`Electronics` (`B2`) → **180.00**
   - `South`/`Software` (`E3`) → **39.98**
   - `East`/`Furniture` (`C4`) → **2063.00**
   - `West`/`Office Supplies` (`D5`) → **33.47**

4. **Add row and column totals.** In `F1`, type `Total`. In `F2:F5`, `=SUM(B2:E2)` filled down (row totals). In `B6:E6`, `=SUM(B2:B5)` filled right (column totals), with `A6` labeled `Total`. `F6` (the grand total, either direction) must read **5240.60**.

5. **Build a second matrix: order *count* instead of dollar total.** Below the first matrix (starting row 9), rebuild the same layout but with `COUNTIFS` instead of `SUMIFS` in `B10`:
   ```
   =COUNTIFS(Orders[Region], $A10, Orders[Category], B$9)
   ```
   Fill it across and down the same way. *(Expected: `East`/`Software` = **2**; the grand total of every cell in this matrix = **24**, the total number of orders.)*

6. **Add a rep breakdown below both matrices.** In a new small table (starting row 18), list each of the 5 reps down column A and write one `SUMIFS` (total) and one `COUNTIFS` (order count) per rep:
   ```
   =SUMIFS(Orders[Total], Orders[Rep], $A19)
   =COUNTIFS(Orders[Rep], $A19)
   ```
   *(Expected: `J. Alvarez` total = **818.19**, count = **5**; `R. Diaz` total = **2254.97**, count = **5**; `T. Osei` total = **1311.49**, count = **4**.)*

7. **Prove it's live.** Go back to `Orders` and change order `1008`'s `Region` from `East` to `North` (a single cell edit, no structural change). *(Expected: without touching a single Summary-sheet formula, `East`/`Furniture` drops by 1745.00 to **318.00**, `North`/`Furniture` gains 1745.00 to become **1874.00**, and both matrices' grand totals stay at 5240.60/24 — only the distribution shifted.)* **Change it back to `East` before continuing**, so the rest of the week's expected numbers still match.

## Expected result (spot checks)

- Task 3 → all four spot-check cells match exactly.
- Task 4 → grand total 5240.60.
- Task 5 → grand total 24.
- Task 6 → J. Alvarez 818.19/5, R. Diaz 2254.97/5, T. Osei 1311.49/4.
- Task 7 → East/Furniture and North/Furniture both update the instant you change one cell, with no formula edits.

## Done when…

- [ ] Both matrices (dollar total and order count) are built from structured references, not `A2:A25`-style ranges.
- [ ] Every spot-check value matches.
- [ ] You've personally watched Task 7's live-update happen and reverted the test edit.
- [ ] The rep breakdown uses the same `SUMIFS`/`COUNTIFS` pattern, adapted to one criterion instead of two.

## Stretch

- Add a third criterion to one `SUMIFS` cell: total sales in the `East` region, `Software` category, **for orders of 3+ units** (`Orders[Qty]`, `">=3"`). Expect **445.00** — of the two East/Software orders (1020 at qty 5, 1024 at qty 2), only order 1020 clears the `>=3` bar, so it alone survives the third criterion.
- Using the `+`-of-two-`SUMIFS` pattern from Lecture 3 Section 5, compute total sales for `Electronics` **or** `Furniture` in one cell, and confirm it equals `SUM(Orders[Total]) - (Office Supplies total) - (Software total)` as a sanity cross-check.

## Submission

Commit the workbook to your portfolio under `c41-week-06/exercise-03/`.
