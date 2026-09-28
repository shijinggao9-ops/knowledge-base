# Lecture 2 — Cleaning Techniques

> **Duration:** ~2 hours. **Outcome:** You can remove exact duplicates with the built-in tool, catch near-duplicates it misses, strip stray whitespace and non-printing characters at scale with `TRIM`/`CLEAN`, extract and reshape values with Flash Fill (Excel) and its Google Sheets equivalents, and turn a "wide" or oddly split layout into one clean row per record.

Lecture 1 taught you to *find* the problems in `RawSignups`. This lecture fixes them. Work through this section in order, on a **copy** of `RawSignups` (right-click the tab → Duplicate/Move or copy) named `CleanSignups` — always clean on a copy, never on the only version of raw data you have. If you make a mistake, you can always start over from the untouched original.

## 1. Remove Duplicates — the built-in tool

Both apps ship a dedicated dedupe tool. Select your data range (include headers), then:

- **Excel:** Data tab → **Remove Duplicates**.
- **Google Sheets:** Data menu → **Data cleanup** → **Remove duplicates**.

Both open a dialog letting you choose **which columns** must match for a row to count as a duplicate. This choice matters enormously:

- Check **only** `CustID` → nothing gets removed (every ID in `RawSignups` is unique, even for the true Sara Kim duplicate — wait, they're different IDs 1005/1006, so this reveals nothing).
- Check **all columns** (Name, Email, State, Tier, Date, Amount) → only rows that are **identical in every single selected column** are treated as duplicates. This is the safest, narrowest setting and the one to reach for first.
- Check **just Name + Email** → this would also catch rows 8/9 (Ana Souza) if their name/email matched exactly — but they don't (`Ana Souza` vs `Ana souza`, different casing), so even this narrower match still misses them.

Run Remove Duplicates on `CleanSignups` checking **all columns**. You should see it report **1 duplicate found and removed** — row 6 (Sara Kim's exact copy). Rows 8/9 (Ana Souza) are untouched, because the tool does **exact, case-sensitive-by-value string comparison** and nothing normalizes the input first.

**The core limitation to internalize:** Remove Duplicates finds rows that are *byte-for-byte identical* in the columns you selected. It does not know that `WA` means the same thing as `Washington`, or that `"Ana Souza"` and `"Ana souza"` are the same human. For that, you clean the *values* first (Sections 2–4 below), and only run Remove Duplicates *after* — dedupe is often the **last** step, not the first, precisely because standardizing values first turns near-duplicates into exact ones the tool can then catch.

## 2. `TRIM` and `CLEAN` — the two functions to run on every text import

**`TRIM`** removes leading and trailing spaces, and collapses any run of multiple spaces *inside* the text down to one:

```
=TRIM("  Ana   Souza  ")     → "Ana Souza"
```

**`CLEAN`** strips non-printing characters — the invisible control characters (line breaks, tabs baked into a cell, artifacts from a PDF or database export) that `TRIM` doesn't touch, because they aren't ordinary spaces:

```
=CLEAN(A2)
```

The standard, defensive habit on **any** freshly imported text column is to run both, nested:

```
=TRIM(CLEAN(A2))
```

Add a helper column next to `Full Name` in `CleanSignups` with this formula, fill it down, then compare visually against the original — most rows won't visibly change (there was no invisible junk), but this habit costs nothing and catches the rows that *do* have it, every single time, without you having to know in advance which rows are affected.

**Committing the cleaned values.** A formula column is not the final answer — it's scaffolding. Once you trust the `TRIM(CLEAN(...))` column:

1. Select it, **Copy** (`Ctrl/Cmd+C`).
2. **Paste Special → Values Only** on top of the original column (Excel: right-click → Paste Special → Values; Sheets: right-click → Paste special → Paste values only, or `Ctrl/Cmd+Shift+V`).
3. Delete the now-redundant helper column.

This "formula, verify, paste-as-values, delete helper" cycle is the backbone of nearly every cleaning task this week. You never manually retype a cleaned value — you compute it once, confirm it, then freeze it as a plain value so it doesn't silently break if you later delete a row the formula depended on.

## 3. Find & Replace — fast, blunt, and dangerous if you're not careful

For a **known, finite** set of substitutions — like collapsing `CA`/`California`/`ca` down to one spelling — Find & Replace (Excel/Sheets: `Ctrl/Cmd+H`) is often faster than a formula.

Two settings matter every time you open the dialog:

- **Match case** — leave this **off** by default so `california` and `California` both match one search, unless case is exactly what you're trying to preserve.
- **Match entire cell contents** — turn this **on** whenever you're replacing a whole category value (like a state), not a substring. Without it, replacing `"CA"` with `"California"` would also corrupt any cell that merely *contains* `"CA"` as a substring of something else — a real risk in address or free-text fields.

Run four replacements on the `State` column of `CleanSignups`, each with "Match entire cell contents" **on**:

1. `CA` → `California`, then also `ca` → `California` (two passes, since Find & Replace is exact about case even with "Match case" off in most implementations for *whole-value* matches — verify your app's behavior on a scratch copy first).
2. `NY` → `New York`, `ny` → `New York`.
3. `TX` → `Texas`.
4. `WA` → `Washington`.

**Do the `Tier` column the same way**, collapsing `gold`/`GOLD` → `Gold`, `silver` → `Silver`, `platinum` → `Platinum`. After this pass, re-run the Section 7-style frequency count from Lecture 1 — you should now see exactly **five** states and **four** tiers, matching reality.

⚠️ **Find & Replace has no undo-per-cell.** It's a global, in-place edit. Always work on a copy of the sheet, and always run your Lecture-1 audit formulas again immediately after, to confirm the replacement did exactly what you intended and nothing more.

## 4. `SUBSTITUTE` — Find & Replace as a formula

Sometimes you want the replacement logic to live in a formula (so it re-runs automatically if new raw rows are added), rather than a one-time manual edit. `SUBSTITUTE` is Find & Replace's formula equivalent, one substitution per call:

```
=SUBSTITUTE(SUBSTITUTE(D2, "CA", "California"), "ca", "California")
```

For **many** substitutions this nests painfully fast and a lookup table (next lecture, and Week 3's `XLOOKUP`) is the cleaner tool — build a two-column `Lookups` table of `RawValue → CleanValue` and `XLOOKUP` against it instead of chaining ten `SUBSTITUTE`s. Use `SUBSTITUTE` for one or two known, stable replacements; switch to a lookup table the moment you're tempted to nest a third.

## 5. Flash Fill (Excel) and its Google Sheets equivalents

**Flash Fill** is Excel's pattern-detection feature: type the result you want for the **first** row by hand, start typing the second, and Excel offers to auto-complete the entire column by inferring the pattern — no formula required.

Try it on `Full Name`: in a new column, type `Alvarez, Maria` for row 2 (last name, comma, first name — reshaping `"Maria Alvarez"`). Start typing `Chen, James` in row 3; Excel should show a grayed-out preview filling the rest of the column. Press `Enter` to accept, or trigger it manually any time via **Data tab → Flash Fill** (or `Ctrl+E`).

Flash Fill is genuinely useful for: splitting a full name into first/last, extracting a domain from an email, reformatting a phone number, or building an initials column — any transformation where you can demonstrate the pattern with one or two examples and let the app infer the rest. Its limits: it's a **one-time, static** operation (results are plain values, not formulas — they don't update if the source cell changes), it can guess wrong on inconsistent input, and Excel-only users on very old versions or Google Sheets don't have an identical feature.

**Google Sheets equivalents**, since Sheets has no direct Flash Fill:

- **Split by delimiter** (Data menu → **Split text to columns**) handles the comma/space-splitting case directly and non-destructively (you choose the delimiter explicitly, rather than the app guessing).
- **Formula-based extraction** is the fully portable, cross-app answer and the one to reach for when you want the result to **stay live**: `=SPLIT(B2, " ")` in Sheets spills first/last name into adjacent cells; the formula equivalent in either app is a `LEFT`/`RIGHT`/`FIND`/`MID` combination from Week 4, e.g. `=LEFT(B2, FIND(" ", B2) - 1)` for the first name.

**Rule of thumb for this course:** reach for Flash Fill/Split-to-columns for a *quick one-off* clean where you'll paste-as-values immediately anyway; reach for a formula when the raw column might still change and you want the extraction to track it automatically.

## 6. Reshaping toward one row per record

Sometimes the structural problem isn't a stray character — it's that the data isn't one-row-per-observation to begin with. Imagine a variant export where signups got pasted with **repeat customers on one row**, order amounts crammed into extra columns (`Order Amt 1`, `Order Amt 2`, `Order Amt 3`) instead of one order per row:

```
     A              B          C          D
1  Name           Order1     Order2     Order3
2  Maria Alvarez  284.50     112.00
3  James Chen     340.00
```

This violates tidy-data rule #2 directly — a "row" here represents a *customer*, but the real observation you care about is an *order*, and orders are smeared sideways across columns instead of stacked as rows. The fix is to **unpivot**: turn each `Order` column into its own row, repeating the customer name for each one:

```
     A              B
1  Name           Order Amt
2  Maria Alvarez  284.50
3  Maria Alvarez  112.00
4  James Chen     340.00
```

For a small table, do this by hand (copy each order column's values into a stacked block, with the name column repeated using a fill-down or a simple `=A2` reference copied alongside each block). For larger, real-world unpivoting, Power Query's **Unpivot Columns** transform (Week 11) automates this completely — this lecture is giving you the *concept* and the manual technique now so Week 11's automated version makes immediate sense instead of feeling like magic.

## 7. Putting it together — the cleaning order that actually works

Clean in this order, every time, and you'll avoid re-doing work:

1. **Audit first** (Lecture 1) — know exactly what's wrong before touching anything.
2. **Fix structure** — reshape to one row per observation if needed (Section 6), *before* dealing with individual values.
3. **Strip whitespace/invisible characters** (`TRIM(CLEAN(...))`) on every text column — this alone turns some near-duplicates into exact ones.
4. **Standardize categories** (Find & Replace or a lookup table) — this turns *more* near-duplicates into exact ones.
5. **Remove duplicates last** — now that values are normalized, the built-in tool catches everything, including what looked like near-duplicates in the raw file.
6. **Re-run your audit formulas** from Lecture 1 to confirm zero duplicates, zero blank rows, and one clean spelling per category remain.

```mermaid
flowchart LR
  A["Audit first"] --> B["Fix structure"]
  B --> C["Strip whitespace"]
  C --> D["Standardize categories"]
  D --> E["Remove duplicates"]
  E --> F["Re-audit"]
```
*The cleaning order that avoids re-doing work — each step turns more near-duplicates into exact ones the next step can catch.*

Run this exact sequence on `CleanSignups` now. End state: 14 data rows (both blank rows removed, the one exact and one near-duplicate collapsed to a single row each), five clean state values, four clean tier values, and every name/email trimmed.

## 8. Check yourself

- Why should Remove Duplicates usually run **last**, not first, in a cleaning sequence?
- What's the difference between what `TRIM` fixes and what `CLEAN` fixes?
- Why is "Match entire cell contents" critical when using Find & Replace on a category column?
- What's the key limitation of Flash Fill compared to a formula-based extraction?
- Rewrite the unpivoting example in Section 6 in your own words: what was wrong with the original shape, and what rule of tidy data did it violate?
- Describe the "formula, verify, paste-as-values, delete helper" cycle and why the paste-as-values step matters.

If those came quickly, move to Lecture 3 — guarding the door so this mess doesn't happen again on the next import.

## Further reading

- **Microsoft — Flash Fill:** <https://support.microsoft.com/en-us/office/using-flash-fill-in-excel-3f9bcf1e-db93-4890-94a0-1578341f73f7>
- **Google — Split text into columns:** <https://support.google.com/docs/answer/6325535>
- **Microsoft — TRIM function:** <https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9>
- **Microsoft — CLEAN function:** <https://support.microsoft.com/en-us/office/clean-function-26f3d7c5-475f-4a9c-90e5-4b8ba987ba2a>
- **Microsoft — SUBSTITUTE function:** <https://support.microsoft.com/en-us/office/substitute-function-6434944e-a904-4c7d-a3b3-e498d81c7ecf>
- **Microsoft — Find and replace text:** <https://support.microsoft.com/en-us/office/find-or-replace-text-and-numbers-on-a-worksheet-0e304ca5-4249-4a13-b74f-9a03a4ec3e6f>
