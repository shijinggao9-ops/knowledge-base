# Exercise 1 — Split Full Names Into Parts

**Goal:** Take a column of full names in two different raw shapes and split each into clean `First` and `Last` columns using formulas — both the classic `FIND`/`LEFT`/`MID` approach and, where available, `TEXTSPLIT`.

**Estimated time:** 1 hour.

## Setup

In your `crunch-week4` workbook, add a new sheet and rename it `Exercise 1`.

## Part A — Enter the data

Starting at `A1`, type this data exactly as shown:

| FullName |
|---|
| Rossi, Olivia |
| Anderson, James |
| Patel, Priya |
| Sharma, Arjun |
| Brown, William |
| Costa, Isabella |
| Meyer, Lucas |
| Johansson, Mia |

Row 1 is your header (`FullName`).

## Part B — Split with FIND + LEFT/MID (do this first, even if TEXTSPLIT is available)

In `B1` and `C1`, add headers `Last` and `First`. In `B2`, extract the last name using the comma position:

```
=LEFT(A2, FIND(",", A2) - 1)
```

In `C2`, extract the first name, skipping the comma and the space after it:

```
=TRIM(MID(A2, FIND(",", A2) + 2, 50))
```

Fill both down through row 9.

## Part C — Split with TEXTSPLIT (Excel 365/Sheets only — skip if unavailable)

In `E1`, add a header `TEXTSPLIT Result`. In `E2` only (let it spill):

```
=TEXTSPLIT(A2, ", ")
```

This should spill into `E2:F2` — last name in `E2`, first name in `F2`. **Do not** put a formula in `F2` — it will block the spill.

Copy `E2` and paste it into `E3` (not `E2:F2` — just the single formula cell) so it spills fresh for each row; repeat for rows 4–9, or use a technique from Lecture 1 to make it work as a single fill-down if your app supports spilling formulas filled down a column (test it — behavior differs slightly between Excel and Sheets).

## Part D — Verify the two approaches agree

In `H2`, write a formula that returns `TRUE` if your Part B `Last` matches your Part C spilled last name, `FALSE` otherwise:

```
=B2=E2
```

Fill down through row 9. Every row should show `TRUE`. If any row shows `FALSE`, one of your two formulas has a bug — find and fix it before moving on (do not just delete the mismatched row).

## Expected result

- `Last` and `First` columns (Part B) correctly split for all 8 rows, with no leading/trailing spaces.
- `TEXTSPLIT` version (Part C) spills correctly and produces the same last names.
- All 8 verification checks (Part D) show `TRUE`.
- `Rossi, Olivia` → `Last: Rossi`, `First: Olivia`. `Johansson, Mia` → `Last: Johansson`, `First: Mia`.

## Done when…

- [ ] All 8 rows entered exactly as shown.
- [ ] `Last`/`First` columns built with `FIND`+`LEFT`/`MID` formulas, not typed values.
- [ ] `TEXTSPLIT` version built (or explicitly skipped with a one-line note if your Excel version lacks it).
- [ ] All 8 `TRUE`/`FALSE` verification checks pass.
- [ ] No column shows leading/trailing whitespace (spot-check with `=LEN()` on a couple of cells — should match the visible character count exactly).

## Stretch

- Add a row with a name that has a suffix, like `Wilson Jr., Ethan`. Does your Part B formula still split it correctly? If not, explain in a comment what breaks and why.
- Build a `FullNameRebuilt` column that reassembles `First` + `" "` + `Last` (no comma) using `TEXTJOIN`, and confirm it reads naturally (`Olivia Rossi`, not `Rossi Olivia`).

## Submission

Keep this sheet in your workbook — you'll reuse the same splitting technique in the mini-project.
