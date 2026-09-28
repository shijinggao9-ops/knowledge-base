# Week 7 — Pivot Tables & Charts

> **Goal:** by Sunday you can take a raw, unsummarized transactions sheet and answer almost any "by X, what is Y?" business question about it in under a minute — build the pivot, group the dates, add the calculated field, show the percentage, and chart it clearly — in both Excel and Google Sheets, without reaching for a tutorial.

Welcome to **C41 · Crunch Excel**, Week 7. Everything through Week 6 was about one row at a time — a formula that looks at a row and computes something for *that* row. This week flips the lens: instead of one row, you're going to summarize **all of them at once**, by whatever dimension a stakeholder cares about. That flip — from "what does this row say" to "what do these 10,000 rows say, grouped by region" — is the single biggest jump in analytical power this course teaches, and the tool that makes it possible is the **pivot table**.

A pivot table takes a flat, row-per-transaction table and lets you reshape it — drag a field into "rows," another into "values," pick an aggregation — and it answers questions instantly that would otherwise take a page of nested `SUMIF`s. Pair it with the right **chart**, and a wall of numbers becomes a picture someone can understand in three seconds. This week you build both skills against one real dataset: a season of sales transactions for a fictional outdoor-gear company, **Crunch Outfitters**.

## Learning objectives

By the end of this week, you will be able to:

- **Build** pivot tables that summarize thousands of rows by any dimension — inserting one from a range or Table, and understanding why a Table source matters.
- **Configure** the four pivot zones (Rows, Columns, Values, Filters) and choose the right aggregation (Sum, Count, Average, Max, Min) for the question being asked.
- **Group** dates into months/quarters/years and numbers into custom bins, and add **calculated fields** that derive new metrics from existing ones.
- **Use "Show Values As"** to reframe raw numbers as % of total, running totals, and rank — without writing a single formula.
- **Choose the right chart type** for a given question, build both regular charts and pivot charts, and strip out the chart-junk that makes charts lie or confuse.
- **Work in both Excel and Google Sheets**, knowing exactly where the two tools' pivot and chart workflows differ.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `QMB 3200` — Summarise thousands of rows with a pivot table — grouping, calculated fields, and values reframed as a share of the total — and choose a chart that answers the question actually asked. |
| Industry | Answer a sales director's fifteen questions in the order they are asked, each within a minute or two, from one dataset and without a new file per question. |
| Beyond the bar | Reproduce a chart that misleads, name the specific device doing the misleading, then rebuild it honestly — `challenges/challenge-02-misleading-chart-fix.md` |


## Prerequisites

- Weeks 1–6 of this course — in particular **Week 6 (Tables & structured references)**. This week's source data lives in a Table, and pivot tables built on a Table auto-expand as rows are added, which is exactly why Week 6 came first.
- Excel (365, 2021, or the web) and/or Google Sheets, same as every prior week.
- No prior pivot-table or charting experience assumed.

## Set up this week's dataset (do this first)

Every lecture, exercise, challenge, and the mini-project this week runs against the **same 86-row transactions log** — six months (January–June 2025) of sales for Crunch Outfitters, an outdoor-gear company with four sales regions, eight reps, five product categories, and three sales channels (Online, Retail, Wholesale). Eighty-six rows is a small, checkable stand-in for what a real export looks like — in the wild this same workflow scales cleanly to hundreds of thousands of rows without changing a single technique you learn this week.

**Step 1 — Create the workbook.** Open a blank workbook/sheet (Excel: `crunch-week7.xlsx`; Sheets: `crunch-week7`). Rename the first sheet `Transactions`.

**Step 2 — Paste the data.** Copy the block below (including the header row) and paste it starting at `A1`. It's comma-separated — in Excel, use **Data → Text to Columns → Delimited → Comma** after pasting into column A if it lands as one column; Google Sheets usually auto-splits pasted CSV text on paste (if it doesn't, use **Data → Split text to columns**).

