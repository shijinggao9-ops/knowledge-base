# Week 2 — Resources

Free, official, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Tools (you already have these from Week 1)

- **Excel** (365, 2021, or Excel for the web) — <https://www.microsoft.com/microsoft-365/excel>
- **Google Sheets** — <https://sheets.google.com> (free with any Google account)

Nothing new to install this week — you're using the same workbook tool, just writing formulas in it.

## Required reading (this week's core)

- **Microsoft — Overview of formulas in Excel:** <https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173>
  *Why: the canonical starting point — how a formula is structured and evaluated.*
- **Microsoft — Calculation operators and precedence in Excel:** <https://support.microsoft.com/en-us/office/calculation-operators-and-precedence-in-excel-48be406d-4975-4d31-b2b8-7af9e0e2878a>
  *Why: the exact, official order-of-operations table — the source of truth behind Lecture 1.*
- **Microsoft — Switch between relative, absolute, and mixed references:** <https://support.microsoft.com/en-us/office/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9>
  *Why: the definitive walkthrough of the `$` sign and the `F4` cycle from Lecture 2.*
- **Microsoft — Define and use names in formulas:** <https://support.microsoft.com/en-us/office/define-and-use-names-in-formulas-4d0f13ac-53b7-422e-afd2-abd7ff379c64>
  *Why: every named-range creation method, naming rule, and scope option covered in Lecture 3.*
- **Google — Named ranges in Google Sheets:** <https://support.google.com/docs/answer/63175>
  *Why: the Sheets-side equivalent, including how Sheets' Named Ranges panel differs from Excel's Name Manager.*

## Reference (keep in tabs)

- **Microsoft — SUM function:** <https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89>
- **Microsoft — AVERAGE function:** <https://support.microsoft.com/en-us/office/average-function-047bac88-d466-426c-a32b-8f33eb960cf6>
- **Microsoft — COUNT / COUNTA functions:** <https://support.microsoft.com/en-us/office/count-function-a59cd7fc-b623-4d93-87a4-d23bf411294c>
- **Microsoft — ROUND function:** <https://support.microsoft.com/en-us/office/round-function-c018c5d8-40fb-4053-90b1-b3e7f61a213c>
- **Microsoft — Create or delete a cell reference (cross-sheet references):** <https://support.microsoft.com/en-us/office/create-or-delete-a-cell-reference-c7b1e3ca-9779-4638-98c7-9ea9d2b18cbc>
- **Microsoft — Detect errors in formulas (the full error-value glossary):** <https://support.microsoft.com/en-us/office/detect-errors-in-formulas-3a8acca5-1d61-4702-80e0-99a36a2822c1>
  *Why: every Excel error value, not just the four covered this week — bookmark this for the rest of the course.*
- **Google — Function list (all built-in Sheets functions):** <https://support.google.com/docs/table/25273>
- **Google — IMPORTRANGE function (pull data from another Sheets file):** <https://support.google.com/docs/answer/3093340>

## Practice beyond this week's exercises

- **Excel Exercises** — free practice problems with instant feedback: <https://excel-exercises.com/>
  *Why: more formula-writing reps in a browser sandbox, no install needed.*
- **GCFGlobal — Excel Formulas tutorial:** <https://edu.gcfglobal.org/en/excel-formulas/>
  *Why: a slower, screenshot-heavy second pass if any Lecture 2 or 3 concept didn't fully click.*
- **GCFGlobal — Excel: Relative and Absolute Cell References:** <https://edu.gcfglobal.org/en/excel/cell-basics/1/>
  *Why: a different explanation of the same `$` mechanic, useful if you want a second angle.*

## Glossary

| Term | Definition |
|------|------------|
| **Formula** | An instruction starting with `=` that computes a value from constants, cell references, and functions. |
| **Operator** | A symbol performing an operation: `+ − * / ^` (arithmetic), `&` (text join). |
| **Order of operations** | The fixed sequence in which operators are evaluated: parentheses, exponents, `*`/`/` left-to-right, `+`/`-` left-to-right. |
| **Function** | A named, pre-built formula taking arguments in parentheses, e.g. `SUM(range)`. |
| **Argument** | A single input to a function, separated from others by commas. |
| **Relative reference** | A plain reference (`A1`) that shifts by the same offset the formula is copied or filled. |
| **Absolute reference** | A fully `$`-locked reference (`$A$1`) that never shifts regardless of where the formula is copied. |
| **Mixed reference** | A partially locked reference (`$A1` or `A$1`) — one half locked, one half floats. |
| **Fill handle** | The small square at the active cell's bottom-right corner, dragged to replicate a formula across a range. |
| **Named range** | A plain-English name assigned to a cell or range, usable in formulas in place of its address; behaves like an absolute reference by default. |
| **Sheet-qualified reference** | A reference to a cell on another sheet, written `SheetName!Cell` (or `'Sheet Name'!Cell` if the name has a space). |
| **`#REF!`** | Error: a formula's reference points at a cell, row, or column that no longer exists. |
| **`#DIV/0!`** | Error: division by zero (or by a blank cell treated as zero). |
| **`#VALUE!`** | Error: a formula received the wrong data type (e.g., text where a number was expected). |
| **`#NAME?`** | Error: the formula contains an unrecognized function name or an undefined/misspelled named range. |
| **`#N/A`** | Not this week's core focus, but related: a lookup searched and found no match — usually a *correct*, working result, not a bug. |

---

*Broken link? Open an issue or PR.*
