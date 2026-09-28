# Lecture 2 — XLOOKUP: Modern Lookups Done Right

> **Duration:** ~2 hours. **Outcome:** You can write an `XLOOKUP` that finds an exact match and returns a value from another table, supply a clean default when nothing matches, return a whole row as an array, and use approximate matching for tiered lookups like shipping cost or discounts.

## 1. The problem a lookup function solves

Every function so far has worked on data that's already in front of it. A **lookup** answers a different question: "given this value, find its matching row somewhere else, and give me a value from that row." That's the single most common thing people do in a spreadsheet outside of pure arithmetic — look up a customer's price, an employee's department, a product's stock level — and it's what the rest of this week is about.

```mermaid
flowchart LR
  A["lookup_value: SKU-102"] --> B["Search lookup_array (Column A)"]
  B --> C["Find matching row"]
  C --> D["Read return_array, same row (Column D)"]
  D --> E["Result: 229.00"]
```
*A lookup walks from a known value to a matched row to the value pulled from that row.*

Build the `PriceList` sheet:

```
      A          B                    C           D        E
1   SKU        Product              Category    Price    InStock
2   SKU-100    Wireless Mouse       Peripherals  24.99    142
3   SKU-101    Mechanical Keyboard  Peripherals  89.99     37
4   SKU-102    27" Monitor          Displays    229.00     18
5   SKU-103    USB-C Hub            Peripherals  34.50     64
6   SKU-104    Webcam 1080p         Peripherals  45.00      0
7   SKU-105    Laptop Stand         Accessories  29.99      93
```

Now, below it, build a small order form that needs to look values up:

```
       A            B          C
9    Order SKU    Product    Price
10   SKU-102
11   SKU-999
12   SKU-101
```

`A11`'s `SKU-999` doesn't exist in the price list on purpose — you'll use it in Section 4 to test the not-found case.

## 2. `XLOOKUP` — the shape

```
=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
```

The first three arguments are the ones you'll use in nearly every formula:

- **`lookup_value`** — the thing you have (the SKU you typed into `A10`).
- **`lookup_array`** — the range to search for it in (`PriceList` column A).
- **`return_array`** — the range to pull the answer from, **same size and shape** as `lookup_array` (`PriceList` column D for price, column B for product name).

In `B10`, look up the product name:

```
=XLOOKUP(A10, PriceList!$A$2:$A$7, PriceList!$B$2:$B$7)
```

In `C10`, look up the price the same way, just pointing at column D:

```
=XLOOKUP(A10, PriceList!$A$2:$A$7, PriceList!$D$2:$D$7)
```

Fill both down through row 12. Notice the `$` absolute locks from Week 2 — the lookup and return ranges must stay fixed as you fill down; only `A10`/`A11`/`A12` should change. Row 10 (`SKU-102`) returns `27" Monitor` and `229`. Row 12 (`SKU-101`) returns `Mechanical Keyboard` and `89.99`. Row 11 will show an error for now — that's the point of the next section.

**`lookup_array` and `return_array` don't have to be adjacent, and the return column can be to the *left* of the lookup column.** This is the first real difference from the old `VLOOKUP` function, covered fully in Section 5 — `XLOOKUP` genuinely doesn't care about column order, because you point it at two independent ranges, not one block plus a column-offset number.

## 3. `if_not_found` — no more raw `#N/A`

Row 11's `SKU-999` isn't in the price list, so both formulas currently show `#N/A` — a real Excel/Sheets error value, not text. That's technically correct (the lookup genuinely found nothing) but it's a bad thing to hand a coworker or ship in a report. The fourth argument replaces it with anything you want:

```
=XLOOKUP(A11, PriceList!$A$2:$A$7, PriceList!$B$2:$B$7, "Not found")
```

