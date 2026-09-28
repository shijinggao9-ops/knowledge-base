# Week 8 — Exercises

Three guided exercises, ~45–90 min each, done **in order** — each one builds directly on the sheet the previous one produced. By the end of Exercise 3 you'll have a functioning (if not yet fully polished) interactive dashboard, which the challenges and mini-project then push further.

1. **[Exercise 1 — Sketch & lay out a dashboard](exercise-01-layout-a-dashboard.md)** — wireframe the Crunch Retail dashboard's zones on paper (or text), then build the empty, zoned skeleton directly on a new sheet tab.
2. **[Exercise 2 — Wire slicers to pivots](exercise-02-wire-up-slicers.md)** — insert Region and Category slicers plus a Timeline, and connect all three to all four pivot tables at once.
3. **[Exercise 3 — Build dynamic KPI tiles](exercise-03-kpi-tiles.md)** — build four formula-driven KPI tiles and a dynamic title that respond live to whatever the slicers currently show.

## Before you start

- You've completed all three lectures.
- Your workbook has the `Orders` Table (48 rows, FY2026) and all four pivots — `PivotByRegion`, `PivotByCategory`, `PivotByRep`, `PivotByMonth` — from this week's [README setup step](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/README.md#set-up-your-workspace-do-this-first). If any pivot is missing, build it before starting Exercise 1; every exercise this week assumes all four exist.
- A new, blank sheet tab named `Dashboard` — this is where every exercise places its work. Keep the four pivot sheets as the data engine behind the scenes; the `Dashboard` tab is the only thing a viewer should ever need to look at.

## Suggested workflow

- Do the sketch in Exercise 1 for real — on paper or in a plain text file — before touching the `Dashboard` sheet. Skipping straight to placing charts is the single most common way this week's dashboard ends up cluttered and needing a rebuild.
- Keep formula view (`Ctrl+`` ``) handy while building KPI tiles in Exercise 3 — you'll want to see the actual `GETPIVOTDATA`/`SUMIFS` formulas, not just their formatted output, while debugging.
- Test every slicer and the timeline after each exercise, not just at the very end — a connection you forget to wire in Exercise 2 is much easier to catch immediately than after Exercise 3's KPI tiles are already built on top of it.

## Note on the two apps

Exercises 1 and 3 work close to identically in Excel and Google Sheets. Exercise 2 — slicers and the timeline specifically — has real platform differences, called out inline in that exercise and revisited in depth in Lecture 2, Section 8 and Challenge 2.
