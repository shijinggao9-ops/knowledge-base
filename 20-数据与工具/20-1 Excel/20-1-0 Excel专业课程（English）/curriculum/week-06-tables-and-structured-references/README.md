# Week 6 — Tables & Structured References

> **Goal:** by Sunday you can convert any flat range into a real Excel Table (or a Google Sheets Table), write formulas that refer to columns by *name* instead of by cell address, and build a summary sheet driven entirely by `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` that keeps itself correct automatically when new rows are added below.

Welcome back to **C41 · Crunch Excel**. For five weeks you've been building formulas against plain ranges — `A2:A25`, `D2:D25`, always some fixed block of cells you typed the boundaries of by hand. That works until the range changes shape, which in real life is *always*: someone adds a row tomorrow, a new order comes in, a new employee joins. This week you stop hard-coding boundaries. A **Table** is a range that knows its own edges, extends itself when you type in the row right below it, and lets every formula that touches it refer to a column by its plain-English name — `Orders[Total]` instead of `D2:D25`. Get this right and a report you build today keeps working correctly a year from now, with zero maintenance, no matter how much data gets added to it.

This week also finally answers the question every SQL-curious spreadsheet user asks: "how do I do a `GROUP BY` in Excel without a pivot table?" The answer is the **IFS family** — `SUMIFS`, `COUNTIFS`, `AVERAGEIFS` — conditional aggregation functions that, combined with structured references, let you build a live summary sheet in a few formulas. Pivot tables arrive properly in Week 7; this week you build the muscle that makes pivot tables make sense.

You work against one seed dataset, a flat sales-order report for a small company called **Crunch Retail**, for the whole week. You paste it in once (below), then every lecture, exercise, challenge, and the mini-project builds on it.

## Learning objectives

By the end of this week, you will be able to:

