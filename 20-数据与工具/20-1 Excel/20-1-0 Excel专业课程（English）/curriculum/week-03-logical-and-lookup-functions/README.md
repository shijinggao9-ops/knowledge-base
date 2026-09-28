# Week 3 — Logical & Lookup Functions

> **Goal:** by Sunday you can branch a formula's result on any condition with `IF`/`IFS`/`AND`/`OR`/`NOT`, pull a value from another table with `XLOOKUP` (or `INDEX`/`MATCH` when you need a lookup XLOOKUP can't do), and wrap every lookup in an error trap so a missing match shows a clean message instead of `#N/A`.

Welcome back to **C41 · Crunch Excel**. Week 1 gave you the grid. Week 2 gave you formulas that calculate and copy correctly. This week your formulas start **making decisions** and **finding things** — the two moves that turn a spreadsheet from a calculator into a small program. Every real workbook you'll ever open uses these constantly: a grading sheet decides a letter grade from a score; an invoice looks up a customer's price from a master list; a payroll sheet decides a bonus tier from a sales total. By Sunday, both of those are things you build, not things you Google.

This week also retires a function you may already know badly: `VLOOKUP`. You'll learn *why* it breaks so easily, and replace it everywhere with `XLOOKUP` (or `INDEX`/`MATCH` where `XLOOKUP` isn't available). If you've never touched a lookup function before, that's fine too — you're starting on the modern, correct tool instead of unlearning the old one.

You'll keep working in the same kind of workbook as Week 2 — build the seed data yourself as each lecture directs; no file to download.

## Learning objectives

By the end of this week, you will be able to:

- **Branch logic** with `IF`, understand when nested `IF`s become unreadable, and replace them with `IFS` for cleaner multi-condition logic.
- **Combine conditions** with `AND`, `OR`, and `NOT` to express real business rules ("both must be true," "either is enough," "the opposite of this").
- **Look up values** with `XLOOKUP`, controlling exact vs. approximate matching, returning whole rows/columns as arrays, and supplying a clean default when nothing matches.
- **Explain concretely** why `VLOOKUP` breaks when columns are inserted, why it can't look left, and why `XLOOKUP` fixes both.
- **Build flexible lookups** with `INDEX` and `MATCH` combined — including left-lookups and two-way (row *and* column) lookups that neither `VLOOKUP` nor `XLOOKUP` alone handles as cleanly.
- **Trap lookup errors** with `IFERROR` and `IFNA` so a missing match never leaks a raw `#N/A`/`#REF!` into a report.
- **Choose the right tool** for a given lookup — and know exactly where Excel and Google Sheets diverge (`XLOOKUP` availability, `IFS`, array-return behavior).

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `QMB 3600` — Branch on conditional logic and look values up across tables, choosing between `XLOOKUP` and `INDEX`/`MATCH` for the case at hand and trapping the miss instead of leaking `#N/A` into a report. |
| Industry | Audit a departed colleague's lookup model and replace every fragile lookup with one that survives an inserted column, a left-lookup and an unmatched key. |
| Beyond the bar | An `Under the hood` block on what `MATCH` is actually doing to find a position, and what that costs — folded, so a learner may skip it and still finish the week — `lecture-notes/03-index-match-and-errors.md` |


## Prerequisites

