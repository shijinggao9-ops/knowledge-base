# Challenge 1 — Replace Every VLOOKUP in a Model

**Time:** ~60 minutes. **Difficulty:** Medium. **No single right formula — but every replacement must survive the stress test.**

## The scenario

You've inherited a small inventory-reorder workbook from a coworker who left the company. It "works," but it's held together with `VLOOKUP`s written the fragile way — hard-coded column numbers, defaults left on approximate match, and one lookup that's flat-out impossible with `VLOOKUP` so it was worked around with a manual copy-paste that's already gone stale. Your job: find every fragility, prove it's real by breaking it, then replace it with something that survives.

## Build the model

Create a `Reorder` sheet with a master item table:

```
       A          B              C            D          E           F
1    ItemCode   ItemName       Supplier     UnitCost   ReorderQty   OnHand
2    ITM-01     Copy Paper     Staples Co.    4.20        50         12
3    ITM-02     Ink Cartridge  InkWorld       28.50       10          3
4    ITM-03     Stapler        Staples Co.    6.75        20         31
5    ITM-04     Binder Clips   OfficeMax      2.10        40          8
6    ITM-05     Whiteboard     OfficeMax      45.00        5          2
7    ITM-06     Sticky Notes   3M Direct      3.85        60         22
```

And a reorder-decision table that uses these formulas (build them exactly as shown, on purpose, so you can watch them break):

```
       A            B                                                         
9    ItemCode     Formula (in ItemName, next column over)                       
10   ITM-03       =VLOOKUP(A10, A2:F7, 2)
11   ITM-05       =VLOOKUP(A11, A2:F7, 2)
```

In `C10`/`C11` (a `UnitCost` column), add: `=VLOOKUP(A10, A2:F7, 4)` and `=VLOOKUP(A11, A2:F7, 4)`.

## The three breaks — reproduce each one, then fix it

### Break 1 — the missing `FALSE`

Look closely at the `VLOOKUP` formulas above: none of them specify `range_lookup`. Test it — type `ITM-99` (doesn't exist) into `A10`. What does `C10` return? Is it an error, or a plausible-looking wrong number? Explain in `challenge-01.md` exactly why it behaves that way, referencing what the *default* `range_lookup` value does.

**Fix:** replace both formulas with `XLOOKUP` (exact match by default, with an explicit `if_not_found`), or `VLOOKUP` with `FALSE` added — but explain in your writeup why `XLOOKUP` is still the better choice even with `FALSE` added.

### Break 2 — the column insert

Insert a new column between `ItemName` (B) and `Supplier` (C) — call it `Category` — and fill it with any values you like for the 6 items. Now look at your *original, unfixed* `C10`/`C11` formulas (the `UnitCost` ones, `VLOOKUP(A10, A2:F7, 4)`). What do they return now, and is it correct? Explain exactly why, referencing what `col_index_num` actually counts.

**Fix:** confirm your `XLOOKUP` replacements from Break 1 were *not* affected by the column insert (they shouldn't need any edits at all) — and explain in one sentence why pointing directly at a range survives a column insert when a counted offset doesn't.

### Break 3 — the impossible left-lookup

Your coworker needed to look up `ItemCode` given a `Supplier` name (e.g., "which item code belongs to InkWorld?") — but `Supplier` sits in a column to the right of `ItemCode`, and `VLOOKUP` can't search anything but its first column. Find evidence in the sheet (or imagine it, and describe it) of how someone would have "solved" this without `INDEX`/`MATCH` or `XLOOKUP` — hint: manually retyping/copy-pasting the answer once, which then never updates again.

**Fix:** write a correct `INDEX`/`MATCH` (or `XLOOKUP`) formula that looks up `ItemCode` from a typed-in `Supplier` name, and test it against at least two suppliers that appear more than once in your table (`Staples Co.` and `OfficeMax` both appear twice — decide and state which match your formula returns when there are duplicates, and whether that's actually the right behavior for this business question).

## Constraints

- Every replacement formula must include explicit error handling (`if_not_found`, or `IFERROR`/`IFNA`) — no raw `#N/A` in your final version.
- State, for each of the 3 breaks, the exact input that reproduces it (a specific `ItemCode`, a specific column insert) so someone else could verify your finding without guessing.
- If you're on Excel without `XLOOKUP`, use `INDEX`/`MATCH` throughout and note that you did.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|---------------|
| Reproduction | Describes breaks in the abstract | Gives the exact input/action that reproduces each break, and the exact wrong output it produced |
| Root cause | "VLOOKUP is old and bad" | Names the specific mechanism (default `range_lookup`, counted `col_index_num`, first-column-only search) |
| Fix quality | Swaps in `XLOOKUP` with no error handling | Every fix includes a fallback for "not found," and the duplicate-supplier judgment call in Break 3 is stated explicitly |
| Verification | Trusts the fix without testing | Re-runs the exact break scenario against the new formula and confirms it now behaves correctly |

## Submission

Save your workbook and `challenge-01.md` (your writeup of all three breaks, their root causes, and your fixes) to your portfolio under `c41-week-03/challenge-01/`.
