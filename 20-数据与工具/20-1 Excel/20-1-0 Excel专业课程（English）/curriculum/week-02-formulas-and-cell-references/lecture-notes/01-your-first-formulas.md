# Lecture 1 — Your First Formulas & Operators

> **Duration:** ~2 hours. **Outcome:** You can write any arithmetic formula, predict its result correctly before you press Enter, and use the five core aggregate functions — `SUM`, `AVERAGE`, `COUNT`, `MIN`, `MAX` — knowing exactly which cells each one includes.

## 1. Every formula starts with `=`

Type anything into a cell that starts with `=` (or `+` — Excel accepts it as a legacy shortcut but silently rewrites it to `=`), and Excel or Sheets stops treating your input as data and starts treating it as an **instruction to compute**. Everything after the `=` is the formula.

```
A1: 10
A2: 20
A3: =A1+A2        → displays 30
```

The cell **displays** the result (`30`), but the cell still **contains** the formula. Click `A3` and look at the **formula bar** (the long input strip above the grid, below the ribbon/toolbar) — it shows `=A1+A2`, not `30`. This is the same value-vs-display idea from Week 1, one level up: a formula cell stores a *formula*, and displays a *computed value*. Every time a cell the formula depends on changes, the formula silently recalculates. That automatic recalculation is the entire point of a spreadsheet.

**Toggle to see every formula at once:** Excel `Ctrl+`` `` (backtick, under Esc) or Sheets `Ctrl+`` `` too — both flip the whole sheet to show formulas instead of results. Toggle it back the same way. Use this constantly while learning; it turns an opaque sheet into a fully readable one.

## 2. The five arithmetic operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `=4+3` | `7` |
| `-` | Subtraction (and unary negative) | `=10-3` | `7` |
| `*` | Multiplication | `=4*3` | `12` |
| `/` | Division | `=12/4` | `3` |
| `^` | Exponentiation | `=2^3` | `8` |

There is no `×` or `÷` key on a spreadsheet — always `*` and `/`. This trips up almost everyone in their first week; make the substitution automatic now.

One more operator worth knowing immediately because you'll use it in Week 4: `&` (or the `CONCATENATE`/`CONCAT` function) joins text. `="Hello, " & "Crunch"` produces `Hello, Crunch`. It's not arithmetic, but it follows the same "starts with `=`, combines cell values" pattern.

## 3. Order of operations — PEMDAS, same as math class

Excel and Google Sheets both evaluate a formula using the **same precedence rules you learned in school**:

1. **Parentheses** `( )` — evaluated first, innermost first.
2. **Exponentiation** `^`
3. **Multiplication and division** `*` `/` — equal precedence, evaluated **left to right**.
4. **Addition and subtraction** `+` `-` — equal precedence, evaluated **left to right**.

```mermaid
flowchart TD
  A["Formula to evaluate"] --> B["1. Parentheses first<br/>innermost to outermost"]
  B --> C["2. Exponentiation ^"]
  C --> D["3. Multiplication and division<br/>left to right"]
  D --> E["4. Addition and subtraction<br/>left to right"]
  E --> F["Final result"]
```
*The order Excel and Sheets always evaluate a formula in, top to bottom.*

```
=2+3*4        → 3*4 first (=12), then 2+12  → 14   (NOT 20)
=(2+3)*4      → parentheses first (=5), then 5*4   → 20
=10-2^2       → exponent first (=4), then 10-4     → 6    (NOT 64)
=20/4/2       → left to right: 20/4=5, then 5/2     → 2.5  (NOT 10)
=100*(1+0.08) → parentheses first (=1.08), then *100 → 108
```

That last pattern — `base * (1 + rate)` — is the single most useful arithmetic idiom in this entire course. You'll use it for tax, tips, markups, growth rates, and interest from Week 2 through Week 9. Memorize the shape: **multiply the base by one plus the percentage**, not the base times the percentage alone (that only gives you the *added amount*, not the *new total*).

**A formula with no parentheses where you meant one is the single most common "wrong number" bug in spreadsheets.** If you want "the sum of A1 and A2, times B1," you must write `=(A1+A2)*B1` — write `=A1+A2*B1` and you silently get `A1 + (A2*B1)` instead, because `*` binds tighter than `+`. When in doubt, **add the parentheses even if they're not strictly required** — a formula that's unambiguous to *read* is worth more than one that's two characters shorter.

## 4. The five core aggregate functions

A **function** is a named, pre-built formula that takes **arguments** in parentheses and returns one value. Functions are what make spreadsheets powerful — instead of writing `=A1+A2+A3+A4+A5+...+A50`, you write `=SUM(A1:A50)`.

Set up this small sales table to follow along (type it into your `Formulas` sheet):

```
      A          B
1   Name       Sales
2   Alicia     4200
3   Ben        3100
4   Carmen     (blank)
5   Deshawn    5000
6   Elle       "N/A"
```

Leave `B4` genuinely empty, and type the literal text `N/A` (not a formula, not a blank) into `B6`.

### `SUM` — total

```
=SUM(B2:B6)     → 12300
```

Adds every **numeric** cell in the range. Blank cells (`B4`) and text cells (`B6`) are silently skipped — they contribute `0`, not an error. This "skip non-numbers quietly" behavior is consistent across all five functions below and is worth internalizing now: aggregate functions are forgiving of blanks and text by design.

