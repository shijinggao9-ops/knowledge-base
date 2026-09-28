# Week 10 — Dynamic Arrays & Modern Functions

> **Goal:** by Sunday you can write a single formula that filters, sorts, and de-duplicates a whole dataset at once and watches its answer "spill" across a grid of cells with no dragging, no helper columns, and no `Ctrl+Shift+Enter` — then wrap that formula in `LET` to make it readable and in your own `LAMBDA` to make it reusable, on both Excel and Google Sheets.

Welcome back to **C41 · Crunch Excel**. Every formula you've written so far has computed **one value in one cell**. Even a `SUMIFS` or an `XLOOKUP` — no matter how clever — has always returned exactly one number or one piece of text into the cell you typed it in. This week that rule breaks, on purpose. A **dynamic array** formula returns a whole rectangle of results from a single cell, and the surrounding cells fill themselves in automatically the moment you press Enter. That one shift — one formula, many results — is what makes `FILTER`, `SORT`, and `UNIQUE` feel like magic the first time you use them, and it's the foundation modern Excel and Google Sheets are now built on.

The second half of the week goes one level deeper. `LET` lets you name the messy sub-expressions buried inside a long formula so it reads like a small paragraph instead of a wall of parentheses. `LAMBDA` lets you go further still — define your **own** function, give it a name, and reuse it anywhere in the workbook exactly like a built-in one. By Friday you'll have written a formula most people never learn to write, and by the mini-project you'll have collapsed a whole multi-step report into a single spilling cell.

We work all week against one seed dataset — 30 rows of order history for a small electronics retailer, **Crunch Gadgets** — and build one running artifact: a `Report` sheet driven entirely by dynamic-array formulas that stay live as the source data changes.

## Learning objectives

By the end of this week, you will be able to:

- **Explain** the spill model and the dynamic-array calculation engine — the anchor cell, the spill range, the `#` spill-range operator, and the `#SPILL!` error — and how it differs from the legacy `Ctrl+Shift+Enter` array formulas it replaced.
- **Filter, sort, and de-duplicate** live data with `FILTER`, `SORT`/`SORTBY`, and `UNIQUE`, including multi-condition filters and multi-key sorts, without touching a helper column.
- **Generate** structured and randomized arrays with `SEQUENCE` and `RANDARRAY`, and combine them with spill references to build ranks, calendars, and test data.
- **Simplify** long, repetitive formulas by naming intermediate results with `LET` — for readability and for genuine calculation-speed gains.
- **Write reusable custom functions** with `LAMBDA`, register them with a name so they behave like built-ins, write a **recursive** `LAMBDA` that calls itself, and apply a `LAMBDA` across a range with the helper functions `MAP`, `REDUCE`, `BYROW`, and `BYCOL`.
- **Compare** Excel's dynamic-array model with Google Sheets' equivalents — where the two apps match almost exactly, and where Sheets' older `ARRAYFORMULA` culture and named-function mechanism genuinely diverge from Excel's.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGMT 47200` — Write formulas that return a whole range of results rather than one value, and name intermediate steps so a long formula stays readable to somebody else. |
| Industry | Replace a report held together by helper columns and a manual re-sort with one that recomputes itself correctly the moment the source data changes. |
| Beyond the bar | A recursive `LAMBDA` that calls itself — answering in one cell the question Week 9 needed a sixty-row schedule to answer — `challenges/challenge-02-recursive-lambda.md` |


## Prerequisites

- Weeks 1–9 complete. You need real fluency with absolute/relative references and named ranges (Week 2), `IF`/`XLOOKUP`/`INDEX MATCH` (Week 3), and structured, clean tabular data (Weeks 5–6) — every formula this week reads a table-shaped range.
- **A version that supports dynamic arrays.** Excel 365 or Excel 2021+ (including Excel for the web) — `FILTER`, `SORT`, `UNIQUE`, `SEQUENCE`, `RANDARRAY`, `LET`, and `LAMBDA` do **not** exist in Excel 2019 or earlier perpetual-license versions. Google Sheets: any current free account — Sheets has supported spilling `FILTER`/`SORT`/`UNIQUE` for years, and added `LET` and `LAMBDA` in 2022. If you're unsure which Excel you have, type `=SEQUENCE(3)` in a blank cell — three stacked numbers spilling down means you're set.
- Comfortable reading `#REF!`, `#VALUE!`, and `#N/A` without panic (Week 3) — this week adds two new errors, `#SPILL!` and `#CALC!`, which Lecture 1 covers in depth.