- Week 1 and Week 2 complete — you're comfortable with A1 references, `$` absolute/relative locking, and the five core aggregate functions (`SUM`, `AVERAGE`, `COUNT`/`COUNTA`, `MIN`/`MAX`).
- Excel (365 or Excel for the web — `XLOOKUP` requires a current version; Excel 2019 and earlier don't have it, use `INDEX`/`MATCH` there) **and/or** Google Sheets (has had `XLOOKUP` since 2022, free with any Google account).
- No macros, no VBA, no prior lookup-function experience required.

## Set up your workspace (do this first)

Open a fresh blank workbook (Excel: `crunch-week3.xlsx` — File → New; Sheets: blank at <https://sheets.google.com>, rename to `crunch-week3`). Add three sheets, renamed exactly as below (double-click a sheet tab to rename in either app):

1. **`Grades`** — you'll build a small gradebook here in Lecture 1 and Exercise 1.
2. **`PriceList`** — a master product price list, built in Lecture 2 and used through Exercise 2 and the mini-project.
3. **`SalesMatrix`** — a rep-by-quarter sales grid for the two-way lookup in Lecture 3 and Exercise 3.

Each lecture tells you exactly what to type into its sheet — you're building the data as you learn, the same way you did in Week 2.

Sanity check: you should have three renamed, empty sheet tabs before starting Lecture 1. If a tab still says `Sheet1`/`Sheet2`, rename it now (Week 1, Lecture 2 covers how).

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | `IF`/`IFS`, `AND`/`OR`/`NOT` — branching logic | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | `XLOOKUP` — exact/approximate match, arrays, defaults | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | `INDEX`/`MATCH`, left-lookups, two-way lookups | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | `IFERROR`/`IFNA`; replacing every `VLOOKUP` | 0h | 0h | 1h | 0.5h | 1h | 1h | 3.5h |
| Friday | Tiered commission logic; catch-up | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (grade a class + price-match a catalog) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5h** | **26.5h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-logical-branching.md](01-logical-branching.md) | `IF`, nested `IF` vs. `IFS`, `AND`/`OR`/`NOT`, and real branching rules | 2h |
| 2 | [lecture-notes/02-xlookup-modern-lookups.md](02-xlookup-modern-lookups.md) | `XLOOKUP` exact/approximate matching, array returns, `if_not_found`, why it replaces `VLOOKUP`/`HLOOKUP` | 2h |
| 3 | [lecture-notes/03-index-match-and-errors.md](03-index-match-and-errors.md) | `INDEX`/`MATCH`, left-lookups, two-way lookups, `IFERROR`/`IFNA` | 2h |
| 4 | [exercises/exercise-01-nested-if-grading.md](exercise-01-nested-if-grading.md) | Grade scores with `IF`/`IFS` | 1h |
| 5 | [exercises/exercise-02-xlookup-price-list.md](exercise-02-xlookup-price-list.md) | Price-match with `XLOOKUP` | 1.5h |
| 6 | [exercises/exercise-03-index-match-two-way.md](exercise-03-index-match-two-way.md) | Two-way `INDEX`/`MATCH` lookup | 1.5h |
| 7 | [challenges/challenge-01-replace-every-vlookup.md](challenge-01-replace-every-vlookup.md) | Replace every `VLOOKUP` in a small model | 1h |
| 8 | [challenges/challenge-02-tiered-commission-logic.md](challenge-02-tiered-commission-logic.md) | Build tiered commission logic | 1h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/mini-project/README.md) | Grade a class + price-match a catalog with `XLOOKUP` and fallbacks | 2.5h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/homework.md) | Extra practice, spaced across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/quiz.md) | 14 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Write a nested `IF` for two or three thresholds, then rewrite it as `IFS` and explain why the second is more readable.
- Combine `AND`/`OR`/`NOT` inside an `IF` to express a compound business rule in a single cell.
- Write an `XLOOKUP` that finds an exact match, returns a whole row as an array, and shows `"Not found"` instead of `#N/A` when nothing matches.
- Explain, with a concrete example, why `VLOOKUP` breaks when a column is inserted and `INDEX`/`MATCH` (and `XLOOKUP`) don't.
- Build a two-way lookup that finds a value at the intersection of a row label and a column label.
- Decide, for a given lookup problem, whether `XLOOKUP` or `INDEX`/`MATCH` is the right tool — and in Excel-without-`XLOOKUP`, fall back correctly.

## Up next

[Week 4 — Text & date functions](../week-04-text-and-date-functions/) — once you can branch and look things up, we start parsing and reshaping messy real-world text and dates.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
