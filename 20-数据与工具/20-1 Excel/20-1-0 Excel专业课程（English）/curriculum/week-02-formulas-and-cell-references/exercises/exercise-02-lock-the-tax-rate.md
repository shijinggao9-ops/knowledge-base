# Exercise 2 — Lock a Rate With Absolute References

**Goal:** Build a small priced order sheet where line totals use relative references and a shared tax rate uses an absolute reference — and prove to yourself, by filling the formula down, that only the absolute one survives correctly.

**Estimated time:** 60–75 minutes.

## Setup

Create (or rename) a sheet tab called `Ex2`. Build this table exactly, starting at `A1`:

```
      A            B         C          D
1   Item         Price     Qty        Line Total
2   Keyboard     45.00     2
3   Mouse        18.50     3
4   Monitor      210.00    1
5   USB Cable    6.25      5
6   Headset      32.00     2
```

Then, off to the side, set up a shared tax rate:

```
      F              G
1   Tax Rate       0.075
```

## Tasks

1. **Line totals (relative references).** In `D2`, write a formula that multiplies price by quantity for that row. Fill it down through `D6`. Confirm every row computed correctly and independently — each row's `Price` and `Qty` should have come from *that same row*, not row 2 repeated.

2. **A broken tax column, on purpose.** In `E1`, label it `Tax (broken)`. In `E2`, write `=D2*G1` — a plain relative reference to the tax rate, **no `$`**. Fill it down through `E6`. Look at the formula in `E4` (use `Ctrl+`` `` to reveal formulas, or click the cell and read the formula bar) and write down, in a `Notes` cell, exactly what reference it's actually pointing at now, and what value (or error) that produces.

3. **A correct tax column.** Label `H1`: `Tax (correct)`. In `H2`, write a formula that multiplies the line total by the tax rate **using an absolute reference** so it survives filling. Fill down through `H6`. Confirm every row now shows a sensible, non-zero, non-error tax amount, all consistent with the same 7.5% rate.

4. **Grand total with tax.** In `D8`, label `A8`: `Grand Total (with tax)`. Write one formula that sums the line totals (`D2:D6`) and adds the sum of the correct tax column (`H2:H6`) — or equivalently, sums `D` and multiplies by `(1 + tax rate)`. Either approach is valid; pick one and be able to explain why it's correct.

5. **Change the rate once, watch it ripple.** Change `G1` from `0.075` to `0.10`. Confirm: the broken `E` column still shows garbage (or gets worse), the correct `H` column updates every row instantly and correctly, and the grand total in `D8` updates too. This one edit — changing a single locked cell and watching every dependent formula update — is the entire point of absolute references.

## Expected results (spot checks, at 7.5% tax)

- `D2` (Keyboard line total) → `90.00`.
- `D6` (Headset line total) → `64.00`.
- `H2` → `6.75` (`90.00 * 0.075`).
- Sum of `D2:D6` → `450.75`.
- Grand total with tax (`D8`) → `484.56` (rounded to 2 decimals; `450.75 * 1.075`).

## Done when…

- [ ] `D2:D6` are all correct, independent, relative-reference line totals.
- [ ] The broken `E` column visibly fails when filled — you can point to exactly which cell each row's formula wrongly references.
- [ ] The correct `H` column is right in every row, using either `$G$1` or a fully absolute reference form.
- [ ] Changing `G1` updates `H2:H6` and `D8` automatically, without retyping any formula.
- [ ] You can state, in one sentence, why `$` on `G1` is required here but was **not** needed on `B2`/`C2` in the line-total formula.

## Stretch

- Add a second shared value, `G2: Shipping Flat Fee` = `4.99`, and a column `I` that adds this flat fee to each row's `Line Total + Tax` — using a second absolute reference alongside the first.
- Delete the broken `E` column entirely once you've learned from it, and confirm nothing else in the sheet breaks (it shouldn't — nothing referenced `E`).

## Submission

Keep the `Ex2` sheet in your `crunch-week2` workbook alongside `Ex1`.
