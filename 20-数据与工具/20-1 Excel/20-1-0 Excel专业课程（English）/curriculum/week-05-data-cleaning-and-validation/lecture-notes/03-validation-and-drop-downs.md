# Lecture 3 — Data Validation & Drop-Downs

> **Duration:** ~2 hours. **Outcome:** You can restrict what a cell will accept using Data Validation (number ranges, date ranges, list-only, custom formula rules), build a drop-down list from a named range, build a **dependent** drop-down whose options change based on another cell, and flag validation violations visually with conditional formatting.

Lecture 1 found the mess. Lecture 2 cleaned it up. This lecture stops the mess from happening again — by restricting what a human (or a paste from another system) is allowed to type into a cell in the first place. This is the single highest-leverage thing you can do to keep a dataset clean over time: **prevention beats cleanup**, every time, because cleanup is a recurring cost and prevention is a one-time setup.

## 1. Build the `Lookups` sheet

Open the `Lookups` sheet. This holds every clean reference list this week's validation rules will point to — keeping lookup lists on their own sheet (never buried inside a validation dialog as typed text) is the correct habit, because it means one edit to the list updates every drop-down that uses it.

```
      A            B              C
1   States       Tiers          Category
2   California   Bronze         Apparel
3   New York     Silver         Footwear
4   Texas        Gold           Gear
5   Washington   Platinum
6   Florida
```

Below that, build the **category → subcategory** mapping the dependent drop-down (Section 4) will use. Lay it out with the category as a repeated key next to each of its subcategories — this "long" shape is what most dependent-drop-down techniques expect:

```
       E            F
8    Category     Subcategory
9    Apparel      Jackets
10   Apparel      Shirts
11   Apparel      Base Layers
12   Footwear     Hiking Boots
13   Footwear     Sandals
14   Footwear     Trail Runners
15   Gear         Tents
16   Gear         Backpacks
17   Gear         Sleeping Bags
```

## 2. Basic Data Validation — restricting a single cell

Select a cell (or column) and open the validation dialog: **Excel** — Data tab → **Data Validation**; **Google Sheets** — Data menu → **Data validation**. Both offer several rule types; the four you'll use constantly:

**List from a range** — restricts entry to values from a range you point at:

- Excel: Allow → **List**, Source → `=Lookups!$A$2:$A$6`.
- Sheets: Criteria → **Dropdown (from a range)** → select `Lookups!A2:A6`.

Apply this to the `State` column in `OrderEntry` (built in Section 5). Now that cell shows a drop-down arrow and **only** accepts one of the six clean state names — typing `"Californa"` (a typo) or `"CA"` (the old abbreviation) is rejected outright.

**Whole number / Decimal, restricted to a range** — for `Order Amt`, restrict to a sane positive range:

- Excel: Allow → **Decimal**, Data → **between**, Minimum `0`, Maximum `5000`.
- Sheets: Criteria → **Number** → **is between** → `0` and `5000`.

**Date, restricted to a range** — for `Signup Date`, prevent obviously wrong entries like a typo'd future year:

- Excel: Allow → **Date**, Data → **between**, Start `1/1/2020`, End `=TODAY()`.
- Sheets: Criteria → **Date** → **is valid date** and, separately, **is before** `=TODAY()+1` if you want to also block future dates.

**Text length** — for a `CustID` field where IDs are always 4 digits: Allow → **Text length** → **equal to** → `4`.

In every case, open the **Input Message** tab/option and add a short helper (e.g., "Pick a state from the list — type-ahead works once you click the cell") and the **Error Alert** tab and choose **Stop** (rejects invalid entry outright) vs. **Warning** (lets the user override with a confirmation). Default to **Stop** for anything a formula downstream depends on being correct; use **Warning** only when a rare legitimate exception might need to get through.

## 3. Custom formula rules — validation that isn't a fixed list or range

The most powerful validation option in both apps lets you supply **any formula that returns TRUE/FALSE**, which is your escape hatch for any rule the built-in types can't express.

**Example — email must contain "@" and end in a recognizable pattern:**

