# Mini-Project — Normalize a Messy Contact + Orders Export

> Take two deliberately messy exported tables — a contact list and an order log — and normalize both completely using only this week's text and date functions: split names, standardize casing, fix phone formats, and convert text-stored dates into real dates you can sort, filter, and do math on.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

This is the week's capstone, and it's deliberately built to feel like a real onboarding task at a real company: someone hands you two exports from two different systems, neither one clean, and asks you to make them usable before Monday. Every technique from all three lectures gets used here — parsing, cleaning, joining, and date math — combined into one realistic pipeline rather than practiced in isolation.

---

## Deliverable

A workbook (new, or clearly separated sheets in `crunch-week4`) containing:

1. A `Contacts_Raw` sheet with the messy source data (below), untouched.
2. A `Contacts_Clean` sheet with fully normalized output, built with formulas that reference `Contacts_Raw`.
3. An `Orders_Raw` sheet with the messy source data (below), untouched.
4. An `Orders_Clean` sheet with fully normalized output, built with formulas that reference `Orders_Raw`.
5. A `Notes` sheet with your reflection (see the end).

**Formulas only.** Every cleaned value must be produced by a formula referencing the raw sheet — no manually retyped "corrections." If the raw data changes, your clean sheets should be able to update by re-filling the formulas down, not by you re-typing anything.

---

## Part 1 — Contacts

### Build `Contacts_Raw`

Type this exactly as shown, preserving the irregular spacing and casing:

| FullName | Email | Phone | JoinDateText |
|---|---|---|---|
|  olivia  rossi | OLIVIA.ROSSI@Crunch.io | (512) 555-0119 | '2018-06-25 |
| ANDERSON, JAMES | james.anderson@CRUNCH.io | 512.555.0120 | '2020-10-19 |
| patel, priya | Priya.Patel@Crunch.IO | 5125550121 | '2021-07-05 |
|  Sharma,  Arjun | ARJUN.SHARMA@crunch.io | 512-555-0122 | '2023-03-20 |
| brown, william | william.brown@Crunch.io | (512)555-0123 | '2014-09-15 |
| costa, isabella | ISABELLA.COSTA@crunch.io | 512 555 0124 | '2019-12-02 |

Row 1 is your header row. Note the mix: some names are `"First Last"`, some are `"Last, First"`, and casing is inconsistent throughout — this is the realistic part; a real export very often mixes conventions row to row because it was assembled from more than one source system.

### Build `Contacts_Clean`

Produce these columns, each formula-driven from `Contacts_Raw`:

- **`FirstName`, `LastName`** — correctly split regardless of whether the source was `"First Last"` or `"Last, First"` format. *(Hint: use `IF` combined with `SEARCH`/`ISNUMBER` to detect whether a comma is present in the cell, and branch your splitting logic accordingly — this is the hardest single piece of the mini-project; budget real time for it.)*
- **`FullNameClean`** — rebuilt as `"First Last"`, Title Case, from your split `FirstName`/`LastName`, using `TEXTJOIN` or `&`.
- **`EmailClean`** — lowercase, trimmed.
- **`PhoneClean`** — digits-only, 10 characters.
- **`PhoneFormatted`** — `(XXX) XXX-XXXX` display format, built from `PhoneClean`.
- **`JoinDate`** — a real date, converted from `JoinDateText` with `DATEVALUE`.
- **`TenureYears`** — complete years since `JoinDate`, computed with `DATEDIF` against `TODAY()`.

## Part 2 — Orders

### Build `Orders_Raw`

Type this exactly as shown:

| OrderRef | CustomerEmail | OrderDateText | Amount |
|---|---|---|---|
| ord-2026-0142 | olivia.rossi@crunch.io | '01/15/2026 | 249.99 |
| ORD-2026-0187 | james.anderson@crunch.io | '02/28/2026 | 89.50 |
| Ord-2026-0203 | priya.patel@crunch.io | '03/31/2026 | 512.00 |
| ord-2026-0256 | arjun.sharma@crunch.io | '06/30/2026 | 34.75 |
| ORD-2026-0301 | william.brown@crunch.io | '09/01/2026 | 178.20 |
| ord-2026-0344 | isabella.costa@crunch.io | '12/01/2026 | 63.40 |

Row 1 is your header row. `OrderRef` has inconsistent casing on the `ord`/`ORD` prefix; `OrderDateText` is stored as text in `MM/DD/YYYY` format (a common CSV export quirk — note this is a *different* text-date shape than `Contacts_Raw` used, on purpose, since real exports rarely agree with each other).

