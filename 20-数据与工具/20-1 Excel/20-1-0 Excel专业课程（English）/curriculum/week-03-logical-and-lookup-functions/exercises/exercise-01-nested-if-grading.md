# Exercise 1 — Grade Scores With IF/IFS

**Goal:** Get `IF`, `IFS`, and `AND`/`OR` into your fingers on a real gradebook — branch a letter grade off a score, flag honor roll off two conditions, and flag "needs review" off either of two.

**Estimated time:** 1 hour.

## Setup

Extend the `Grades` sheet from Lecture 1. Confirm it looks like this before starting (add any missing rows):

```
      A          B        C            D
1   Student    Score    Attendance   Notes
2   Amara      92       1.00
3   Devon      67       0.85
4   Priya      81       0.95
5   Malik      58       0.70
6   Sofia      74       1.00
7   Kenji      88       0.60
8   Rosa       95       0.90
9   Tomas      71       0.55
```

Format `C2:C9` as Percentage if it isn't already.

## Tasks

1. **Pass/Fail.** In `E1`, header `Pass/Fail`. In `E2`, write an `IF` that returns `"Pass"` for a score of 60 or above, `"Fail"` otherwise. Fill down through `E9`. *(Expected: only Malik and Tomas show `"Fail"`.)*

2. **Letter grade with `IFS`.** In `F1`, header `Grade`. In `F2`, write one `IFS` formula covering: `90+` → `"A"`, `80+` → `"B"`, `70+` → `"C"`, `60+` → `"D"`, otherwise → `"F"`. Remember the `TRUE, "F"` catch-all. Fill down. *(Expected: Amara `A`, Devon `D`, Priya `B`, Malik `F`, Sofia `C`, Kenji `B`, Rosa `A`, Tomas `C`.)*

3. **Same grade with nested `IF`.** In `G1`, header `Grade (nested)`. In `G2`, write the *same* letter-grade logic as Task 2 using nested `IF` instead of `IFS`. Fill down and confirm `F2:F9` matches `G2:G9` exactly, row for row.

4. **Honor roll — `AND`.** In `H1`, header `Honor Roll`. In `H2`, write `IF(AND(...), "Honor Roll", "")` for score `90+` **and** attendance `90%+`. Fill down. *(Expected: exactly 2 — Amara (92, 100%) and Rosa (95, 90%). Kenji has an 88, which fails the score bar even though nothing else about him looks weak — that's the point of `AND`: one failing condition sinks the whole row.)*

5. **Needs review — `OR`.** In `I1`, header `Needs Review`. In `I2`, write `IF(OR(...), "Review", "")` for score **under 65** or attendance **under 65%**. Fill down. *(Expected: exactly 3 — Malik (flagged on score), Kenji (flagged on attendance), Tomas (flagged on both).)*

6. **Compound rule.** In `J1`, header `Scholarship Eligible`. In `J2`, a student is eligible if **(score 85+ AND attendance 85%+) OR score is 95+ regardless of attendance**. Write one formula combining `OR` and `AND`. Fill down. *(Expected: exactly 2 — Amara and Rosa. Priya (81, 95%) fails: her score is under 85, so the `AND` branch fails, and 81 is nowhere near the 95+ escape clause. Kenji (88, 60%) also fails: his score clears 85, but attendance at 60% fails the `AND`, and 88 doesn't reach the 95+ clause either. Work through why each excluded student fails *before* checking your formula — that's the actual exercise.)*

## Expected result (spot checks)

- Task 1 → exactly 2 `"Fail"`s (Malik, Tomas).
- Task 2 and Task 3 → identical values in every row; if they differ, one of your two formulas has the threshold order backwards.
- Task 4 → exactly 2 `"Honor Roll"`s.
- Task 5 → exactly 3 `"Review"`s.

## Done when…

- [ ] `F2:F9` and `G2:G9` match exactly, confirming your `IFS` and nested `IF` encode the same logic.
- [ ] You can explain, without looking, why the grade thresholds must be tested highest-to-lowest.
- [ ] `H` uses `AND`, `I` uses `OR`, and you can state in one sentence why swapping them would break each rule.
- [ ] `J2:J9` reflects a formula that nests `AND` inside `OR` (not the other way around).

## Stretch

- Add a `K` column, `Grade + Trend`, that appends `" (strong attendance)"` to the letter grade from `F` when attendance is 95%+, using `&` to concatenate — e.g., `IF(C2>=0.95, F2&" (strong attendance)", F2)`.
- Rewrite Task 6's compound rule using `NOT` somewhere in it and confirm it still gives identical results — this is a good check that you actually understand what the original rule meant, not just that you can type it.

## Submission

Save your workbook. You'll extend the `Grades` sheet again in the mini-project.
