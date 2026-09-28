# Exercise 3 — Build Dynamic KPI Tiles

**Time:** ~60–90 min. **Builds on:** Exercise 2's connected slicers/timeline. **Produces:** four live KPI tiles and a dynamic title in the `Dashboard` sheet's KPI row and title zone.

## Goal

Fill in the four KPI placeholders from Exercise 1 with real, filter-aware formulas, and make the title zone rewrite itself to describe whatever's currently filtered — so the dashboard's headline numbers and headline text both track every click on the slicers and timeline, automatically.

## Part A — Total Sales tile (15 min)

In the cell beneath the `TOTAL SALES` label:

**Excel (`GETPIVOTDATA` — preferred):**
```
=GETPIVOTDATA("Total", PivotByRegion!$A$3)
```
Type `=`, then click directly on the grand-total cell inside `PivotByRegion` — Excel writes the full `GETPIVOTDATA` formula for you. Confirm the reference points at the pivot's **grand total** row, not one specific region's row.

**Both apps (`SUMIFS` fallback — required in Sheets, optional backup in Excel):**
```
=SUMIFS(Orders[Total], Orders[Region], IF($K$1="All","*",$K$1))
```
This variant needs a helper cell (`K1`) tracking the current slicer selection — see Part E for wiring that helper. For this exercise, if you're using the `SUMIFS` approach, it's acceptable to start with the simpler unfiltered version `=SUM(Orders[Total])` and revisit true filter-tracking once Part E's helper cells exist.

Format the result as **Currency, no decimals** (e.g., `$10,787`), sized large (28pt+) to match its KPI-tile-headline role from Lecture 1.

## Part B — Total Orders tile (10 min)

```
=GETPIVOTDATA("Count of OrderID", PivotByRep!$A$3)
```
(Or the `COUNTIFS` equivalent against the `Orders` Table, following the same pattern as Part A.) Format as a plain integer, no decimals.

## Part C — Average Order Value tile (10 min)

Build this from the **other two tiles**, not a fresh independent calculation — reference the Total Sales tile's cell and the Total Orders tile's cell directly:

```
=[Total Sales cell] / [Total Orders cell]
```

If either referenced tile is currently `0` (e.g., a slicer combination with zero matching orders), wrap it defensively so it doesn't throw `#DIV/0!` on the dashboard:

```
=IFERROR([Total Sales cell]/[Total Orders cell], 0)
```

Format as **Currency, 2 decimals** (average order values are smaller numbers where cents are more visible/meaningful than in the large Total Sales figure).

## Part D — Top Region tile (15–20 min)

Read the currently-highest region directly from the connected, filtered `PivotByRegion` pivot using `INDEX`/`MATCH` (Week 3):

```
=INDEX(PivotByRegion!$A$4:$A$7, MATCH(MAX(PivotByRegion!$B$4:$B$7), PivotByRegion!$B$4:$B$7, 0))
```

Adjust the row range (`$A$4:$A$7` / `$B$4:$B$7`) to match wherever your pivot's actual region rows sit — check the pivot's layout first. This formula reads whatever region rows the pivot is currently displaying, so it automatically tracks the slicer/timeline state without any extra wiring.

## Part E — Dynamic title (15–20 min)

Build a helper cell reflecting the current filter state, then reference it from the title zone:

1. In a hidden helper cell (place it off to the side, or on a separate `Helpers` tab — see Lecture 3, Section 5 on hiding scaffolding), reference the pivot's own filter-state indicator: whatever cell your pivot layout uses to show `(All)` or a specific selected item for the Region field.
2. In the title zone (merged cell from Exercise 1):
```
="Crunch Retail Sales — "&[helper cell]&" — FY2026"
```
3. Test: click a single region in the slicer and confirm the title text changes to name that region. Clear the filter and confirm it reverts to something like `"Crunch Retail Sales — (All) — FY2026"` — if `(All)` reads awkwardly, wrap the helper formula in an `IF` that substitutes a friendlier string, e.g. `IF([raw value]="(All)","All Regions",[raw value])`.

## Part F — Full test pass (10 min)

- [ ] Click `South` in the Region slicer. All four tiles update, and the title now mentions South.
- [ ] Add `Q2` on the Timeline. Tiles narrow further; Total Orders drops, Average Order Value likely shifts.
- [ ] Clear all filters. Total Sales returns to **$10,787** (the FY2026 grand total, rounded), matching this week's sanity-check figure from the README setup step.
- [ ] Every tile's formatting (currency, decimals, font size) stays consistent before and after filtering — only the *value*, never the *format*, should change.

## Expected outcome

Four KPI tiles that visibly recompute the instant a slicer or timeline selection changes, plus a title that rewrites its own text to name the current filter state — with no manual re-entry required for any of it, ever, no matter what the viewer clicks.

## Self-check

- [ ] Average Order Value tile references the Total Sales and Total Orders tile cells directly, not an independent pivot read (Lecture 2, Section 6's "one source of truth" principle).
- [ ] Top Region tile uses `INDEX`/`MATCH` against the *currently filtered* pivot range, so it's correct under every filter combination, not just the unfiltered default.
- [ ] The dynamic title correctly handles both a specific selection and the "nothing filtered" / `(All)` state without showing a raw, awkward pivot placeholder string.
- [ ] Zero filter combination you tested threw a visible error (`#DIV/0!`, `#REF!`, `#N/A`) on the dashboard.

Move to the [challenges](../challenges/) once every box above is checked.