### `AVERAGE` — mean

```
=AVERAGE(B2:B6)   → 4100
```

This is **not** `SUM/5`. `AVERAGE` divides by the **count of numeric cells only** — here that's 3 (Alicia `4200`, Ben `3100`, Deshawn `5000`; Carmen's blank and Elle's `"N/A"` text are both excluded). So `12300 / 3 = 4100`, not `12300 / 5`. The rule: **`AVERAGE` divides by how many cells actually held a number, not by the size of the range.** This is the single most common source of "why is my average wrong" — a blank or text cell in the range silently shrinks the denominator, which is usually what you want (you don't want a missing sale counted as a zero-dollar sale) but you must know it's happening.

### `COUNT` vs `COUNTA` — how many, of what

```
=COUNT(B2:B6)    → 3   (counts only numeric cells: 4200, 3100, 5000)
=COUNTA(B2:B6)   → 4   (counts non-empty cells of any type: the three numbers + "N/A" text)
```

`COUNT` counts **numbers only**. `COUNTA` counts **anything that isn't blank** — numbers, text, even `TRUE`/`FALSE`. Confusing these two is extremely common: if you want "how many salespeople reported *any* figure, including a note like N/A," use `COUNTA`; if you want "how many actual numeric sales figures exist," use `COUNT`. A third, `COUNTBLANK(B2:B6)`, counts the empty cells (`1`, for Carmen) — useful for spotting missing data before you trust an average.

### `MIN` and `MAX` — extremes

```
=MIN(B2:B6)   → 3100   (Ben — smallest number in range, text/blank ignored)
=MAX(B2:B6)   → 5000   (Deshawn — largest number in range)
```

Same "ignore text and blanks" behavior as `SUM` and `AVERAGE`.

### `ROUND` — controlling precision on the *stored* value

Recall from Week 1: formatting a cell to show 2 decimals doesn't change what's stored underneath. `ROUND` actually changes the stored value.

```
=ROUND(4100.5, 0)     → 4101   (0 decimal places — nearest whole number)
=ROUND(4100.567, 2)   → 4100.57
=ROUND(4100.567, -2)  → 4100   (nearest hundred)
=ROUND(1234, -3)      → 1000   (negative digits round to tens/hundreds/thousands)
```

The second argument is how many decimal places to keep — `0` for whole numbers, positive numbers for decimals, **negative** numbers to round to the nearest 10, 100, 1000, etc. You'll reach for `ROUND` constantly once real money math starts (Week 2's mini-project has a locked tax rate that needs exactly this).

## 5. Every function argument, spelled out

A function call has the shape `FUNCTION(argument1, argument2, ...)`. Arguments can be:

- A **literal value**: `=SUM(10, 20, 30)` → `60`
- A **single cell**: `=SUM(B2, B3)` → adds just those two cells
- A **range**: `=SUM(B2:B6)` → adds the whole block
- A **mix of ranges and cells**, comma-separated: `=SUM(B2:B4, B6, 500)` → adds the range, one more cell, and a literal number, all in one call
- **Another formula's result** (nesting): `=ROUND(AVERAGE(B2:B6), 1)` — the innermost function (`AVERAGE`) runs first, its result feeds `ROUND`. Nesting functions inside functions is normal and you'll do it constantly from Week 3 onward.

## 6. AutoSum — the fast path, and why to still know the manual formula

Both Excel and Sheets have an **AutoSum** button (Σ symbol, Home tab in Excel / toolbar in Sheets, or `Alt+=` in Excel) that guesses a range above or beside the active cell and inserts `=SUM(...)` for you. It's a fine shortcut once you already understand what it's doing — but if you only ever click the button, you'll be lost the moment you need `AVERAGE`, a partial range, or a formula AutoSum guesses wrong. Learn to type the formula by hand first; use AutoSum to go faster once it's automatic.

## 7. Check yourself

- Without a calculator: what does `=3+4*2^2` evaluate to? Walk through the precedence order out loud.
- Why does `=A1+A2*B1` give a different answer than `=(A1+A2)*B1`?
- A range has 10 cells: 7 contain numbers, 2 are blank, 1 contains the text `"pending"`. What do `SUM`, `AVERAGE`, `COUNT`, and `COUNTA` each return, in terms of that setup (you don't need exact numbers — describe which cells each one uses)?
- What's the difference between what a formula cell *stores* and what it *displays*, and how do you toggle a whole sheet to show formulas instead of results?
- Why is `base * (1 + rate)` usually the formula you want, rather than `base * rate`, when computing a total that includes a percentage increase?

If those came quickly, move to Lecture 2 — references, and the single `$` character that controls what happens when you copy a formula.

## Further reading

- **Microsoft — Overview of formulas in Excel:** <https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173>
- **Microsoft — Calculation operators and precedence:** <https://support.microsoft.com/en-us/office/calculation-operators-and-precedence-in-excel-48be406d-4975-4d31-b2b8-7af9e0e2878a>
- **Microsoft — SUM function:** <https://support.microsoft.com/en-us/office/sum-function-043e1c7d-7726-4e80-8f32-07b23e057f89>
- **Google — SUM/AVERAGE/COUNT function list:** <https://support.google.com/docs/table/25273>
