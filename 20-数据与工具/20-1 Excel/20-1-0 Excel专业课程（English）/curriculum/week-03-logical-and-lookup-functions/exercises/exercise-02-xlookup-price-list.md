# Exercise 2 — Price-Match With XLOOKUP

**Goal:** Build a working order form that looks up product name, price, and stock from a master price list with `XLOOKUP`, handles unknown SKUs cleanly, and applies an approximate-match shipping tier.

**Estimated time:** 1.5 hours.

## Setup

Use the `PriceList` sheet from Lecture 2. Confirm it has all 6 products (`SKU-100` through `SKU-105`). Add a new sheet, `Orders`, with:

```
       A            B          C        D          E              F
1    Order SKU    Product    Price    In Stock    Line Total     Status
2    SKU-101
3    SKU-104
4    SKU-999
5    SKU-102
6    SKU-103
```

Add a `Qty` column between `A` and `B` (shift everything right by one, or insert a column) so your final headers read: `Order SKU | Qty | Product | Price | In Stock | Line Total | Status`. Fill `Qty` with `2, 1, 3, 1, 5` for rows 2–6.

## Tasks

1. **Product name.** In `C2` (the `Product` column), write an `XLOOKUP` that finds `A2` in `PriceList!$A$2:$A$7` and returns the matching value from `PriceList!$B$2:$B$7`, with `"SKU not found"` as the fallback. Fill down through row 6.

2. **Price.** In `D2`, the same `XLOOKUP` shape, returning from `PriceList!$D$2:$D$7` instead, fallback `0`. Fill down. *(Think about why the fallback here is `0`, a number, and not a string like in Task 1 — what would happen to Task 4's math if it were text?)*

3. **Stock check.** In `E2`, `XLOOKUP` returning `InStock` from `PriceList!$E$2:$E$7`, fallback `0`. Fill down.

4. **Line total.** In `F2`, compute `Qty * Price` (`B2*D2`). Fill down. *(Expected: row 4, the unknown SKU, should compute to `0`, not an error — confirm your Task 2 fallback is doing its job.)*

5. **Status.** In `G2`, write an `IF` (nesting the logic from Exercise 1) that shows `"Unavailable"` if `E2` (stock) is `0`, `"Low stock"` if `E2` is between 1 and 10 inclusive, and `"OK"` otherwise. Use `IFS` or nested `IF` — your choice, but be consistent. Fill down. *(Expected: row 3, `SKU-104`, has 0 stock in the price list → `"Unavailable"`. Row 4, the unknown SKU, also shows `0` from your fallback, so it will *also* say `"Unavailable"` — that's a real limitation worth noticing: your fallback of `0` for "not found" is indistinguishable from a genuinely out-of-stock item once it reaches Task 5's logic. Add a stretch fix below if you want to close that gap.)*

6. **Shipping tier.** Below the order table, build the weight-tier table from Lecture 2 (`MinWeight`/`Cost`: `0`→`4.99`, `5`→`8.99`, `10`→`14.99`, `25`→`24.99`, `50`→`39.99`) in `A9:B13`. In `B15`, given a package weight typed into `A15`, write an `XLOOKUP` with `match_mode = -1` that returns the correct tier cost. Test with `18` (expect `14.99`), `4` (expect `4.99`), and `60` (expect `39.99`).

## Expected result (spot checks)

- Row 2 (`SKU-101`, qty 2): Product = `Mechanical Keyboard`, Price = `89.99`, Line Total = `179.98`.
- Row 4 (`SKU-999`, qty 3): Product = `"SKU not found"`, Price = `0`, Line Total = `0`, Status = `"Unavailable"`.
- Shipping tier for weight `18` → `14.99`.

## Done when…

- [ ] All five order-form columns (`C`–`G`) are filled down through row 6 with no raw `#N/A` anywhere.
- [ ] You can explain why Task 2's fallback is a number and Task 1's is text, and what would break if you swapped them.
- [ ] The shipping tier formula correctly returns `4.99`, `14.99`, and `39.99` for the three test weights.
- [ ] You've written one sentence (in a `Notes` cell or comment) about the Task 5 fallback ambiguity noted above.

## Stretch

- Fix the ambiguity from Task 5: use `IF(OR(exact match failed...))` — or more directly, wrap Task 1's lookup in a helper column `Found?` using `=ISNA(XLOOKUP(A2, PriceList!$A$2:$A$7, PriceList!$B$2:$B$7))` (returns `TRUE` if genuinely not found), then reference that helper column in Task 5's status logic instead of relying on the stock number alone.
- Add a `Discount` column: 10% off any line where `Qty >= 5`, using `IF`.

## Submission

Save your workbook. `PriceList` and `Orders` feed directly into the mini-project.
