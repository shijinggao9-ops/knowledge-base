# Mini-Project — A One-Screen Interactive Sales Dashboard

> Ship a single-screen, interactive sales dashboard for Crunch Retail's FY2026 data — slicers and a timeline that filter multiple pivots at once, KPI tiles and a dynamic title that respond live, charts with a clear visual hierarchy, and sparklines for compact trend context. This is the week's capstone: every lecture, exercise, and challenge from this week, combined into one artifact you could genuinely open in front of a manager and trust.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

A dashboard is the perfect proof of this week's skills because, unlike a formula, it fails *visibly and immediately* if you got the design or the wiring wrong — a chart that doesn't move when you click a slicer, a cluttered screen nobody can read in five seconds, a KPI tile stuck at a stale number. Get every piece right and you have something you'd actually be willing to present.

---

## Deliverable

A `Dashboard` sheet tab (built on your Week 8 workbook, with the `Orders` Table and four pivots feeding it) meeting every requirement below, plus a short `notes.md` reflection (see the end).

---

## Required structure

### 1. Title zone

- A clear, prominent dashboard title.
- **Dynamic** — the title text changes to name the current filter selection (e.g., "Crunch Retail Sales — South — FY2026" when the Region slicer has South selected, reverting to an "All Regions" phrasing when cleared).
- A small, quiet "Data as of" note (Lecture 3, Section 6).

### 2. KPI row — four tiles, in this priority order (left to right)

| Tile | Must be |
|---|---|
| **Total Sales** | Formula-driven, filter-aware (`GETPIVOTDATA` or `SUMIFS`), Currency formatted |
| **Total Orders** | Formula-driven, filter-aware, integer formatted |
| **Average Order Value** | Derived from the two tiles above (not an independent calculation), Currency with 2 decimals, wrapped against `#DIV/0!` |
| **Top Region** | `INDEX`/`MATCH` against the currently-filtered `PivotByRegion` pivot, text output |

All four must visibly update within one click when any slicer or the timeline changes.

### 3. Chart zone — clear visual hierarchy

- **One largest chart**: Sales by Month trend (built from `PivotByMonth`), occupying the most screen real estate in the chart zone — this is the "which direction are we going" chart and should read as the dashboard's second-most-important element after the KPI row.
- **At least two smaller charts**: Sales by Region and Sales by Category (built from their respective pivots), sized visibly smaller than the trend chart.
- Every chart must be connected to the same slicers/timeline as the KPI tiles — clicking a filter should move the charts too, not just the numbers.

### 4. Filter zone

- A Region slicer and a Category slicer, both connected (via Report Connections or the documented Sheets-equivalent workaround) to **all four** underlying pivots.
- A Timeline (or Sheets date-slicer equivalent) on `OrderDate`, connected the same way.
- Visually quiet relative to the KPI row — smaller, more neutral styling, per Lecture 1's hierarchy rule.

### 5. At least one in-cell visual

- At minimum one: a sparkline (Lecture 3, Section 2) showing the twelve-month trend somewhere near the Total Sales tile, **or** a data bars / color scale treatment (Lecture 3, Section 3) applied to a rep- or category-level breakdown table on the dashboard. Both is stronger than one.

### 6. Single-screen constraint

- The entire dashboard — every element above — must be visible with **zero scrolling** at a normal laptop window size (1366×768 or larger, 100% zoom), matching Challenge 1's constraint.

## Required behaviors (test these yourself before submitting)

- [ ] Click a single region in the slicer. All four KPI tiles, the title, and all three charts update to reflect that region only.
- [ ] Add a category filter on top of the region filter. Everything narrows further (filters combine, don't replace).
- [ ] Select a quarter on the timeline in addition to the above. Everything narrows again.
- [ ] Clear all three filters. The dashboard returns to the full FY2026 view, and the Total Sales tile shows a figure consistent with this week's sanity-check total, **$10,786.94** (formatted per your KPI tile's chosen decimal precision).
- [ ] No filter combination you test produces a visible error (`#DIV/0!`, `#REF!`, `#N/A`) anywhere on the dashboard.
- [ ] The dashboard is fully visible with no scrolling in either direction at the target window size.

## Formatting requirements

- One locked, consistent color palette across every chart, tile, and status indicator (Lecture 3, Section 4) — not each app's uncoordinated chart defaults.
- One consistent currency format across every money value on the dashboard.
- Gridlines off on the `Dashboard` sheet; any helper/scaffolding cells (dynamic-title helpers, sparkline data ranges) hidden or moved to a separate `Helpers` tab.
- Thin, intentional borders or shading separating the title, KPI row, chart zone, and filter zone.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Interactivity correctness | 30% | All six required-behavior tests pass; filters genuinely control every element, not just some |
| Layout & hierarchy | 20% | KPI order, chart sizing, and filter-zone quietness all match Lecture 1's hierarchy principles |
| KPI formula quality | 20% | `GETPIVOTDATA`/`SUMIFS` used correctly; Average Order Value derived from other tiles, not recalculated independently; no unguarded division |
| Single-screen constraint | 15% | Genuinely fits with no scrolling at a real laptop resolution |
| Polish (theming, in-cell visuals, chrome removal) | 15% | Consistent palette and formatting; at least one working sparkline or data-bar/color-scale visual |

## Reflection (`notes.md`, ~150–200 words)

1. Which of the six required-behavior tests was hardest to get passing, and what was actually wrong when it first failed?
2. What did you cut from an earlier, more-crowded draft of the dashboard to make the single-screen constraint work, and how did you decide it was safe to cut?
3. If a colleague opened this dashboard cold, with no explanation from you, what's the first thing you'd want them to notice — and does the current layout actually make that the first thing they'd see?

## Stretch goals

- **A fifth KPI tile: month-over-month change.** Add a tile showing this month's sales vs. last month's, formatted with an up/down icon (conditional formatting icon set) reflecting direction — requires pulling two adjacent months' values out of `PivotByMonth` and computing the delta.
- **A Rep leaderboard mini-table** inside the dashboard (not a separate tab) — Rep name, Total Sales, with a data-bar or color-scale treatment — that also respects the active slicers/timeline.
- **A print-ready export.** Set the print area to exactly the dashboard's single-screen bounds and export to PDF; confirm nothing is clipped or spills onto a second page.

## Why this matters

Every skill from Weeks 6-8 converges here: a real Table (Week 6) feeding pivot tables (Week 7) feeding a coordinated, interactive, polished single-screen dashboard (this week). This is the artifact type most people mean when they say "I need a spreadsheet that shows me how the business is doing" — and it's the first time this course has asked you to build something explicitly designed for someone *other than the person who built it* to read correctly in five seconds, with zero explanation required.

When done: push/save your work, take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-08-dashboards-and-visualization/quiz.md), and start Week 9 — Financial & what-if modeling.
