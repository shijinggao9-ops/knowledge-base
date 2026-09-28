# Week 2 — Formulas & Cell References

> **Goal:** by Sunday you can write a formula that computes correctly, uses the *right kind* of reference for the job, copies cleanly across an entire range without breaking, and — when it does break — you can read the error and fix it in seconds instead of minutes.

Last week you learned the grid: cells, rows, columns, sheets, and how a cell's stored value differs from its display format. This week the grid starts **calculating**. A formula is nothing mystical — it's a small program that lives in a cell, reads other cells, and produces one value. Once you understand how a formula's references behave when you copy it, you understand the single mechanic that every function, lookup, pivot table, and dashboard in the rest of this course is built on top of. Get references right now — relative, absolute, mixed — and formulas become a tool you wield deliberately instead of a thing that mysteriously "breaks when I drag it."

This week you keep building in a workbook of your own — no seed file to download until Week 3, when real datasets start arriving. Every lecture, exercise, challenge, and the mini-project has you build the formulas yourself, by hand, in both Excel and Google Sheets where the two differ.

## Learning objectives

By the end of this week, you will be able to:

- **Write arithmetic formulas** using `+ − * / ^` and know the exact order of operations Excel and Sheets apply — including how parentheses override it.
- **Use the five core aggregate functions** — `SUM`, `AVERAGE`, `COUNT`, `MIN`, `MAX` — and know precisely which cells each one counts, ignores, or errors on.
- **Distinguish relative, absolute (`$`), and mixed references** and choose the correct one so a formula behaves correctly when copied or filled.
- **Copy and fill formulas** across a range — by drag-fill, copy/paste, and double-click autofill — without breaking references or overwriting formatting you want to keep.
- **Define named ranges** and use them in formulas for self-documenting, less error-prone spreadsheets.
- **Reference cells on other sheets** (`Sheet!A1`) and, in Excel, other workbooks, correctly.
- **Read and diagnose the four most common formula errors** — `#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?` — and know the fix for each.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `ISM 3113` — Build arithmetic and aggregate formulas, and choose relative, absolute or mixed references so a formula still behaves correctly once it is copied or filled. |
| Industry | Inherit a workbook that opens fine and quietly returns wrong numbers, and find the cause of each one before changing a single cell. |
| Beyond the bar | Fill a whole 12×12 result grid from one formula typed once into one cell — a constraint that forces the mixed-reference rule rather than testing it — `challenges/challenge-01-build-a-multiplication-grid.md` |


## Prerequisites

- Week 1 complete: you can navigate, select, and format a sheet from the keyboard, and you understand the value-vs-display-format distinction.
- The same workbook tool from Week 1 — Excel and/or Google Sheets. This week again teaches both side by side.
- No prior formula experience assumed. If you've never typed `=` into a cell before, you're exactly where this week expects you to be.

## Set up your workspace (do this first)

You'll build on a fresh workbook this week, separate from Week 1's budget file.

**Excel:**

1. **File → New → Blank workbook.**
2. **File → Save As** → `crunch-week2.xlsx`, same folder as last week's file.
3. Rename `Sheet1` to `Formulas` (double-click the tab) — you'll add more sheets in Lecture 3.

**Google Sheets:**

1. <https://sheets.google.com> → blank **(+)** template.
2. Rename the file (top-left title field) to `crunch-week2`.
3. Rename the default tab to `Formulas`.

Sanity check — in cell `A1` type `10`, in `A2` type `20`, and in `A3` type `=A1+A2` and press **Enter**. `A3` should show `30`. If you instead see the *text* `=A1+A2`, your cell was formatted as Text before you typed — clear the formatting (`Ctrl+1` → General, or right-click → Clear Formatting) and re-enter it. That's the first formula bug you'll ever hit, and now you know the fix.

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Operators, order of operations, first functions | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Relative vs. absolute vs. mixed references | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Fill/drag behavior; locking rates | 0h | 1.5h | 1h | 0.5h | 1h | 0h | 4h |
| Thursday | Named ranges; cross-sheet references | 2h | 1h | 1h | 0.5h | 1h | 1h | 6.5h |
| Friday | Error values; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (self-calculating invoice) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **5h** | **3h** | **3.5h** | **5h** | **5h** | **27.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-your-first-formulas.md](01-your-first-formulas.md) | The `=` sign, operators, order of operations, `SUM`/`AVERAGE`/`COUNT`/`MIN`/`MAX` | 2h |
| 2 | [lecture-notes/02-relative-absolute-mixed.md](02-relative-absolute-mixed.md) | Why `$` matters, how fill changes references, one formula you can drag everywhere | 2h |
| 3 | [lecture-notes/03-named-ranges-and-cross-sheet.md](03-named-ranges-and-cross-sheet.md) | Naming cells, referencing other sheets/workbooks, reading error values | 2h |
| 4 | [exercises/exercise-01-operator-precedence-drills.md](exercise-01-operator-precedence-drills.md) | Predict-then-check drills on order of operations and the five aggregates | 1h |
| 5 | [exercises/exercise-02-lock-the-tax-rate.md](exercise-02-lock-the-tax-rate.md) | Build a priced order sheet with a correctly locked absolute reference | 1.5h |
| 6 | [exercises/exercise-03-name-your-ranges.md](exercise-03-name-your-ranges.md) | Convert magic-cell formulas into readable named-range formulas | 1h |
| 7 | [challenges/challenge-01-build-a-multiplication-grid.md](challenge-01-build-a-multiplication-grid.md) | One formula, filled in every direction, builds a full 12×12 grid | 1h |
| 8 | [challenges/challenge-02-fix-the-broken-references.md](challenge-02-fix-the-broken-references.md) | Diagnose and repair a small workbook full of reference bugs | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/mini-project/README.md) | Build a self-calculating invoice: line totals, subtotal, locked tax, grand total | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-02-formulas-and-cell-references/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Write any arithmetic formula and predict its result correctly before pressing Enter, including formulas mixing `^`, `*`, `/`, `+`, `-`, and parentheses.
- Choose `A1`, `$A$1`, `$A1`, or `A$1` correctly, on the first try, based on what should and shouldn't change when the formula is copied.
- Fill a formula across a full range in one motion and trust that every cell computed the *correct*, context-appropriate result.
- Name a range and read a formula that uses it as easily as one that doesn't.
- Look at `#REF!`, `#DIV/0!`, `#VALUE!`, or `#NAME?` and know, without searching, what caused it.

## Up next

[Week 3 — Logical & lookup functions](../week-03-logical-and-lookup-functions/) — once formulas and references are automatic, we teach the sheet to make decisions and look things up.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