```csv
OrderID,OrderDate,Region,SalesRep,Category,Product,Channel,Units,UnitPrice,Discount,TotalRevenue
1001,2025-01-21,North,Priya Shah,Camping,Compact Camp Stove,Online,3,59.99,0.00,179.97
1002,2025-01-24,North,Priya Shah,Footwear,Cascade Trail Runners,Online,4,99.99,0.00,399.96
1003,2025-01-07,South,Elena Ruiz,Electronics,SolarCharge Power Bank,Retail,2,44.99,0.15,76.48
1004,2025-01-18,West,Jack Rivera,Accessories,Trekker Daypack 28L,Online,5,74.99,0.00,374.95
1005,2025-01-25,South,Tom Baker,Apparel,Ridgeline Fleece Pullover,Online,3,64.99,0.00,194.97
1006,2025-01-04,North,Marcus Lee,Apparel,Summit Rain Jacket,Retail,3,129.99,0.10,350.97
1007,2025-01-09,North,Marcus Lee,Electronics,SolarCharge Power Bank,Wholesale,1,44.99,0.05,42.74
1008,2025-01-03,East,Sam Chen,Footwear,Cascade Trail Runners,Retail,2,99.99,0.00,199.98
1009,2025-01-22,South,Tom Baker,Apparel,Summit Rain Jacket,Wholesale,2,129.99,0.05,246.98
1010,2025-01-09,West,Wendy Kim,Camping,Alpine 2-Person Tent,Online,3,219.99,0.15,560.97
1011,2025-01-09,North,Priya Shah,Electronics,SolarCharge Power Bank,Online,6,44.99,0.05,256.44
1012,2025-01-13,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Retail,3,24.99,0.00,74.97
1013,2025-02-08,North,Marcus Lee,Camping,Basecamp Sleeping Bag,Online,3,149.99,0.10,404.97
1014,2025-02-23,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Online,4,24.99,0.15,84.97
1015,2025-02-15,South,Tom Baker,Camping,Alpine 2-Person Tent,Retail,2,219.99,0.10,395.98
1016,2025-02-09,West,Wendy Kim,Apparel,Ridgeline Fleece Pullover,Wholesale,2,64.99,0.00,129.98
1017,2025-02-17,West,Jack Rivera,Electronics,Trailhead Headlamp,Wholesale,1,32.99,0.00,32.99
1018,2025-02-21,South,Tom Baker,Footwear,Cascade Trail Runners,Online,1,99.99,0.10,89.99
1019,2025-02-15,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Online,6,24.99,0.10,134.95
1020,2025-02-25,East,Sam Chen,Apparel,Summit Rain Jacket,Online,3,129.99,0.05,370.47
1021,2025-02-01,East,Nadia Osei,Electronics,SolarCharge Power Bank,Wholesale,1,44.99,0.00,44.99
1022,2025-02-27,South,Elena Ruiz,Apparel,Ridgeline Fleece Pullover,Online,2,64.99,0.10,116.98
1023,2025-02-01,East,Sam Chen,Footwear,Trailblazer Hiking Boots,Wholesale,1,89.99,0.00,89.99
1024,2025-03-08,North,Priya Shah,Footwear,Glacier Insulated Boots,Wholesale,5,159.99,0.00,799.95
1025,2025-03-24,West,Jack Rivera,Electronics,Trailhead Headlamp,Retail,5,32.99,0.00,164.95
1026,2025-03-22,West,Jack Rivera,Electronics,TrailCam GPS Watch,Wholesale,5,249.99,0.05,1187.45
1027,2025-03-31,South,Elena Ruiz,Camping,Compact Camp Stove,Online,3,59.99,0.15,152.97
1028,2025-03-21,East,Sam Chen,Footwear,Glacier Insulated Boots,Online,5,159.99,0.00,799.95
1029,2025-03-08,North,Marcus Lee,Footwear,Trailblazer Hiking Boots,Retail,5,89.99,0.10,404.95
1030,2025-03-08,North,Priya Shah,Camping,Compact Camp Stove,Online,6,59.99,0.00,359.94
1031,2025-03-29,North,Marcus Lee,Apparel,Summit Rain Jacket,Online,5,129.99,0.15,552.46
1032,2025-03-16,South,Elena Ruiz,Camping,Compact Camp Stove,Retail,5,59.99,0.00,299.95
1033,2025-03-26,West,Wendy Kim,Accessories,EcoFlow Water Bottle,Online,1,18.99,0.05,18.04
1034,2025-03-12,West,Wendy Kim,Accessories,Trekker Daypack 28L,Online,6,74.99,0.15,382.45
1035,2025-03-21,North,Priya Shah,Camping,Basecamp Sleeping Bag,Online,6,149.99,0.00,899.94
1036,2025-03-08,South,Elena Ruiz,Electronics,SolarCharge Power Bank,Online,4,44.99,0.00,179.96
1037,2025-03-09,West,Jack Rivera,Accessories,Peak Trekking Poles,Online,1,54.99,0.10,49.49
1038,2025-04-04,North,Priya Shah,Apparel,Summit Rain Jacket,Online,2,129.99,0.05,246.98
1039,2025-04-16,South,Tom Baker,Footwear,Glacier Insulated Boots,Online,1,159.99,0.00,159.99
1040,2025-04-13,East,Sam Chen,Electronics,TrailCam GPS Watch,Retail,4,249.99,0.15,849.97
1041,2025-04-26,West,Jack Rivera,Accessories,EcoFlow Water Bottle,Online,3,18.99,0.00,56.97
1042,2025-04-19,North,Marcus Lee,Footwear,Trailblazer Hiking Boots,Retail,1,89.99,0.10,80.99
1043,2025-04-30,South,Elena Ruiz,Electronics,SolarCharge Power Bank,Wholesale,1,44.99,0.00,44.99
1044,2025-04-20,North,Priya Shah,Camping,Basecamp Sleeping Bag,Wholesale,1,149.99,0.10,134.99
1045,2025-04-08,North,Priya Shah,Camping,Basecamp Sleeping Bag,Retail,6,149.99,0.10,809.95
1046,2025-04-11,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Online,6,24.99,0.00,149.94
1047,2025-04-13,South,Tom Baker,Accessories,Trekker Daypack 28L,Wholesale,3,74.99,0.00,224.97
1048,2025-04-01,West,Jack Rivera,Apparel,Summit Rain Jacket,Online,5,129.99,0.00,649.95
1049,2025-04-05,East,Nadia Osei,Footwear,Glacier Insulated Boots,Online,2,159.99,0.00,319.98
1050,2025-04-15,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Online,5,24.99,0.15,106.21
1051,2025-04-04,South,Tom Baker,Apparel,Summit Rain Jacket,Retail,1,129.99,0.00,129.99
1052,2025-04-09,East,Nadia Osei,Camping,Compact Camp Stove,Online,3,59.99,0.15,152.97
1053,2025-04-28,East,Sam Chen,Electronics,TrailCam GPS Watch,Online,1,249.99,0.05,237.49
1054,2025-05-27,East,Nadia Osei,Footwear,Trailblazer Hiking Boots,Retail,3,89.99,0.15,229.47
1055,2025-05-09,South,Tom Baker,Electronics,SolarCharge Power Bank,Online,6,44.99,0.00,269.94
1056,2025-05-04,North,Priya Shah,Electronics,SolarCharge Power Bank,Retail,1,44.99,0.10,40.49
1057,2025-05-18,South,Tom Baker,Camping,Alpine 2-Person Tent,Online,1,219.99,0.00,219.99
1058,2025-05-29,East,Nadia Osei,Apparel,Summit Merino Socks (3-pack),Retail,2,24.99,0.00,49.98
1059,2025-05-25,West,Jack Rivera,Footwear,Glacier Insulated Boots,Wholesale,2,159.99,0.00,319.98
1060,2025-05-29,West,Jack Rivera,Camping,Alpine 2-Person Tent,Wholesale,6,219.99,0.05,1253.94
1061,2025-05-26,South,Tom Baker,Camping,Alpine 2-Person Tent,Online,6,219.99,0.00,1319.94
1062,2025-05-28,West,Jack Rivera,Accessories,EcoFlow Water Bottle,Online,4,18.99,0.00,75.96
1063,2025-05-08,North,Priya Shah,Camping,Basecamp Sleeping Bag,Online,3,149.99,0.00,449.97
1064,2025-05-31,East,Sam Chen,Apparel,Summit Merino Socks (3-pack),Online,5,24.99,0.10,112.45
1065,2025-05-11,North,Priya Shah,Footwear,Glacier Insulated Boots,Online,3,159.99,0.00,479.97
1066,2025-05-02,North,Marcus Lee,Apparel,Ridgeline Fleece Pullover,Retail,6,64.99,0.05,370.44
1067,2025-05-20,North,Marcus Lee,Footwear,Glacier Insulated Boots,Online,5,159.99,0.00,799.95
1068,2025-05-23,West,Jack Rivera,Electronics,SolarCharge Power Bank,Retail,5,44.99,0.15,191.21
1069,2025-05-24,South,Tom Baker,Camping,Basecamp Sleeping Bag,Wholesale,1,149.99,0.00,149.99
1070,2025-05-20,East,Nadia Osei,Camping,Compact Camp Stove,Online,3,59.99,0.15,152.97
1071,2025-05-14,East,Sam Chen,Camping,Compact Camp Stove,Retail,3,59.99,0.00,179.97
1072,2025-06-14,West,Jack Rivera,Footwear,Cascade Trail Runners,Online,5,99.99,0.10,449.95
1073,2025-06-27,North,Marcus Lee,Electronics,TrailCam GPS Watch,Online,2,249.99,0.10,449.98
1074,2025-06-20,East,Sam Chen,Accessories,Trekker Daypack 28L,Retail,4,74.99,0.10,269.96
1075,2025-06-16,South,Elena Ruiz,Electronics,TrailCam GPS Watch,Retail,5,249.99,0.10,1124.96
1076,2025-06-11,North,Priya Shah,Apparel,Summit Merino Socks (3-pack),Online,3,24.99,0.00,74.97
1077,2025-06-05,North,Priya Shah,Accessories,EcoFlow Water Bottle,Retail,4,18.99,0.00,75.96
1078,2025-06-15,West,Jack Rivera,Camping,Compact Camp Stove,Online,6,59.99,0.05,341.94
1079,2025-06-08,South,Elena Ruiz,Footwear,Glacier Insulated Boots,Retail,1,159.99,0.00,159.99
1080,2025-06-06,West,Jack Rivera,Electronics,SolarCharge Power Bank,Wholesale,2,44.99,0.00,89.98
1081,2025-06-15,South,Tom Baker,Apparel,Summit Merino Socks (3-pack),Wholesale,5,24.99,0.10,112.45
1082,2025-06-11,West,Wendy Kim,Accessories,Peak Trekking Poles,Online,5,54.99,0.00,274.95
1083,2025-06-24,West,Wendy Kim,Electronics,TrailCam GPS Watch,Retail,2,249.99,0.00,499.98
1084,2025-06-25,West,Jack Rivera,Electronics,TrailCam GPS Watch,Online,4,249.99,0.00,999.96
1085,2025-06-08,East,Sam Chen,Apparel,Ridgeline Fleece Pullover,Online,5,64.99,0.00,324.95
1086,2025-06-08,West,Jack Rivera,Camping,Compact Camp Stove,Online,2,59.99,0.05,113.98
```

