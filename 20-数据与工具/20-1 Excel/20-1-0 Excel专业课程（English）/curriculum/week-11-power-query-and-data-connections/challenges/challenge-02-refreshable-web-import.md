# Challenge 2 — Build a Refreshable Web Import

**Time:** ~90 minutes. **Difficulty:** Medium. **You pick the page (within constraints).**

## The scenario

Not every data source Crunch Wholesale needs lives in a file someone emails around. Some of it lives on a public web page — a shipping-rate table, a currency-conversion reference, a public dataset a partner maintains and updates on their own schedule. Power Query's **From Web** connector treats a page's HTML table the same way it treats a CSV: something to import, clean, and — critically — something you can hit **Refresh** on later to pick up whatever the page currently shows, without re-doing the import from scratch.

## Your task

Find a public web page containing at least one genuine HTML `<table>` (not an image of a table, not a table rendered entirely by JavaScript after the page loads — Power Query's Web connector reads the page's HTML directly and cannot execute client-side scripts, so pick a page where the table exists in the raw page source). A reliable category to search: any Wikipedia "List of..." article with a data table (population by country, GDP by country, a sports league's standings table, a list of world capitals) — these are stable in structure even as their numbers update, which is exactly the property this challenge needs.

### Requirements

1. **Import via `Data → Get Data → From Other Sources → From Web`**, paste your chosen URL, and use the **Navigator** pane to identify and select the correct table object (a page can expose several — pick the one matching what you intended, not just the first one listed).
2. **Clean the result** with at least three distinct transform steps from this week's vocabulary — at minimum, one type conversion (a column that imported as text but should be numeric — web tables are notorious for numbers arriving with footnote markers, commas, or `%` signs baked in as text), one column removal or rename, and one row filter (removing a footnote row, a "Total" summary row, or anything that isn't a genuine data row).
3. **Load to a Table**, named descriptively (not `Table1`).
4. **The refresh test.** Note down (in `challenge-02.md`) the exact value of one specific cell right after your first successful load — a specific country's population, a specific team's win count, whatever your table shows. Wait at least a few minutes (or come back to this later in the week), then click **Refresh** on the query. Report whether the value changed, stayed the same, or the import broke entirely — all three are valid, informative outcomes; document whichever one actually happened and why you think it happened (a page that updates rarely may show no change in a short window — that's expected, not a failure).
5. **Document the failure mode.** In `challenge-02.md`, describe what you'd expect to happen to this query if the source page's table structure changed significantly (a column added, removed, or renamed) — you don't have to actually cause this, just reason through it based on what you know about how Power Query's steps reference columns by name.

## Constraints

- The page must be genuinely public (no login required) and must contain a real HTML `<table>` element — if the Navigator pane shows no usable tables for a page, that's a sign the content is JavaScript-rendered or structured differently; pick a different page rather than fighting it.
- At least one of your cleaning steps must handle a real messiness the page's raw data has (a footnote marker like `[12]` inside what should be a plain number, a unit suffix, inconsistent capitalization) — if your chosen table imports perfectly clean with nothing to fix, pick a richer page with more visible formatting quirks.
- Do not fabricate the refresh-test result — an honest "the value didn't change in the 10 minutes I waited, and here's why that's expected for this page" is a complete, valid answer.

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Table selection | Wrong or clearly mismatched table imported | Correct table identified via the Navigator, confirmed against the page visually |
| Cleaning | Data left with visible junk (footnote markers, text-typed numbers) | At least 3 real, necessary cleaning steps applied and named sensibly |
| Refresh test | Skipped, or asserted without evidence | Specific before/after value documented, outcome explained |
| Reasoning about fragility | Not addressed | A clear, specific explanation of what would break the query and why |

## Submission

Commit the workbook plus `challenge-02.md` (the URL used, your before/after refresh values, and your fragility reasoning) to your portfolio under `c41-week-11/challenge-02/`.
