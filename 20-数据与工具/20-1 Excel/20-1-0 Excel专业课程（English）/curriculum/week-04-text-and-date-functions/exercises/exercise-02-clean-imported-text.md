# Exercise 2 — Clean Imported Text Fields

**Goal:** Take a deliberately messy imported table — extra spaces, inconsistent casing, and phone numbers in several formats — and clean every field with formulas: `TRIM`, `CLEAN`, `SUBSTITUTE`, `UPPER`/`LOWER`/`PROPER`, and `TEXTJOIN`.

**Estimated time:** 1.5 hours.

## Setup

Add a new sheet, rename it `Exercise 2`.

## Part A — Enter the messy data

Type this **exactly as shown**, including the irregular spacing (double spaces, leading spaces) — do not "fix" anything while typing:

| RawCompany | RawContact | RawEmail | RawPhone |
|---|---|---|---|
|  crunch  worldwide | maria  santos | MARIA.SANTOS@Crunch.io | (415) 555-0142 |
| ACME CORP | John O'Brien | john.obrien@ACME.com | 415.555.0187 |
| bright path llc |  DAVID  chen | David.Chen@BrightPath.io | 4155550199 |
| Nova Retail Group | priya desai | PRIYA.DESAI@novaretail.com | 415-555-0163 |
| summit consulting | Ethan  Wright | ethan.wright@Summit.Co | (415)555-0121 |

Row 1 is your header row.

## Part B — Clean the company and contact names

In `F1`/`G1`, add headers `CleanCompany` and `CleanContact`. In `F2`:

```
=PROPER(TRIM(CLEAN(A2)))
```

In `G2`:

```
=PROPER(TRIM(CLEAN(B2)))
```

Fill both down through row 6. Check `G3` specifically — `"John O'Brien"` should read `"John O'brien"` after `PROPER` (the known limitation from Lecture 2). Leave it as-is for this exercise; you'll handle the fix explicitly in Part E.

## Part C — Clean the email

In `H1`, add header `CleanEmail`. In `H2`:

```
=LOWER(TRIM(CLEAN(C2)))
```

Fill down through row 6. Every email should now be fully lowercase with no stray whitespace.

## Part D — Normalize the phone number to digits-only

In `I1`, add header `CleanPhone`. Strip every non-digit character using chained `SUBSTITUTE` calls, then `TRIM`:

```
=TRIM(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(D2, "(", ""), ")", ""), "-", ""), ".", ""))
```

Fill down through row 6. Every result should be a 10-digit string with no punctuation or spaces (`4155550142`, `4155550187`, etc.). Row 3's `4155550199` should come out unchanged since it had no punctuation to strip.

## Part E — Fix the PROPER/O'Brien problem explicitly

In `J1`, add header `FixedContact`. Layer a targeted `SUBSTITUTE` on top of your `CleanContact` column (`G`, from Part B) to correct the one known casing bug:

```
=SUBSTITUTE(G2, "O'brien", "O'Brien")
```

Fill down through row 6 — rows without `"O'brien"` in them pass through completely unchanged, since `SUBSTITUTE` only touches the exact match.

## Part F — Build a formatted phone display

In `K1`, add header `FormattedPhone`. Using your `CleanPhone` (digits-only) column, rebuild a standard `(XXX) XXX-XXXX` display using `LEFT`/`MID`/`RIGHT` and `TEXTJOIN` or `&`:

```
="(" & LEFT(I2, 3) & ") " & MID(I2, 4, 3) & "-" & RIGHT(I2, 4)
```

Fill down through row 6. Every row should now display in the identical `(415) 555-0142` style, regardless of how it was originally formatted.

## Expected result

- `CleanCompany`/`CleanContact`: consistent Title Case, no extra spaces.
- `CleanEmail`: fully lowercase, trimmed.
- `CleanPhone`: 10 digits only, no punctuation, for all 5 rows.
- `FixedContact`: `"John O'Brien"` correctly capitalized; all other rows unchanged from `CleanContact`.
- `FormattedPhone`: identical `(XXX) XXX-XXXX` format across all 5 rows, despite 4 different input formats.

## Done when…

- [ ] All 5 rows entered with the messy spacing/casing preserved exactly as given.
- [ ] Every cleaning formula references the *raw* column, not a previously-cleaned column that itself was manually retyped.
- [ ] `CleanPhone` is exactly 10 digits for every row (spot-check with `=LEN()`).
- [ ] `FixedContact` correctly shows `"John O'Brien"`.
- [ ] `FormattedPhone` is visually identical in format across all rows.

## Stretch

- Add a 6th row where `RawPhone` includes a leading `"1-"` country code (e.g., `"1-415-555-0175"`). Does your `CleanPhone` formula still produce exactly 10 digits? If not, extend it (hint: `SUBSTITUTE` the leading `"1-"` first, or use `RIGHT(..., 10)` on the digits-only result to always take just the last 10).
- Write one formula that produces a single `TEXTJOIN`-built mailing label combining `CleanCompany`, `FixedContact`, and `FormattedPhone` on one line, separated by ` — `.

## Submission

Keep this sheet in your workbook — the mini-project reuses this exact cleaning pipeline on a larger dataset.
