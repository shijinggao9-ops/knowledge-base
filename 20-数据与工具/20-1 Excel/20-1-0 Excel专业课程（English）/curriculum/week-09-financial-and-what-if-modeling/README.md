# Week 9 — Financial & What-If Modeling

> **Goal:** by Sunday you can build a loan amortization schedule from a rate and a term, evaluate whether an investment is worth making with NPV and IRR, structure a model so someone else can audit it in five minutes, and answer "what if the rate goes up two points?" with a data table instead of forty manual re-calculations.

Every week so far has taught you to *describe* data — clean it, look it up, summarize it, chart it. This week the spreadsheet starts **deciding**. A financial model doesn't just report what happened; it predicts what would happen under a loan you haven't signed yet, an investment you haven't made yet, a price you haven't set yet. That's a different kind of formula-writing — one where the inputs are assumptions, not facts, and where the whole point is to change those assumptions on purpose and watch the answer move. Get comfortable with that, and you've picked up the single most valuable spreadsheet skill outside of pure reporting: **modeling**.

We build one running example all week: **Crunch Manufacturing** needs a $250,000 equipment loan and is deciding between two capital projects to fund with the cash it frees up. Every lecture, exercise, challenge, and the mini-project extends that same scenario — by Saturday you'll have a single workbook that amortizes the loan, prices the two investments, and stress-tests both against optimistic and pessimistic assumptions.

## Learning objectives

By the end of this week, you will be able to:

- **Build a loan amortization schedule** using `PMT`, `IPMT`, and `PPMT` — computing the fixed payment, and the interest/principal split for any period, on both Excel and Google Sheets.
- **Evaluate investments** with `NPV` and `IRR` for evenly-spaced cash flows, and `XNPV`/`XIRR` when cash flows land on real, irregular calendar dates.
- **Structure a model** with clearly separated **inputs**, **calculations**, and **outputs** — so a stranger (or you, in six months) can audit it without reverse-engineering a wall of formulas.
- **Run one- and two-variable data tables** to see a formula's result across a whole grid of assumptions at once, instead of changing one cell and re-reading the answer by hand.
- **Use Goal Seek** to run a formula backwards — "what input produces this target output?" — and **Scenario Manager** to save and compare named sets of assumptions (Best/Base/Worst) with one click.
- **Document assumptions and stress-test outputs** — the difference between a model you built and a model you'd actually trust with a real decision.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `QMB 3600` — Build a loan amortisation schedule and evaluate an investment with `NPV`/`IRR`, lay the model out as separated inputs, calculations and outputs, and test it across a range of assumptions with data tables, Goal Seek and Scenario Manager. |
| Industry | Give a CFO the monthly payment across every rate-and-term combination the bank might offer, on one screen, before anything is signed. |
| Beyond the bar | An `Under the hood` block on what a data table is really recalculating behind that grid, folded so a learner may skip it entirely — `lecture-notes/03-what-if-analysis.md` |


## Prerequisites

- Weeks 1–8 complete, especially Week 2 (formulas and references — absolute references are everywhere this week) and Week 6 (structured references — the model layout leans on named ranges and Tables).
- Comfortable building a formula from scratch and reading `#REF!`/`#VALUE!`/`#NUM!` errors without panic.
- Excel and/or Google Sheets. **This is the one week the two apps genuinely diverge** — Excel ships Data Tables and Scenario Manager as built-in features; Google Sheets has Goal Seek but no native Data Table or Scenario Manager, so every lecture that touches those two features gives you the Sheets-native workaround. Read both halves even if you only use one app day to day — the workaround technique (a scenario switcher built from `CHOOSE`/data validation) is a useful skill on its own.

## Set up your workspace (do this first)

**Excel:**

1. **File → New → Blank workbook.**
2. **File → Save As** → `crunch-week9.xlsx`.
3. Create three sheet tabs: `Loan`, `Investments`, `WhatIf`. You'll fill each one across the week.

**Google Sheets:**

1. <https://sheets.google.com> → blank **(+)** template.
2. Rename the file to `crunch-week9`.
3. Create the same three tabs: `Loan`, `Investments`, `WhatIf`.

Sanity check — in any empty cell, type `=PMT(0.06/12, 60, 250000)` and press **Enter**. You should see approximately **`-$4,832.57`** (negative — that's a payment *out*, and Section 2 of Lecture 1 explains exactly why the sign is negative and why that's correct, not a bug).

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Time value of money; `PMT`/`IPMT`/`PPMT` | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | `NPV`/`IRR`/`XNPV`/`XIRR` | 2h | 1.5h | 0h | 0.5h | 1h | 0h | 5h |
| Wednesday | Structuring a model: inputs/calcs/outputs | 2h | 1h | 1h | 0.5h | 1h | 0h | 5.5h |
| Thursday | Data tables, Goal Seek, Scenario Manager | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Stress-testing; challenges | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (loan + investment model) | 0h | 0h | 0h | 0h | 0h | 3h | 3h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4h** | **3h** | **3.5h** | **5h** | **5.5h** | **30h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-financial-functions.md](01-financial-functions.md) | Time value of money, `PMT`/`IPMT`/`PPMT`, `NPV`/`IRR`/`XNPV`/`XIRR` | 2h |
| 2 | [lecture-notes/02-model-structure.md](02-model-structure.md) | Inputs vs. calculations vs. outputs, assumption cells, auditability | 2h |
| 3 | [lecture-notes/03-what-if-analysis.md](03-what-if-analysis.md) | One/two-variable data tables, Goal Seek, Scenario Manager | 2h |
| 4 | [exercises/exercise-01-amortization-schedule.md](exercise-01-amortization-schedule.md) | Build a full 60-month amortization schedule for the equipment loan | 1h |
| 5 | [exercises/exercise-02-npv-irr-compare.md](exercise-02-npv-irr-compare.md) | Compare two capital projects with `NPV` and `IRR`, pick the winner | 1.5h |
| 6 | [exercises/exercise-03-goal-seek-breakeven.md](exercise-03-goal-seek-breakeven.md) | Use Goal Seek to find a product's break-even unit volume | 1h |
| 7 | [challenges/challenge-01-sensitivity-table.md](challenge-01-sensitivity-table.md) | Build a two-variable sensitivity table (rate × term) for the loan payment | 1.5h |
| 8 | [challenges/challenge-02-three-scenario-model.md](challenge-02-three-scenario-model.md) | Model Best/Base/Worst cases for the investment decision | 1.5h |
| 9 | [mini-project/README.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/mini-project/README.md) | Loan + investment model: structured inputs, amortization, NPV/IRR, 3 scenarios | 3h |
| 10 | [homework.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-09-financial-and-what-if-modeling/resources.md) | Official docs + the few tools worth your time | — |

## By the end of this week you can…

- Compute a loan's payment, and split any single payment into interest and principal, from the rate and term alone.
- Look at a set of cash flows and correctly judge, with `NPV` and `IRR`, whether a project clears its hurdle rate.
- Hand a model to a stranger and have them find the three inputs that matter without reading a single formula.
- Answer "what if the rate is 7% instead of 6%?" — and "what if it's 7% *and* the term is 4 years?" — without touching a single input cell by hand.
- Build a Best/Base/Worst comparison and explain, in one sentence each, what has to be true for each case to happen.

## Up next

[Week 10 — Dynamic arrays & modern functions](../week-10-dynamic-arrays-and-modern-functions/) — once your models compute correctly, we make them shorter and more powerful with `FILTER`, `SORT`, `UNIQUE`, `LET`, and `LAMBDA`.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