## Set up your workspace (do this first)

**Excel:**

1. **File → New → Blank workbook.**
2. **File → Save As** → `crunch-week10.xlsx`.
3. Rename the first sheet tab **`Orders`**. Add a second tab named **`Report`** — this is where every dynamic-array formula this week will live, kept deliberately separate from the source data.

**Google Sheets:**

1. <https://sheets.google.com> → blank **(+)** template.
2. Rename the file `crunch-week10`.
3. Rename the first sheet tab **`Orders`**, add a second tab **`Report`**.

On the `Orders` tab, starting at `A1`, type the header row exactly as shown, then paste (or type) the 30 rows beneath it:

```
OrderID  OrderDate   Rep       Region  Product             Category      Qty  UnitPrice  Total   Status
3001     2026-01-05  A. Kim    North   Wireless Earbuds    Audio         1    59.00      59.00   Shipped
3002     2026-01-07  B. Silva  West    USB-C Cable         Accessories   1    9.00       9.00    Pending
3003     2026-01-10  C. Novak  East    Fitness Band        Wearables     2    45.00      90.00   Shipped
3004     2026-01-13  D. Osei   South   Video Doorbell       Smart Home    1    129.00     129.00  Shipped
3005     2026-01-15  E. Park   North   Phone Case           Accessories   3    15.00      45.00   Shipped
3006     2026-01-18  A. Kim    West    Bluetooth Speaker    Audio         2    89.00      178.00  Pending
3007     2026-01-21  B. Silva  East    Smart Plug           Smart Home    1    22.00      22.00   Shipped
3008     2026-01-23  C. Novak  South   Smartwatch           Wearables     4    199.00     796.00  Cancelled
3009     2026-01-26  D. Osei   North   Wireless Earbuds     Audio         2    59.00      118.00  Shipped
3010     2026-01-29  E. Park   West    USB-C Cable          Accessories   1    9.00       9.00    Pending
3011     2026-02-01  A. Kim    East    Fitness Band         Wearables     1    45.00      45.00   Shipped
3012     2026-02-03  B. Silva  South   Video Doorbell       Smart Home    1    129.00     129.00  Shipped
3013     2026-02-06  C. Novak  North   Phone Case           Accessories   2    15.00      30.00   Shipped
3014     2026-02-09  D. Osei   West    Bluetooth Speaker    Audio         1    89.00      89.00   Pending
3015     2026-02-11  E. Park   East    Smart Plug           Smart Home    3    22.00      66.00   Shipped
3016     2026-02-14  A. Kim    South   Smartwatch           Wearables     2    199.00     398.00  Cancelled
3017     2026-02-17  B. Silva  North   Wireless Earbuds     Audio         1    59.00      59.00   Shipped
3018     2026-02-19  C. Novak  West    USB-C Cable          Accessories   4    9.00       36.00   Pending
3019     2026-02-22  D. Osei   East    Fitness Band         Wearables     2    45.00      90.00   Shipped
3020     2026-02-25  E. Park   South   Video Doorbell       Smart Home    1    129.00     129.00  Shipped
3021     2026-02-28  A. Kim    North   Phone Case           Accessories   1    15.00      15.00   Shipped
3022     2026-03-02  B. Silva  West    Bluetooth Speaker    Audio         1    89.00      89.00   Pending
3023     2026-03-05  C. Novak  East    Smart Plug           Smart Home    2    22.00      44.00   Shipped
3024     2026-03-08  D. Osei   South   Smartwatch           Wearables     1    199.00     199.00  Cancelled
3025     2026-03-10  E. Park   North   Wireless Earbuds     Audio         3    59.00      177.00  Shipped
3026     2026-03-13  A. Kim    West    USB-C Cable          Accessories   2    9.00       18.00   Shipped
3027     2026-03-16  B. Silva  East    Fitness Band         Wearables     1    45.00      45.00   Pending
3028     2026-03-18  C. Novak  South   Video Doorbell       Smart Home    4    129.00      516.00  Shipped
3029     2026-03-21  D. Osei   North   Phone Case           Accessories   2    15.00      30.00   Shipped
3030     2026-03-24  E. Park   West    Bluetooth Speaker    Audio         1    89.00      89.00   Pending
```

