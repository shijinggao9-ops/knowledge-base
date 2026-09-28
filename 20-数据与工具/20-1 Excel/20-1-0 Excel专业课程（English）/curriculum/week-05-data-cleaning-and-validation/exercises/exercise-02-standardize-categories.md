# Exercise 2 — Standardize Category Values

**Goal:** Collapse a fragmented category/unit column down to one canonical spelling per real-world value, using the frequency-count audit and Find & Replace / `SUBSTITUTE` techniques from Lectures 1 and 2.

**Estimated time:** 45–60 minutes.

## Setup

Add a new sheet named `Ex2-Standardize`. Type this raw product list in exactly as shown:

```
      A          B                    C            D
1   SKU        Product              Category     Weight
2   SKU-201    Trail Backpack       Gear         2.3kg
3   SKU-202    Down Jacket          apparel      1.1 kg
4   SKU-203    Hiking Boots         Footwear     900g
5   SKU-204    Water Bottle         gear         0.4kg
6   SKU-205    Rain Shell           Apparel      0.5 kg
7   SKU-206    Trekking Poles       GEAR         600g
8   SKU-207    Wool Socks           footwear     0.1kg
9   SKU-208    Base Layer Top       apparel      0.2 kg
10  SKU-209    Camp Stove           Gear         450g
11  SKU-210    Sandals              Footwear     0.3kg
12  SKU-211    Fleece Pullover      APPAREL      0.6kg
13  SKU-212    Sleeping Bag         gear          1.8 kg
14  SKU-213    Trail Runners        Footwear     700g
```

Two separate standardization problems live in this one table:

- **`Category`** has three real categories (`Apparel`, `Footwear`, `Gear`) spelled with **six** total casing variants (`Gear`/`gear`/`GEAR`, `Apparel`/`apparel`/`APPAREL`, `Footwear`/`footwear`).
- **`Weight`** mixes **units** (`kg` vs `g`) *and* formatting (some have a space before the unit, some don't) inside what should be one consistent numeric measurement.

## Tasks

### Part A — Category casing

1. Run a frequency-count audit (Lecture 1, Section 7 — `UNIQUE` + `COUNTIF`, or a `COUNTIF` per known value if your app lacks `UNIQUE`) on the `Category` column. Confirm you count exactly the fragmentation described above before fixing anything.

2. Standardize using **either** approach — do both and compare:
   - Find & Replace with **Match entire cell contents ON**, running one pass per casing variant.
   - A single formula: `=PROPER(TRIM(C2))`, then paste-as-values. *(Careful: `PROPER` alone won't fix `GEAR` → `Gear` incorrectly — check it actually does what you expect on an all-caps input before trusting it on the whole column.)*

3. Re-run your frequency-count audit. You should now see exactly **3** distinct values: `Apparel`, `Footwear`, `Gear`.

### Part B — Weight units

This one can't be fixed with casing tools — it needs actual unit conversion, because `2.3kg` and `900g` aren't spelling variants of the same value, they're **different units measuring the same kind of thing**.

4. Build a helper column that extracts the **numeric portion** of each `Weight` cell. One approach: `=VALUE(LEFT(TRIM(D2), FIND(" ", TRIM(D2) & " ") - 1))` (this trims the cell, appends a trailing space so `FIND` always locates one even on inputs with no space before the unit, then takes everything before it and converts to a real number). Test this against a couple of rows by hand before trusting it on the whole column.

5. Build a second helper column that detects the **unit**: `=IF(RIGHT(TRIM(D2), 2) = "kg", "kg", "g")`.

6. Combine both into a single **standardized-to-kilograms** column: if the unit is already `kg`, keep the number as-is; if it's `g`, divide by 1000.

   ```
   =IF(<unit helper> = "kg", <number helper>, <number helper> / 1000)
   ```

7. Format the final column to two decimal places and confirm every value is now a real number in kilograms, not a mixed-unit text string.

## Expected result

- `Category` column: exactly 3 distinct values, correctly assigned (`Gear` for SKU-201/204/206/209/212, `Apparel` for SKU-202/205/208/211, `Footwear` for SKU-203/207/210/213).
- Standardized weights (kg): SKU-201 → `2.30`, SKU-203 → `0.90`, SKU-206 → `0.60`, SKU-210 → `0.30`, SKU-213 → `0.70`.
- `=ISNUMBER(F2)` (or wherever your final standardized column lands) returns `TRUE` for every row — the whole point of Part B is turning mixed-unit **text** into uniform **numbers** you can actually `SUM` or `AVERAGE`.

## Done when…

- [ ] `Category` has exactly 3 distinct spellings, verified by a fresh frequency-count audit.
- [ ] Every `Weight` value has been converted to a single unit (kilograms) and stored as a real number, not text.
- [ ] You can `=SUM()` the standardized weight column and get a sensible total (mixing kg and g text values in a raw `SUM` would either error or silently ignore the text cells — confirm you understand why that's dangerous).
- [ ] Helper columns are converted to values (or clearly kept as an auditable intermediate step) rather than left as fragile formulas referencing cells you might later delete.

## Stretch

- Add a `Category` validation drop-down (Lecture 3) to the now-clean column so no future row can reintroduce a casing variant.
- The raw data conveniently only mixed `kg` and `g`. Real-world weight columns often also mix `lb`/`lbs`/`oz`. Extend your unit-detection helper to handle `lb` (1 lb = 0.453592 kg) as a third case, and note what changes about your `IF` logic once there are three branches instead of two (hint: this is exactly the nested-`IF`-vs-`IFS` decision from Week 3).

## Submission

Commit your cleaned `Ex2-Standardize` sheet to your portfolio under `c41-week-05/exercise-02/`.
