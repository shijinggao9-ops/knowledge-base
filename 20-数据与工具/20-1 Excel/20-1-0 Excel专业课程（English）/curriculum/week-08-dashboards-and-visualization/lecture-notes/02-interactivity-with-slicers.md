# Lecture 2 — Interactivity: Slicers & Controls

> **Duration:** ~2.5 hours. **Outcome:** You can insert a slicer and a timeline, connect either one to every pivot table on your dashboard at once, and build KPI tiles and a title that recompute correctly the instant the viewer clicks a filter — without touching a single formula by hand afterward.

## 1. The problem this lecture solves

You have four pivot tables from this week's setup — `PivotByRegion`, `PivotByCategory`, `PivotByRep`, `PivotByMonth` — each built from the same `Orders` Table. Right-click any one of them and you can filter it: click the `Region` field's dropdown, uncheck `North`, and that one pivot updates. But the other three don't move. A viewer who wants to see "just the West region" across every chart on the dashboard would have to filter all four pivots individually, one dropdown at a time — exactly the kind of tedious, error-prone, multi-click friction a dashboard exists to eliminate.

A **slicer** solves this directly: it's a visible button panel — one button per unique value (`North`, `South`, `East`, `West`) — that filters not just one pivot but every pivot you connect it to, simultaneously, with a single click. A **timeline** is the date-specific version of the same idea: a horizontal slider for filtering by year, quarter, month, or day. Together, slicers and a timeline are what turn four separate pivot tables into one coherent, clickable dashboard.

## 2. Inserting a slicer

**In Excel:** click anywhere inside a pivot table, then `PivotTable Analyze → Insert Slicer` (or `Insert → Slicer` with the pivot selected). Check the fields you want slicer buttons for — for this week's dashboard, insert two slicers: one for `Region`, one for `Category`. Excel drops a floating slicer panel on the sheet; drag it to the filter zone from your Lecture 1 sketch.

Click a button inside the slicer (`South`, for example) and watch: the pivot table you inserted it from re-filters instantly to show only South's numbers. Click a second button while holding `Ctrl` (Windows) / `Cmd` (Mac) to multi-select — e.g., `South` and `West` together. Click the small "clear filter" icon in the slicer's top-right corner to reset it.

**In Google Sheets:** select the data range or click into a pivot table, then `Data → Add a slicer`. Choose the column to slice by (`Region`) in the side panel that opens. Sheets slicers look and behave similarly — a dropdown-style panel with checkboxes for each value — but there's a structural difference covered in Section 8 below.

## 3. Connecting one slicer to multiple pivot tables — Report Connections

Here's the part that actually makes a slicer a *dashboard* tool instead of a single-pivot convenience: **by default, a slicer you insert from a specific pivot is connected only to that pivot.** Click a button and only that one table reacts. To make it filter every pivot on the dashboard at once, you have to explicitly wire the connection.

```mermaid
flowchart LR
  S["Region Slicer"] --> P1["PivotByRegion"]
  S --> P2["PivotByCategory"]
  S --> P3["PivotByRep"]
  S --> P4["PivotByMonth"]
```
*After Report Connections, one slicer click re-filters all four pivots at once.*

**In Excel:**

1. Click the slicer to select it (not a pivot — the slicer itself).
2. `Slicer → Report Connections` (Excel 365/2021) or `PivotTable Connections` (older versions) — both live on the ribbon when a slicer is selected.
3. A dialog lists every PivotTable in the workbook with a checkbox. Check **all four**: `PivotByRegion`, `PivotByCategory`, `PivotByRep`, `PivotByMonth`.
4. Click OK. Click a button in the slicer again — now all four pivots re-filter together, in sync.

Repeat for the `Category` slicer and for the timeline (Section 4) — each control needs its own Report Connections pass, checked against all four pivots.

