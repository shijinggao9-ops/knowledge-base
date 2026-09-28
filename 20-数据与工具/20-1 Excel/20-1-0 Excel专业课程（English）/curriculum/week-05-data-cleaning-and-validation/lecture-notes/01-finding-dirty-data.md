# Lecture 1 — Finding Dirty Data

> **Duration:** ~2 hours. **Outcome:** You can look at a raw dataset and name its specific quality problems — exact duplicates, near-duplicates, blank/whitespace-only rows, inconsistent category spellings, and type mismatches — using formulas that surface each problem instead of eyeballing 2,000 rows. You can also explain what "tidy data" means and why it's the target every cleaning technique this week is aiming at.

## 1. Why this week exists

Every week so far handed you data that was already usable — clean column headers, one value per cell, consistent types. That was deliberate scaffolding, and it's over. In the real world, data arrives from a CRM export, a Google Form, a vendor's CSV, or a coworker's "quick copy-paste from the other sheet," and it is never clean on arrival. It has duplicate rows because someone double-submitted a form. It has `"NY"` next to `"New York"` next to `"ny "` (note the trailing space) because three different people typed it over two years. It has a date column that's half real dates and half text that merely *looks* like a date.

None of this is a formula problem. `SUMIF`, `XLOOKUP`, `IF` — all of Weeks 2–4 — silently produce **wrong answers** on dirty data, with no error, no warning. `SUMIF(State, "NY", Sales)` quietly ignores every row where someone typed `"new york"` in lowercase or left a trailing space. The formula isn't broken; the data is, and the formula has no way to know. Cleaning is not optional busywork before "the real work" — it *is* the real work, because a wrong number that looks confident is worse than an obvious error.

Build the raw sheet now — you'll audit and clean this exact data through the rest of the week.

## 2. Build `RawSignups` — type this in exactly as shown

Open the `RawSignups` sheet from your Week 5 workbook. Type the following **exactly as written**, including the inconsistent casing and any leading/trailing spaces you see — that messiness is the lesson. (A trailing space after `CA ` is invisible in print but very real in a cell; type a literal space where you see one.)

```
     A          B                  C                          D              E        F              G
1  CustID     Full Name          Email                      State          Tier     Signup Date    Order Amt
2  1001       Maria Alvarez      maria.alvarez@mail.com     CA             Gold     3/4/2025       284.50
3  1002       James Chen         james.chen@mail.com        California     gold     2025-03-04      284.50
4  1003        Priya Nair        priya.nair@mail.com        NY             Silver   03/09/2025     112.00
5  1004       Tom O'Brien        tom.obrien@mail.com        ny             silver   3/9/25          112
6  1005       Sara Kim           sara.kim@mail.com          TX             GOLD     3/15/2025      340.00
7  1006       Sara Kim           sara.kim@mail.com          TX             Gold     3/15/2025      340.00
8
9  1007       Dan Whitfield      dan.whitfield@mail.com      Texas          Bronze   3/18/2025      45.00
10 1008       Ana Souza          ana.souza@mail.com          WA             silver   3/20/2025      98.25
11 1009       Ana souza          ana.souza@mail.com          Washington     Silver   3/20/2025      98.25
12 1010       Kevin Park         KEVIN.PARK@MAIL.COM         wa             Bronze   3/22/2025      67.00
13
14 1011       Grace Liu          grace.liu@mail.com          FL             platinum 3/25/2025      510.00
15 1012       Omar Haddad        omar.haddad@mail.com        Florida        Platinum 3/25/2025      510
16 1013       Nina Volkov                                    CA              Gold    3/29/2025      199.00
17 1014       Ben Fischer        ben.fischer@mail.com        ca             Gold     3/29/2025      199.00
```

A few things to notice as you type, because noticing *is* the skill this lecture builds:

- Row 8 and row 13 are **completely blank** — spacer rows nobody meant to leave, or an artifact of how the export was generated.
- Rows 2–3 are the **same person** (Maria Alvarez / James Chen are different people, ignore that — look at rows 5–6 instead: Sara Kim appears **twice**, identical in every column). That's an **exact duplicate**.
- Rows 8 and 9 (Ana Souza / Ana souza) are the **same person** with a casing difference in the name and `WA` vs `Washington` in state — a **near-duplicate**, not exact.
- Row 16 (Nina Volkov) has a **blank email** — a missing value, not a duplicate or formatting problem, but still something an audit needs to catch.
- The `State` column has three spellings each for California and New York/Washington/Texas/Florida: postal code, full name, and inconsistent casing.
- The `Tier` column has `Gold`, `gold`, `GOLD` — same value, three casings.
- The `Signup Date` column mixes `3/4/2025`, `2025-03-04` (which most spreadsheet apps will auto-parse as a real date, but verify it lands in the same column type as the others), and `3/9/25` (2-digit year).
- The `Order Amt` column mixes `284.50` (two decimals) with `112` (no decimals) — same underlying type, cosmetically different, worth normalizing for display consistency even though the math still works.

