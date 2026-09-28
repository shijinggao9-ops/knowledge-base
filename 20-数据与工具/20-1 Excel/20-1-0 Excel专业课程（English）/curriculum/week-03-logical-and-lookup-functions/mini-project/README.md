# Mini-Project — Grade a Class & Price-Match a Catalog

> Build one workbook, two independent deliverables: a gradebook that assigns letter grades and honor-roll status with `IF`/`IFS`/`AND`/`OR`, and a product catalog matched against a master price list with `XLOOKUP` and graceful fallbacks for anything that doesn't match.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone. Both parts are things you'll build for real, more than once, outside this course: a gradebook is the canonical `IF`/`IFS` exercise because everyone understands score → letter grade intuitively; a price-match is the canonical lookup exercise because "does this row from list A match a row in list B, and what happens when it doesn't" is the single most common cross-table problem in business spreadsheets. Ship both cleanly and you've proven you can branch logic **and** find things — this week's whole point.

---

## Deliverable

One workbook (`crunch-week3-miniproject.xlsx` or a Google Sheet), with these sheets:

1. **`Gradebook`** — Part 1's data and formulas.
2. **`MasterPriceList`** and **`Catalog`** — Part 2's data and formulas.
3. **`Summary`** — a short written summary (see the end).

---

## Part 1 — Grade a class (Sections A–B)

### A. Build the gradebook

Create 12 students with `Name`, three test scores (`Test1`, `Test2`, `Test3`, each 0–100), and `Attendance` (a decimal fraction, 0–1). Invent realistic, varied data — include at least: one student who'd fail on scores alone, one with perfect attendance but a mediocre average, one right at a grade-boundary value (e.g., exactly 80 or 89.5), and one with genuinely excellent everything.

### B. Required formulas

1. **`Average`** — the mean of the three test scores, rounded to 1 decimal place (`ROUND`, from Week 2).
2. **`Letter Grade`** — using `IFS` on `Average`: `90+` → `A`, `80+` → `B`, `70+` → `C`, `60+` → `D`, else `F`. State your boundary rule (inclusive at the floor of each tier) in `Summary`.
3. **`Honor Roll`** — `"Yes"` if `Average >= 90` **AND** `Attendance >= 0.90`, else `""`. Use `AND` explicitly.
4. **`Academic Concern`** — `"Flag"` if `Average < 65` **OR** `Attendance < 0.75`, else `""`. Use `OR` explicitly.
5. **`Status Summary`** — one formula combining the above into a single readable string per student, e.g., `"B — Honor Roll"` or `"D — Flag"` or just `"C"` if neither applies. (Hint: nested `IF`s checking `Honor Roll`/`Academic Concern` first, falling back to just the letter grade, combined with `&`.)

**Verify:** every one of your boundary-value students lands in the tier you intended — hand-check at least 2 of them against your formula's output before moving on.

---

## Part 2 — Price-match a product catalog (Sections C–D)

### C. Build the master price list and catalog

**`MasterPriceList`** — 10 products: `SKU`, `Product`, `Category`, `Price`, `InStock`. Reuse/extend the `PriceList` sheet from this week's lectures if you like, expanded to 10 rows.

**`Catalog`** — a separate "what a customer is browsing" list of 12 SKUs, `SKU` and `RequestedQty` only. **Deliberately include 2–3 SKUs that don't exist in `MasterPriceList`** (typos or discontinued items) — this is the point of the fallback logic below, not an accident to avoid.

### D. Required formulas (in `Catalog`)

1. **`Product Name`** — `XLOOKUP` against `MasterPriceList`, fallback `"Unknown SKU"`.
2. **`Unit Price`** — `XLOOKUP` against `MasterPriceList`, fallback `0`.
3. **`In Stock`** — `XLOOKUP` against `MasterPriceList`, fallback `0`.
4. **`Line Total`** — `RequestedQty * Unit Price`.
5. **`Availability`** — `IFS`: `"No match"` if the SKU wasn't found (use a helper `ISNA`/lookup check, not just "stock is 0" — Exercise 2 showed you why those two aren't the same thing), `"Out of stock"` if found but `InStock = 0`, `"Low stock"` if `InStock` is 1–10, `"Available"` otherwise.
6. **Grand total** — a single cell below the table, `SUM` of `Line Total`, excluding unmatched SKUs from distorting the total (they should already compute to `0`, confirm this rather than assume it).

**Verify:** your 2–3 deliberately-broken SKUs show `"Unknown SKU"` / `0` / `"No match"` cleanly — no `#N/A` visible anywhere in the sheet.

---

## Section E — Written summary (`Summary` sheet, ~150 words)

1. State your grade-boundary rule from Part 1B(2).
2. Which of the two parts (gradebook branching, or catalog lookup) took longer to get right, and what specifically tripped you up?
3. In the catalog, explain the difference between "SKU not found" and "SKU found but out of stock" — and why `Availability` needed a genuine not-found check instead of just testing `InStock = 0`.
4. One thing you'd change if this workbook needed to scale to 500 products instead of 10 (a hint toward Week 6's Tables, if you want to look ahead).

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 35% | All formulas produce the right value for every row, including deliberately-planted edge cases |
| Logical branching (Part 1) | 20% | `IF`/`IFS`/`AND`/`OR` used correctly and legibly; boundary rule stated and consistently applied |
| Lookup + error handling (Part 2) | 25% | `XLOOKUP` used correctly with real fallbacks; not-found genuinely distinguished from out-of-stock |
| Readability | 10% | Formulas and headers a stranger could follow without you narrating |
| Written summary | 10% | Answers all four prompts specifically, not generically |

---

## Stretch goals

- Rebuild the `Availability` not-found check and at least one `Catalog` lookup using `INDEX`/`MATCH` instead of `XLOOKUP`, and confirm identical output — proof you can move between the two tools.
- Add a `Discount` column to `Catalog`: 5% off any line where `RequestedQty >= 10`, applied to `Line Total`.
- In `Gradebook`, add a `Rank` column using `RANK` (a new function — look up its syntax) ordering students by `Average`, highest first.

---

## Why this matters

Grading and price-matching look like two unrelated toy problems, but they're the same underlying skill twice: read a value, decide something about it (branch), or find a related value elsewhere (lookup), and handle the case where the "obvious" answer doesn't exist. That pattern — branch, look up, handle the miss — is underneath almost every spreadsheet you'll build for the rest of this course, from Week 5's data validation through Week 9's financial models. Keep this workbook; Week 4 builds directly on the habit of clean, defaulted, error-trapped formulas you practiced here.

When done: push, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-03-logical-and-lookup-functions/quiz.md) and start [Week 4 — Text & date functions](../../week-04-text-and-date-functions/).
