# Lecture 3 — Named Ranges & Cross-Sheet References

> **Duration:** ~2 hours. **Outcome:** You can name a cell or range and use that name in formulas instead of a raw address, reference cells on other sheets (and, in Excel, other workbooks) correctly, and read `#REF!`, `#DIV/0!`, `#VALUE!`, and `#NAME?` as precise diagnostic clues instead of generic failures.

## 1. Why `$F$1` still isn't good enough

Lecture 2 fixed the *mechanics* of the tax-rate formula: `=D2*$F$1` correctly keeps pointing at the tax rate no matter where you fill it. But six months from now, looking at `=D2*$F$1` cold, you have no idea what `$F$1` *means* without clicking over to check. Multiply that by a workbook with forty formulas referencing a dozen different constant cells, and you have a spreadsheet only its original author can maintain — and even they'll struggle after a few weeks away from it.

**Named ranges** solve this: give a cell or range a plain-English name, and use that name in formulas instead of its address.

```
=D2*$F$1        ← what does F1 hold? you have to go look.
=D2*TaxRate      ← self-documenting. No lookup required.
```

## 2. Creating a named range

**Excel — two ways:**

1. **Name Box method (fastest):** select the cell or range (e.g., click `F1`), then click into the **Name Box** (top-left, above column `A`, where it normally shows the address like `F1`), type the name (`TaxRate`, no spaces), press **Enter**.
2. **Formulas tab → Define Name:** gives you a dialog with a **Scope** dropdown (Workbook vs. a specific sheet) and a **Comment** field — use this when you want the name available on every sheet or want to document it.

**Google Sheets:**

**Data → Named ranges** opens a side panel. Select the range, type a name, click **Done**. Sheets also lets you edit or delete existing named ranges from the same panel, and shows you every named range currently defined in the file — useful for auditing a large workbook.

## 3. Naming rules — what's allowed

- Must start with a **letter or underscore**, not a number or symbol.
- No spaces — use `TaxRate` or `Tax_Rate`, never `Tax Rate`.
- Cannot look like a valid cell reference — `A1` or `B12` are rejected as names, because the engine can't tell them apart from addresses.
- Case is preserved for display but names are **not case-sensitive** when you use them — `TaxRate` and `taxrate` refer to the same name.
- Keep them short but unambiguous: `TaxRate`, `ShippingCost`, `PriceList`, not `TR` (too cryptic) or `TheCurrentApplicableTaxRateForThisQuarter` (too long to type in a formula).

## 4. Using a named range in a formula

Once `F1` is named `TaxRate`, just type the name where you'd have typed the address — autocomplete will even suggest it as you type:

```
=D2*TaxRate
```

Fill this down exactly like `=D2*$F$1` — a named range behaves like an **absolute reference by default**: it always points at the same cell no matter where the formula containing it is copied. You get the self-documenting benefit *and* the locking behavior in one step, which is why named ranges are usually a strict upgrade over `$F$1` for constants you reference often.

A named range can cover a **block**, not just one cell — name `B2:B20` as `Prices` and write `=SUM(Prices)` instead of `=SUM(B2:B20)`. This becomes especially valuable once you reach lookup functions in Week 3 (`VLOOKUP`/`XLOOKUP` against a named `PriceList` reads far better than against a raw range).

**Managing names:** Excel's **Formulas → Name Manager** (`Ctrl+F3`) lists every named range in the workbook, lets you edit the range it points to, rename it, or delete it. Sheets' **Data → Named ranges** panel does the same. Check this whenever a name-based formula gives an unexpected result — the name may have been left pointing at the wrong cell after rows were inserted or deleted above it.

## 5. Referencing another sheet

Every workbook this course builds ends up with multiple sheets — a `Data` sheet, a `Summary` sheet, an `Assumptions` sheet. To reference a cell that lives on a **different** sheet than the formula, prefix the cell address with the sheet's name and an exclamation mark:

```
=Data!B2          → cell B2 on the sheet named "Data"
=Summary!A1:A10    → a range on the sheet named "Summary"
```

If the sheet name contains a **space or starts with a number**, wrap it in single quotes:

```
='Q1 Budget'!B2    → sheet named "Q1 Budget" (has a space, needs quotes)
```

Both Excel and Sheets insert this syntax for you automatically if you **click the target sheet's tab, then click the cell**, while building a formula — you never have to type the sheet-qualified reference by hand. Start a formula with `=`, click over to the other sheet, click the cell, press Enter; the correct `Sheet!Cell` reference appears in your original formula for you.

Cross-sheet references follow the exact same relative/absolute/mixed rules from Lecture 2 — `Data!$B$2` locks the reference on the `Data` sheet just like `$B$2` would locally.

## 6. Referencing another workbook (Excel only, with a caveat)

Excel can reference a cell in a **different file** entirely:

```
='[Budget2026.xlsx]Summary'!$B$2
```

The workbook name is in square brackets, the sheet name follows, then the usual `!` and cell address, all wrapped in quotes because of the special characters. This works while both files are open, but **breaks or requires the other file to be present at a known path** once you close it or move either file — external-workbook references are fragile and best avoided unless you specifically need to pull a single value from another file and understand the risk. Google Sheets has no direct equivalent — the closest is the `IMPORTRANGE` function, which explicitly pulls a range from another Sheets file by URL and requires a one-time permission grant the first time it runs. You won't need either this week; it's here so you recognize the syntax if you meet it in the wild.

## 7. Reading error values — the four you'll meet this week

An error value isn't a crash — it's the spreadsheet telling you *exactly* what kind of problem it hit. Learn to read them as diagnostic messages, not generic failures.