- **Convert** a plain range into an Excel Table (`Ctrl+T`) or a Google Sheets Table, and explain exactly what changes the moment you do — auto-expansion, banded formatting, the filter/sort arrows, and the auto-fill of formulas down a new row.
- **Write formulas with structured references** — `Table[Column]`, `Table[@Column]`, `Table[#Headers]`, `Table[#Data]`, `Table[#Totals]`, `Table[#All]` — instead of raw `A2:A25`-style addresses, and explain why they survive inserted rows and columns while A1 references don't.
- **Use `SUMIFS`, `COUNTIFS`, and `AVERAGEIFS`** to aggregate a Table by one or many criteria at once — the everyday replacement for "I wish Excel had a `WHERE` clause."
- **Add a Total Row** to a Table, choose per-column aggregate functions from its dropdown, and apply built-in and custom Table styles.
- **Build slicers** (Excel) to filter a Table interactively without touching a formula, and understand Google Sheets' nearest equivalents (filter views, dropdown chips in Sheets Tables).
- **Replicate Table behavior in Google Sheets** — its own Tables feature, what it shares with Excel Tables, and precisely where the two diverge (structured-reference formula syntax is the big one).
- **Build a live summary sheet** — a small matrix of `SUMIFS` formulas — that stays correct automatically as new rows are appended to the source Table, with zero manual range edits.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGMT 47200` — Convert a range into a table, write structured references in place of A1 addresses, and aggregate conditionally with `SUMIFS`, `COUNTIFS` and `AVERAGEIFS`. |
| Industry | Hand a manager a summary sheet that stays correct as they append rows to it for a year, without anyone going back to edit a range. |
| Beyond the bar | Port a table-driven model between Excel and Google Sheets in either direction and write down every place the two applications disagree — `challenges/challenge-02-sheets-vs-excel-tables.md` |


## Prerequisites

- Weeks 1–5 complete. You need real fluency with: relative/absolute/mixed references and named ranges (Week 2), `IF`/`AND`/`OR` logic and `XLOOKUP` (Week 3), and the general shape of a "clean dataset" — one header row, no blank rows, one value per cell (Week 5's data-cleaning discipline is exactly what makes a range Table-ready).
- Excel (365, 2021, or Excel for the web — Tables have existed since Excel 2007, so any modern version has them) **and/or** Google Sheets (its Tables feature is available to any free Google account as of this course's writing — if your version doesn't show **Insert → Tables**, the fallback described in Lecture 1 and Challenge 2 still gets you equivalent behavior).
- No prior database or "Table" experience assumed — if the only table you've built so far is a plain range with a bold header row, that's exactly where this week expects you to start.

## Set up your workspace (do this first)

Open a fresh workbook (Excel: `crunch-week6.xlsx`; Sheets: blank at <https://sheets.google.com>, renamed `crunch-week6`). Rename the first sheet tab **`Orders`**.

Starting at `A1`, type the header row exactly as shown, then paste (or type) the 24 rows of data beneath it. This is a flat report — **do not** convert it to a Table yet; Lecture 1 walks you through that conversion step by step, and part of the point is feeling the "before."

```
OrderID  OrderDate   Rep         Region  Product               Category         Qty  UnitPrice  Total
1001     2026-02-02  J. Alvarez  South   Webcam 1080p          Electronics      1    45.00      45.00
1002     2026-02-03  M. Chen     North   Notebook Pack         Office Supplies  2    12.50      25.00
1003     2026-02-03  R. Diaz     West    CRM License           Software         3    89.00      267.00
1004     2026-02-04  S. Kim      East    Wireless Mouse        Electronics      1    24.99      24.99
1005     2026-02-05  T. Osei     South   Bookshelf             Furniture        2    129.00     258.00
1006     2026-02-05  J. Alvarez  North   Stapler               Office Supplies  4    6.99       27.96
1007     2026-02-06  M. Chen     West    Project Mgmt License  Software         1    59.00      59.00
1008     2026-02-09  R. Diaz     East    Standing Desk         Furniture        5    349.00     1745.00
1009     2026-02-09  S. Kim      South   Printer Paper         Office Supplies  2    34.75      69.50
1010     2026-02-10  T. Osei     North   Antivirus License     Software         1    39.99      39.99
1011     2026-02-11  J. Alvarez  West    27in Monitor          Electronics      3    229.00     687.00
1012     2026-02-12  M. Chen     East    Filing Cabinet        Furniture        2    159.00     318.00
1013     2026-02-12  R. Diaz     South   Whiteboard            Office Supplies  1    42.00      42.00
1014     2026-02-13  S. Kim      North   Backup Software       Software         2    29.99      59.98
1015     2026-02-16  T. Osei     West    Office Chair          Furniture        3    189.50     568.50
1016     2026-02-17  J. Alvarez  East    Sticky Notes          Office Supplies  1    8.25       8.25
1017     2026-02-17  M. Chen     South   Cloud Storage Plan    Software         2    19.99      39.98
1018     2026-02-18  R. Diaz     North   Webcam 1080p          Electronics      4    45.00      180.00
1019     2026-02-19  S. Kim      West    Notebook Pack         Office Supplies  1    12.50      12.50
1020     2026-02-20  T. Osei     East    CRM License           Software         5    89.00      445.00
1021     2026-02-23  J. Alvarez  South   Wireless Mouse        Electronics      2    24.99      49.98
1022     2026-02-24  M. Chen     North   Bookshelf             Furniture        1    129.00     129.00
1023     2026-02-25  R. Diaz     West    Stapler               Office Supplies  3    6.99       20.97
1024     2026-02-26  S. Kim      East    Project Mgmt License  Software         2    59.00      118.00
```

Notes on entering it:

- **`OrderDate`** — type as `2026-02-02` etc. Both apps recognize `YYYY-MM-DD` as a real date on entry; if a cell left-aligns instead of right-aligns after you type it, it landed as text — reformat the column (Week 1, Lecture 3) before continuing.
- **`Total`** column — for now, type these as **plain typed numbers**, not formulas. Lecture 2 has you replace them with a real `Qty * UnitPrice` structured-reference formula once the range becomes a Table — typing the values first lets you verify your formula later by comparing against numbers you know are right.
- **`UnitPrice`** and **`Total`** — format both columns as **Currency** once entered (Week 1, Lecture 3).

Sanity check — the range is `A1:I25` (header + 24 rows). Put `=SUM(I2:I25)` in any empty cell below the data; it must show **5240.60**. If it doesn't, recheck your `Total` entries against the table above before moving on — the entire week's formulas are built to match this exact number.

## Weekly schedule

The schedule below adds up to approximately **27 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Range → Table conversion; styles, total row | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Structured references — column names, `@`, `#` | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` over a Table | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Slicers; building a summary sheet | 0h | 0h | 1h | 0.5h | 1h | 1h | 3.5h |
| Friday | Google Sheets Tables; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (report → Tables + summary sheet) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **26.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-why-tables.md](01-why-tables.md) | Converting a range to a Table, auto-expansion, styles, the Total Row | 2h |
| 2 | [lecture-notes/02-structured-references.md](02-structured-references.md) | `Table[Column]`, `[@Column]`, `[#Headers]`/`[#Data]`/`[#Totals]`/`[#All]`, surviving inserted rows/columns | 2h |
| 3 | [lecture-notes/03-conditional-aggregation.md](03-conditional-aggregation.md) | `SUMIFS`/`COUNTIFS`/`AVERAGEIFS`, multi-criteria filtering, building a live summary sheet | 2h |
| 4 | [exercises/exercise-01-range-to-table.md](exercise-01-range-to-table.md) | Convert the `Orders` range to a Table and prove it auto-expands | 1h |
| 5 | [exercises/exercise-02-structured-ref-formulas.md](exercise-02-structured-ref-formulas.md) | Rewrite A1-style formulas as structured references | 1.5h |
| 6 | [exercises/exercise-03-sumifs-summary.md](exercise-03-sumifs-summary.md) | Summarize the Table with `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` | 1.5h |
| 7 | [challenges/challenge-01-self-growing-tracker.md](challenge-01-self-growing-tracker.md) | Build a tracker where every total updates itself as rows are added | 1h |
| 8 | [challenges/challenge-02-sheets-vs-excel-tables.md](challenge-02-sheets-vs-excel-tables.md) | Port the Table model to Google Sheets and document the differences | 1h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/mini-project/README.md) | Convert a flat report to Tables + build a self-updating summary sheet | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Convert any clean flat range into a Table in one keystroke and know exactly what four things changed the instant you did.
- Write a formula that says `[@Qty] * [@UnitPrice]` instead of `D2*E2`, and explain why the structured version survives an inserted row and the A1 version doesn't.
- Build a `SUMIFS` that filters on two or three criteria at once against a Table column, without ever typing a hard-coded range boundary.
- Add rows to a Table and watch a summary sheet elsewhere in the workbook update itself with no manual edits.
- Describe precisely what Google Sheets Tables share with Excel Tables, and what a workbook loses (or must do differently) when it moves between the two.

## Up next

[Week 7 — Pivot tables & charts](../week-07-pivot-tables-and-charts/) — once you can aggregate a Table with formulas, we hand the same job to a purpose-built tool that groups, pivots, and charts it for you.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
