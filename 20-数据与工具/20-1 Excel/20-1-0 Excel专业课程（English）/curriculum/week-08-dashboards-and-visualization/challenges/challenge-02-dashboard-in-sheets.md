# Challenge 2 — Rebuild the Dashboard in Google Sheets

**Time:** ~90-120 min. **Requires:** the completed dashboard (ideally after Challenge 1's single-screen pass, though this challenge stands alone). **If you already built this week's exercises in Google Sheets:** do this challenge in Excel instead, porting the other direction — the deliverable and rubric are identical either way.

## The task

Rebuild the entire Crunch Retail dashboard — pivots, slicers/timeline-equivalent, KPI tiles, dynamic title, sparklines, conditional formatting — in **Google Sheets**, starting from the same 48-row `Orders` dataset. This is not a "does it work at all" bar; it's a "does it hold up to the same tests" bar, using Exercise 2's Part C and Exercise 3's Part F test lists as your acceptance criteria in the new platform.

## Steps

1. In a new Google Sheets file, paste the same 48-row `Orders` dataset from this week's README setup step. Convert to a Sheets Table (or a named range, if your account's Sheets Table feature differs — see Week 6's Challenge 2 notes on that).
2. Build the same four pivot tables: `PivotByRegion`, `PivotByCategory`, `PivotByRep`, `PivotByMonth`.
3. Add slicers per pivot (`Data → Add a slicer`), following the multi-slicer pattern from Lecture 2, Section 8 and Exercise 2's Google Sheets variant, since there's no single shared-connection control.
4. Build four KPI tiles using `SUMIFS`/`COUNTIFS` against the source range (Technique B from Lecture 2, Section 6) — `GETPIVOTDATA` is not available, so this is your only path.
5. Build a dynamic title using the same helper-cell-plus-concatenation pattern from Exercise 3, Part E, adapted to whatever your Sheets slicer/helper-cell setup produces.
6. Add sparklines using the `=SPARKLINE()` function (Lecture 3, Section 2) in place of Excel's Insert-menu sparklines.
7. Add a color scale (`Format → Conditional formatting`) in place of Excel's data bars, or use a `SPARKLINE(..., {"charttype","bar"})` formula as the closer bar-in-cell equivalent (Lecture 3, Section 3).
8. Run every test from Exercise 2, Part C and Exercise 3, Part F against the Sheets version.

## Deliverable

The Sheets dashboard file (shared or exported), plus a `sheets-vs-excel.md` write-up (300-400 words, or a table) covering **at minimum** these five specific divergences:

1. **Slicer connection model** — what you had to do differently to get multiple pivots filtering together, since there's no Report Connections dialog.
2. **Timeline replacement** — what you used instead of a draggable date-range Timeline, and what capability was lost (if any) compared to Excel's version.
3. **KPI formula approach** — why `GETPIVOTDATA` wasn't available and what you used instead, with the actual formula.
4. **In-cell visual differences** — `SPARKLINE()` as a function vs. Excel's menu-driven sparklines, and the data-bars gap specifically.
5. **One thing that was equally easy (or easier!) in Sheets** — not everything in this challenge should read as "Sheets is missing X"; name at least one piece that ported over cleanly or was simpler to set up.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Functional parity | 35% | The Sheets dashboard passes the same tests the Excel version did — correct filtered totals, working title, working sparklines |
| Accuracy of the write-up | 30% | Each of the five required points names the *actual* feature gap and workaround, not a vague generalization |
| Honest balance | 15% | The write-up includes at least one genuine "this was fine/better in Sheets" point, not pure complaint |
| Visual polish carried over | 20% | The Sheets version applies Lecture 3's theming/polish principles too, not just raw function parity |

## Why this matters

Real teams are split across Excel and Google Sheets constantly, and a dashboard built assuming one platform's exact toolset often breaks — or looks noticeably worse — the moment someone opens it in the other. Knowing precisely where the two diverge (not vaguely, precisely — which dialog doesn't exist, which function has no equivalent) is what lets you design a dashboard that's genuinely portable, or at least warn a teammate exactly what won't survive the move before they find out the hard way.
