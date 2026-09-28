# Mini-Project — Rebuild the Report as One Spilling Formula

> Take a multi-step report — the kind you'd normally build with a `UNIQUE` column, a few `SUMIFS`/`COUNTIFS` next to it, a manual sort, and a helper column for classification — and rebuild the entire thing as **two spilling formulas**, each wrapped in `LET`, each calling a custom `LAMBDA` you register yourself. This is the week's capstone: proof that `FILTER`/`SORT`/`UNIQUE`, `LET`, and `LAMBDA` aren't three separate tricks, but one connected way of building live, self-maintaining reports.

**Estimated time:** 3 hours, best done Saturday after the exercises and challenges.

---

## Deliverable

A directory in your portfolio `c41-week-10/mini-project/` containing:

1. `crunch-week10-mini.xlsx` (or the equivalent Sheets file, shared/exported) — the full workbook: `Orders` tab (unchanged source data), `Report` tab (your two formulas), and your registered `LAMBDA` (visible in Name Manager / Named functions).
2. `report.md` — the two formulas as text (copy-pasted from the formula bar), a screenshot or transcription of each one's spilled output, and one paragraph explaining your design choices.
3. `notes.md` — a short reflection (see the end).

Everything runs against the `Orders` data from the [week README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/README.md). Works on Excel 365/2021/web or Google Sheets — note which you used.

---

## Part 1 — Register your LAMBDA helper

Before building either report formula, write and register **one** reusable function, `SIZETIER`, that classifies an order by its `Total`:

- `< $50` → `"Small"`
- `$50` to `< $150` → `"Medium"`
- `>= $150` → `"Large"`

*(This is the same rule from Exercise 3 — reuse it if you already built it there, or write it fresh. Either way it needs to be a genuinely **registered**, named function, callable as `SIZETIER(some_value)` from any cell — not just an inline `LAMBDA` buried inside a bigger formula.)*

## Part 2 — The Shipped Orders Report (one formula)

In one anchor cell, build a single `LET`-wrapped formula that:

1. Filters `Orders` down to **Shipped** status only.
2. Sorts the result by `Total`, highest first.
3. Returns these columns, in this order: `OrderID, OrderDate, Rep, Region, Product, Total`, **plus** a seventh column, `SizeTier`, computed by calling your registered `SIZETIER` function against each row's `Total` (hint: `MAP` over the `Total` column, then `HSTACK` it onto the rest).

**Expected:** 19 rows (all Shipped orders), led by order 3028 ($516.00, "Large"), with a `SizeTier` column that has no blanks and no errors anywhere.

## Part 3 — The Regional Summary Report (one formula)

In a second anchor cell, build a single `LET`-wrapped formula that:

1. Finds the distinct regions that have **at least one Shipped order** (not all four — only the ones actually represented).
2. For each, computes: `OrderCount`, `TotalRevenue`, and `AvgOrderValue`, all for Shipped orders only.
3. Returns columns `Region, OrderCount, TotalRevenue, AvgOrderValue`, sorted by `TotalRevenue` descending.

**Expected:** 3 rows (one region has zero Shipped orders — Challenge 1 walks through exactly this scenario if you completed it; if not, work out which region and why before you build this). Every region's `TotalRevenue` should sum to **$1,838.00**, the company-wide Shipped total.

## Part 4 — Prove it's live

Add **one new order** to the `Orders` tab — invent it yourself, but make it `Status = "Shipped"`, give it a `Total` of at least $600 (higher than anything currently in the dataset), and put it in whichever region currently has the *fewest* Shipped orders. Do **not** touch either report formula. Confirm, and screenshot or describe in `report.md`:

- The new order now appears at the **top** of the Shipped Orders Report (Part 2), correctly tagged `"Large"`.
- The Regional Summary Report (Part 3) has updated that region's `OrderCount` and `TotalRevenue` — and, if that region wasn't in the report before (zero Shipped orders previously), it now **appears** as a new row, automatically, with no formula edits.

Then remove the row you added and confirm both reports return to their original state.

---

## Milestones

- **Milestone 1 (45 min):** Register `SIZETIER`, test it standalone against a few values, confirm it matches the plain-English rule exactly at the boundaries (test `$49.99`, `$50.00`, `$149.99`, `$150.00` specifically — boundary bugs are the most common mistake here).
- **Milestone 2 (60 min):** Build and debug the Shipped Orders Report (Part 2) — get the `FILTER`+`SORT` working first without the `SizeTier` column, confirm the row count and top order, *then* add the `MAP`/`HSTACK` step for the tier.
- **Milestone 3 (60 min):** Build and debug the Regional Summary Report (Part 3) — verify the revenue-sums-to-$1,838.00 check before moving on.
- **Milestone 4 (15 min):** Part 4's live-update proof, plus writing `report.md` and `notes.md`.

---

## Rules

- **Two anchor cells total** for the two reports (plus wherever `SIZETIER` lives in Name Manager/Named functions — that doesn't count as a report cell). No helper cells feeding into either report formula.
- **Every `LET` name must be self-explanatory.** A reviewer should be able to read your `LET` top to bottom and understand the report's logic without you explaining it out loud.
- **`SIZETIER` must be called by name**, not re-written inline inside the report formula — the whole point is proving a registered function is reusable.
- Boundary values matter: an order of *exactly* $50.00 must land in `"Medium"`, not `"Small"`; exactly $150.00 must land in `"Large"`, not `"Medium"`.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 35% | Row counts, sorted order, and dollar totals all match the expected results exactly |
| One-formula discipline | 20% | Zero helper cells feeding either report; everything lives inside `LET` |
| LAMBDA reuse | 15% | `SIZETIER` is genuinely registered and called by name, boundary values correct |
| Live-update proof (Part 4) | 15% | Both reports correctly reflect the added order with zero formula edits, and correctly revert after removal |
| Readability | 15% | `LET` names read as clear phrases; `report.md` formulas are legible, not a single unbroken line with no explanation |

---

## Reflection (`notes.md`, ~200 words)

1. Which part of this project took the longest to debug, and what was actually wrong?
2. Compare this to how you'd have built the same two reports back in Week 6 or Week 7 (a Table + `SUMIFS`, or a pivot table). What's genuinely better about the dynamic-array version? What, if anything, is worse or harder to explain to a non-technical teammate?
3. Where did `LET` earn its keep the most — which named step, if you'd left it un-named and inline, would have been the hardest to read later?
4. One real report from your own life (school, work, a hobby) you could rebuild this way. What would the `FILTER` condition and the `LAMBDA` helper be?

---

## Why this matters

Real analytics work is full of reports that get rebuilt from scratch every time someone asks "can you also break it down by X?" A report built from `FILTER`/`SORT`/`UNIQUE` wrapped in `LET`, calling a named `LAMBDA` for any custom business logic, isn't just shorter — it's a report that **updates itself** the moment the source data changes, with a single formula a teammate can actually audit top to bottom. That combination — self-updating *and* auditable — is what separates a spreadsheet you trust from one you're afraid to touch. It's also exactly the discipline that makes Week 11's Power Query pipelines, and Week 12's automated dashboard, straightforward instead of terrifying.

When done: push, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/quiz.md) and start [Week 11 — Power Query & data connections](../../week-11-power-query-and-data-connections/).
