# Exercise 1 — Build a Live FILTER Report

**Goal:** Get `FILTER`, `SORT`, and `UNIQUE` into your fingers — alone, nested together, and with multi-condition boolean math. By the end, reaching for a spilling formula instead of a helper column feels automatic.

**Estimated time:** 1–1.5 hours.

## Setup

You already have the `Orders` data loaded (see the [week README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/README.md)). Confirm the checksums:

```excel
=SUM(Orders!I2:I31)                                    ' must show 3748.00
=SUMIFS(Orders!I2:I31, Orders!J2:J31, "Shipped")        ' must show 1838.00
```

Work on the `Report` tab. Put a bold label above each task (`Task 1`, `Task 2`, ...) so your spill ranges don't collide with each other — leave at least 6 empty rows between tasks.

## Tasks

1. **Unique regions.** `=UNIQUE(Orders!D2:D31)`. *(Expected: 4 values, in this order: North, West, East, South.)*

2. **Unique products, alphabetized.** Nest `UNIQUE` inside `SORT`. *(Expected: 8 products, Bluetooth Speaker first alphabetically.)*

3. **Shipped orders only.** `=FILTER(Orders!A2:J31, Orders!J2:J31="Shipped")`. *(Expected: 19 rows.)*

4. **Shipped orders, highest Total first.** Nest Task 3's filter inside `SORT`, sorting by column 9 descending. *(Expected: same 19 rows, now led by order 3028, Total 516.00.)*

5. **Two-condition AND.** Use `FILTER` with the `*` pattern to get every order that is `Wearables` category **and** `Shipped` status. *(Expected: 4 rows, totaling 270.00 — check with a `SUM` wrapped around your `FILTER`.)*

6. **Two-condition OR.** Every order in `East` **or** `South` region, `Shipped` status. Use `+` for the region OR, `*` to combine with the status AND. *(Expected: 11 rows, totaling 1305.00.)*

7. **An empty result, handled properly.** Filter for orders that are in the `North` region **and** have `Status` of `Pending` **or** `Cancelled`. *(Expected: this genuinely matches zero rows — every North order shipped. Without an `if_empty` argument you'll get `#CALC!`; add `"No matching orders"` as the third argument and confirm it displays instead of erroring.)*

8. **Multi-key sort.** Sort the whole `Orders` range first by `Region` ascending, then by `Total` descending within each region, using the `{col1,col2}`/`{1,-1}` array syntax from Lecture 1. *(Expected: still 30 rows; the first few should all be `East` region, highest `East` total first.)*

9. **Distinct combinations.** `UNIQUE` on `Region` and `Category` together (two full columns, not one). *(Expected: 8 distinct (Region, Category) pairs — check by counting your spill.)*

10. **Top 5, ranked.** Take Task 4's sorted-Shipped-orders formula and wrap it with `TAKE` to keep only the first 5 rows. *(Expected: the same 5 orders as the worked "top 5" example in Lecture 1 — Total values 516.00, 177.00, 129.00, 129.00, 129.00.)*

## Expected result (spot checks)

- Task 1 → 4 regions, North first.
- Task 3 → 19 rows.
- Task 5 → 4 rows, sum 270.00.
- Task 6 → 11 rows, sum 1305.00.
- Task 7 → `#CALC!` without `if_empty`; `"No matching orders"` with it.
- Task 10 → top Total is 516.00 (order 3028).

## Done when…

- [ ] All 10 tasks have a labeled spill formula on the `Report` tab.
- [ ] Task 7 demonstrates both the broken (`#CALC!`) and fixed (`if_empty`) versions, side by side, with a one-line note explaining what changed.
- [ ] You can explain, out loud, why Task 6 uses `+` and Task 5 uses `*`.
- [ ] Every row count above matches what your spill actually shows.

## Stretch

- Rebuild Task 6 using `SORTBY` instead of `SORT`, sorting the Rep/Product/Total-only columns by the full `Total` column even though `Total` itself isn't displayed.
- Add a Task 11: the single highest-Total order in the whole dataset regardless of status, returned as a one-row `FILTER` (hint: compare `Total` to `MAX(Orders!I2:I31)`).

## Submission

Commit your workbook (or a screenshot + formula list) to your portfolio under `c41-week-10/exercise-01/`.
