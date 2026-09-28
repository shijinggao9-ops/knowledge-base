# Exercise 1 — Dedupe a Customer List

**Goal:** Take a fresh, messier customer list and dedupe it completely — catching both exact duplicates and near-duplicates — using the audit-then-clean sequence from Lectures 1 and 2.

**Estimated time:** 45 minutes.

## Setup

Add a new sheet named `Ex1-Dedupe`. Type this raw list in **exactly as shown**, whitespace and casing included:

```
     A          B                  C                        D
1  CustID     Full Name          Email                    Phone
2  2001       Rachel Green       rachel.green@mail.com    555-201-4471
3  2002        Ross Geller       ross.geller@mail.com      555-201-4472
4  2003       Monica Geller      monica.geller@mail.com   555-201-4473
5  2004       Rachel Green       rachel.green@mail.com    555-201-4471
6  2005       Chandler Bing      chandler.bing@mail.com   555-201-4474
7  2006       Joey Tribbiani     joey.tribbiani@mail.com  555-201-4475
8  2007       ross geller        ross.geller@mail.com     555-201-4472
9  2008       Phoebe Buffay      phoebe.buffay@mail.com   555-201-4476
10 2009       Chandler bing      chandler.bing@mail.com    555-201-4474
11 2010       Monica Geller      MONICA.GELLER@MAIL.COM   555-201-4473
12
13 2011       Gunther Centralperk gunther.c@mail.com       555-201-4477
14 2012       Rachel Green        rachel.green@mail.com    555-201-9999
15 2013       David Scientist    david.scientist@mail.com 555-201-4478
```

Note what you're looking at before you touch anything:

- Row 5 is an **exact duplicate** of row 2 (same everything, including `CustID` pattern — actually a different `CustID`, but identical name/email/phone, which is the part that matters for "is this the same customer").
- Row 8 is a **near-duplicate** of row 3 (`ross geller` lowercase vs `Ross Geller`).
- Row 10 is a **near-duplicate** of row 4 (`Chandler bing` vs `Chandler Bing`, one letter's casing differs).
- Row 11 is a **near-duplicate** of row 3 (name matches exactly, but email is `MONICA.GELLER@MAIL.COM` in all caps).
- Row 12 is a genuinely blank spacer row.
- Row 14 is a **partial** near-duplicate of row 2 — same name and email, but a **different phone number** (`555-201-9999` vs `555-201-4471`). This one is a judgment call: is it the same person with an updated phone, or two different people who happen to share a name and email? You'll need to decide and document it.

## Tasks

1. **Audit first.** Build a helper column using the normalized-key technique from Lecture 1, Section 5 (`LOWER(TRIM(...))` on name + email, joined). Flag every row whose key has appeared before, using the `COUNTIF` growing-range pattern.

2. **Count the flags.** How many rows does your audit flag as a duplicate-of-something-earlier? Write the number down before moving on — you'll check your final row count against it.

3. **Decide on row 14.** Read the note above about the phone-number conflict. Write one sentence stating your decision (keep it as a separate customer, treat it as an update and keep only the newer phone, or something else) — there's no single correct answer, but you must be explicit about which you chose and why.

4. **Remove the blank row.** Delete row 12 (or use `COUNTA`/`TRIM`-based blank-row detection from Lecture 1 to find it programmatically first, then delete).

5. **Standardize casing before deduping.** Apply `PROPER()` (title-case function — covered in Week 4, but usable here: `=PROPER(B2)` capitalizes the first letter of each word) to the `Full Name` column and `LOWER()` to the `Email` column, via the formula → verify → paste-as-values cycle from Lecture 2.

6. **Run Remove Duplicates.** Now that casing is standardized, run the built-in Remove Duplicates tool checking **Full Name + Email** as the match columns. Confirm it reports the correct number removed.

7. **Re-audit.** Re-run your Task 1 formula against the cleaned result. It should now flag **zero** rows.

## Expected result

- Starting rows: 13 data rows (2001–2013, minus the blank row 12 which isn't a data row).
- After cleaning: **10 unique customers** remain, assuming you treated row 14 (the phone conflict) as the same customer as row 2 and kept one record. If you instead decided row 14 represents a genuinely different situation and kept it separate, you should have **11** — either is acceptable as long as Task 3's written decision matches your final count.
- `Gunther Centralperk` (row 13) and `David Scientist` (row 15/13-original) have no duplicates anywhere and should survive unchanged.

## Done when…

- [ ] Your normalized-key audit formula correctly flags rows 5, 8, 10, and 11 as duplicates of an earlier row (and does **not** flag row 14, since its email domain-and-user match but you're evaluating the phone-conflict on its own terms per Task 3).
- [ ] Task 3's written decision is present and your final row count matches it.
- [ ] `Full Name` is consistently title-cased and `Email` is consistently lowercase across every surviving row.
- [ ] Remove Duplicates was run **after** standardizing casing, not before.
- [ ] Re-running the audit formula on the final result returns zero flags.

## Stretch

- Add a second normalized-key column keyed on `Phone` alone (normalize by stripping non-digit characters with `SUBSTITUTE` chained three times, once per `-`). Does phone-based deduping agree with name/email-based deduping, or does it surface a case your first pass missed?
- Write one sentence: if this list had 50,000 rows instead of 13, which of today's techniques would still work by hand, and which would become impractical? (Foreshadows Power Query, Week 11.)

## Submission

Commit your cleaned `Ex1-Dedupe` sheet (or a CSV export of it) plus your one-sentence Task 3 decision to your portfolio under `c41-week-05/exercise-01/`.
