# Week 7 — Exercises

Three guided exercises, ~1–1.5 hours each. Work them in order — Exercise 2 analyzes the exact scale of test you size in Exercise 1, and Exercise 3 uses the same statistical machinery to catch a trap.

1. **[Exercise 1 — Size an experiment for a target effect](exercise-01-size-an-experiment.md)** — turn a baseline rate and a target MDE into a required sample size and test duration.
2. **[Exercise 2 — Analyze A/B results in Python](exercise-02-analyze-ab-results-in-python.md)** — take a 14-day daily dataset and compute lift, significance, and a confidence interval.
3. **[Exercise 3 — Spot the p-hacking in a result](exercise-03-spot-the-p-hacking.md)** — diagnose exactly where and how a peeking-driven "win" fell apart.

## Before you start

- You've completed all three lectures, especially Lecture 2 (the sample-size formula and the Python code you'll reuse here).
- You have Python 3.10+ with `numpy`, `scipy`, `statsmodels`, and `pandas` installed:

```bash
pip install numpy scipy statsmodels pandas
```

Check it:

```bash
python3 -c "import numpy, scipy, statsmodels, pandas; print('ready')"
```

- A text editor and a place to run `.py` scripts or a Jupyter/IPython session — whichever you're comfortable with. All code in this week's exercises is plain Python; no notebook is required.

## Suggested workflow

- Open the exercise file beside your editor.
- **Do the arithmetic by hand first** where a lecture gave you the formula, then verify with the library call. Feeling the formula matters more than the library call — the library is what you'll use on the job, but you won't trust its output (or catch its misuse) if you've never done the calculation yourself.
- Save each exercise's code in its own `.py` file (e.g., `exercise-01.py`) with comments showing your answer to each task. You'll commit these.
- If a number surprises you, stop and figure out why before moving on — in this week especially, "that seems too big/small" is usually the whole lesson (see Lecture 2's note on how fast sample size grows as the MDE shrinks).

## A note on precision

Every dataset in these exercises is complete and self-contained — you don't need outside data. Numbers are given to enough decimal places to reproduce exactly; if your computed p-value or confidence interval differs from the exercise's answer by more than rounding error, you likely have a formula or a data-entry bug, not a "close enough" situation. Statistics rewards exactness far more than most product work does — get comfortable re-checking your arithmetic here.
