# Exercise 3 — Write a Reusable LAMBDA

**Goal:** Write a custom function from scratch, register it with a name, call it like a built-in, and apply it across a whole column with `MAP`. By the end, `LAMBDA` feels less like a scary advanced feature and more like "I ran out of built-in functions, so I made one."

**Estimated time:** 1.5 hours.

## Setup

Work on the `Report` tab. You already have the `Orders` data loaded.

## Tasks

1. **Write the rule in plain English first.** Before touching a formula, write one sentence: "An order is **Small** if its Total is under $50, **Medium** if it's $50 up to (but not including) $150, and **Large** if it's $150 or more." Put that sentence in a cell as a comment or note — you'll compare your formula against it in Task 2.

2. **Write the inline `LAMBDA`, unregistered.** Build and immediately call it to test three values:

   ```excel
   =LAMBDA(order_total, IF(order_total < 50, "Small", IF(order_total < 150, "Medium", "Large")))(45)   ' expect "Small"
   =LAMBDA(order_total, IF(order_total < 50, "Small", IF(order_total < 150, "Medium", "Large")))(90)   ' expect "Medium"
   =LAMBDA(order_total, IF(order_total < 50, "Small", IF(order_total < 150, "Medium", "Large")))(200)  ' expect "Large"
   ```

   Confirm all three before moving on.

3. **Register it.** Give it the name `ORDERSIZE` (Excel: `Formulas → Define Name`; Sheets: `Data → Named functions → Add new function`), using the same `LAMBDA` body **without** the trailing call-parentheses. Test the registered version:

   ```excel
   =ORDERSIZE(45)     ' "Small"
   =ORDERSIZE(Orders!I5)  ' tier for whatever order sits in row 5
   ```

4. **Apply it across the whole column with `MAP`.**

   ```excel
   =MAP(Orders!I2:I31, ORDERSIZE)
   ```

   *(Expected: a 30-row spill of `"Small"`/`"Medium"`/`"Large"` tags, one per order, matching the Totals column row for row.)*

5. **Count each tier.** Using a `#` spill reference on your Task 4 formula, count how many orders fall into each tier with `COUNTIF`:

   ```excel
   =COUNTIF(D2#, "Small")     ' adjust D2 to wherever your Task 4 formula's anchor cell actually is
   ```

   *(Expected across all 30 orders, any status: 12 Small, 12 Medium, 6 Large. Verify all three counts and confirm they sum to 30.)*

6. **Extend the rule — a second parameter.** Real order-size logic shouldn't tag a **cancelled** order at all. Rewrite `ORDERSIZE` to take **two** parameters — `order_total` and `status` — and return `"N/A"` whenever `status = "Cancelled"`, otherwise the same Small/Medium/Large logic as before. Re-register it (same name is fine — editing an existing named function/`LAMBDA` updates every cell that calls it). Re-run Task 4 as `=MAP(Orders!I2:I31, Orders!J2:J31, ORDERSIZE)` and confirm the 3 Cancelled orders (order IDs 3008, 3016, 3024) now show `"N/A"` instead of a size tag.

## Done when…

- [ ] Your plain-English rule (Task 1) matches what your formula actually does.
- [ ] The three inline test calls (Task 2) all return the expected tier.
- [ ] `ORDERSIZE` is registered and callable by name from any cell.
- [ ] The `MAP`'d column (Task 4) has exactly 30 spilled values, and your `COUNTIF` counts (Task 5) sum to 30.
- [ ] The two-parameter version (Task 6) correctly shows `"N/A"` for all 3 Cancelled orders and unchanged tiers for everything else.

## Stretch

- Add a fourth tier, `"Flagship"`, for orders `>= 500`, and confirm exactly one order (3028) now falls into it instead of `"Large"`.
- Write a second `LAMBDA`, `REGIONCODE`, that maps each of the 4 region names to a 2-letter code of your choosing (e.g., `North` → `"NO"`), register it, and `MAP` it across the `Region` column.

## Submission

Commit your registered `LAMBDA` definition (copy the "Refers to"/formula text) plus the Task 5 counts to your portfolio under `c41-week-10/exercise-03/`.
