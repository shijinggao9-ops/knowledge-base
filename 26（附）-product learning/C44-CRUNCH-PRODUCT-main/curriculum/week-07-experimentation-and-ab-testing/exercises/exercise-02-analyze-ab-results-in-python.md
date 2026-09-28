# Exercise 2 — Analyze A/B Results in Python

**Goal:** Take a real (seeded) 14-day daily A/B dataset for Loopline's Quick Add button — the exact test you sized in Exercise 1 — and compute lift, a two-proportion z-test, and a 95% confidence interval, then write the ship/no-ship read in plain English.

**Estimated time:** 1.5 hours.

## Setup

```bash
pip install numpy scipy statsmodels pandas
```

Create `exercise-02.py`.

## The dataset

Loopline ran the Quick Add test (from Exercise 1) for its full planned 14-day window, individually randomized by session (a private, per-user UI change — no shared surface, so user/session-level randomization is correct here, per Lecture 1 §3). Daily counts, exactly as logged:

```
day  n_control  created_control  n_treat  created_treat
  1        257               68      214             52
  2        256               62      252             78
  3        216               68      229             67
  4        244               55      219             69
  5        239               60      254             68
  6        217               55      233             59
  7        237               61      243             69
  8        247               55      219             65
  9        231               57      213             62
 10        225               36      245             70
 11        249               60      213             66
 12        237               49      217             59
 13        232               40      244             68
 14        219               48      233             61
```

`n_control` / `n_treat` = eligible sessions that day in each arm. `created_control` / `created_treat` = of those, how many included creating at least one task (the primary metric from Exercise 1).

Build this as a `pandas.DataFrame` (type it in, or read it from a CSV you save from the table above) — you'll need it as data, not just as a table to eyeball.

## Tasks

1. **Load and total.** Load the daily data into a DataFrame with columns `day, n_control, created_control, n_treat, created_treat`. Sum each of the four count columns across all 14 days to get the test's totals.

2. **Compute the conversion rate per arm** from the totals (`created / n` for each arm). Report both rates to 4 decimal places.

3. **Run the two-proportion z-test** on the totals using `statsmodels.stats.proportion.proportions_ztest`. Report the z-statistic and the p-value.

```python
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

count = np.array([total_created_treat, total_created_control])
nobs  = np.array([total_n_treat, total_n_control])
z, p_value = proportions_ztest(count, nobs, alternative='two-sided')
```

4. **Compute the 95% confidence interval of the absolute difference** (treatment rate − control rate) using the standard-error formula from Lecture 2 §3. Report both bounds.

5. **Compute the relative lift**: `(rate_treat - rate_control) / rate_control`, as a percentage.

6. **Plot (or at least tabulate) the daily conversion rate per arm across all 14 days** — even a simple printed table of `day, rate_control, rate_treat` is fine if you don't have a plotting library set up. Does the gap look stable across days, or does it show a trend (novelty/primacy — Lecture 3 §3)?

7. **Write the verdict**, in 3–5 sentences, covering: is the result statistically significant? What's the effect size, and is the lower bound of the confidence interval still big enough to matter (compare it against the original 3-point MDE from Exercise 1)? Would you ship Quick Add?

## Expected results (spot checks)

- Task 1 totals → `n_control = 3306`, `created_control = 774`; `n_treat = 3228`, `created_treat = 913`.
- Task 2 → control rate ≈ **0.2341**, treatment rate ≈ **0.2828**.
- Task 3 → z ≈ **4.499**, p ≈ **0.00001** (well below 0.05).
- Task 4 → 95% CI of the difference ≈ **[0.0275, 0.0699]**.
- Task 5 → relative lift ≈ **20.8%**.

If your numbers are noticeably off, check that you summed the right columns (a common bug is summing `n_control` into the treatment total by copy-paste) and that you're passing `[treatment, control]` in a consistent order to `proportions_ztest` (it doesn't matter which order *as long as it matches* between `count` and `nobs`, but flipping just one of the two silently breaks the result).

## Done when…

- [ ] `exercise-02.py` prints the totals, both rates, z and p, the CI, and the relative lift.
- [ ] Your numbers match the spot checks above.
- [ ] Task 6's daily table/plot is present and you've noted whether the gap looks stable.
- [ ] Task 7's verdict directly references the CI's lower bound against the 3-point MDE — not just the p-value.

## Stretch

- Recall from Exercise 1 that the required sample size for a 3-point MDE was 3,311 per arm. This test's actual totals (3,306 control / 3,228 treatment) came in just under that. Using `statsmodels.stats.power.NormalIndPower().power(...)`, compute the achieved power at the actual sample sizes for a true 3-point effect. How close to 0.80 is it, and does that change how much you trust this result compared to a test that hit its target n exactly?
- Loopline's data engineer asks you to also produce this same total in SQL, from a raw `sessions` table with one row per session and a boolean `created_task` column. Write the `GROUP BY arm` query from Lecture 2 §3 and confirm it would produce the same four totals you used above.

## Submission

Commit `exercise-02.py` (or `.ipynb`) and your verdict paragraph to your portfolio under `c44-week-07/exercise-02/`.
