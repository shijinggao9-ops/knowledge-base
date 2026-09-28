# Week 9 — Exercises

Three guided exercises, ~1–1.5 hours each, all built on the same running Crunch Manufacturing scenario from the lectures. **Build every formula yourself** — don't paste in finished numbers from this document; predicting a result before you check it is what makes these functions stick.

1. **[Exercise 1 — Build an Amortization Schedule](exercise-01-amortization-schedule.md)** — the full 60-month loan schedule from Lecture 1, with a running balance that hits exactly zero.
2. **[Exercise 2 — Compare Projects With NPV/IRR](exercise-02-npv-irr-compare.md)** — evaluate two capital projects and recommend which one Crunch should fund.
3. **[Exercise 3 — Find Break-Even With Goal Seek](exercise-03-goal-seek-breakeven.md)** — use Goal Seek to find the unit volume a new product needs to break even.

## Before you start

- You've completed all three lectures.
- Your `crunch-week9` workbook has its `Loan`, `Investments`, and `WhatIf` tabs from the README's setup step.
- You're comfortable naming a cell (Week 2) and can find **Data → What-If Analysis** (Excel) or **Tools → Goal Seek** (Sheets) without hunting.

## Suggested workflow

- Build the **Assumptions** block first, name every input cell, and only then write the calculation formulas that reference those names — Lecture 2's structure isn't optional decoration here, the later exercises and the mini-project assume it's already in place.
- Predict each result before you press Enter. If a `PMT`, `NPV`, or `IRR` comes back with the wrong sign or an unexpected magnitude, stop and work out why before moving on — that's usually a sign convention or a range that's one row off, not a typo in the function name.
- Keep each exercise in its own labeled section of the relevant tab (or its own tab) so your workbook stays one continuous, growing model across the week.

## Note on the two apps

Exercises 1 and 2 use only functions (`PMT`, `IPMT`, `PPMT`, `NPV`, `IRR`) that work identically in Excel and Google Sheets. Exercise 3 uses Goal Seek, which exists in both apps under different menus — the exercise gives both paths.
