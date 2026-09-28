# Week 11 — Power Query & Data Connections

> **Goal:** by Sunday you can pull raw data from a file, a folder of files, or a web page into Power Query; shape it with repeatable transform steps (split, unpivot, type-convert, filter, group); merge and append it against a second source; and hit **Refresh** and watch the whole pipeline re-run itself against new data with zero manual rework.

Welcome back to **C41 · Crunch Excel**. Every week so far has started the same way: you typed or pasted a clean-ish dataset into a sheet by hand, then built formulas, Tables, pivots, or models on top of it. That's not how data actually arrives in a real job. It arrives as a CSV attached to an email, a folder of CSVs — one per warehouse, one per week — a report copy-pasted out of another system in the wrong shape, or a table sitting on a web page you don't control. And it arrives *again* next week, in the same messy shape, needing the exact same cleanup you just did by hand. This week is about refusing to do that cleanup by hand twice.

**Power Query** (Excel's "Get & Transform," built into every modern Excel and available as an add-in for older versions) is a dedicated ETL tool living inside your spreadsheet app — **E**xtract data from a source, **T**ransform it into the shape you need, **L**oad the result somewhere useful. Every click you make in its editor — promote headers, split a column, remove a row, change a type — is recorded as a named, reorderable **step**. Once the steps are recorded, they're not a one-time cleanup; they're a saved recipe. Next week, when the source file changes, you click **Refresh** and the exact same sequence of operations runs again, automatically, against the new data. You clean it once. You benefit from that cleanup forever.

This week runs one continuous scenario: **Crunch Wholesale**, a distributor with three regional warehouses (North, South, West), each exporting a CSV of that week's orders. You'll clean one messy export by hand-guided steps, unpivot a wide monthly report into a proper long table, merge orders against a product lookup table to pull in category and supplier data, then combine all three warehouses' files from a folder into one refreshable pipeline — the exact shape of a real weekly reporting job.

## Learning objectives

By the end of this week, you will be able to:

- **Import data** into Power Query from a single file, an entire folder of files, a web page, and (conceptually) a database connection — and explain what "connection only" vs. "load to a Table" vs. "load to the Data Model" each mean for where the data ends up.
- **Navigate the Power Query editor** — the ribbon, the Applied Steps pane, the formula bar (the `M` language peeking through), and the data preview — well enough to build, reorder, rename, and delete steps deliberately.
- **Apply core transform steps**: promote/demote headers, change column data types, split a column by delimiter or position, filter rows, remove errors and blank rows, trim/clean text, and group rows into an aggregate summary.
- **Unpivot and pivot columns** to reshape a wide crosstab report into a tidy long table (and back), the Power Query equivalent of the manual unpivot technique from Week 5.
- **Merge two queries** (a join — one row per match, adding columns from the second source) and **append two or more queries** (a stack — same columns, more rows), and correctly choose which operation a given task calls for.
- **Understand the query dependency chain** — how one query can reference another as its source, why load order matters, and what happens end-to-end when you click **Refresh All**.
- **Load results** to a worksheet Table, to the Excel Data Model (for pivot tables that span multiple sources), or as a **connection only** (an intermediate step referenced by other queries but never itself dumped onto a sheet).
- **Replicate the same outcomes in Google Sheets** with `IMPORTRANGE`, `IMPORTHTML`, `IMPORTDATA`, `IMPORTXML`, and Connected Sheets — and state precisely which Power Query capabilities Sheets' formula-based approach cannot match.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 4402` — Build a repeatable path from raw sources to an analysis-ready table — import, transform, unpivot, merge and append — so the same answer can be produced again next month. |
| Industry | Build the pipeline that absorbs a new warehouse's first export on the next refresh, instead of somebody editing a query when it lands. |
| Beyond the bar | Past the outcome set: a refreshable import taken straight off a public web page, and what to do when the page changes shape under you — `challenges/challenge-02-refreshable-web-import.md` |


## Prerequisites

- Weeks 1–6 complete, at minimum. This week assumes fluent Table conversion and structured references (Week 6) — every Power Query output lands as a Table, and you'll immediately be writing `SUMIFS`/formulas against it the way Week 6 taught.
- Week 5's data-cleaning vocabulary (duplicates, blanks, standardization, unpivoting) is reused directly — Power Query mechanizes exactly what Week 5 taught you to do by hand.
- **Excel 365, Excel 2016 or later** (Power Query, branded "Get & Transform Data," ships built into the **Data** tab). Excel 2010/2013 users need the free **Power Query add-in** from Microsoft — same engine, older install path.
- **Google Sheets** with an active internet connection, for the parity sections (`IMPORTHTML`/`IMPORTXML`/`IMPORTRANGE` are covered as the Sheets-side answer, not a full substitute).
- A plain-text editor (Notepad, TextEdit, VS Code — anything that saves literal `.csv` files) to build the seed files below. You are not using Excel to "save as CSV" this week — you're typing raw CSV text directly, the way a real export actually looks.

## Set up your workspace (do this first)

Create a folder on your machine named `crunch-wholesale` — everything this week reads from or writes to this one folder. Excel's **From Folder** connector (Lecture 3, Exercise 3, Challenge 1, and the mini-project) needs a real folder path, not a workbook sheet, so this step is not optional.

Inside `crunch-wholesale`, create a subfolder named `warehouse-exports`, and inside *that*, create three plain-text files — `North_Week1.csv`, `South_Week1.csv`, and `West_Week1.csv` — each containing exactly the text shown below (including the header row). Save each as plain text with the `.csv` extension, not as an Excel workbook.

**`North_Week1.csv`**
```
OrderID,OrderDate,SKU,ProductName,Qty,UnitCost
N-5001,2026-03-02,SKU-100,Trail Backpack,12,42.50
N-5002,2026-03-03,SKU-104,Camp Stove,8,28.00
N-5003,2026-03-03,SKU-101,Hiking Boots,15,55.00
N-5004,2026-03-05,SKU-103,Water Bottle,40,4.25
N-5005,2026-03-06,SKU-102,Rain Shell,10,22.00
```

**`South_Week1.csv`** — notice the columns are in a *different order* than North's. This is deliberate: real exports from different systems rarely agree on column order, and Power Query's combine step matches by column **name**, not position, which is exactly what this file tests.
```
OrderID,SKU,ProductName,OrderDate,Qty,UnitCost
S-6001,SKU-101,Hiking Boots,2026-03-02,20,55.00
S-6002,SKU-100,Trail Backpack,2026-03-04,18,42.50
S-6003,SKU-105,Tent 4-Person,2026-03-05,6,89.00
S-6004,SKU-103,Water Bottle,2026-03-06,50,4.25
```

**`West_Week1.csv`**
```
OrderID,OrderDate,SKU,ProductName,Qty,UnitCost
W-7001,2026-03-02,SKU-104,Camp Stove,10,28.00
W-7002,2026-03-03,SKU-102,Rain Shell,14,22.00
W-7003,2026-03-04,SKU-105,Tent 4-Person,4,89.00
W-7004,2026-03-06,SKU-100,Trail Backpack,22,42.50
W-7005,2026-03-07,SKU-101,Hiking Boots,9,55.00
```

Directly inside `crunch-wholesale` (not the `warehouse-exports` subfolder), create one more file, **`Products.csv`** — the lookup table Lecture 3 and Exercise 3 merge against the orders:
```
SKU,Category,Supplier
SKU-100,Gear,Alpine Supply Co.
SKU-101,Footwear,TrailWorks Inc.
SKU-102,Apparel,StormGuard Ltd.
SKU-103,Gear,Alpine Supply Co.
SKU-104,Gear,Summit Gear Partners
SKU-105,Gear,Summit Gear Partners
```

Sanity check — multiply `Qty × UnitCost` for every row across all three warehouse files and sum the result: it must total **6934.50**. North alone totals **1949.00**, South **2611.50**, West **2374.00**. Keep these numbers — every lecture, exercise, and challenge this week checks its output against them.

## Weekly schedule

The schedule below adds up to approximately **27 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Power Query intro — get & transform, editor, steps | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Transform & shape — split, unpivot, type, group | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Merging queries; the Products lookup | 1h | 1.5h | 1h | 0.5h | 1h | 0h | 5h |
| Thursday | Appending, folders, refresh chain; Sheets parity | 1h | 0h | 1h | 0.5h | 1h | 1h | 4.5h |
| Friday | Web imports; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (full ETL pipeline) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **26.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it, and the seed files created above are used by every single one of them.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-power-query-intro.md](01-power-query-intro.md) | The get-and-transform workflow, the query editor, applied steps, why Power Query beats manual copy-paste cleaning | 2h |
| 2 | [lecture-notes/02-transform-and-shape.md](02-transform-and-shape.md) | Splitting columns, unpivoting, type conversion, grouping, building a clean output from a messy source | 2h |
| 3 | [lecture-notes/03-merge-append-refresh.md](03-merge-append-refresh.md) | Combining files from a folder, merge vs. append, the dependency chain, refresh, Google Sheets equivalents | 1h |
| 4 | [exercises/exercise-01-import-and-clean.md](exercise-01-import-and-clean.md) | Import a messy raw export and clean it into a real Table | 1h |
| 5 | [exercises/exercise-02-unpivot-a-crosstab.md](exercise-02-unpivot-a-crosstab.md) | Unpivot a wide Product × Month report into a tidy long table | 1.5h |
| 6 | [exercises/exercise-03-merge-two-sources.md](exercise-03-merge-two-sources.md) | Merge Orders against the Products lookup table | 1.5h |
| 7 | [challenges/challenge-01-folder-of-files-pipeline.md](challenge-01-folder-of-files-pipeline.md) | Combine all three warehouse files from a folder into one query | 1.5h |
| 8 | [challenges/challenge-02-refreshable-web-import.md](challenge-02-refreshable-web-import.md) | Build a Power Query web import that re-pulls current data on refresh | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-11-power-query-and-data-connections/mini-project/README.md) | Full ETL pipeline: import, clean, merge, append, refresh | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-11-power-query-and-data-connections/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-11-power-query-and-data-connections/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-11-power-query-and-data-connections/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Point Power Query at a messy CSV, a folder of CSVs, or a web page, and land clean, typed, analysis-ready data on a sheet without touching Find & Replace once.
- Read an Applied Steps pane and know exactly what each step does and in what order it runs — and reorder, rename, or delete a step without breaking the ones after it.
- Choose correctly between **Merge** (add columns from a second source, matched on a key) and **Append** (stack more rows from sources with the same columns) for any two-source combination task.
- Combine an entire folder of same-shaped files into one query that automatically picks up a new file the next time you drop one in and hit Refresh.
- Explain, specifically, what Google Sheets' `IMPORTHTML`/`IMPORTRANGE`/`IMPORTXML`/Connected Sheets can and cannot do compared to Power Query's step-based editor.

## Up next

[Week 12 — Capstone: automation + dashboard](../week-12-capstone-automation-and-dashboard/) — with a refreshable pipeline feeding clean data automatically, the final week wires macros/VBA (or Apps Script) around it so the whole workbook updates and reports itself with one click.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
