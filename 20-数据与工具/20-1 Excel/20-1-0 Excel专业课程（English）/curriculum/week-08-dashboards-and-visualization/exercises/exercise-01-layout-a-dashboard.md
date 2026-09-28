# Exercise 1 — Sketch & Lay Out a Dashboard

**Time:** ~45–60 min. **Builds on:** the four pivot tables from this week's setup step. **Produces:** a wireframe (on paper or in text) plus an empty, zoned `Dashboard` sheet tab.

## Goal

Design the Crunch Retail dashboard's layout — where the title, KPI row, charts, and filter controls go — **before** placing a single real element. This exercise is deliberately "no formulas, no pivots yet" — it's pure layout thinking, the discipline from Lecture 1.

## Part A — The wireframe (15–20 min, off the sheet)

On paper, in a text file, or using the shape tool directly on a blank sheet, sketch boxes for:

1. **Title zone** — one row, spanning the full width, top of the page.
2. **KPI row** — four equal boxes side by side, directly below the title: Total Sales, Total Orders, Average Order Value, Top Region (in that left-to-right order — recall Lecture 1's hierarchy rule: most important tile goes leftmost).
3. **Chart zone** — the largest area on the page, below the KPI row. Sketch at minimum: one larger box for the Sales by Month trend (this should be the single largest chart — it answers "which direction are we going"), and two smaller boxes beside or below it for Sales by Region and Sales by Category.
4. **Filter zone** — a slim strip, either directly under the title or along one side, for the Region slicer, Category slicer, and Timeline. Keep this visually quiet — small buttons, no large text — per Lecture 1's warning against controls competing with KPI tiles for attention.

Write, in one sentence at the top of your sketch, the **governing question** this dashboard answers (Lecture 1, Section 2) — e.g., *"Is FY2026 on track, and where's the weak spot?"* Check every zone against that sentence: does this zone help answer it?

## Part B — Build the empty skeleton (25–35 min, on the sheet)

On the new `Dashboard` sheet tab:

1. Turn off gridlines (`View → Gridlines`, unchecked) — do this first, so you're designing against a blank canvas, not a spreadsheet grid.
2. Set every column to a uniform, narrow width (e.g., ~20-24 px / ~2-3 characters) across the whole dashboard area — this turns the column grid into a fine, even design canvas rather than fighting Excel's default column widths.
3. Merge a cell range across the top for the **title zone** and type a placeholder: `Crunch Retail Sales Dashboard`. Set it large (28-32pt) and bold.
4. Merge four equal-width cell ranges directly below for the **KPI row**, and label each with a placeholder: `TOTAL SALES`, `TOTAL ORDERS`, `AVG ORDER VALUE`, `TOP REGION`. Leave the values blank — Exercise 3 fills these in.
5. Add thin borders (or shaded background rectangles) outlining the **chart zone** (subdivided per your sketch: one larger area, two smaller ones) and the **filter zone** — these are placeholders; Exercise 2 fills the filter zone with real slicers, and the chart zone gets real pivot charts inserted (drag/resize existing pivot charts from your pivot sheets, or build new ones from the pivots, sized to fit the placeholder boxes).
6. Confirm the whole skeleton is visible with **no scrolling** at a normal laptop window size (per Lecture 1's single-screen rule) — this is the constraint every remaining piece of the dashboard has to keep respecting as it fills in.

## Expected outcome

A `Dashboard` sheet with: no gridlines, a title placeholder, four empty KPI tile outlines in the correct hierarchy order, a subdivided chart zone (one large area + two smaller ones), and a filter zone strip — all fitting on one screen with nothing built yet inside them except labels. It should look like a floor plan, not a finished room.

## Self-check

- [ ] Gridlines are off on the `Dashboard` sheet specifically (your pivot sheets can keep them).
- [ ] The four KPI placeholders are ordered left-to-right by importance, matching Lecture 1's hierarchy discussion.
- [ ] The trend-over-time chart zone is visibly the **largest** single area in the chart zone, not equal-sized with the others.
- [ ] The filter zone is visually smaller/quieter than the KPI row — a viewer's eye should land on the numbers first, the controls second.
- [ ] Everything fits without scrolling at a real laptop window size — check this now, before Exercise 2 adds real content that could push it over.

Move to [Exercise 2](exercise-02-wire-up-slicers.md) once your skeleton passes every check above.
