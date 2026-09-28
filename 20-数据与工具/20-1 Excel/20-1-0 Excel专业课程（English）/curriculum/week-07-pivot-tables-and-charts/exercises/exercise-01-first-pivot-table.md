# Exercise 1 — Build Your First Pivot Table

**Goal:** Get pivot table mechanics into your fingers — insert one, place fields into the four zones, switch aggregations, and read what the pivot is telling you. By the end, dragging a field into the right zone should feel automatic.

**Estimated time:** 45 minutes.

## Setup

Confirm your `Transactions` Table is set up (see the [week README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/README.md)) — an empty-cell check of `=COUNTA(Transactions[OrderID])` should show `86`. Create a new sheet named `Ex1-Pivot` for this exercise's work.

## Tasks

Build each pivot as its own separate pivot table (new pivot, or clear and rebuild the same one) so you can compare shapes. Note the "Expected" values as you go.

1. **Revenue by region.** Insert a pivot table. `Region` in Rows, `TotalRevenue` (Sum) in Values. *(Expected: 4 rows, Grand Total = 27,494.99. North should be the highest region.)*

2. **Switch the aggregation.** On the same pivot, change `TotalRevenue`'s summary function from Sum to **Average**. *(Expected: North's average order is roughly 376.83 — noticeably different from its Sum-based ranking story.)*

3. **Add a Count.** Add a second value field: `OrderID` set to **Count**. You should now see both Sum/Average of `TotalRevenue` and Count of `OrderID` side by side, per region. *(Expected counts: North 23, South 20, East 21, West 22.)*

4. **Two-level rows.** Build a fresh pivot: `Region` in Rows, then drag `Category` into Rows *underneath* it, `TotalRevenue` (Sum) in Values. Each region should expand to show its category breakdown nested inside. *(Expected: 4 region groups, each expandable into up to 5 category sub-rows.)*

5. **Crosstab with Columns.** Build a fresh pivot: `Region` in Rows, `Channel` in Columns, `TotalRevenue` (Sum) in Values. *(Expected: a 4-row × 3-column grid, e.g., West × Wholesale = 3,014.32.)*

6. **Filter it.** On the pivot from Task 5, drag `Category` into **Filters** and set it to show only `Camping`. *(Expected: the whole crosstab recalculates to camping-only revenue; South's Camping+Online cell should read 1,319.94 — that single largest order in the dataset.)*

7. **Count vs. Sum disagree.** Build a fresh pivot: `Category` in Rows, `OrderID` (Count) and `TotalRevenue` (Sum) both in Values. Identify which category has the *most orders* and which has the *most revenue* — write one sentence explaining why they're not the same category.

## Expected result (spot checks)

- Task 1 → Grand Total 27,494.99; North is the top region by Sum.
- Task 3 → Region order counts: North 23, South 20, East 21, West 22 (sums to 86).
- Task 6 → South's Camping revenue via Online channel = 1,319.94.
- Task 7 → Apparel has the most orders (21); Camping has the most revenue (8,535.29). Different categories.

## Done when…

- [ ] You've built at least 5 distinct pivot configurations on `Ex1-Pivot` (or clearly separated sheets), each labeled with a note stating what question it answers.
- [ ] You can explain, in one sentence, why Task 2's numbers looked completely different from Task 1's even though both used `TotalRevenue`.
- [ ] Task 7's one-sentence explanation is written down.
- [ ] All your numbers match the spot checks above.

## Stretch

- Build a pivot with `SalesRep` in Rows, `TotalRevenue` (Sum, Average, and Max) all three in Values side by side. Which rep has the highest *average* order — is it the same rep who has the highest *total*?
- Remove `TotalRevenue` from Values entirely and put `Units` (Sum) there instead — total units sold across all 86 orders should read **290**.

## Submission

Keep `Ex1-Pivot` in your `crunch-week7` workbook — no separate file needed, but be ready to walk through your pivots if asked in review.