```
=AND(ISNUMBER(SEARCH("@", A2)), ISNUMBER(SEARCH(".", A2, SEARCH("@", A2))))
```

This checks that an `@` exists, and that a `.` exists **somewhere after** the `@` (the nested `SEARCH` uses the first search's position as the second search's starting point) — catching `"not-an-email"` and `"missing-dot@nowhere"` while allowing `"real@address.com"`.

- Excel: Allow → **Custom**, Formula → the expression above, referencing the **first cell** of the range you're applying it to (Excel copies the relative reference down automatically as it does for any formula).
- Sheets: Criteria → **Custom formula is** → same expression.

**Example — no duplicate Order ID allowed in the column:**

```
=COUNTIF($A$2:$A$500, A2) = 1
```

Applied to every cell in the `Order ID` column, this rejects a newly typed ID the instant it matches one already in the column — turning Lecture 1's duplicate-*detection* into duplicate-*prevention*, live, at entry time.

Custom-formula validation is where Data Validation stops being "pick from a list" and becomes "encode any business rule you can express as a formula" — the ceiling here is exactly as high as your formula-writing skill from Weeks 2–4.

## 4. Dependent (cascading) drop-downs

A dependent drop-down is two linked cells: pick a value in the first (`Category`), and the second (`Subcategory`) only offers the options that make sense for that choice. This is what turns "Apparel" + "Hiking Boots" (nonsensical — boots aren't apparel) into an impossible combination instead of a data-entry mistake waiting to happen.

**The core technique — `FILTER` (modern, both apps) driving the list source:**

In `OrderEntry`, set `Category` (say cell `B2`) to a normal List validation pointing at `Lookups!$G$2:$G$4` (a small helper cell listing the three unique categories `Apparel`, `Footwear`, `Gear` — build it with `=UNIQUE(Lookups!E9:E17)`, previewed in Lecture 1).

For `Subcategory` (cell `C2`), instead of a static range, point the List validation's source at a **dynamic array formula** that filters `Lookups!F9:F17` down to only the rows whose `Lookups!E` matches whatever's currently in `B2`:

```
=FILTER(Lookups!$F$9:$F$17, Lookups!$E$9:$E$17 = B2)
```

- **Excel:** paste this formula into a helper cell (say `Lookups!H2`) so it spills the filtered list there, then set `C2`'s List validation Source to that spilling range, e.g. `=Lookups!$H$2#` (the trailing `#` — the "spill reference" operator — always means "however many cells this formula currently spills into," so the drop-down auto-adjusts if the filtered list grows or shrinks).
- **Google Sheets:** Sheets' Data Validation "Dropdown (from a range)" can point directly at a range containing a `FILTER` formula's spill; some setups are more reliable using a named range aimed at the spill output — test yours by changing `B2` and confirming `C2`'s drop-down list updates.

```mermaid
flowchart LR
  A["Pick Category in B2"] --> B["FILTER Lookups!F9:F17 where E = B2"]
  B --> C["Spills matching subcategories"]
  C --> D["Subcategory C2 dropdown updates"]
```
*Changing the parent cell re-filters the source range, which reshapes what the dependent drop-down offers.*

Change `B2` from `Apparel` to `Footwear` and re-open `C2`'s drop-down — the options should switch from `Jackets/Shirts/Base Layers` to `Hiking Boots/Sandals/Trail Runners` immediately. If `C2` already held `Jackets` when you changed `B2`, the cell's *value* doesn't auto-clear (validation controls what you *can type next*, not what's already there) — that's a real gotcha worth building a habit around: after changing a parent drop-down, always re-check the dependent cell's current value.

**Older-Excel fallback (no `FILTER`/dynamic arrays):** use `INDIRECT` with named ranges. Name each category's subcategory list identically to the category text itself (a named range literally called `Apparel`, another called `Footwear`, another called `Gear`), then set the dependent validation's source to `=INDIRECT(B2)`. This is more setup work (one named range per category, maintained by hand) but works in every Excel version back to the 2000s and in Sheets.

