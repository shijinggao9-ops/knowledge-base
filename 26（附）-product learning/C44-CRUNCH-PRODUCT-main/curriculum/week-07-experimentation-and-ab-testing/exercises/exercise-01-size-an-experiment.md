# Exercise 1 — Size an Experiment for a Target Effect

**Goal:** Turn a baseline rate and a target MDE into a required sample size and a real calendar duration — by hand and in Python — for three different scenarios, so the inverse relationship between MDE and sample size stops being an abstraction.

**Estimated time:** 1 hour.

## Setup

```bash
pip install numpy scipy statsmodels
```

Create `exercise-01.py`. Put each task's code under a `# Task N` comment, and print your answers clearly labeled.

## Background

Loopline is planning a test of its "Quick Add" floating button — a one-click way to create a task from anywhere in the app. The hypothesis (from Lecture 1's template):

> If we add a Quick Add button, then the share of sessions where a user creates at least one task will increase, because removing the multi-click path to task creation lowers the friction that currently causes users to defer or skip logging small tasks.

Baseline: **24% of sessions** currently include creating at least one task (`p1 = 0.24`). Loopline gets **850 eligible new sessions per day**, split 50/50 across the two arms once the test starts.

## Tasks

1. **Reproduce the lecture's worked example by hand.** Using the formula from Lecture 2 §2, compute the required sample size per arm to detect a **3-percentage-point** lift (p2 = 0.27) at α = 0.05 (two-sided) and power = 0.80. Show your intermediate values: p̄, p̄(1−p̄), (p2−p1)², and the final n. Your answer should land close to **3,311 per arm** — if it's off by more than rounding, recheck your z-values (z_{α/2} = 1.96, z_β = 0.84).

2. **Confirm it in Python** using `statsmodels`:

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

p1, p2 = 0.24, 0.27
effect_size = proportion_effectsize(p1, p2)
n_per_arm = NormalIndPower().solve_power(
    effect_size=effect_size, alpha=0.05, power=0.80, ratio=1.0, alternative='two-sided'
)
print(f"n per arm: {n_per_arm:.0f}")
```

Confirm it matches your hand calculation from Task 1 (within a couple of units — rounding).

3. **Convert to a duration.** At 850 eligible sessions/day split 50/50 (425/arm/day), how many **days** does the test need to reach the required n per arm from Task 1? Round up to a whole day. Show the formula, not just the number.

4. **Contrast three MDEs.** Repeat Tasks 1–3 (Python is fine here — no need to hand-calculate all three) for MDEs of **2 points** and **5 points**, keeping p1 = 0.24 and everything else the same. Produce a small table:

   | MDE | p2 | n per arm | Total n | Days needed |
   |----:|---:|----------:|--------:|-------------:|
   | 2pp | 0.26 | ? | ? | ? |
   | 3pp | 0.27 | 3,311 | 6,622 | 8 |
   | 5pp | 0.29 | ? | ? | ? |

5. **Write one paragraph** (in a comment or a `notes.md`) answering: Loopline's roadmap review is in 10 days. Which of the three MDEs above is actually achievable in that window, and what would you tell the PM who wants to detect a 2-point lift on this timeline?

6. **Power, not just sample size.** Suppose Loopline can only get 1,500 sessions per arm before the roadmap review (not the full 3,311). Using `NormalIndPower().power(...)` instead of `.solve_power(...)`, compute the **achieved power** at n=1,500/arm for the original 3-point MDE. Is it still above the 0.80 target? What does that number mean in plain English?

```python
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

effect_size = proportion_effectsize(0.24, 0.27)
achieved_power = NormalIndPower().power(effect_size=effect_size, nobs1=1500, alpha=0.05, ratio=1.0)
print(f"achieved power at n=1500/arm: {achieved_power:.3f}")
```

## Expected results (spot checks)

- Task 1/2 → **3,311 per arm** for the 3-point MDE.
- Task 3 → **8 days** (7.79 rounded up).
- Task 4 → 2pp MDE needs **~7,356/arm**; 5pp MDE needs **~1,221/arm**. Notice the 2pp scenario needs more than **6×** the sample of the 5pp scenario for a smaller effect — that ratio is the MDE-squared relationship from Lecture 2 in action.
- Task 6 → achieved power at n=1,500/arm for the 3pp MDE should come out **below 0.80** (roughly 0.5) — confirming that stopping at 1,500/arm undershoots the power you designed for.

## Done when…

- [ ] `exercise-01.py` runs top to bottom and prints all six tasks' answers.
- [ ] Your hand calculation in Task 1 and your Python result in Task 2 agree.
- [ ] The Task 4 table is filled in and committed (as a comment, a printed table, or a small markdown block).
- [ ] Task 5's paragraph gives a real recommendation, not just "it depends."
- [ ] You can explain, without looking it up, why achieved power (Task 6) came out below the 0.80 target.

## Stretch

- Recompute Task 1 with power = 0.90 instead of 0.80, holding everything else fixed. How much does the required sample size grow? (This is the same "tightening a knob costs samples" lesson as the MDE, applied to power instead.)
- Loopline's daily eligible sessions vary — some days 700, some days 1,000. Using the 3-point MDE's required n, write a short Python loop that simulates daily traffic as `numpy.random.randint(700, 1000)` per day and reports how many simulated days it actually takes to hit 6,622 total sessions. Run it a few times — does the day count ever change? Why would a real team build in a buffer beyond the "average day" estimate?

## Submission

Commit `exercise-01.py` (and `notes.md` if you used one) to your portfolio under `c44-week-07/exercise-01/`.
