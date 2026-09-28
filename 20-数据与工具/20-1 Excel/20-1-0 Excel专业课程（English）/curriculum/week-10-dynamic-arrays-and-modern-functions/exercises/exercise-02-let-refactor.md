# Exercise 2 — Refactor a Formula With LET

**Goal:** Take a formula that's correct but genuinely hard to read — because it computes the same thing multiple times — and rebuild it with `LET` so every value is named once and reused. This is the single most common real-world use of `LET`: not writing new capability, but making an existing formula maintainable.

**Estimated time:** 1 hour.

## Setup

Work on the `Report` tab. You already have the `Orders` data loaded.

## The starter formula

Type this **exactly as shown** into a cell (it will be long — that's the point):

```excel
=IF(AVERAGE(FILTER(Orders!I2:I31, (Orders!D2:D31="North")*(Orders!J2:J31="Shipped"))) > AVERAGE(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")), "Above company average", "At or below company average") & " (" & TEXT(AVERAGE(FILTER(Orders!I2:I31, (Orders!D2:D31="North")*(Orders!J2:J31="Shipped"))), "$0.00") & " vs " & TEXT(AVERAGE(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")), "$0.00") & ")"
```

Run it. It should produce:

```
At or below company average ($66.63 vs $96.74)
```

## Tasks

1. **Count the repetition.** Before touching `LET`, read the formula carefully and count: how many times does `AVERAGE(FILTER(Orders!I2:I31, (Orders!D2:D31="North")*(Orders!J2:J31="Shipped")))` (the North-shipped average) appear? How many times does `AVERAGE(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped"))` (the company-wide shipped average) appear? Write both counts down.

2. **Refactor with `LET`.** Rewrite the formula so each of those two averages is computed **exactly once**, named, and reused. Your final calculation should read cleanly — something close to:

   ```excel
   =LET(
       region_avg, <your regional average expression>,
       company_avg, <your company-wide average expression>,
       label, IF(region_avg > company_avg, "Above company average", "At or below company average"),
       label & " (" & TEXT(region_avg, "$0.00") & " vs " & TEXT(company_avg, "$0.00") & ")"
   )
   ```

   Fill in the two named values yourself — don't just copy this skeleton's blanks from the starter formula verbatim; write them so you understand exactly what each computes.

3. **Verify it matches.** Confirm your `LET` version produces the **identical** output string as the starter formula: `At or below company average ($66.63 vs $96.74)`.

4. **Generalize it — make the region a parameter.** The starter formula hard-codes `"North"`. Refactor again so the region is read from a **cell** (put `"North"` in, say, `Report!B1`, and reference `$B$1` inside your `LET` instead of the literal string). Change `B1` to `"South"` and confirm the whole sentence updates correctly. *(Expected for South: 4 Shipped orders totaling $903.00, so the average is $225.75 — well above the $96.74 company average, flipping the label to "Above company average." Work out the by-hand numbers yourself from the `Orders` data and confirm your formula matches.)*

## Done when…

- [ ] You've written down the repetition counts from Task 1.
- [ ] Your `LET` version produces the exact same string as the starter formula.
- [ ] Changing the region cell (Task 4) changes the output correctly, with no other edits to the formula.
- [ ] You can explain in one sentence why the `LET` version is **not just prettier** — what it actually does differently at calculation time.

## Stretch

- Add a third named value, `pct_diff`, computing how far the regional average is from the company average as a percentage (`(region_avg - company_avg) / company_avg`), and fold it into the output sentence.
- Rebuild the whole thing to loop over **all four regions at once** using `MAP` and `LAMBDA` (a preview of Lecture 3/Exercise 3) — one spilled sentence per region, four total, no copy-pasting the formula down.

## Submission

Commit both formula versions (starter and refactored) plus your written repetition-count answer to your portfolio under `c41-week-10/exercise-02/`.