**One requirement that trips people up:** Report Connections can only link pivots that share the **same underlying source** (all four of this week's pivots read from the same `Orders` Table, so this works cleanly). A slicer built from a pivot on a *different* data source cannot connect to pivots on this one — Excel will simply not list it as an option.

## 4. Adding a timeline for date filtering

Click into any pivot table with a date field (`PivotByMonth`, whose row field is grouped by Month from `OrderDate`), then `PivotTable Analyze → Insert Timeline`. Check `OrderDate` in the dialog. Excel drops a horizontal slider showing all twelve months of 2026 as clickable blocks, with a level selector (Years / Quarters / Months / Days) in its top-right corner.

Click a single month block to filter to just that month; click-drag across several blocks to select a range (e.g., `Jan`–`Mar` for Q1). Just like a slicer, a freshly inserted timeline is connected only to the pivot it came from — run the same **Report Connections** step from Section 3 to wire it to all four pivots.

**Google Sheets has no dedicated Timeline control.** The closest equivalent is a slicer built on the `OrderDate` column itself, which gives checkboxes per date rather than a draggable range slider — a real capability gap covered in Section 8 and revisited in Challenge 2.

## 5. Dynamic titles — text that rewrites itself

A dashboard title that always reads "Crunch Retail Sales Dashboard" no matter what's filtered is a missed opportunity — the title is prime top-left real estate (Lecture 1, Section 3) and can do real work by telling the viewer *what they're currently looking at*.

Build a dynamic title with `TEXT` and string concatenation (`&`), referencing a cell that reflects the current slicer state. The simplest reliable technique: have the KPI formula area (Section 6) compute a "current scope" description in a helper cell, then reference that cell from the title:

```
' In a helper cell, e.g. H1:
=IF(COUNTA(FILTER-SOURCE)=1, FILTER-SOURCE-VALUE, "All Regions")

' In the title cell, e.g. A1 (merged across the title zone):
="Crunch Retail — "&H1&" — FY2026"
```

In practice, the cleanest version pulls directly from a pivot's current filtered field using `GETPIVOTDATA`'s companion technique — referencing the pivot's own filter-state field cell, which Excel keeps up to date automatically:

```
="Crunch Retail Sales — "&PivotByRegion!B1&" View"
```

where `PivotByRegion!B1` is the pivot's own "(All)" / selected-item indicator cell in its layout. The exact cell address depends on your pivot's layout (Compact vs. Tabular), so check the pivot header area for wherever it displays the current filter state and point your title formula there.

## 6. KPI tiles — formulas that respond to the same filters

A KPI tile is nothing more than a big, prominently formatted cell containing a formula that reads a **filtered** total. Two techniques get you there:

**Technique A — `GETPIVOTDATA` (Excel, reading directly off a connected pivot):**

```
=GETPIVOTDATA("Total", PivotByRegion!$A$3)
```

`GETPIVOTDATA` reads the *currently displayed* (i.e., currently filtered) value from a pivot table — so once `PivotByRegion` is slicer-connected, a KPI tile built this way updates automatically the instant the viewer clicks a slicer button, with zero extra logic. The fastest way to write one correctly: click into an empty cell, type `=`, then click directly on the number inside the pivot table you want to reference — Excel builds the full `GETPIVOTDATA` formula for you automatically. (If you'd rather type plain cell references instead, turn this behavior off via `File → Options → Formulas → uncheck "Use GETPIVOTDATA functions for PivotTable references"` — but for KPI tiles that need to track a filtered pivot, leaving it on and letting Excel write the formula is the reliable path.)

**Technique B — `SUMIFS`/`COUNTIFS` against slicer-linked cells (works in both apps, and is the only option in Sheets):**

Because Google Sheets has no `GETPIVOTDATA` equivalent, build KPI tiles there — and as a robust fallback in Excel — with `SUMIFS` reading the source Table directly, driven by helper cells that a slicer or dropdown controls:

```
=SUMIFS(Orders[Total], Orders[Region], $K$1)
```

where `K1` holds the currently selected region (typed, or driven by a linked cell/dropdown). This is less automatic than `GETPIVOTDATA` — it requires a helper cell wired to the filter — but it's transparent, debuggable, and identical in both apps.

**This week's four KPI tiles**, all rebuilt live from whichever technique fits your app:

| Tile | Formula shape |
|---|---|
| **Total Sales** | `=GETPIVOTDATA("Total", PivotByRegion!$A$3)` (grand total row of a connected pivot) |
| **Total Orders** | `=GETPIVOTDATA("Count of OrderID", PivotByRep!$A$3)` (or `COUNTIFS` fallback) |
| **Average Order Value** | `=[Total Sales tile] / [Total Orders tile]` — a ratio built from the two tiles above, not a fresh pivot read |
| **Top Region** | `=INDEX(PivotByRegion!A4:A7, MATCH(MAX(PivotByRegion!B4:B7), PivotByRegion!B4:B7, 0))` — an `INDEX`/`MATCH` (Week 3) reading the pivot's own filtered rows |

Notice the **Average Order Value** and **Top Region** tiles are built from the *other tiles or pivot ranges*, not re-derived independently — this is deliberate. One correct, filter-aware source of truth (the connected pivots) feeds everything downstream, so there's exactly one place a filter's effect has to propagate correctly, not four.

## 7. Worked example: wiring it all together

Sequence for the Crunch Retail dashboard, once all four pivots exist:

1. Insert a `Region` slicer and a `Category` slicer from any one pivot.
2. Insert a `Timeline` on `OrderDate` from `PivotByMonth`.
3. Select the `Region` slicer → **Report Connections** → check all four pivots.
4. Repeat step 3 for the `Category` slicer and the timeline.
5. Click `West` in the Region slicer and `Q2` on the timeline together. Confirm **all four pivots** — including ones you're not currently looking at — show only West, Q2 data. Switch tabs to check each one; don't just trust the one on screen.
6. Build the four KPI tiles per Section 6, placed on the dashboard sheet (not on a pivot sheet), and confirm each one changes when you toggle the slicers.
7. Build the dynamic title per Section 5, confirm it rewrites correctly.

If any pivot fails to update when a slicer is clicked, the almost-certain cause is a missed connection — go back to Report Connections for that specific slicer and check the box for the pivot that isn't responding.

## 8. Where Google Sheets diverges

Google Sheets' Slicer tool (`Data → Add a slicer`) looks similar but has real structural differences worth knowing before Challenge 2 later this week:

- **No Report Connections dialog.** A Sheets slicer filters the **data range or pivot table it's attached to directly** — there's no separate "connect this slicer to N other pivots" step, because a single slicer is scoped to one range. To filter multiple pivots with one control, the cleanest pattern is building every pivot from the **same source range** and placing one slicer per pivot, all pointed at the same filtering column — they won't share literal state, but setting them to matching selections achieves the same visual effect.
- **No Timeline control.** Use a slicer on the date column itself (checkbox-per-date, not a draggable range), or a helper `SUMIFS`-driven date-range picker built from two typed cells (`Start Date`, `End Date`).
- **No `GETPIVOTDATA` function.** KPI tiles in Sheets are built with Technique B (`SUMIFS`/`COUNTIFS` against the source range) exclusively — there's no direct formula-based read off a pivot's displayed values.

None of this makes a Sheets dashboard impossible — Challenge 2 has you build one — it just means Technique B, not Technique A, is the backbone of every interactive element once you cross platforms.

## 9. Check yourself

- Why does inserting a slicer from one pivot table not automatically filter the other three, and what's the one setting that fixes it?
- What's the practical difference between a slicer and a timeline, and why does a timeline only make sense on a date field?
- Why does the Average Order Value KPI tile reference the Total Sales and Total Orders tiles instead of computing its own independent pivot read?
- Name the one Excel feature this lecture relies on that has **no equivalent** in Google Sheets, and what technique replaces it there.
- A viewer clicks `South` in the Region slicer and only two of your four pivots update. What's the most likely cause, and how do you fix it?

If those came quickly, move to Lecture 3 — sparklines, data bars, and the theming and polish pass that turns a working dashboard into a genuinely readable one.

## Further reading

- **Microsoft — Use slicers to filter data:** <https://support.microsoft.com/en-us/office/use-slicers-to-filter-data-249f966b-a9d5-4b0f-b31a-12651785d29d>
- **Microsoft — Create a PivotTable timeline to filter dates:** <https://support.microsoft.com/en-us/office/create-a-pivottable-timeline-to-filter-dates-d3956083-01be-408c-906d-6fc99d9fadfa>
- **Microsoft — GETPIVOTDATA function:** <https://support.microsoft.com/en-us/office/getpivotdata-function-8c083b99-a922-4ca0-af5e-3af55960761f>
- **Google — Filter charts and tables with Slicers:** <https://support.google.com/docs/answer/9245556>
