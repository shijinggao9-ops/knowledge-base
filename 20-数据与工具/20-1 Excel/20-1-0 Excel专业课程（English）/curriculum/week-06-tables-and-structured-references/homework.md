# Week 6 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on formula practice, a written explanation, and a build-your-own-Table task. Commit each.

All formulas run against the `Orders` Table from the [README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/README.md) unless a problem says otherwise. Keep the Table at its original 24 rows for Problems 1–3; Problem 5 has you extend it deliberately.

---

## Problem 1 — Twenty warm-up `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` (75 min)

Write and run each as a structured-reference formula. Put them in a `Checks` sheet with a `-- N` comment above each, and note the result beneath.

1. Total sales for rep `M. Chen`. *(Expect 570.98, 5 orders.)*
2. Count of orders with `Qty` exactly `1`. *(Expect 8.)*
3. Total sales in the `West` region. *(Expect 1614.97, 6 orders.)*
4. Total sales in `Office Supplies` where `Qty >= 2`. *(Expect 143.43, 4 orders.)*
5. Total sales in the `Electronics` category. *(Expect 986.97, 5 orders.)*
6. Total sales for rep `S. Kim`. *(Expect 284.97, 5 orders.)*
7. Total sales in `North` region, `Software` category. *(Expect 99.97, 2 orders.)*
8. Total sales in `South` region, `Furniture` category. *(Expect 258.00, 1 order.)*
9. Count and total of orders with `Qty` exactly `2`. *(Expect 938.44, 8 orders.)*
10. Total and count of orders with `UnitPrice >= 50`. *(Expect 4594.50, 10 orders.)*
11. Average order value across every order (plain `AVERAGE`, not `AVERAGEIFS`). *(Expect ≈218.36.)*
12. The single largest order's `Total`, and the `Product` on that order, using `XLOOKUP` on the structured `Total` column. *(Expect 1745.00, "Standing Desk".)*
13. The single smallest order's `Total` and `Product`. *(Expect 8.25, "Sticky Notes".)*
14. Count of distinct categories represented among orders placed by `T. Osei`. *(Hint: list them by eye first — there are only 4 categories total — then count with `COUNTIFS` per category and count the non-zero results.)*
15. Total sales for orders placed in the first half of February (`OrderDate <= 2026-02-15`) vs. the second half. *(Two formulas. Expect 3668.42 for the first half, 1572.18 for the second — they must sum to 5240.60.)*
16. Total sales where `Region` is `East` **or** `West` (use the `SUMIFS + SUMIFS` `OR` pattern from Lecture 3). *(Expect 4274.21.)*
17. Average `UnitPrice` for the `Furniture` category only. *(Expect ≈191.10.)*
18. Count of orders where `Category` is `Furniture` **and** `Category` is `Electronics` at the same time. *(Trick question — think about why a single row can never satisfy both, and explain what the correct `COUNTIFS` for "Furniture or Electronics" would need instead.)*
19. Total sales for the rep with the **highest** total (don't hard-code the name — find it, then confirm with a formula).
20. `COUNT(Orders[OrderID])` vs. `COUNTA(Orders[Rep])` vs. `ROWS(Orders[#Data])` — run all three. *(Expect all three return 24 — explain in one sentence why these three genuinely different formulas land on the same answer here.)*

---

## Problem 2 — Explain structured references (45 min)

In `structured-refs-writeup.md`, answer in prose (no more than 400 words total):

1. In your own words, what does the `@` symbol mean inside a structured reference, and what breaks if you accidentally omit it in a formula meant to compute a per-row value?
2. Give a concrete example (can be from this week's `Orders` Table or invented) of a formula that would silently return the *wrong* answer after a column insert if it used `D2` instead of `[@UnitPrice]`.
3. Explain the difference between `Orders[Total]` and `Orders[[#Totals],[Total]]` — what does each one actually point at?
4. Why does `SUMIFS` list its sum range *first*, while the older `SUMIF` lists it *last* — and why might that argument-order difference matter more than it seems?

---

## Problem 3 — Structured references across two engines (45 min)

The same summary, two ways. In a new sheet `CrossCheck`:

1. Build one `SUMIFS` cell using structured references: total sales in `Software`, `Qty >= 2`.
2. Build the *same* total using a plain `A2:A25`-style range formula instead (temporarily — this is for comparison only, not to keep).
3. Confirm both return the identical number.
4. Now insert one new row into the Table, in the middle, with `Category = "Software"` and `Qty = 3`. Re-check both formulas.

**Deliver** the two formulas plus a two-sentence note: which one updated correctly, which one didn't, and exactly what about its range definition caused the difference.

---

## Problem 4 — Build a second Table from scratch (60 min)

Make a second, independent Table in the same workbook (new sheet, e.g. `Inventory`) — a small stock list: `SKU`, `Product`, `Category`, `OnHand`, `ReorderPoint`, at least 10 rows of your own invented data.

1. Convert it to a Table named `Inventory`.
2. Add a computed column `NeedsReorder` = `[@OnHand] < [@ReorderPoint]` (a `TRUE`/`FALSE` formula).
3. Add a `COUNTIFS` cell counting how many items currently need reordering.
4. Add 3 new rows and confirm the reorder count updates automatically.

**Deliver** the workbook with both `Orders` and `Inventory` Tables intact.

---

## Problem 5 — Extend the dataset (60 min)

Make the `Orders` data your own and query it.

1. Add **5 new orders** of your invention directly into the Table (typed into the row below the last one, per Lecture 1's auto-expansion). Include at least: one in a brand-new `Region` not currently in the dataset (e.g., `"Central"`), one with the highest `Total` in the whole Table, and one in `Category = "Software"`.
2. Confirm the Table now has 29 data rows and the Total Row's `Total` cell reflects the new grand total.
3. Go back to your `Summary` sheet's Region × Category matrix (from Exercise 3 / the mini-project). Since your new `"Central"` region wasn't a row label in that matrix, its orders currently aren't captured by any matrix cell — **add a `Central` row to the matrix** and confirm its `SUMIFS` formulas (copied from an existing row, same structured-reference pattern) correctly pick up just the new Central orders.
4. Then **undo** it cleanly: delete the 5 rows you added (Table → right-click → Delete → Table Rows) and remove the `Central` row from the matrix, confirming you're back to the original 24-row, 5240.60 state.

**Deliver** a before/after note: the Total Row's `Total` value before adding rows, immediately after, and after cleanup (should match the "before" exactly) — plus one sentence on what surprised you about extending a Table compared to extending a plain range.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 45 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 60 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/mini-project/README.md).
