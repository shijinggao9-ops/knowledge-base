# Week 10 — Homework

Five problems, ~5 hours total, spread across the week. These reinforce the lectures with a mix of hands-on formula practice, a written explanation, a `LET` cross-check, and a build-your-own-`LAMBDA` task. Commit each.

All formulas run against the `Orders` data from the [README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/README.md) unless a problem says otherwise. Keep the data at its original 30 rows for Problems 1–4; Problem 5 has you extend it deliberately.

---

## Problem 1 — Twenty warm-up FILTER/SORT/UNIQUE formulas (75 min)

Write and run each as a spilling formula on your `Report` tab. Label each with a `Task N` header above it, and note the result beneath.

1. Distinct categories, in first-seen order (no sort). *(Expect 4: Audio, Accessories, Wearables, Smart Home.)*
2. Distinct categories, alphabetized. *(Expect: Accessories, Audio, Smart Home, Wearables.)*
3. Count and total revenue of every order in the `Audio` category, any status. *(Expect 8 orders, $858.00.)*
4. Count and total revenue of every order in the `Wearables` category, any status. *(Expect 7 orders, $1,663.00.)*
5. All orders with `Qty >= 3`, any status. *(Expect 6 orders: 3005, 3008, 3015, 3018, 3025, 3028.)*
6. All Pending orders, sorted by `Total` descending. *(Expect 8 rows, led by order 3006 at $178.00.)*
7. All East-region orders, sorted by `OrderDate` ascending. *(Expect 7 rows, earliest is order 3003 on 2026-01-10.)*
8. Total revenue for Shipped orders placed by rep `C. Novak`. *(Expect $680.00, 4 orders.)*
9. Total revenue for Shipped orders placed by rep `A. Kim`. *(Expect $119.00, 3 orders.)*
10. All Smart Home category orders that are Shipped, sorted by `Total` descending. *(Expect 7 rows, led by order 3028 at $516.00, summing to $1,035.00.)*
11. Distinct (Rep, Region) combinations across all 30 orders. *(Expect 20 — every rep appears in every region exactly once. Confirm this by counting your spill's rows.)*
12. The 3 products with the highest total Shipped revenue, and their revenue, ranked highest first. *(Expect: Video Doorbell $903.00, Wireless Earbuds $413.00, Fitness Band $270.00.)*
13. All orders placed in **February 2026**, any status. *(Hint: compare `OrderDate` against `>= DATE(2026,2,1)` and `< DATE(2026,3,1)`. Expect 11 orders totaling $1,086.00.)*
14. The single highest-`Total` order company-wide, any status, returned as a one-row `FILTER`. *(Expect order 3008, $796.00 — note it's Cancelled, which is exactly why a real report needs a status filter, not just a max.)*
15. Every Cancelled order. *(Expect 3 orders: 3008, 3016, 3024, totaling $1,393.00.)*
16. Distinct reps who have **at least one** Cancelled order. *(Expect: A. Kim, C. Novak, D. Osei — 3 reps.)*
17. All orders **not** in the `Audio` or `Accessories` categories, sorted by `OrderDate`. *(Expect 14 rows — the Wearables + Smart Home orders, oldest first.)*
18. `SORTBY` the `Rep`/`Product` columns only (2 columns) by `Total` descending, without displaying `Total` itself. *(Expect the first row to be C. Novak / Smartwatch — the $796.00 order — even though $796.00 never appears in the output.)*
19. Using `TAKE`, the 3 **most recently placed** orders (any status), most recent first. *(Expect order 3030 first, dated 2026-03-24.)*
20. `COUNTA` on a `UNIQUE` of `Product`, vs. `COUNTA` on a `UNIQUE` of `Category`. *(Expect 8 and 4 respectively — explain in one sentence why a business would care about the ratio between these two numbers.)*

---

## Problem 2 — Explain the spill model and LET (45 min)

In `spill-and-let-writeup.md`, answer in prose (no more than 400 words total):

1. In your own words, what's the difference between the *anchor cell* and the rest of a *spill range*? What error message would you expect if a spill range's landing zone already has data in it?
2. Explain why `FILTER(range, cond1 * cond2)` means AND while `FILTER(range, cond1 + cond2)` means OR — walk through what `TRUE`/`FALSE` actually become in that arithmetic.
3. Give a concrete example (from this week's `Orders` data or invented) of a formula that would be genuinely *slower*, not just uglier, without `LET` — one where a sub-expression is repeated at least three times.
4. What's the practical difference between `SORT`'s `sort_index` argument and `SORTBY`'s design — when would you reach for one over the other?

---

## Problem 3 — LET cross-check across two engines (45 min)

The same computation, two ways. In a new area of the `Report` tab, `CrossCheck`:

1. Build one `LET`-wrapped formula: the average `Total` of Shipped orders in the `East` region.
2. Build the *same* average using a plain nested formula with **no** `LET` (repeat the `FILTER` expression as many times as needed — this is for comparison only, not to keep).
3. Confirm both return the identical number. *(Expect ≈$57.43.)*
4. Now add one new row to `Orders`, in the middle, with `Region = "East"`, `Status = "Shipped"`, `Total = 300`. Re-check both formulas.

**Deliver** the two formulas plus a two-sentence note: did both update correctly? If so, what does that tell you about when `LET` actually matters — is it about correctness, or about something else? *(Then remove the row you added and confirm both formulas return to their original values.)*

---

## Problem 4 — Build a second LAMBDA from scratch (60 min)

Design and register a new function, `SHIPCOST`, that estimates a shipping surcharge for an order based on its `Category`:

- `Smart Home` → `$12.00` flat (bulky items)
- `Wearables` or `Audio` → `$4.00` flat
- `Accessories` → `$0.00` (ships free)

1. Write the `LAMBDA` (one parameter: `category`), test it inline against all 4 category names first.
2. Register it as `SHIPCOST`.
3. Apply it with `MAP` across the entire `Category` column, spilling one surcharge per order.
4. Add a `SUM` beneath your spill: total shipping surcharge across all 30 orders, any status. *(Expect: 8 Audio × $4.00 + 8 Accessories × $0.00 + 7 Wearables × $4.00 + 7 Smart Home × $12.00 = $32.00 + $0.00 + $28.00 + $84.00 = $144.00.)*

**Deliver** the registered `LAMBDA` definition and the $144.00 total, confirmed.

---

## Problem 5 — Extend the dataset and confirm the reports still work (60 min)

Make the `Orders` data your own and re-run this week's reports against it.

1. Add **4 new orders** of your invention directly below row 31. Include at least: one Shipped order over $600 (higher than any current Shipped order), one Cancelled order, and one in a category you invent (e.g., `"Home Office"`) with at least one product.
2. Update your named range `Orders` to cover the new rows (Week 2's Name Manager — extend `A1:J31` to `A1:J35`).
3. Re-run any two `LET`-wrapped formulas from Problem 1 or the exercises and confirm they pick up the new rows correctly with **zero formula edits** — only the named range's boundary changed.
4. If you built a `LAMBDA` this week (`ORDERSIZE`, `SIZETIER`, or `SHIPCOST`), confirm it correctly classifies your new invented category too (or explain, in one sentence, why it doesn't and what you'd need to add to make it handle a category it's never seen).

**Deliver** a before/after note: which two formulas you re-ran, their result before adding rows, and their result after — plus one sentence on what, if anything, broke and why.

---

## Time budget

| Problem | Time |
|--------:|----:|
| 1 | 75 min |
| 2 | 45 min |
| 3 | 45 min |
| 4 | 60 min |
| 5 | 60 min |
| **Total** | **~4.75 h** |

After homework, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/quiz.md) and ship the [mini-project](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-10-dynamic-arrays-and-modern-functions/mini-project/README.md).
