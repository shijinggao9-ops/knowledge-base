# Week 10 — Exercises

Three guided exercises, ~1–1.5 hours each. **Do every step yourself, in the actual app** — spilling only really sinks in once you've watched a spill range grow and shrink live as you edit the source data.

1. **[Exercise 1 — Build a Live FILTER Report](exercise-01-filter-sort-unique.md)** — write `FILTER`, `SORT`, and `UNIQUE` formulas against the `Orders` data, alone and nested together.
2. **[Exercise 2 — Refactor a Formula With LET](exercise-02-let-refactor.md)** — take a genuinely ugly nested formula and rebuild it as a readable, named `LET`.
3. **[Exercise 3 — Write a Reusable LAMBDA](exercise-03-write-a-lambda.md)** — write, register, and test your own named function, then apply it across a range with `MAP`.

## Before you start

- You've completed all three lectures.
- You have the `Orders` data from the week README loaded on the `Orders` tab (`A1:J31`, named range `Orders`), with a `Report` tab ready for these formulas.
- Excel 365/2021/web with dynamic arrays, or current Google Sheets. If `=SEQUENCE(3)` doesn't spill three stacked numbers when you test it, you're on an unsupported version — see the week README's prerequisites.

## Suggested workflow

- Do each step in order — Exercise 3's `LAMBDA` reuses a rule from Exercise 1.
- Keep every exercise's formulas on the `Report` tab in clearly labeled sections (a bold header row above each, e.g. `Exercise 1 — Task 3`), rather than overwriting earlier work — the mini-project pulls techniques from all three.
- After every formula, glance at its spill range before moving on: does it spill as many rows as you expect? If a `#SPILL!` or `#CALC!` shows up, resolve it before continuing — don't work around it with a smaller range.