## 3. What "tidy data" means

Before fixing anything, you need a target to fix *toward*. The data-science term for a well-structured table is **tidy data**, and it has exactly three rules:

1. **Each variable is a column.** `State` is one column, not smeared across `City, State` in a single cell.
2. **Each observation is a row.** One customer signup is one row — not spread across two rows, and not two signups crammed into one row.
3. **Each value is atomic** — one piece of information per cell. A cell holding `"Maria Alvarez, CA, Gold"` violates this even though it's technically "one cell"; it's really three variables jammed together.

`RawSignups` mostly follows this shape already (that's why it's a reasonable starting point) but violates it in spirit through inconsistency: `"CA"` and `"California"` are meant to be the *same value* of the *same variable*, but as typed they're two different strings, which breaks every formula that groups, filters, or counts by state. **Tidy data isn't just about shape — it's about every occurrence of the same real-world value being spelled identically.** That second half is what most of this week is actually about.

```mermaid
flowchart TD
  A["Row in RawSignups"] --> B{"COUNTA/TRIM = 0?"}
  B -->|Yes| C["Blank row"]
  B -->|No| D{"Exact match on Name+Email+State?"}
  D -->|Yes| E["Exact duplicate"]
  D -->|No| F{"Normalized key matches another row?"}
  F -->|Yes| G["Near-duplicate"]
  F -->|No| H{"ISNUMBER on date/amount?"}
  H -->|No| I["Type mismatch"]
  H -->|Yes| J["Passes audit"]
```
*The audit sequence in Sections 4–8: each row gets checked against these questions in order before it's trusted.*

## 4. Auditing for exact duplicates

The fastest way to *see* duplicates before you touch Remove Duplicates (next lecture) is to flag them with a formula, so you can inspect what you're about to delete rather than trusting a dialog blindly.

In a scratch column (say `I2`), flag whether the whole row is a duplicate of an **earlier** row:

```
=COUNTIFS($B$2:B2, B2, $C$2:C2, C2, $D$2:D2, D2) > 1
```

