# Exercise 2 — Wire Slicers to Pivots

**Time:** ~60–90 min. **Builds on:** Exercise 1's `Dashboard` skeleton and the four pivot tables. **Produces:** a Region slicer, a Category slicer, and a Timeline, all connected to all four pivots at once, placed in the `Dashboard` sheet's filter zone.

## Goal

Turn four independently-filterable pivot tables into one coordinated set — click one button anywhere and watch every pivot (and, once they're placed, every chart) move together.

## Part A — Insert the controls (20 min)

1. Click into `PivotByRegion`. `Insert → Slicer` (or `PivotTable Analyze → Insert Slicer`). Check `Region`. Click OK.
2. Click into `PivotByCategory`. Insert another slicer, this time checking `Category`.
3. Click into `PivotByMonth`. `Insert → Timeline` (or `PivotTable Analyze → Insert Timeline`). Check `OrderDate`. Click OK.
4. Drag all three controls onto the `Dashboard` sheet's filter zone (from Exercise 1). Resize them to fit cleanly within that zone without crowding — a slicer with buttons crammed too small to click accurately defeats its own purpose.

## Part B — Connect every control to every pivot (25–35 min)

This is the step that's easy to skip and breaks the whole dashboard if you do.

1. Click the **Region slicer** to select it. Open **Report Connections** (Excel 365/2021 — button appears on the ribbon's `Slicer` tab when a slicer is selected) or **PivotTable Connections** (older Excel).
2. In the dialog, check **all four** pivot tables: `PivotByRegion`, `PivotByCategory`, `PivotByRep`, `PivotByMonth`. Click OK.
3. Repeat step 1-2 for the **Category slicer**.
4. Repeat step 1-2 for the **Timeline** (its equivalent connections dialog).

## Part C — Prove it works (15–20 min)

Do **all four** of these tests. Don't skip any — each one catches a different possible mistake:

- [ ] Click a single region button (e.g., `South`) in the Region slicer. Switch to each of the four pivot sheet tabs in turn and confirm **every one** shows South-only totals — not just the one the slicer happened to be inserted from.
- [ ] Click a single category button (e.g., `Software`) in the Category slicer, in addition to the region filter still active. Confirm all four pivots now show South + Software only — filters should combine (AND together), not replace each other.
- [ ] Drag-select a quarter (e.g., `Q2`) on the Timeline. Confirm all four pivots narrow further to South + Software + Q2.
- [ ] Click the clear-filter icon on each control in turn (top-right corner of each slicer, and the Timeline's clear button). Confirm every pivot returns to the full, unfiltered FY2026 totals after all three are cleared — and cross-check the grand total against this week's sanity-check figure, **10786.94**, to confirm nothing was left partially filtered.

## Google Sheets version (if working in Sheets instead of Excel)

Sheets has no Report Connections dialog and no Timeline control — see Lecture 2, Section 8 for the full explanation. For this exercise in Sheets:

1. Build each of the four pivots from the **same source range** (the `Orders` data), not copies of each other.
2. `Data → Add a slicer` from each pivot separately, choosing `Region` each time — you'll end up with **four separate Region slicers**, one per pivot, rather than one shared control.
3. Set all four to the same selection manually to simulate the coordinated effect — this is real, documented friction, not a mistake on your part; Challenge 2 has you write this up formally.
4. For a Timeline-equivalent, add a fifth slicer per pivot on the `OrderDate` column, using checkboxes instead of a date-range slider.

## Expected outcome

Three controls (two slicers, one timeline — or, in Sheets, the multi-slicer workaround) sitting in the `Dashboard` sheet's filter zone, all provably connected to all four pivots, correctly combining filters (AND logic) and correctly resetting to the full FY2026 total when cleared.

## Common mistakes

- **Forgetting Report Connections entirely.** Symptom: clicking a slicer button only changes the one pivot it was inserted from. Fix: revisit Part B for that specific control.
- **Connecting a slicer to a pivot built from a different source.** If your `PivotByMonth` was accidentally built from a *copy* of the `Orders` Table rather than the Table itself, it won't appear as a connectable option — Excel silently omits sources it can't link. Rebuild that pivot from the real `Orders` Table.
- **Testing on only one pivot sheet.** A slicer can look like it's "working" if you only ever glance at the pivot you happened to insert it from — always check all four, per Part C.

Move to [Exercise 3](exercise-03-kpi-tiles.md) once every checkbox in Part C passes.
