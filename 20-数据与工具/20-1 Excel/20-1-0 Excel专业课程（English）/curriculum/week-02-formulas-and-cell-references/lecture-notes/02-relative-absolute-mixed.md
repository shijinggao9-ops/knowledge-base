# Lecture 2 — Relative, Absolute & Mixed References

> **Duration:** ~2 hours. **Outcome:** You can predict exactly what a formula becomes after you copy or fill it anywhere on the sheet, and you can choose `A1`, `$A$1`, `$A1`, or `A$1` correctly on the first try — the skill that separates "I dragged it and it broke" from "I dragged it and it just worked."

## 1. The problem this lecture solves

Build this small table:

```
      A          B              C
1   Item       Price       Qty
2   Pencil     0.50        10
3   Notebook   3.20        4
4   Eraser     0.75        6
```

In `D2`, write a formula for the line total: `=B2*C2` → `5`. Now **fill it down** to `D3` and `D4` — select `D2`, grab the little square at its bottom-right corner (the **fill handle**), and drag down to `D4`. Or select `D2:D4` and press `Ctrl+D` (Excel) / `Ctrl+D` (Sheets, "fill down").

Result: `D3` becomes `=B3*C3` → `12.80`, and `D4` becomes `=B4*C4` → `4.50`. **Every reference shifted down by the same number of rows the formula moved.** This is not a coincidence — it's the default, and it's called a **relative reference**, and it's exactly what you want here: each row's total should multiply *that row's* price and quantity.

Now the problem case. Add a tax rate in a single cell, `F1: 0.08`, and try to compute tax for each row in `E2`: `=D2*F1` → `0.40`. Fill it down. `E3` becomes `=D3*F2` — **not** `=D3*F1`. `F2` is empty, so `E3` shows `0` (or an error once you multiply by more empty cells below). The reference to the tax rate shifted right along with everything else, and now every row after the first is pointing at the wrong — usually empty — cell. This is the single most common formula bug in real spreadsheets, and the fix is one character.

## 2. Relative references — the default, and when they're correct

A reference like `B2`, `C2`, `A1` with **no `$`** is **relative**. When you copy or fill a formula containing a relative reference, the reference shifts by exactly the same offset the formula moved — same direction, same distance, both row and column.

Relative references are what you want whenever **the thing you're pointing at should change in step with the formula itself** — which is most of the time. Line totals, per-row calculations, per-column running sums: all relative.

## 3. Absolute references — the `$` sign locks a cell in place

Prefix a column letter, a row number, or both with `$` to **lock** that part so it does **not** shift when the formula is copied.

```
$B$2   → fully absolute: neither the column nor the row shifts, ever, no matter where you copy this formula
```