```mermaid
flowchart TD
  A["Cell shows an error"] --> B{"Which symbol?"}
  B -- "#REF!" --> C["Reference points at a deleted cell"]
  B -- "#DIV/0!" --> D["Division by zero or a blank cell"]
  B -- "#VALUE!" --> E["Wrong data type fed into the formula"]
  B -- "#NAME?" --> F["Typo'd function or named range"]
  B -- "#N/A" --> G["Lookup ran and found nothing"]
```
*Reading the error symbol tells you which of five distinct problems to go fix.*

### `#REF!` — a reference points at a cell that no longer exists

```
A1: =B1+C1
```

Now **delete column B** entirely. `A1` becomes `=#REF!+C1` and shows `#REF!`. The formula was pointing at a specific cell, and that cell was deleted out from under it — there's nothing left to point *at*. This also happens if you delete a row or column that a formula referenced, or if you cut-and-paste in a way that removes the source cell of a reference.

**Fix:** you generally can't "repair" a `#REF!` in place — the original reference is gone. Retype the formula pointing at the correct, currently-existing cell.

### `#DIV/0!` — division by zero (or by blank)

```
=10/0        → #DIV/0!
=10/B5       → #DIV/0!  if B5 is 0 or blank
```

Extremely common with computed averages or rates where the denominator can legitimately be zero — e.g., "average sale per customer" when a region has zero customers. Not a bug in your formula logic; it's the math itself being undefined.

**Fix:** wrap in `IFERROR` (you'll formalize this in Week 3) or guard with `IF`: `=IF(B5=0, 0, 10/B5)` — decide what should display when the denominator is zero (often `0` or a blank, sometimes "N/A").

### `#VALUE!` — the formula got the wrong *type* of input

```
A1: "hello"
A2: =A1+5      → #VALUE!
```

You asked for arithmetic on something that isn't a number. Classic causes: a cell that *looks* numeric but is actually text (a number typed after formatting the cell as Text, or pasted from a system that added invisible characters), a date typed in a format the app didn't recognize, or a function argument in the wrong position.

**Fix:** check the offending cell's actual type — select it and glance at alignment (text left-aligns, numbers right-align) or run `=ISTEXT(A1)` to confirm. Common repair: `=VALUE(A1)+5` explicitly converts text-that-looks-numeric into a real number first, or clean the source data.

### `#NAME?` — the formula contains something it doesn't recognize

```
=SUME(A1:A10)      → #NAME?   (typo: should be SUM)
=A1*TaxRat          → #NAME?   (typo'd named range)
=A1&" units"        → fine — this is valid, not an error
```

Almost always a **typo** — a misspelled function name, a named range that doesn't exist (or was deleted), or text that should have been in quotes but wasn't (`=A1+hello` instead of `=A1&"hello"`).

**Fix:** re-check spelling character by character. If it's a named-range typo, open the Name Manager / Named ranges panel to confirm the exact spelling you defined.

### One more you'll see occasionally: `#N/A`

Not from this week's material directly, but worth planting now because it looks similar: `#N/A` means "a lookup searched and found nothing" — you'll meet it properly with `VLOOKUP`/`XLOOKUP` in Week 3. Unlike the four above, `#N/A` usually means the formula is *working correctly* and honestly reporting "not found," not that something is broken.

## 8. A general debugging technique: Trace Precedents / Trace Dependents

When a formula error's cause isn't obvious, both apps offer visual tracing:

- **Excel — Formulas tab → Trace Precedents** draws arrows from the active cell back to every cell it depends on. **Trace Dependents** draws arrows forward to every cell that depends on the active cell — useful before you delete or change something, to see what else would break.
- **Google Sheets** has a lighter version: click a cell, and any cell it references highlights automatically with colored borders while you're editing the formula bar. For deeper tracing, select the cell and check **the formula's referenced ranges highlight in the same colors as they appear in the formula bar** — click into edit mode to see it.

Use tracing whenever a formula three sheets deep is producing a number you don't trust — walk the arrows back to the actual source data instead of guessing.

## 9. Check yourself

- Name cell `B1` as `Rate`. Write a formula in `C1` that multiplies `A1` by `Rate` using the name, not the address.
- Why does a named range behave like an absolute reference by default when you fill or copy a formula that uses it?
- Write a formula in a sheet called `Summary` that adds cell `B2` from a sheet called `Q1 Data` (note the space) to cell `B2` on the current sheet.
- You delete a column, and a formula that used to work now shows `#REF!`. What exactly happened, and can you "undo" it by re-typing the same formula?
- A cell shows `#VALUE!` when you try to add `5` to it. What's the most likely underlying problem, and what's the fastest way to check?
- What's the difference between what `#DIV/0!` and `#N/A` are each telling you?

If those came quickly, you're done with this week's lectures — move to the exercises and start building references with your own hands, then the challenges, then the mini-project.

## Further reading

- **Microsoft — Create a named range from selected cells:** <https://support.microsoft.com/en-us/office/define-and-use-names-in-formulas-4d0f13ac-53b7-422e-afd2-abd7ff379c64>
- **Microsoft — Reference the contents of cells in another worksheet:** <https://support.microsoft.com/en-us/office/create-or-delete-a-cell-reference-c7b1e3ca-9779-4638-98c7-9ea9d2b18cbc>
- **Google — Named ranges in Google Sheets:** <https://support.google.com/docs/answer/63175>
- **Google — IMPORTRANGE function:** <https://support.google.com/docs/answer/3093340>
- **Microsoft — Overview of Excel error messages:** <https://support.microsoft.com/en-us/office/detect-errors-in-formulas-3a8acca5-1d61-4702-80e0-99a36a2822c1>