Fill down. This counts how many times the combination of Name+Email+State has appeared **from the top of the range down through the current row** — the classic "growing range" trick (notice the anchor `$B$2` stays fixed while `B2` shifts as you fill down). The **first** occurrence of a duplicate shows `1` (not a dupe *yet*, from this row's point of view); the **second and later** occurrences show `TRUE`, correctly flagging them as the copies to remove, while leaving the original in place.

Run it and confirm: rows 5 and 6 (both Sara Kim, TX, Gold) — row 6 should flag `TRUE`, row 5 should not.

## 5. Auditing for near-duplicates

Exact-duplicate detection misses rows 8 and 9 entirely, because `"Ana Souza"` ≠ `"Ana souza"` as raw strings, and `"WA"` ≠ `"Washington"`. This is the harder, more common real-world case: two rows that a human instantly recognizes as the same customer, but a computer sees as unrelated text.

Build a **normalized comparison key** — a helper column that strips out exactly the kind of noise (casing, whitespace) that shouldn't count as a real difference:

```
=LOWER(TRIM(B2)) & "|" & LOWER(TRIM(E2))
```

This lowercases and trims the name and email, joins them with a separator, and gives you a key that's identical for true duplicates regardless of casing or stray spaces. Fill this into a helper column (say `J`), then reuse the Section 4 pattern against **this** column instead of the raw one:

```
=COUNTIF($J$2:J2, J2) > 1
```

Now rows 8 and 9 both resolve to the same normalized key and row 9 flags correctly. **This is the general technique for near-duplicate detection: normalize first (strip the noise you don't care about), then compare.** You'll use exactly this pattern again in Exercise 1 and the mini-project, on messier real data.

## 6. Auditing for blank and whitespace-only rows

A row that's genuinely empty is easy to spot by eye in a 16-row sheet; it's invisible in a 4,000-row one. Flag every row where the "identifying" columns are empty:

```
=COUNTA(A2:G2) = 0
```

`COUNTA` counts non-blank cells in the range; if it's `0`, the entire row is empty. But watch out for the sneakier cousin: a row that *looks* blank but actually contains a single space character (someone hit the spacebar instead of leaving the cell alone). `COUNTA` treats a lone space as non-blank — it **will not** catch that case, which is exactly why the next lecture's `TRIM`/`CLEAN` matters even on cells that look empty. A more thorough check:

```
=SUMPRODUCT(--(TRIM(A2:G2)<>""))=0
```

This trims every cell in the row first, then counts how many are non-empty *after* trimming — catching whitespace-only rows that `COUNTA` alone would miss.

## 7. Auditing for inconsistent categories

For a categorical column like `State` or `Tier`, the fastest audit isn't a formula per row — it's a **frequency count** of every distinct value that currently exists, so you can see the fragmentation at a glance. Build this in a fresh scratch area:

```
=UNIQUE(D2:D17)
```

(`UNIQUE` is a modern dynamic-array function — full coverage in Week 10 — but it's genuinely useful *now* for exactly this kind of audit, so we're borrowing it a few weeks early. If your app doesn't have `UNIQUE` yet, skip to a plain `COUNTIF` per known value instead.) Spill this into a column and next to each result run:

```
=COUNTIF($D$2:$D$17, I2)
```

For `State` this reveals the fragmentation immediately: `CA` (2), `California` (1), `NY` (1), `ny` (1), `TX` (2), `Texas` (1), `WA` (1), `wa` (1), `FL` (1), `Florida` (1), `ca` (1) — eleven distinct spellings representing what should be **six actual states**. That gap between "distinct strings" and "distinct real-world values" is the single most common data-quality problem you'll fix this week, and this frequency-count technique is how you *discover* the gap before you fix it.

## 8. Auditing for type mismatches

A column that's supposed to be uniformly dates or uniformly numbers sometimes has a few cells that are secretly **text** — usually because they were pasted from another system, or typed in a format the app didn't recognize as a real date/number on entry. Text-that-looks-like-a-number breaks `SUM`; text-that-looks-like-a-date breaks date math and sorts wrong (alphabetically instead of chronologically).

The tell: a genuine number or date is **right-aligned** by default; text is **left-aligned** by default. Scan a column visually first — a left-aligned value sitting in a column of right-aligned numbers is a type mismatch, full stop. To check it formulaically instead of relying on eyesight:

```
=ISNUMBER(G2)          -- TRUE for a real number, FALSE if G2 is secretly text
=ISNUMBER(F2)           -- TRUE only if F2 is a real date value, not date-shaped text
```

Run `ISNUMBER` down the `Signup Date` column. If `3/9/25` parsed correctly it returns `TRUE` (dates are numbers underneath, per Week 1); if any date entry got treated as literal text (common with 2-digit years or unusual regional formats), it returns `FALSE` and you've found your mismatch before it silently breaks a chronological sort or a `DATEDIF` in a later week.

## 9. Check yourself

- Name the three rules of tidy data, in your own words.
- What's the difference between an exact duplicate and a near-duplicate, and why does `Remove Duplicates` (next lecture) only catch one of them reliably?
- Why does `COUNTA` fail to catch a whitespace-only "blank" row, and what formula fixes that?
- Write the normalized-key formula for detecting near-duplicates on a `Name` + `Phone` pair instead of `Name` + `Email`.
- How can you tell, without a formula, whether a cell holding what looks like a date is actually stored as a real date or as text?
- In `RawSignups`, how many *distinct real-world states* exist versus how many *distinct strings* currently represent them?

If those came quickly, move to Lecture 2 — turning everything you just found into an actual clean dataset.

## Further reading

- **Wickham, "Tidy Data" (the paper that coined the term):** <https://vita.had.co.nz/papers/tidy-data.pdf>
- **Microsoft — Find and remove duplicates:** <https://support.microsoft.com/en-us/office/find-and-remove-duplicates-00e35bea-b46a-4d5d-b28e-66a552dc138d>
- **Google — Remove duplicate rows in Google Sheets:** <https://support.google.com/docs/answer/9532984>
- **Microsoft — COUNTA function:** <https://support.microsoft.com/en-us/office/counta-function-7dbe4c6e-cdb0-40ec-a34e-8e0d8c5b8ce1>
- **Microsoft — UNIQUE function:** <https://support.microsoft.com/en-us/office/unique-function-c5ab87fd-30a3-4ce9-9d1a-40204fb85e1e>
