# Week 3 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on formula-writing, a written explanation, and a small independent build. Commit each.

All work builds on the `Grades`, `PriceList`, and `SalesMatrix` sheets from this week's lectures unless a problem says otherwise.

---

## Problem 1 — Twenty logic and lookup warm-ups (75 min)

Write and test each in a `warmups` sheet, one formula per row with the question as a comment or in a neighboring cell.

1. `IF` that returns `"Even"`/`"Odd"` for a number in `A1` (hint: `MOD(A1,2)=0`).
2. `IFS` that returns a shipping speed label for a number of days: `1` → `"Overnight"`, `2-3` → `"Express"`, `4-7` → `"Standard"`, else `"Economy"`.
3. `AND` formula: `TRUE` only if a number is both positive and even.
4. `OR` formula: `TRUE` if a number is negative or greater than 1000.
5. `NOT` formula that flips `ISBLANK(A1)` — explain in one sentence what the combined formula actually tests for.
6. `XLOOKUP` on `PriceList`: given a `Product` name (not SKU), return its `Price`. *(Note: you're now looking up by the second column instead of the first — same formula shape, different range.)*
7. Same lookup as #6, but with `if_not_found` set to `"No such product"`.
8. `XLOOKUP` returning the full row (`Product` through `InStock`) for a given `SKU`, spilling across 4 cells.
9. `XLOOKUP` with `match_mode = 1` (next **larger**) on the shipping-tier table from Lecture 2 — explain in one sentence how this differs from `-1`, and give an input where the two modes would return different tiers.
10. `MATCH` alone: what position is `"SKU-103"` in `PriceList!A2:A7`?
11. `INDEX` alone: what's in the 4th row, 3rd column of `PriceList!A2:E7`?
12. Combine #10 and #11's technique into one `INDEX`/`MATCH` that returns `SKU-103`'s `Category`.
13. A left-lookup: given an `InStock` count, find the corresponding `SKU` (assume unique stock counts for this one). Explain why `VLOOKUP` can't do this directly.
14. Wrap #13 in `IFERROR` with a sensible fallback.
15. `IFNA` vs `IFERROR`: write a formula that would behave *differently* under the two — i.e., one where `IFERROR` would hide a real bug that `IFNA` would let through. Explain the scenario in one sentence.
16. A two-way lookup on `SalesMatrix`: total sales for `"Devon"` in `"Q4"`.
17. The same two-way lookup, but with the rep name typo'd on purpose — confirm it errors, then wrap it to fail gracefully.
18. A compound `IF`: `"Bonus"` if `SalesMatrix` Q4 for a rep is both the rep's own highest quarter **and** over `40000`. *(Hint: compare `E-column` value to `MAX` of that rep's row.)*
19. Rewrite #2's shipping-speed `IFS` as nested `IF` instead, and confirm identical output for all 4 categories.
20. One formula that combines a logical test *and* a lookup: `IF` the product's `InStock` (via `XLOOKUP`) is `0`, return `"Reorder"`, else return the `InStock` number itself.

---

## Problem 2 — Explain the fragility, in writing (40 min)

In `vlookup-writeup.md`, answer in prose (no more than 350 words total):

1. In your own words, explain why `VLOOKUP`'s default `range_lookup` behavior is dangerous, using a concrete example with real numbers (not "it can go wrong" — show a specific formula and the specific wrong answer it would give).
2. Explain, with an example, what "the return column is counted by position, not name" means in practice, and what single spreadsheet edit breaks it.
3. Name one situation this week where `VLOOKUP` genuinely cannot solve the problem at all (not just "less safely") — and what you used instead.

---

## Problem 3 — Build a grade-band lookup table (50 min)

You wrote grade bands as `IFS` thresholds in Lecture 1. Now rebuild the same logic as a **lookup table** instead, and compare.

1. Build a small table: `MinScore` / `Letter` — `0`/`F`, `60`/`D`, `70`/`C`, `80`/`B`, `90`/`A`.
2. Write an `XLOOKUP` with `match_mode = -1` against this table that returns the correct letter for any score in `Grades!B2:B9`.
3. Confirm it produces identical letters to your Lecture 1 `IFS` formula for all 8 students.
4. In `lookup-table-writeup.md`, write 3–4 sentences: which approach (formula-with-hardcoded-thresholds, or lookup-table) would you rather maintain if the grading scale changed every semester, and why?

---

## Problem 4 — Case study: a broken formula (45 min)

You're handed this real (deliberately buggy) formula from a coworker's workbook, meant to flag students needing academic support:

```
=IF(B2<70 AND C2<0.8, "Support", "")
```

1. Run it. What error does Excel/Sheets give, and why? *(Hint: this is a syntax problem, not a logic problem — `AND` is a function, not an infix operator like `+`.)*
2. Fix it, and confirm it now works.
3. This coworker also has: `=IF(B2<70, IF(C2<0.8, "Support", ""), "")` — nested `IF` instead of `AND`, functioning correctly. Explain in one sentence why this alternate version *does* work despite avoiding `AND` entirely, and which version you'd actually prefer to maintain.

**Deliver** `broken-formula.md` with your answers to all three.

---

## Problem 5 — Independent build: a discount-tier calculator (60 min)

Design and build, from scratch, a small workbook section with **no starter data given** — this is the least scaffolded problem this week on purpose.

1. Invent an order-total-to-discount-rate policy with at least 4 tiers (e.g., under \$50 → 0%, \$50–\$199 → 5%, \$200–\$499 → 10%, \$500+ → 15%).
2. Build 8 sample orders with varied totals, including at least 2 right at your tier boundaries.
3. Compute each order's discount rate using **either** `IFS` or a lookup table (your choice — state which and why in one sentence).
4. Compute the final discounted total for each order.
5. Add one row that intentionally tests a boundary edge case, and confirm your formula puts it in the tier you intended.

**Deliver** your workbook plus `discount-tiers.md` (your policy, your tool choice and why, and confirmation the boundary case landed correctly).

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 40 min |
| 3 | 50 min |
| 4 | 45 min |
| 5 | 60 min |
| **Total** | **~4.5 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/mini-project/README.md).