Rewrite both `B11` and `C11` (or better — rewrite the whole column's formula once and fill down, since `if_not_found` should apply to every row, not just the one you know will fail):

```
B10: =XLOOKUP(A10, PriceList!$A$2:$A$7, PriceList!$B$2:$B$7, "Not found")
C10: =XLOOKUP(A10, PriceList!$A$2:$A$7, PriceList!$D$2:$D$7, "Not found")
```

Fill both down through row 12. Now row 11 shows `Not found` in both columns instead of `#N/A` — a formula error a downstream `SUM` or chart would choke on has become a plain, informative string. **Always supply `if_not_found` in any lookup that faces real-world data entry** — a typo'd SKU is a certainty, not an edge case, the moment a human is typing the lookup value.

## 4. `match_mode` — exact vs. approximate

The fifth argument controls *how* `XLOOKUP` decides something matches. The default (omit it, or pass `0`) is **exact match** — which is what you've used so far, and what you want for IDs, SKUs, and names. The other modes matter for a different kind of lookup: **tiered thresholds**, where you want "the largest bracket boundary that's still ≤ the value," not an exact hit.

Build a small shipping-cost tier table:

```
      A            B
1   MinWeight    Cost
2   0            4.99
3   5            8.99
4   10          14.99
5   25          24.99
6   50          39.99
```

A package weighing `18` lbs should match the `10` row (its bracket) — not fail because `18` isn't listed exactly. That's **approximate match, next-smaller**, `match_mode = -1`:

```
=XLOOKUP(18, A2:A6, B2:B6, "N/A", -1)
```

This returns `14.99` — the cost for the `10` bracket, because `18` falls between `10` and `25`. The `match_mode` values:

| `match_mode` | Behavior |
|---|---|
| `0` (default) | Exact match only. No match → `if_not_found` (or `#N/A`). |
| `-1` | Exact match, or if none, the next **smaller** item. |
| `1` | Exact match, or if none, the next **larger** item. |
| `2` | Wildcard match (`*`, `?`) — for text pattern lookups. |

**This is a genuine behavior change from `VLOOKUP`'s old `range_lookup=TRUE`, not just a rename.** The old approximate `VLOOKUP` *required* the lookup column to be sorted ascending, or it silently returned wrong answers with no warning. `XLOOKUP` with `-1`/`1` still expects the data reasonably ordered for the "next smaller/larger" logic to make sense, but it's explicit about *which direction* it's rounding — you choose `-1` or `1` on purpose, rather than getting whatever `VLOOKUP` decided based on sort order and a `TRUE` you may have set without fully understanding it.

## 5. `search_mode` — which end to start from

The sixth argument controls scan direction and is rarely needed, but two values are worth knowing: `1` (default) searches first-to-last; `-1` searches last-to-first, useful when a table has duplicate lookup values and you specifically want the *most recent* match (e.g., a transaction log where the same customer ID appears many times and you want their latest order, not their first).

## 6. Returning a whole row or column as an array

`return_array` doesn't have to be a single column. Point it at a multi-column range and `XLOOKUP` returns every value in that row **at once**, spilling across adjacent cells — this is a *dynamic array* formula, one of the modern behaviors that make `XLOOKUP` feel different from older functions:

```
=XLOOKUP(A10, PriceList!$A$2:$A$7, PriceList!$B$2:$E$7, "Not found")
```

Put this in `B10` alone (don't also fill `C10`/`D10`/`E10` — the formula spills into them automatically) and it fills `B10:E10` with Product, Category, Price, and InStock all from one formula. This is genuinely new: `VLOOKUP` returns exactly one value per formula, full stop. If you need five columns from `VLOOKUP`, you write five formulas, each recomputing the same match internally. One spilling `XLOOKUP` call replaces all five.

**Excel vs. Google Sheets — both spill,** but check your Excel version: dynamic array spilling (and `XLOOKUP` itself) requires Excel 365 or Excel 2021+. Older perpetual-license Excel (2019 and earlier) has neither — that audience needs `INDEX`/`MATCH`, covered next lecture, which has always worked everywhere.

## 7. Why XLOOKUP replaces VLOOKUP and HLOOKUP

You'll meet `VLOOKUP` constantly in older workbooks and tutorials, so you need to recognize it and know exactly why this course teaches `XLOOKUP` (or `INDEX`/`MATCH`) instead:

```
=VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])
```

`VLOOKUP` searches the **first column** of `table_array` and returns a value `col_index_num` columns to the right, counted manually. Three specific fragilities, all fixed by `XLOOKUP`:

1. **It can't look left.** The lookup value must be in the leftmost column of the range. If the value you *have* is in column D and the value you *want* is in column A, `VLOOKUP` cannot do it at all — you'd have to rearrange the source data. `XLOOKUP`'s `lookup_array`/`return_array` are independent ranges, so direction never matters.
2. **`col_index_num` is a hard-coded position, not a name.** `=VLOOKUP(A10, PriceList!A:E, 4, FALSE)` says "4th column of the range" — insert one new column into `PriceList` (say, a `Brand` column between `Product` and `Category`) and every `VLOOKUP` pointing past it now returns the *wrong* column, silently, with no error. `XLOOKUP` points its `return_array` directly at column D — insert a column elsewhere and the reference still tracks column D correctly, because it's a real range reference, not a counted offset.
3. **The `range_lookup` default is a trap.** Omit the fourth argument (or pass nothing) and `VLOOKUP` defaults to **approximate match** — the dangerous kind covered in Section 4 — not exact. Thousands of real spreadsheets ship with `=VLOOKUP(A2, B:C, 2)`, silently doing approximate matching nobody intended, because the author forgot the trailing `,FALSE`. `XLOOKUP` defaults to **exact match**, the safe behavior, so forgetting an argument fails safe instead of failing silently.

```mermaid
flowchart LR
  A["VLOOKUP fragilities"] --> B["Can't look left"]
  A --> C["Hard-coded col_index_num"]
  A --> D["range_lookup defaults to approximate"]
  B --> E["XLOOKUP: independent lookup_array / return_array"]
  C --> F["XLOOKUP: return_array is a real column reference"]
  D --> G["XLOOKUP: exact match is the default"]
```
*The three VLOOKUP fragilities, and the XLOOKUP behavior that fixes each one.*

`HLOOKUP` is `VLOOKUP`'s row-oriented twin (searches the first *row*, returns from a row below) and has the identical three problems. `XLOOKUP` handles both directions with the same one function — there's no separate "horizontal" version to remember.

## 8. Check yourself

- Write an `XLOOKUP` that looks up a product name in `PriceList!A2:A7` and returns the `InStock` count, with `"Unknown"` for anything not found.
- What does `match_mode = -1` do that plain exact match (`0`) doesn't, and why is it the right choice for a shipping-cost tier table?
- Name the three specific ways `VLOOKUP` is more fragile than `XLOOKUP`, in your own words — not "it's old," the actual mechanics.
- What Excel version cutoff means `XLOOKUP` won't be available, and what's the fallback?
- If you point `return_array` at a 4-column range instead of 1, what happens to the cells around the formula?

If those came quickly, move to Lecture 3 — `INDEX`/`MATCH`, the lookup approach that predates `XLOOKUP` and still matters for two-way lookups and older Excel.

## Further reading

- **Microsoft — XLOOKUP function:** <https://support.microsoft.com/en-us/office/xlookup-function-b7fd680e-6d10-43e6-84f9-88eae8bf5929>
- **Microsoft — Why XLOOKUP is better than VLOOKUP:** <https://support.microsoft.com/en-us/office/looking-up-data-with-vlookup-0bc48973-d3d3-4c15-8324-9e363b2f4e08>
- **Google — XLOOKUP:** <https://support.google.com/docs/answer/12360774>
- **Microsoft — VLOOKUP function (for reference, and recognizing legacy formulas):** <https://support.microsoft.com/en-us/office/vlookup-function-0bbc8083-26fe-4963-8ab8-93a18ad188a1>
