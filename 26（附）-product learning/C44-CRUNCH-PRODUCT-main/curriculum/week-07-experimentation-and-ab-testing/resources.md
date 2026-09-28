# Week 7 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

- **Python 3.10+** with the statistics stack this week runs on:

```bash
pip install numpy scipy statsmodels pandas
```

Check it:

```bash
python3 -c "import numpy, scipy, statsmodels, pandas; print('ready')"
```

- **PostgreSQL 16+** — the course's primary engine, for the SQL aggregation portions:
  <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **SQLite 3.35+** — the zero-setup fallback; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- If `pip install` is blocked by an externally-managed-environment error (common on newer macOS/Homebrew Python), create a virtual environment first: `python3 -m venv .venv && source .venv/bin/activate && pip install numpy scipy statsmodels pandas`.

## Required reading (this week's core)

- **statsmodels — Power and Sample Size Calculations:** <https://www.statsmodels.org/stable/stats.html#power-and-sample-size-calculations>
  *Why: the exact library reference for `NormalIndPower`, `TTestIndPower`, `proportion_effectsize`, and `proportions_ztest` used throughout this week's lectures and exercises.*
- **Evan Miller — "How Not To Run An A/B Test":** <https://www.evanmiller.org/how-not-to-run-an-ab-test.html>
  *Why: the canonical, short, sharp explanation of the peeking problem — the single most common real-world A/B testing mistake.*
- **Evan Miller — "Sample Size Calculator" (and the math writeup behind it):** <https://www.evanmiller.org/ab-testing/sample-size.html>
  *Why: a second, independent derivation of the sample-size formula from Lecture 2 — useful for cross-checking your own calculations.*
- **Kohavi, Tang, Xu — *Trustworthy Online Controlled Experiments* (free chapters/preprint materials from the authors):** <https://exp-platform.com/trustworthyonlinecontrolledexperiments/>
  *Why: the field's standard reference, written by the people who built experimentation platforms at Microsoft, Airbnb, and LinkedIn. Chapters 1–4 and 19 map directly onto this week's three lectures.*

## Reference (keep in tabs)

- **statsmodels — `proportions_ztest` API reference:** <https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportions_ztest.html>
- **statsmodels — `proportion_confint` API reference (confidence intervals for a proportion):** <https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html>
- **scipy.stats — `ttest_ind` (Welch's t-test) reference:** <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html>
- **PostgreSQL — Aggregate functions reference:** <https://www.postgresql.org/docs/current/functions-aggregate.html>
  *Why: `SUM`, `COUNT`, `AVG`, and `GROUP BY` are how you'll produce the raw counts SQL feeds into the Python significance tests.*
- **Microsoft ExP Platform — "Guidelines for A/B Testing":** <https://exp-platform.com/guidelines-for-ab-testing/>
  *Why: a practitioner-level checklist covering SRM checks, guardrails, and common pitfalls, from the team that runs experimentation at Microsoft scale.*

## Practice beyond the seed data

- **PostgreSQL Exercises** — free, browser-based, graded `SELECT`/aggregate drills: <https://pgexercises.com/>
  *Why: more reps on the `GROUP BY`/aggregate SQL this week's mini-project and homework use to produce experiment totals.*
- **Optimizely's "Stats Engine" whitepaper (free, no signup for the PDF):** <https://www.optimizely.com/insights/blog/optimizely-stats-engine/>
  *Why: a real commercial platform's public explanation of sequential testing — the proper fix for wanting to peek safely, referenced in Lecture 3 §1.*

## Deeper background (optional this week)

- **Card, Krueger — the original minimum-wage diff-in-diff study:** <https://davidcard.berkeley.edu/papers/njmin-aer.pdf>
  *Why: the canonical applied example of difference-in-differences reasoning, from outside tech — useful for seeing the method in its original, non-software context before you apply it to a pricing page in Challenge 2.*
- **Netflix Technology Blog — experimentation series:** <https://netflixtechblog.com/tagged/experimentation>
  *Why: real, detailed write-ups of how a large product org designs, monitors, and interprets experiments at scale.*
- **Airbnb Engineering — "Experiments at Airbnb":** <https://medium.com/airbnb-engineering/experiments-at-airbnb-e2db3abf39e7>
  *Why: an accessible account of building an internal experimentation culture and platform from scratch.*

## Glossary

| Term | Definition |
|------|------------|
| **Hypothesis** | A falsifiable if/then/because statement naming a change, a primary metric, a direction/magnitude, and a mechanism. |
| **Primary metric** | The single metric that decides ship/no-ship for an experiment. |
| **Guardrail metric** | A metric that must not get meaningfully worse; vetoes a ship even if the primary metric wins. |
| **Unit of randomization** | The entity (user, session, team, geography) randomly assigned to control or treatment. |
| **SUTVA / contamination** | Stable Unit Treatment Value Assumption; violated when a treated unit's exposure leaks into a control unit's outcome. |
| **MDE (minimum detectable effect)** | The smallest true effect a test is designed to reliably detect; a business decision. |
| **α (significance level)** | The tolerance for a false positive — wrongly declaring a win when there's no real effect. Conventionally 0.05. |
| **Power (1 − β)** | The probability of correctly detecting a real effect of size MDE. Conventionally 0.80. |
| **p-value** | The probability of observing data this extreme (or more) if the null hypothesis (no effect) were true. |
| **Confidence interval (CI)** | The range of true effect sizes consistent with the observed data at a given confidence level (typically 95%). |
| **Statistical vs. practical significance** | A result can be statistically significant (unlikely due to chance) yet too small in magnitude to matter for the business, or vice versa in an underpowered test. |
| **Pseudoreplication** | Analyzing correlated sub-units (e.g., incidents within a team) as if they were independent samples, artificially shrinking the p-value. |
| **Sample ratio mismatch (SRM)** | When the observed split between arms differs meaningfully from the assigned split — usually signals a broken randomization or logging pipeline. |
| **Peeking / optional stopping** | Checking a result repeatedly and stopping the moment it looks significant, which inflates the true false-positive rate above the nominal α. |
| **Multiple comparisons** | Checking many metrics or segments and treating any one significant hit as meaningful, without correcting for the number of looks. |
| **Novelty effect** | A temporary metric spike from users trying something new, which fades — overstates long-run benefit if measured too early. |
| **Primacy effect** | Temporary friction from an unfamiliar change that recovers over time — understates long-run benefit if measured too early. |
| **Holdout group** | A small slice deliberately kept on the old experience after a feature ships broadly, to measure durable/long-run effects. |
| **Switchback design** | Alternating the entire population between control and treatment over time periods, used when individual units can't be split. |
| **Difference-in-differences (diff-in-diff)** | Comparing the before/after change in a treated group against the before/after change in a similar, untreated comparison group, to net out confounds. |

---

*Broken link? Open an issue or PR.*