Notes on entering it:

- **`OrderDate`** — type as `2026-01-05` etc.; both apps recognize `YYYY-MM-DD` as a real date on entry.
- **`UnitPrice`** and **`Total`** — format both columns as **Currency** (Week 1, Lecture 3). Type `Total` as a plain number for now; it's `Qty * UnitPrice` and you're welcome to replace it with that formula once the sheet is set up.
- Data occupies `A1:J31` — header in row 1, 30 orders in rows 2–31.
- Select `A1:J31` and, using the Name Box (top-left, left of the formula bar), name the range **`Orders`** (Week 2, Lecture 3) — every formula this week can then refer to `Orders` instead of retyping `Orders!$A$1:$J$31`.

Sanity check — on the `Report` tab, in cell `A1`, type `=SUM(Orders!I2:I31)`. It must show **`3748.00`**. A second check: `=SUMIFS(Orders!I2:I31, Orders!J2:J31, "Shipped")` must show **`1838.00`**. If either doesn't match, recheck your entries against the table above — every formula this week is built to match these exact numbers.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | The spill model; `FILTER`/`SORT`/`UNIQUE` | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Tuesday | `LET`, `SEQUENCE`, `RANDARRAY` | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Wednesday | `LAMBDA`, recursion, `MAP`/`REDUCE`/`BYROW` | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Thursday | One-formula reports; challenges begin | 0h | 0h | 1.5h | 0.5h | 1h | 1h | 4h |
| Friday | Recursive `LAMBDA`; challenges finish | 0h | 0h | 1.5h | 0.5h | 1h | 1.5h | 4.5h |
| Saturday | Mini-project (one-formula report + `LAMBDA`) | 0h | 0h | 0h | 0h | 0h | 3h | 3h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5.5h** | **27h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-the-spill-model.md](01-the-spill-model.md) | Spill ranges, the `#` operator, `FILTER`/`SORT`/`SORTBY`/`UNIQUE`, `#SPILL!`/`#CALC!` | 2h |
| 2 | [lecture-notes/02-let-and-readable-formulas.md](02-let-and-readable-formulas.md) | `LET` named variables, `SEQUENCE`, `RANDARRAY`, readability + performance | 2h |
| 3 | [lecture-notes/03-lambda-custom-functions.md](03-lambda-custom-functions.md) | `LAMBDA`, naming/registering functions, recursion, `MAP`/`REDUCE`/`BYROW`/`BYCOL` | 2h |
| 4 | [exercises/exercise-01-filter-sort-unique.md](exercise-01-filter-sort-unique.md) | Build a live `FILTER` report against the `Orders` data | 1.5h |
| 5 | [exercises/exercise-02-let-refactor.md](exercise-02-let-refactor.md) | Refactor a nested, repetitive formula with `LET` | 1h |
| 6 | [exercises/exercise-03-write-a-lambda.md](exercise-03-write-a-lambda.md) | Write, register, and test your own reusable `LAMBDA` | 1.5h |
| 7 | [challenges/challenge-01-one-formula-report.md](challenge-01-one-formula-report.md) | Collapse a whole multi-step report into one spilling formula | 1.5h |
| 8 | [challenges/challenge-02-recursive-lambda.md](challenge-02-recursive-lambda.md) | Solve a running-balance problem with a recursive `LAMBDA` | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/mini-project/README.md) | Rebuild a report as one formula with `FILTER`/`SORT`/`UNIQUE`, `LET`, and a `LAMBDA` helper | 3h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Look at a formula and correctly predict whether, where, and how far it will spill — and fix a `#SPILL!` error by finding what's in the way.
- Build a live report — filtered, sorted, de-duplicated — in a single cell, with zero helper columns, that updates the instant the source data changes.
- Take a 200-character nested formula and rewrite it with `LET` so a teammate can read it top to bottom without unwinding parentheses.
- Write your own named function with `LAMBDA`, including one that calls itself, and explain when `MAP`/`REDUCE`/`BYROW` beat a manual loop of formulas.
- Explain, concretely, where Excel's dynamic-array model and Google Sheets' array culture agree and where they genuinely differ.

## Up next

[Week 11 — Power Query & data connections](../week-11-power-query-and-data-connections/) — once a single formula can reshape data already in the sheet, we bring in data that *isn't* in the sheet yet, and build a repeatable import pipeline.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
