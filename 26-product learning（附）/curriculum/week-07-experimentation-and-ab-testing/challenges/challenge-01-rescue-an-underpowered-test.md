# Challenge 1 — Rescue an Underpowered Test

**Time:** ~90 minutes. **Difficulty:** Hard. **No single right answer.**

## The scenario

You ran the Stuck Task Alerts experiment from this week's seed data (`stuck_alert_experiment` — see the [week README](26-product%20learning（附）/curriculum/week-07-experimentation-and-ab-testing/README.md) to load it if you haven't). Analyzed correctly, at the **team level** (the unit of randomization — Lecture 2 §4), the result is a directionally positive but statistically **inconclusive** test:

- Control teams' mean 24-hour unstick rate: **27.7%** (sd 24.2%, n=20 teams)
- Treatment teams' mean 24-hour unstick rate: **33.4%** (sd 21.7%, n=20 teams)
- Welch's t-test: **t ≈ 0.782, p ≈ 0.439** — nowhere close to significant
- 95% CI of the difference: **[−9.1pp, +20.4pp]** — consistent with anything from "the alerts hurt a little" to "the alerts help a lot"

Meanwhile, the guardrail (overall task completion rate) shows no meaningful difference between arms (control 70.9%, treatment 72.9%, p ≈ 0.18) — no red flag there.

Your VP of Product looks at this and says: "So... did it work or not? We've been running this for three weeks. I need an answer before the roadmap review." That's your job in this challenge — not to run one more formula, but to figure out *what actually went wrong* and *what Loopline should really do*.

## Your task

Work through the diagnosis and the options below, then write a final recommendation memo (`challenge-01.md`) that your VP could act on.

### Part A — Diagnose why the test is underpowered

1. Compute the **achieved statistical power** of this test as it actually ran (n=20 teams/arm, the observed effect size). Use `statsmodels.stats.power.TTestIndPower`:

```python
import numpy as np
from statsmodels.stats.power import TTestIndPower

control_mean, control_sd = 0.277, 0.242
treat_mean, treat_sd = 0.334, 0.217
n = 20

pooled_sd = np.sqrt((control_sd**2 + treat_sd**2) / 2)
effect_size = (treat_mean - control_mean) / pooled_sd   # Cohen's d

achieved_power = TTestIndPower().power(effect_size=effect_size, nobs1=n, alpha=0.05, ratio=1.0)
print(f"cohen's d: {effect_size:.3f}")
print(f"achieved power: {achieved_power:.3f}")
```

2. Compute **how many teams per arm** would actually be required to detect this effect size at 80% power, using `.solve_power(...)` instead of `.power(...)`.

3. In 3–4 sentences, explain *why* this happened even though the sample-size formula was applied correctly in Lecture 1/2 design — connect it to the team-level randomization decision and the between-team variance discussed in Lecture 1 §3 and Lecture 2 §4.

### Part B — Evaluate three rescue options

For each option below, do the calculation and state the real-world cost.

**Option 1 — Extend the test's duration.** Loopline onboards roughly **6–7 new eligible teams per arm per week** onto this feature. Using the required-n figure from Part A, Task 2, how many *additional weeks* would the test need to run to reach that sample size? Is that a realistic ask ahead of a roadmap review?

**Option 2 — Reduce variance with a pre-period covariate (CUPED).** CUPED (Controlled-experiment Using Pre-Experiment Data) uses each team's own *historical* stuck-rate (before the test started) as a covariate to shrink the variance of the outcome metric, which reduces the required sample size without collecting more data. The size of the benefit depends on how correlated (ρ) a team's historical rate is with its rate during the test — roughly, variance shrinks by a factor of `(1 − ρ²)`. Compute the required n per arm at three plausible correlations:

```python
import numpy as np
from statsmodels.stats.power import TTestIndPower

pooled_sd = 0.230          # from Part A
observed_diff = 0.057      # treat_mean - control_mean

for rho in [0.3, 0.5, 0.7]:
    reduced_sd = pooled_sd * np.sqrt(1 - rho**2)
    effect_size = observed_diff / reduced_sd
    n = TTestIndPower().solve_power(effect_size=effect_size, alpha=0.05, power=0.80, ratio=1.0)
    print(f"rho={rho}: required n per arm = {n:.0f}")
```

Even at a fairly optimistic ρ = 0.7 (a team's history strongly predicts its future), does CUPED alone get you to a realistic team count? What would it get you to in *combination* with a modest duration extension?

**Option 3 — Change the unit of randomization.** If instead of randomizing by team, Loopline randomized by **individual stuck incident** (i.e., a coin flip decides whether *this specific* stuck task gets an alert, regardless of team), the required sample size for the pooled incident-level rates (control 24.5%, treatment 35.7%) would only be about **262 incidents per arm** — a number Loopline already has after three weeks (147 control incidents, 168 treatment incidents logged). Using Lecture 1 §3, explain **why this option is statistically tempting but methodologically risky** for this specific feature. Would you recommend it? Under what condition would it become acceptable?

### Part C — Write the recommendation memo

In `challenge-01.md`, write a memo (300–500 words) to your VP covering:

1. **The honest headline**: is this a "no" (alerts don't work), a "yes" (alerts work, ship it), or something else? Say which, and why the p-value alone doesn't answer the question your VP is actually asking.
2. **Your recommended path forward** — pick one of the three options from Part B, or a combination, and defend the choice against the other two.
3. **What you'd tell the VP about the roadmap review** — can you give them an answer today, and if not, what's the honest timeline?
4. **One sentence on what you'd design differently** if you were starting this experiment from scratch, knowing what you know now.

## Constraints

- Every number in Part A and B must come from an actual calculation you ran — no eyeballed estimates.
- Your Part C memo may pick any defensible path, but it must explicitly name the cost of the path *not* chosen — a strong memo shows you considered the alternative and can say why it loses.
- If you recommend Option 3 (change the randomization unit), you must also address the SUTVA/contamination risk from Lecture 1 §3 directly — silence on that point is an incomplete answer.

## Hints

<details>
<summary>On why the test came out underpowered despite a "correct" design (Part A)</summary>

The original power calculation for this test (implicitly) assumed a between-team standard deviation small enough that 20 teams per arm would suffice. In reality, individual teams' stuck-rates vary hugely — some teams have a rough week and every stuck task lingers, others resolve everything fast regardless of alerts — so the pooled standard deviation (≈0.23 on a 0–1 rate) is enormous relative to the ≈0.057 observed difference between arms. A large between-unit variance relative to the effect size is *exactly* the situation Lecture 2's "team-level randomization costs you sample size" warning describes. This isn't a bug in this week's data — it's a realistic illustration of how often team/account-level randomization runs into exactly this wall in practice.

</details>

<details>
<summary>On Option 3's real risk</summary>

Randomizing by incident instead of by team reintroduces the SUTVA violation Lecture 1 §3 specifically ruled out: if two stuck tasks on the *same* team get different treatment, a control-arm task on a team where a treatment-arm task just got an alert can still benefit — a manager who saw the Slack alert for one task often checks the whole team's board, not just the alerted task. The gain in statistical power is real, but it comes at the cost of introducing exactly the contamination this week's Lecture 1 spent a whole section explaining how to avoid. A defensible middle path: keep team-level randomization, but consider whether a **cluster-robust** analysis with a much larger team count (via Option 1/2) is worth the wait rather than trading away validity for power.

</details>

## Submission

Commit `challenge-01.md` (with your Part A/B calculations shown, e.g. as code + output, and the Part C memo) to your portfolio under `c44-week-07/challenge-01/`.