## 5. Build the `OrderEntry` guarded form

Lay out a small entry area combining everything above:

```
     A          B            C              D           E            F
1  Order ID   Customer     State          Category    Subcategory  Order Amt
2  (blank — apply custom-formula uniqueness validation)
```

Apply: List validation on `State` (from `Lookups!A2:A6`), List validation on `Category` (from the unique-category helper), the `FILTER`-driven dependent List on `Subcategory`, Decimal-between validation on `Order Amt` (`0` to `5000`), and the uniqueness custom formula on `Order ID`. Type a few valid rows to confirm every drop-down works and every rejection actually rejects.

## 6. Conditional formatting — flagging what slips through anyway

Validation guards **new** typing, but it does nothing retroactively to data that's pasted in bulk (most apps let a bulk paste bypass validation, or at best mark the cells for review rather than blocking the paste) or that existed before you added the rule. Conditional formatting is the visual safety net that catches this — highlighting bad values wherever they are, old or new.

**Flag out-of-range amounts** — select the `Order Amt` column, add a conditional format rule with a custom formula:

```
=OR(F2<0, F2>5000)
```

Fill color: red. Any amount outside the sane range lights up instantly, whether it arrived via validated typing (which shouldn't be possible) or a bulk paste (which might have skipped validation).

**Flag duplicate Order IDs** — same idea as the validation formula, but as a *visible* flag rather than a blocker, useful for auditing existing data:

```
=COUNTIF($A$2:$A$500, A2) > 1
```

**Flag blank required fields** — highlight any row missing a `Customer` or `State`:

```
=OR($B2="", $C2="")
```

Apply this rule to the **whole row range** (`$A2:$F2`), not just column B/C, with the formula anchored on column with `$` locking the column but not the row (`$B2`, `$C2`) so the *whole row* highlights when either named field is blank — a small but important formula-anchoring detail: without the `$` before `B` and `C`, the rule would misapply as you moved across columns.

Run all three rules on `CleanSignups` from Lecture 2 as a final check — a properly cleaned sheet should show **zero** highlighted cells. If anything lights up, your cleaning pass from Lecture 2 missed something; go back and find it. This is the week's actual finish line: a dataset where the automated flags all come back clean.

## 7. Check yourself

- What's the practical difference between a Stop error alert and a Warning error alert, and when would you choose each?
- Write a custom-formula validation rule (in words, then as a formula) that rejects any `Quantity` entry that isn't a whole number greater than zero.
- Why does changing a parent drop-down's value **not** automatically clear an already-selected dependent value, and why does that matter?
- What does the Excel spill reference operator `#` mean, and why is it useful as a Data Validation List source?
- Name one thing conditional formatting can catch that Data Validation cannot, and explain why.
- In the "flag blank required fields" rule, why does the `$` need to sit before the column letter but not the row number?

If those came quickly, you're ready for this week's exercises — dedupe a real list, standardize real categories, and build a real dependent drop-down from scratch.

## Further reading

- **Microsoft — Apply data validation to cells:** <https://support.microsoft.com/en-us/office/apply-data-validation-to-cells-29fecbcc-d1b9-42c1-9d76-eff3ce5f7249>
- **Microsoft — Create a drop-down list:** <https://support.microsoft.com/en-us/office/create-a-drop-down-list-7693307a-59ef-400a-b769-c5402dce407d>
- **Microsoft — Create a dependent drop-down list:** <https://support.microsoft.com/en-us/office/create-a-dependent-drop-down-list-c5c9edfb-38d0-4d51-88d2-a3f4c8b1b1f7>
- **Google — Add data validation to cells:** <https://support.google.com/docs/answer/186103>
- **Microsoft — FILTER function:** <https://support.microsoft.com/en-us/office/filter-function-f4f7cb66-82eb-4767-8f7c-4877ad80c759>
- **Microsoft — Use conditional formatting rules with a custom formula:** <https://support.microsoft.com/en-us/office/use-a-formula-to-apply-conditional-formatting-fed60dfa-1d3f-4e13-9ecb-f1951ff89d7f>
