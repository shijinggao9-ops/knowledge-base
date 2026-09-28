# Challenge 2 — Port a Table Model to Google Sheets

**Time:** ~60 minutes. **Difficulty:** Medium. **Comparative — no single right answer.**

## The scenario

A coworker built a beautiful Table-driven `Orders` model in Excel. You've just been told the team is moving to Google Sheets for this project — or, conversely, someone built a Sheets Table model that has to move into Excel for a client who only uses Microsoft 365. Either direction, your job is the same: get the model working in the other app, and — the actually valuable part — write down **exactly** what didn't come along unchanged.

## Your task

Pick a direction:

- **Excel → Sheets:** export/re-create your `Orders` Table (from this week's exercises) in Google Sheets, using its Tables feature.
- **Sheets → Excel:** if you did this week's exercises primarily in Google Sheets, rebuild the model in Excel instead.

Either way, rebuild:

1. The `Orders` Table itself (24 rows, 9 columns), converted to the target app's Table feature.
2. The `[@Qty]*[@UnitPrice]`-equivalent `Total` formula.
3. At least 3 `SUMIFS`/`COUNTIFS` summary formulas referencing the Table.
4. A Total Row with at least one Sum aggregate.

## What to specifically test and document

For each of the following, note in `challenge-02.md` whether it worked **identically**, worked **but required different syntax**, or **doesn't exist** in the target app:

1. **Formula syntax.** Does the target app support true bracket structured references (`Table[Column]`, `[@Column]`), or do you have to fall back to named ranges / plain A1 references pointing at the Table's current extent?
2. **Auto-fill of formulas into new rows.** Type a new row directly below the Table — does your `Total`-equivalent formula appear in it automatically, immediately, with no action from you?
3. **Auto-expansion of `SUM`/`SUMIFS`-style formulas.** Add a new row with a distinct value in a criterion column (e.g., a new region "Central") and confirm whether your summary formulas' totals change without edits.
4. **Total Row behavior.** Does the target app have an equivalent, and does it offer the same per-column aggregate function choices (Sum, Average, Count, Max, Min, etc.)?
5. **Column type / validation.** If you're going Excel → Sheets, try Sheets' column-type feature (Dropdown/Date/Currency) on a column like `Category` — this has no Excel Table equivalent; note what it does and whether Excel's Data Validation (Week 5) is the closest substitute.
6. **Table styles.** Compare the built-in style galleries — richer in one app or the other?

## Constraints

- Don't just read documentation and guess — actually build the model in the target app and test each point live.
- If a feature genuinely doesn't exist in the target app, don't skip it — describe the closest workaround (a named range that must be manually resized, a filter view instead of a Table filter dropdown, etc.) and its limitation compared to the real thing.

## Hints

<details>
<summary>On structured references in Google Sheets (if going Excel → Sheets)</summary>

Google Sheets Tables (as of this course's writing) give you the *visual and behavioral* parity — auto-expansion, banded formatting, filter dropdowns, a totals row, and even column-type validation Excel doesn't have. What they do **not** give you is Excel's bracket structured-reference formula syntax. A formula inside a Sheets Table still typically resolves to a plain A1 reference or a Sheets-native named-range-like reference under the hood, even though the Table's *range* auto-expands. The practical effect: test very specifically whether a `SUM`-style formula written against the Table's column, once the Table grows, actually captures new rows automatically — behavior can differ from Excel's guaranteed structured-reference growth, and this is exactly the gap worth documenting precisely rather than assuming.

</details>

<details>
<summary>On the reverse direction (Sheets → Excel)</summary>

Anything you built with Sheets' column-type/dropdown validation needs to be rebuilt as Excel Data Validation (Week 5) by hand — it won't transfer automatically even if you literally copy-paste the data, because it's a Sheets-specific Table feature, not a value or a format that travels with the cells.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Actually built it | Describes what "probably" happens | Built and tested the model live in the target app |
| Precision | "Sheets tables are basically the same" | Names the exact formula syntax difference, with a working example of each |
| Honesty about gaps | Glosses over what doesn't transfer | Explicit workaround + its limitation for every missing feature |
| Comparison table | Prose only | A clear point-by-point table matching the 6 test items above |

## Submission

Commit both workbooks (source and ported) plus `challenge-02.md` (your 6-point comparison table and notes) to your portfolio under `c41-week-06/challenge-02/`.