### Build `Orders_Clean`

Produce these columns, formula-driven from `Orders_Raw`:

- **`OrderRefClean`** — uppercase, consistent (`ORD-2026-0142` style for every row).
- **`OrderYear`, `OrderMonth`** — pulled from a correctly-parsed real date (you'll need `DATEVALUE` — note `MM/DD/YYYY` still parses correctly with `DATEVALUE` in both apps as long as your locale expects that date order; if it doesn't, use `DATE(VALUE(RIGHT(text,4)), VALUE(LEFT(text,2)), VALUE(MID(text,4,2)))` to build the date manually from the known fixed positions instead).
- **`OrderDate`** — the real date value itself.
- **`FiscalPeriodLabel`** — using the fiscal-year logic from Challenge 2 (fiscal year starts July 1), a label like `"FY2026-FQ3"` built with `TEXT`/`&` from your parsed `OrderDate`.
- **`AmountFormatted`** — the `Amount` value formatted as currency text with `TEXT`, e.g., `"$249.99"`.

### Join the two clean tables

In `Orders_Clean`, add one more column, **`CustomerName`** — look up each order's customer name from `Contacts_Clean` using `XLOOKUP` (Week 3) matching on email. This is the payoff of cleaning both tables the same way: the `XLOOKUP` only works because `CustomerEmail` in `Orders_Raw` and `EmailClean` in `Contacts_Clean` are now in the **identical** lowercase, trimmed format — an uncleaned lookup here would silently fail to match rows where casing or whitespace differed.

---

## Milestones

- **Milestone 1 (45 min):** `Contacts_Raw` entered; `FirstName`/`LastName` split logic working for both name formats.
- **Milestone 2 (30 min):** Remaining `Contacts_Clean` columns (email, phone, join date, tenure) complete.
- **Milestone 3 (30 min):** `Orders_Raw` entered; date parsing and `OrderRefClean` working.
- **Milestone 4 (30 min):** `FiscalPeriodLabel` and `AmountFormatted` complete.
- **Milestone 5 (20 min):** `CustomerName` lookup working and matching all 6 rows correctly.
- **Milestone 6 (15 min):** `Notes` reflection.

---

## Rules

- **No manual corrections.** Every cleaned cell must trace back to a formula referencing the raw sheet.
- **The name-split logic must handle both formats** present in `Contacts_Raw` — a formula that only works for one format and silently mishandles the other does not meet the bar.
- **The cross-table `XLOOKUP` must succeed for all 6 rows** — if any row fails to match, your cleaning wasn't consistent between the two tables; go back and fix the mismatch rather than patching the lookup.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|---------------------|
| Name splitting | 25% | Correctly handles both `"First Last"` and `"Last, First"` with one robust formula pattern |
| Text cleaning | 20% | Email, phone, and casing fully normalized and consistent across every row |
| Date conversion | 20% | Both text-date formats correctly converted to real, sortable dates |
| Fiscal labeling | 15% | `FiscalPeriodLabel` correct for every row, verified by hand against at least 2 |
| Cross-table lookup | 15% | All 6 `CustomerName` lookups succeed with no `#N/A` |
| Formula discipline | 5% | No manually retyped "corrections" anywhere in either `_Clean` sheet |

---

## Reflection (`Notes` sheet, ~200 words)

1. Which single formula in this project took the most iterations to get right, and what was the specific bug each iteration fixed?
2. Describe, concretely, why the cross-table `XLOOKUP` at the end would have failed if you'd cleaned `Contacts` and `Orders` with even slightly different casing/trimming rules.
3. `Contacts_Raw` and `Orders_Raw` used two *different* text-date formats. What real-world situation does that simulate, and why is it realistic rather than an artificial complication?
4. If you had 50,000 rows instead of 6, which part of this pipeline would you be most worried about silently getting wrong at scale, and how would you spot-check it?

---

## Why this matters

Nearly every dataset you'll touch professionally arrives shaped like this week's raw sheets — not like the clean seed tables from Weeks 1–3. The specific skill of turning "technically has the information, technically unusable" into "clean, joinable, sortable, trustworthy" is one of the highest-leverage things a spreadsheet person can do, because it's the gate every other analysis has to pass through first. Keep both clean sheets — you'll build on exactly this kind of normalized data in Week 5, when the focus shifts from *fixing* messy data to *preventing* it from getting messy in the first place.

When done: push/save your work, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-04-text-and-date-functions/quiz.md) and start [Week 5 — Data cleaning & validation](../../week-05-data-cleaning-and-validation/).