Fix the tax formula: in `E2`, write `=D2*$F$1` instead of `=D2*F1`. Now fill down to `E4`. Each formula keeps `D2`, `D3`, `D4` shifting relatively (correct — each row's own total) while `$F$1` stays locked to the one shared tax-rate cell, everywhere it's copied:

```
E2: =D2*$F$1
E3: =D3*$F$1     ← F1 did NOT become F2
E4: =D4*$F$1     ← F1 did NOT become F3
```

**The rule in one sentence: use `$` on any part of a reference that points at a single, shared value — a rate, a constant, a lookup table's corner — that every copy of the formula should keep pointing at.**

## 4. Mixed references — locking only the row, or only the column

You can lock just one half of a reference:

| Form | Column shifts? | Row shifts? | Reads as |
|---|---|---|---|
| `A1` | Yes | Yes | Fully relative |
| `$A1` | **No** | Yes | Column locked, row floats |
| `A$1` | Yes | **No** | Row locked, column floats |
| `$A$1` | **No** | **No** | Fully absolute |

```mermaid
flowchart TD
  A["Copying or filling a formula"] --> B{"Should the column shift?"}
  B -- Yes --> C{"Should the row shift?"}
  B -- No --> D{"Should the row shift?"}
  C -- Yes --> E["A1 — fully relative"]
  C -- No --> F["A$1 — row locked"]
  D -- Yes --> G["$A1 — column locked"]
  D -- No --> H["$A$1 — fully absolute"]
```
*Which reference form to pick, based on what should stay fixed when you fill.*

Mixed references matter most when you fill a formula in **two directions** — down *and* across — from a single cell, which is exactly what a multiplication table, a distance chart, or any "every row against every column" grid needs. (This is the exact mechanic behind this week's Challenge 1 — one formula, filled across a whole 12×12 grid.)

**Worked example.** Build row and column headers for a small multiplication grid:

```
      A     B     C     D
1           2     3     4
2     5
3     6
4     7
```

You want `B2` to equal `5*2 = 10`, and you want to write **one formula in `B2`** that you can fill right *and* down to correctly fill the entire grid — `B2` through `D4`.

Every cell in the grid multiplies "the row header in column A" by "the column header in row 1" — so work out, for each of those two references, which half must stay locked and which half must be free to move:

The row header is always in **column A**, whatever row you're in: reference it as `$A2` (column locked so it never becomes `B2` when you fill right; row left relative so it correctly becomes `$A3`, `$A4` when you fill down).

The column header is always in **row 1**, whatever column you're in: reference it as `B$1` (row locked so it never becomes `B2` when you fill down; column left relative so it correctly becomes `C$1`, `D$1` when you fill right).

```
B2: =$A2*B$1
```

Select `B2`, fill right to `D2`, then select the whole `B2:D2` row and fill down through row 4. Trace what each direction does to the reference:

- **Filling right** (`B2` → `C2` → `D2`): `$A2` is column-locked, so it never changes. `B$1` is row-locked but its *column* is free, so it advances to `C$1`, then `D$1`.
- **Filling down** (`B2` → `B3` → `B4`): `B$1` is row-locked, so it never changes. `$A2` is column-locked but its *row* is free, so it advances to `$A3`, then `$A4`.

Combine both directions and every cell in the grid resolves correctly from the one formula entered once in `B2`:

| | `B` (`$1=2`) | `C` (`$1=3`) | `D` (`$1=4`) |
|---|---|---|---|
| **row 2** (`$A2=5`) | `=$A2*B$1` → 10 | `=$A2*C$1` → 15 | `=$A2*D$1` → 20 |
| **row 3** (`$A3=6`) | `=$A3*B$1` → 12 | `=$A3*C$1` → 18 | `=$A3*D$1` → 24 |
| **row 4** (`$A4=7`) | `=$A4*B$1` → 14 | `=$A4*C$1` → 21 | `=$A4*D$1` → 28 |

One formula, typed once, correctly fills a 3×3 grid — and the same idea scales to the 12×12 grid in this week's Challenge 1.

## 5. The `$` is just text — toggle it with `F4`, not by hand

You don't need to type `$` characters manually. With your cursor inside a reference in the formula bar (or right after typing one), press **`F4`** (Excel — both Windows and Mac with a full keyboard; Mac trackpad-only users may need `Fn+F4` or `Cmd+T` depending on version) to **cycle through all four forms**:

```
A1  →  F4  →  $A$1  →  F4  →  A$1  →  F4  →  $A1  →  F4  →  A1  (back to start)
```

**Google Sheets** uses the same `F4` cycle (or `Ctrl+Shift+4`... actually just `F4` while editing the formula, same as Excel, on both Mac and Windows in-browser). Practicing this cycle until it's a reflex is worth more than memorizing the table above — you'll type `A1` naturally, glance at what you're building, hit `F4` the right number of times, and move on without ever consciously thinking "column locked, row floats."

## 6. Fill vs. copy/paste — same reference rules, different mechanics

Three ways to replicate a formula, all obeying the exact same relative/absolute rules above:

- **Fill handle drag** — grab the small square at the active cell's bottom-right corner, drag across the range. Fastest for a visible, contiguous range.
- **Double-click the fill handle** — with a formula in the top cell of a column that has data in the **adjacent** column, double-clicking the fill handle auto-fills down to match the adjacent column's last row. Extremely fast for long tables — this is how you'd fill hundreds of line-total rows in one click instead of dragging.
- **Copy (`Ctrl+C`) then Paste (`Ctrl+V`)** — works on non-contiguous selections and across sheets; identical reference-shifting rules apply based on the *offset* between the copied cell and the paste target.
- **`Ctrl+D`** (fill down) / **`Ctrl+R`** (fill right) — select the source cell plus the destination range together, then one keystroke fills in that direction. No mouse required.

One paste-related gotcha worth flagging now: **regular paste also overwrites formatting** at the destination. If you've already formatted the destination range (borders, colors) and only want the formula, use **Paste Special → Formulas only** (Excel: `Ctrl+Alt+V` then choose Formulas; Sheets: `Ctrl+Shift+V` then choose "Paste formula only").

## 7. Check yourself

- You fill `=B2*C2` from `D2` down to `D10`. What does the formula in `D6` read?
- You have a tax rate in `F1` and want every row's tax to reference it without drifting. What exact reference do you put in the formula, and why?
- What's the difference between `$A1` and `A$1`? Give a scenario where each is the correct choice.
- Starting from `A1`, how many times do you press `F4` to reach `A$1`?
- Why does a multiplication-grid formula filled in two directions need a **mixed** reference on both the row-header cell and the column-header cell — not a fully relative or fully absolute reference on either?

If those came quickly, move to Lecture 3 — naming ranges so formulas read like sentences, referencing other sheets, and decoding the error values you'll now start seeing when a reference goes wrong.

## Further reading

- **Microsoft — Switch between relative, absolute, and mixed references:** <https://support.microsoft.com/en-us/office/switch-between-relative-absolute-and-mixed-references-dfec08cd-ae65-4f56-839e-5f0d8d0baca9>
- **Microsoft — Copy and paste specific cell contents:** <https://support.microsoft.com/en-us/office/copy-and-paste-specific-cell-contents-6dbcf070-9490-47a8-b3e5-3053b0b939d5>
- **Google — Lock cell references (Sheets Help):** <https://support.google.com/docs/answer/75509>