**Step 3 — Turn it into a Table.** Select any cell inside the data, then:

- **Excel:** `Ctrl+T` (Windows) / `Cmd+T` (Mac) → confirm "My table has headers" → name it `Transactions` in the Table Design tab's Table Name box.
- **Google Sheets:** select the full range → **Insert → Table** (or keep it as a plain named range via **Data → Named ranges** if your Sheets version doesn't offer Tables yet — either works for this week; a Table is preferred because it auto-expands).

**Sanity check** — this should read `86` in an empty cell: `=COUNTA(Transactions[OrderID])` (Excel structured reference) or `=COUNTA(A2:A87)` (plain range). Grand total revenue should read **$27,494.99**: `=SUM(Transactions[TotalRevenue])` or `=SUM(K2:K87)`.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Setup; pivot mechanics, the four zones | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Aggregation choices, refreshing | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Grouping dates/numbers, calculated fields | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Show Values As: %, running total, rank | 0h | 1.5h | 1h | 0.5h | 1h | 1h | 5h |
| Friday | Charts that communicate; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (15 sales questions) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **5.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-pivot-table-mechanics.md](01-pivot-table-mechanics.md) | The four zones, aggregation choices, refreshing, "by X, what is Y?" | 2h |
| 2 | [lecture-notes/02-grouping-and-calculations.md](02-grouping-and-calculations.md) | Grouping dates/numbers, calculated fields, Show Values As | 2h |
| 3 | [lecture-notes/03-charts-that-communicate.md](03-charts-that-communicate.md) | Chart-type-to-question fit, pivot charts, avoiding chart-junk | 2h |
| 4 | [exercises/exercise-01-first-pivot-table.md](exercise-01-first-pivot-table.md) | Build your first pivot table | 1h |
| 5 | [exercises/exercise-02-group-and-percent.md](exercise-02-group-and-percent.md) | Group dates & show % of total | 1h |
| 6 | [exercises/exercise-03-pick-the-chart.md](exercise-03-pick-the-chart.md) | Pick the right chart | 1h |
| 7 | [challenges/challenge-01-answer-with-pivots.md](challenge-01-answer-with-pivots.md) | Answer 15 questions with pivots | 1.5h |
| 8 | [challenges/challenge-02-misleading-chart-fix.md](challenge-02-misleading-chart-fix.md) | Fix a misleading chart | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/mini-project/README.md) | Answer 15 sales questions with pivots + pivot charts | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/homework.md) | Extra practice, spaced out | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/resources.md) | Official docs + the few links worth your time | — |

## By the end of this week you can…

- Look at a raw transactions export and, in under a minute, produce a summary by any dimension the export contains.
- Choose the right aggregation for a question, and explain why `COUNT` and `SUM` can rank the same dimension in a different order.
- Group a date column into months/quarters and a numeric column into bins, without a single helper formula.
- Add a calculated field, and reframe raw sums as % of total, running total, or rank using Show Values As.
- Pick a chart type that matches the question and strip a chart down to what actually helps the reader.

## Up next

[Week 8 — Dashboards & visualization](../week-08-dashboards-and-visualization/) — once pivots and charts are fluent, we assemble several of them into a single interactive dashboard screen.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
