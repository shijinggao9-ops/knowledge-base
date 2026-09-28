# Week 7 — Homework

A practice set to tie the week together. Spread this across the week rather than doing it all in one sitting — pivot configuration only becomes automatic through repetition. Budget roughly 5 hours total.

## How to use this

Each task below is short (10–30 minutes) and targets a specific skill from the lectures. Do them in a fresh area of your `crunch-week7` workbook (a `Homework` sheet group, or one sheet per part) so nothing collides with the exercises, challenges, or mini-project.

## Part A — Pivot mechanics reps (≈1 hour)

1. Build five separate one-question pivots, each answering a different "by X, what is Y?" shape, using five **different** dimension fields from `Transactions` (not just Region — try `SalesRep`, `Channel`, `Product`, and two others). For each, write the field you put in Rows, the field and aggregation you put in Values, and the answer.
2. Build one pivot with `Region` in Rows and `Category` in Columns, `TotalRevenue` (Sum) in Values. Then **swap** them — `Category` in Rows, `Region` in Columns. Confirm the grand total is identical either way, and write one sentence on when you'd prefer one layout over the other (hint: think about which one has more values along each axis, and which is easier to scan).
3. Deliberately break refresh in Excel: build a plain pivot (any configuration), then go change one cell's `TotalRevenue` value directly in `Transactions`. Confirm the pivot does **not** update until you manually refresh. Then repeat the same test in Google Sheets and note the difference in your homework notes.
4. Add a brand-new row (order `1087`, any realistic values) directly below the last row of the `Transactions` Table. Confirm a pivot built on the Table's structured reference picks it up after a refresh, without you touching the pivot's source range setting.

## Part B — Grouping and calculated fields (≈1.5 hours)

5. Group `OrderDate` by **Week** instead of Month (Excel: Group dialog, set "Days" grouping to 7-day intervals starting on your first order date; Sheets: try the closest native grouping option, or note if your version doesn't support weekly grouping directly). Compare the shape of a weekly trend chart to the monthly one from Lecture 2 — is weekly too granular to read at a glance, or does it reveal something month-level grouping hid?
6. Build a numeric grouping on `UnitPrice` instead of `Units` — bin it into ranges of $50 (e.g., $0–50, $50–100, etc.) and count orders per price bin. Which price bin has the most orders?
7. Add a second calculated field: `DiscountedAmount = TotalRevenue * Discount` is *not* quite right (Discount is already baked into TotalRevenue) — instead build `EffectiveDiscountRate`, roughly `1 - (TotalRevenue / (Units * UnitPrice))`, and put it in Values by Category. Which category has the highest effective average discount rate applied? *(This is a deliberately trickier calculated field — expect to iterate on the formula once or twice before it reads correctly.)*
8. Build a pivot with `Category` in Rows, `TotalRevenue` (Sum) in Values, and **three** Show Values As variants of the same field side by side: No Calculation, % of Grand Total, and Rank Largest to Smallest. Confirm all three tell a consistent story (the category ranked #1 should also have the highest % of grand total).

## Part C — Charts (≈1.5 hours)

9. Build the same monthly revenue data as three different chart types: line, column, and area. Write one sentence on which felt clearest for a trend question, and one sentence on when an area chart's filled-in look might actually mislead (hint: think about what the filled area *visually* implies about cumulative totals versus what it's actually showing).
10. Take any pivot chart you've already built and intentionally add a second, unrelated value field on a secondary axis (a dual-axis chart) — e.g., revenue on the left axis, order count on the right. Does the chart make it look like the two series move together more than they actually do? Write two sentences on what you observed.
11. Build a chart comparing `SalesRep` revenue, then apply direct data labels (the value shown right on or next to each bar) and remove the legend entirely (a single-series chart doesn't need one). Compare readability to the same chart with a legend and no data labels.
12. Pick any two charts you've built this week and make sure their color for the same category (e.g., "Camping") matches across both. Write one sentence on why this consistency matters once a report has more than 2–3 charts in it.

## Part D — Reflection (≈30 min)

13. In a few sentences: which pivot configuration (Rows/Columns/Values/Filters combination) do you predict you'll reach for most often in real work, and why?
14. Open any spreadsheet report you've seen before (school, work, a template, a news article's embedded chart) and find one chart that violates at least one of Lecture 3's readability rules. Describe the violation and how you'd fix it, using this week's vocabulary (zero baseline, chart-junk, direct labels, etc.).

## Submission

Keep your homework work in a `Homework` area of your workbook (or a separate file) — no formal submission format required, but be ready to reference specific tasks if asked in review.
