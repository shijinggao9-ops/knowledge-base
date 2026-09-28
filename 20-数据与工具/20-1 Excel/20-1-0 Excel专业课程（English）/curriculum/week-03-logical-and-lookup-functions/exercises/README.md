# Week 3 — Exercises

Three guided exercises, ~1–1.5 hours each. **Type every formula yourself** — don't copy-paste. Typing forces you to notice the `$` locks, the argument order, and the commas, all of which you'll get wrong at least once, which is exactly how they stick.

1. **[Exercise 1 — Grade scores with IF/IFS](exercise-01-nested-if-grading.md)** — nested `IF`, `IFS`, and `AND`/`OR` on a real gradebook.
2. **[Exercise 2 — Price-match with XLOOKUP](exercise-02-xlookup-price-list.md)** — exact match, `if_not_found`, and an approximate-match shipping tier.
3. **[Exercise 3 — Two-way INDEX/MATCH lookup](exercise-03-index-match-two-way.md)** — a row-and-column lookup plus a left-lookup, wrapped in `IFERROR`.

## Before you start

- You've completed all three lectures and built the `Grades`, `PriceList`, and `SalesMatrix` sheets they describe.
- You're comfortable with Week 2's `$` absolute/mixed references — every lookup this week needs a locked range.
- You have a workbook open (Excel or Google Sheets — every exercise works in both; differences are called out inline).

## Suggested workflow

- Open the exercise file beside your workbook.
- Build each task's formula, check it against the "Expected" note, and only then move on.
- If a result surprises you, stop and figure out *why* before continuing — chasing that confusion down is the actual lesson, not a distraction from it.
- Keep your workbook — you'll extend it in the mini-project.

## Note on the two engines

Every exercise works in both Excel (365/2021+) and Google Sheets. Where `XLOOKUP` isn't available (Excel 2019 and earlier), the exercise tells you the `INDEX`/`MATCH` fallback to use instead.
