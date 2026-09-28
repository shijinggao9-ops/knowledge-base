# Exercise 3 — Age & Tenure Date Math

**Goal:** Given a small roster of birth dates and hire dates — some stored as real dates, some stored as text imported from a CSV — compute exact ages, tenures, and next-anniversary dates, correctly handling the real-date-vs-text-date trap.

**Estimated time:** 1.5 hours.

## Setup

Add a new sheet, rename it `Exercise 3`.

## Part A — Enter the data

Starting at `A1`, type this data exactly as shown. **Important:** enter `BirthDateText` and `HireDateText` (columns D and E) with a **leading apostrophe** (`'2026-01-15`) so your app stores them as literal text, not real dates — this is deliberate, simulating a CSV import where dates arrive as text.

| Name | BirthDate | HireDate | BirthDateText | HireDateText |
|---|---|---|---|---|
| Noah Silva | 1997-03-22 | 2022-02-14 | '1997-03-22 | '2022-02-14 |
| Emma Schmidt | 1998-06-30 | 2023-01-09 | '1998-06-30 | '2023-01-09 |
| Arjun Sharma | 1999-02-28 | 2023-03-20 | '1999-02-28 | '2023-03-20 |
| Isabella Costa | 1990-07-19 | 2019-12-02 | '1990-07-19 | '2019-12-02 |
| Lucas Meyer | 1993-10-03 | 2021-04-12 | '1993-10-03 | '2021-04-12 |

Row 1 is your header row. `BirthDate` and `HireDate` should be right-aligned (real dates); `BirthDateText` and `HireDateText` should be left-aligned (text) — confirm this before continuing. If any column landed the wrong way, fix your entry method and re-type it.

## Part B — Fix the text-dates

In `F1`/`G1`, add headers `BirthDateFixed` and `HireDateFixed`. Convert the text columns back into real dates:

```
F2: =DATEVALUE(D2)
G2: =DATEVALUE(E2)
```

Fill both down through row 6. Confirm both new columns are right-aligned (real dates now). Confirm `F2` equals `B2` and `G2` equals `C2` with a quick check formula in `H2`: `=AND(F2=B2, G2=C2)` — should read `TRUE` for every row.

## Part C — Compute exact age in years

In `I1`, add header `AgeYears`. Compute each person's current age in complete years using `DATEDIF` against `TODAY()`:

```
=DATEDIF(B2, TODAY(), "Y")
```

Fill down through row 6.

## Part D — Compute tenure in years and months

In `J1`/`K1`, add headers `TenureYears` and `TenureExtraMonths`. Compute complete years of tenure, then the leftover months beyond those complete years:

```
J2: =DATEDIF(C2, TODAY(), "Y")
K2: =DATEDIF(C2, TODAY(), "YM")
```

Fill both down through row 6. Build a readable combined label in `L2` using `TEXTJOIN`/`&`:

```
=J2 & " years, " & K2 & " months"
```

Fill down. `Isabella Costa`'s row (hired `2019-12-02`) should read something like `"6 years, X months"` depending on today's date.

## Part E — Next birthday and next work anniversary

In `M1`/`N1`, add headers `NextBirthday` and `NextAnniversary`. Build each person's **next** birthday — this year's birthday if it hasn't happened yet, otherwise next year's:

```
M2: =IF(DATE(YEAR(TODAY()), MONTH(B2), DAY(B2)) >= TODAY(), DATE(YEAR(TODAY()), MONTH(B2), DAY(B2)), DATE(YEAR(TODAY())+1, MONTH(B2), DAY(B2)))
```

Same pattern for the work anniversary in `N2`, using `HireDate` instead of `BirthDate`. Fill both down through row 6.

## Expected result

- `BirthDateFixed`/`HireDateFixed` are real, right-aligned dates matching columns B/C exactly.
- `AgeYears` and tenure columns show sensible whole numbers (spot-check one by hand: someone born `1997-03-22`, as of any date in 2026, is 28 or 29 depending on whether their birthday has passed this year).
- `NextBirthday`/`NextAnniversary` are always **today or in the future**, never in the past — verify this explicitly with one more check column: `=M2 >= TODAY()` should read `TRUE` for every row.

## Done when…

- [ ] `BirthDateText`/`HireDateText` were entered as genuine text (left-aligned) before conversion.
- [ ] `DATEVALUE` conversions match the real-date columns exactly (Part B check column all `TRUE`).
- [ ] `AgeYears` and tenure columns computed with `DATEDIF`, not manual subtraction and division.
- [ ] `NextBirthday`/`NextAnniversary` are never in the past (verified with the `>= TODAY()` check).

## Stretch

- Add a 6th row for someone whose birthday is *today* (use `=TODAY()` as a literal reference, or hard-code today's month/day with this year). Confirm your `NextBirthday` formula correctly returns *today*, not next year — this is the boundary condition (`>=` vs `>`) the formula is specifically designed to get right.
- Compute `DaysUntilNextBirthday` as a simple subtraction (`NextBirthday - TODAY()`), and sort the sheet by that column ascending to see who's closest to their next birthday.

## Submission

Keep this sheet in your workbook.
