# Mini-Project — Convert a Flat Report to Tables With a Self-Updating Summary

> Take the `Orders` flat report from this week's setup, convert it to a real Table, and build a full summary sheet driven entirely by structured-reference `SUMIFS`/`COUNTIFS`/`AVERAGEIFS` — then prove, with a live growth test, that the whole thing keeps itself correct as new orders are added. This is the week's capstone: every skill from all three lectures, combined into one workbook you could genuinely hand to a manager who adds rows to it every week.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

A summary sheet is the perfect proof of this week's skills because it fails loudly and obviously if you get structured references wrong — a total that doesn't move when a new order is entered, a matrix cell that silently excludes half the data because a formula still points at row 25 when the Table now has 30 rows. Get it right and you've built the thing every real business report actually is underneath: one growing Table, and a summary that trusts it completely.

---

## Deliverable

A workbook `orders-summary.xlsx` (or Google Sheets equivalent) containing:

1. An `Orders` sheet — the Table, built to spec below.
2. A `Summary` sheet — the matrices and breakdowns, built to spec below.
3. A `report.md` — a short written report (see the end) documenting your growth test.

---

## Part A — The `Orders` Table

Starting from the flat `A1:I25` range in the week README:

1. Convert it to a Table, named `Orders`, with a style applied (banded rows on).
2. Replace the typed `Total` values with `=[@Qty]*[@UnitPrice]`.
3. Add a Total Row: `Sum` on `Qty` and `Total`.
4. Confirm the Total Row's `Total` cell reads **5240.60** before moving to Part B.

## Part B — The `Summary` sheet

Build **all four** of the following sections on one `Summary` sheet. Every formula must use structured references (`Orders[Column]` / `[@Column]`) — no `A2:A25`-style ranges anywhere on this sheet.

### 1. Region × Category dollar matrix

A 4×4 grid (regions down, categories across) using `SUMIFS`, plus row totals, column totals, and a grand total. *(This is the matrix from Lecture 3 / Exercise 3 — rebuild it here even if you already have a copy elsewhere; this workbook should stand alone.)*

### 2. Region × Category order-count matrix

The same grid shape, `COUNTIFS` instead of `SUMIFS` — how many orders, not how many dollars, per region/category combination.

### 3. Rep leaderboard

One row per rep (5 rows), three columns: **Total Sales** (`SUMIFS`), **Order Count** (`COUNTIFS`), **Average Order Size** (`AVERAGEIFS`, wrapped in `IFERROR` to show `0` instead of `#DIV/0!` for any rep with zero orders — defensive even though every current rep has at least one order).

### 4. Top-line KPIs

Four single-cell figures, clearly labeled, anywhere convenient on `Summary`:

- **Total Revenue** — `SUM(Orders[Total])`.
- **Total Orders** — `COUNT(Orders[OrderID])`.
- **Average Order Value** — `AVERAGE(Orders[Total])`.
- **Largest Single Order** — `MAX(Orders[Total])`, plus (stretch-adjacent but required here) the `Product` of that order using `XLOOKUP` against the `Total` column to find it (Week 3 skill, now combined with a structured reference as the lookup range: `=XLOOKUP(MAX(Orders[Total]), Orders[Total], Orders[Product])`).

## Part C — The growth test (required, not optional)

This is the actual point of the mini-project — everything above just sets it up.

1. **Record every KPI and matrix grand total from Parts B1–B4 in `report.md`** before you add anything — this is your "before" snapshot.
2. **Add 4 new orders** to the `Orders` Table, typed directly into the row below the last existing one, one at a time. Invent realistic data: at least one new order should use a **region and category combination already in the matrix** (to test an existing cell updates), and at least one should be a genuinely **new high value** that would change the `MAX`/largest-order KPI.
3. **After each of the 4 new rows, record in `report.md`:** which KPI(s) and which matrix cell(s) changed, and by how much. Confirm each change matches what you'd expect by hand-checking the new row's own values against the categories it falls into.
4. **Take a final "after" snapshot** of every KPI and both matrices' grand totals. The dollar matrix's grand total minus the original grand total must exactly equal the sum of your 4 new orders' `Total` values — this is your correctness check.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Table correctness | 20% | `Orders` is a properly named, styled Table with a working formula-driven `Total` column |
| Structured references only | 25% | Zero `A2:A25`-style ranges anywhere on `Summary`; every formula uses `Orders[...]` |
| Summary completeness | 20% | All four sections (dollar matrix, count matrix, rep leaderboard, KPIs) present and correct |
| Growth test | 25% | 4 real rows added; every affected number tracked and verified in `report.md`, including the exact-match correctness check |
| Report clarity | 10% | `report.md` clearly shows before/after and explains *why* each number moved |

## Reflection (part of `report.md`, ~150–200 words)

1. Which part of the growth test surprised you — a number that moved differently than you expected, or one that didn't move when you thought it would?
2. If you'd built this same summary with `A2:A25`-style ranges instead of structured references, name one specific step in the growth test that would have broken, and exactly how.
3. Which of this week's three lecture topics (Table conversion, structured references, `SUMIFS`/`COUNTIFS`/`AVERAGEIFS`) do you still want more reps on before Week 7's pivot tables?

## Stretch goals

- Add a **fifth KPI**: percentage of total revenue from the single largest category, computed as `MAX(matrix column totals) / Total Revenue`, formatted as a Percentage.
- Add a **slicer** (Excel) on `Region` connected to the `Orders` Table, and confirm the Table itself filters — note in `report.md` whether the `Summary` sheet's `SUMIFS` totals change too, and explain *why* they do or don't (hint: `SUMIFS` reads underlying values, not visible-row state — contrast this with the Total Row's behavior from Lecture 1).
- Build a fifth matrix: total sales **by week** (group the 24 orders into their calendar week using a date formula) × category, proving structured references compose cleanly with date logic from earlier weeks.

## Why this matters

This mini-project is the shape of every recurring report you'll ever be asked to maintain: a growing log of raw events on one side, a set of formulas that summarize it on the other, and a promise — kept automatically, not by remembering to update something — that the summary is never stale. Nail this pattern and Week 7's pivot tables will feel like a faster way to do something you already deeply understand, not a black box you're trusting blindly.

When done: push/save your work, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-06-tables-and-structured-references/quiz.md), and start [Week 7 — Pivot tables & charts](../../week-07-pivot-tables-and-charts/).
