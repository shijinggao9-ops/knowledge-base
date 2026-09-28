# Challenge 1 — One Formula, Whole Grid

**Time:** ~45–60 minutes. **Difficulty:** Medium. **Constraint: exactly one formula, typed once.**

## The scenario

Lecture 2 built a small 3×3 multiplication grid using one formula with mixed references, filled in two directions. This challenge scales that idea up: a full **12×12 multiplication table** (1 through 12 on both axes — the classic "times table"), built from **one formula typed into one cell**, filled right and down to cover all 144 result cells.

The constraint is strict: if you find yourself typing more than one distinct formula anywhere in the 12×12 result grid, or manually adjusting any `$` after the fill, you've missed the point of mixed references. This challenge exists to prove you can reason about what should lock and what should float *before* you type, not after you debug.

## Your task

1. **Build the headers.** In a fresh sheet tab `Challenge1`, put `1` through `12` across row 1, starting at `B1` (so `B1=1`, `C1=2`, … `M1=12`). Put `1` through `12` down column `A`, starting at `A2` (so `A2=1`, `A3=2`, … `A13=12`). You may type these by hand or use a fill sequence (Excel: type `1` and `2`, select both, drag the fill handle; Sheets: same, or `Edit → Fill → Fill down/right` with a numeric pattern).

2. **Write exactly one formula in `B2`.** It should multiply "the row header for this row" by "the column header for this column," using the correct mixed reference on each half so the formula is valid **everywhere** in the grid, not just at `B2`.

3. **Fill right, then fill down — or fill the whole block at once.** Either: fill `B2` right to `M2` first, then select `B2:M2` and fill down to row 13; or select the entire target range `B2:M13`, then use **Fill → Right** then **Fill → Down** (or the keyboard equivalents), or paste the single formula into the whole selected range at once (Excel/Sheets both apply one formula to a whole selection if you type it then press `Ctrl+Enter` instead of `Enter`, filling every selected cell with the *relatively adjusted* version of that formula — try this as a faster alternative to dragging).

4. **Verify a full row, a full column, and the diagonal.** Spot-check that row 7 (multiples of 7) reads `7, 14, 21, 28, ..., 84` left to right, column 7 (down from `M1=... ` — actually column header 7's column) reads the same multiples top to bottom, and the diagonal from `B2` to `M13` reads perfect squares: `1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144`.

5. **Add a highlight (optional but recommended).** Apply conditional formatting to shade every cell in the grid divisible by 5 (any fill color). This previews Week 5's conditional-formatting-as-data-analysis idea using nothing but what you already know: a formula-based conditional rule like `=MOD(B2,5)=0`.

## What "done" looks like

- A 144-cell grid where every cell's formula, when you click on it and read the formula bar, has the **identical relative/absolute pattern** — only the row and column position differs, never the reference shape.
- Row 12 (the last row) times column 12 (the last column), i.e. cell `M13`, reads `144`.
- You did **not** type 144 individual formulas, and you did **not** manually edit any `$` after the initial fill.

## Constraints

- One formula shape, entered once, filled to cover the entire 12×12 result block.
- No helper columns or rows beyond the two header strips (row 1 and column A).
- Use `F4` to build the reference, not manual `$` typing — practice the reflex from Lecture 2.

## Hints

<details>
<summary>Stuck on which half to lock</summary>

Ask, for any arbitrary cell in the grid: "what two headers should this cell multiply?" Always its **row's** header (living in column `A`, same row) and its **column's** header (living in row `1`, same column). The row header always lives in column `A` — so lock the *column* of that reference (`$A2`, never becomes `B2` etc. when you fill right). The column header always lives in row `1` — so lock the *row* of that reference (`B$1`, never becomes `B2` etc. when you fill down). The formula in `B2` is therefore `=$A2*B$1` — identical shape to the 3×3 warm-up in Lecture 2, just filled across a bigger range.

</details>

<details>
<summary>Sanity-checking one cell by hand</summary>

Cell `F7` sits in column `F` (the 5th data column, since `B` is the 1st) and row `7` (the 6th data row, since row `2` is the 1st). Its column header (row 1 of column `F`) is `5`; its row header (column A of row 7) is `6`. So `F7` should read `30`. If your grid disagrees, the bug is almost always a `$` on the wrong half of one of the two references.

</details>

<details>
<summary>Filling a whole selection at once</summary>

Select the entire target range `B2:M13` first (click `B2`, then shift-click `M13`). Type the formula as if you were typing it into `B2` specifically. Instead of `Enter`, press **`Ctrl+Enter`** (both Excel and Sheets). This fills every selected cell with the formula, each relatively adjusted to its own position — identical end result to drag-filling, in one keystroke.

</details>

## Stretch

- Extend the grid to 20×20 and confirm it still works with zero changes to the formula in `B2` — only the header ranges grow.
- Build a **second** grid below it that computes each cell as row-header **plus** column-header instead of times, reusing the same header strips, to prove the mixed-reference technique isn't specific to multiplication.

## Submission

Keep the `Challenge1` sheet in your `crunch-week2` workbook. In a `Notes` cell near the grid, write the exact formula you used in `B2` and one sentence on which half of each reference you locked and why.
