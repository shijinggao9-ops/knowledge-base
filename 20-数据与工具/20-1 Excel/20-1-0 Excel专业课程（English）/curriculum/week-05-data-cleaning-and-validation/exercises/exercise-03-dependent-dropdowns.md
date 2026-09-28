# Exercise 3 — Build Dependent Drop-Downs

**Goal:** Build a working two-level dependent drop-down from a blank sheet — Category first, Subcategory second, filtered by whatever Category was chosen — plus the surrounding validation and flags that make it a genuinely guarded entry point.

**Estimated time:** 60–90 minutes.

## Setup

Add a new sheet named `Ex3-Dropdowns`. You're building a **repair-ticket intake form** for Crunch Outfitters' gear-repair counter — a customer drops off a broken item, staff logs what kind of item and what's wrong with it.

Build the reference lists first, in columns `H` onward (kept off to the side so the form itself, in `A:E`, stays clean):

```
      H            I                     J           K
1   ItemType     Issue                 Priority
2   Backpack     Broken Zipper         Low
3   Backpack     Torn Strap            Medium
4   Backpack     Frame Bent            High
5   Tent         Pole Snapped          High
6   Tent         Seam Leaking          Medium
7   Tent         Zipper Stuck          Low
8   Boots        Sole Separating       High
9   Boots        Lace Eyelet Torn      Low
10  Boots        Waterproofing Failed  Medium
11  Jacket       Zipper Stuck          Low
12  Jacket       Seam Ripped           Medium
13  Jacket       Insulation Leaking    High
```

Column `K` (`Priority`) is a fixed three-value list: `Low`, `Medium`, `High` — not dependent on anything, you'll validate it directly.

## Tasks

1. **Build the unique Item Type list.** In `H16` (or wherever convenient), write `=UNIQUE(H2:H13)` to spill the four distinct item types (`Backpack`, `Tent`, `Boots`, `Jacket`). If your app lacks `UNIQUE`, type the four values manually into a small fixed list instead.

2. **Lay out the intake form** in `A1:E1`: `Ticket ID`, `Item Type`, `Issue`, `Priority`, `Notes`.

3. **Validate `Item Type` (column B)** as a List sourced from your Task 1 unique list.

4. **Build the dependent `Issue` list (column C).** Following Lecture 3, Section 4: write a `FILTER` formula in a helper cell that returns every `Issue` from the reference table where `ItemType` matches the current row's `B` value, then point column C's List validation at that filtered spill (or its named-range/`INDIRECT` equivalent if your app version needs the fallback).

   ```
   =FILTER(I2:I13, H2:H13 = B2)
   ```

5. **Validate `Priority` (column D)** as a simple, non-dependent List sourced from a fixed `Low, Medium, High` list.

6. **Validate `Ticket ID` (column A)** with a custom-formula rule enforcing uniqueness: `=COUNTIF($A$2:$A$200, A2) = 1`.

7. **Test the cascade.** Enter 5 test tickets, picking a different `Item Type` each time and confirming the `Issue` drop-down only ever offers options that belong to that item type. Deliberately try to break it: pick `Boots`, then change `Item Type` to `Tent` **without** touching `Issue` — what happens to the now-stale `Issue` value already sitting in the cell? Write one sentence describing what you observed (this connects directly to Lecture 3 Section 4's warning about dependent values not auto-clearing).

8. **Add a flag.** Conditional-format the whole row red if `Issue` no longer belongs to the current `Item Type` — i.e., catch exactly the staleness you just triggered in Task 7. Formula (anchored so it evaluates per-row when applied to the full range `$A2:$E200`):

   ```
   =AND($C2<>"", COUNTIFS($H$2:$H$13, $B2, $I$2:$I$13, $C2) = 0)
   ```

   This reads: "if `Issue` is non-blank, but no row in the reference table has this exact `Item Type` + `Issue` combination, something's stale — flag it."

## Expected result

- Picking `Backpack` in `Item Type` limits `Issue` to exactly `Broken Zipper`, `Torn Strap`, `Frame Bent` — never any tent/boot/jacket issue.
- Re-triggering the Task 7 staleness scenario (change `Item Type` after `Issue` is already set) should turn that row red once your Task 8 rule is active — proving the flag genuinely catches what the drop-down alone couldn't prevent.
- Typing a duplicate `Ticket ID` is rejected outright by the Task 6 validation rule.

## Done when…

- [ ] `Item Type` drop-down works and offers all 4 values.
- [ ] `Issue` drop-down correctly filters to only the current `Item Type`'s issues, for all 4 item types.
- [ ] Task 7's written observation about stale dependent values is present.
- [ ] Task 8's conditional-formatting flag correctly highlights a row you deliberately made stale, and does **not** highlight rows where `Item Type`/`Issue` are consistent.
- [ ] `Ticket ID` uniqueness validation rejects a duplicate you test on purpose.

## Stretch

- Add a **third** dependent level: a `Repair Cost Estimate` column that `XLOOKUP`s a price from a small `ItemType + Issue → Cost` reference table (Week 3 skill, reused here) once both `Item Type` and `Issue` are set.
- Research (or test) whether your app's dependent-drop-down behavior changes if the parent list has **duplicate** entries in the reference table versus not — does `FILTER` handle a reference table with an accidental duplicate `Backpack, Broken Zipper` row gracefully, or does it just return the duplicate twice in the drop-down?

## Submission

Commit your working `Ex3-Dropdowns` sheet (with all 5 test tickets, including the one deliberately made stale for Task 7/8) to your portfolio under `c41-week-05/exercise-03/`.
