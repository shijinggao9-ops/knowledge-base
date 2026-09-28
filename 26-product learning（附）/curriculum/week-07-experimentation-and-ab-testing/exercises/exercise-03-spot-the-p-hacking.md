# Exercise 3 — Spot the P-Hacking in a Result

**Goal:** Given a real (seeded) daily result log and the Slack thread of a PM watching it live, identify exactly where the process went wrong, reproduce the honest full-duration result, and rewrite the monitoring protocol so it can't happen again.

**Estimated time:** 1 hour.

## Setup

```bash
pip install numpy scipy statsmodels pandas
```

Create `exercise-03.py`.

## The scenario

Loopline is testing a redesigned notification digest email — same content, sent as one consolidated email instead of several separate ones — hypothesizing it will increase the **7-day return rate** for users who receive it (the primary metric). The test was planned for **14 days**, sized to detect a 3-point lift at 80% power. Here's the actual, real (seeded) daily cumulative log, and the PM's Slack messages alongside it:

```
day  n_control  conv_control  n_treat  conv_treat  rate_c   rate_t   p_value
  1        130            29      136          11   0.2231   0.0809   0.0012
  2        266            51      266          31   0.1917   0.1165   0.0163
  3        403            76      398          56   0.1886   0.1407   0.0678
  4        546           104      543          87   0.1905   0.1602   0.1893
  5        682           137      696         113   0.2009   0.1624   0.0635
  6        830           167      844         137   0.2012   0.1623   0.0391
  7        955           196      991         176   0.2052   0.1776   0.1211
  8       1109           219     1138         202   0.1975   0.1775   0.2251
  9       1244           248     1288         233   0.1994   0.1809   0.2366
 10       1375           273     1434         258   0.1985   0.1799   0.2075
 11       1524           298     1576         290   0.1955   0.1840   0.4131
 12       1665           318     1714         319   0.1910   0.1861   0.7171
 13       1790           341     1843         344   0.1905   0.1867   0.7667
 14       1922           361     1994         370   0.1878   0.1856   0.8555
```

The PM's running Slack commentary:

> **Day 1:** "Whoa, p = 0.0012 already?! Treatment's tanking though — is the new digest actively hurting return rate?? Should we kill it now?"
> **Day 2:** "Still p < 0.05 (0.016) and treatment's still behind. Getting nervous, but let's give it a couple more days like we planned."
> **Day 6:** "OK it's p = 0.039 again — that's twice now it's dipped under 0.05. I think we have a real, statistically significant result: the new digest design hurts 7-day return rate. Writing up the recommendation to kill the consolidated digest and keep the old multi-email format."
> **Day 14 (test's real planned end):** "...huh, it's basically flat now. p = 0.86. Weird, must be some late-week noise. I'll just report the day 6 number since that's when it was clearly significant."

## Tasks

1. **Reproduce the full table** as a `pandas.DataFrame` and confirm the p-values in the log by recomputing them yourself with `proportions_ztest` at each day's cumulative counts. (This checks you can trust the log — always verify a number before you build a critique on top of it.)

2. **Name every mistake in the PM's process**, one per Slack message, in plain English. For each one, say which trap from Lecture 3 it is (peeking/optional stopping, multiple comparisons, novelty/primacy, or something else) and *why* it's a mistake — not just "this is wrong" but the mechanism.

3. **Compute the true, honest result.** What is the correct p-value and conclusion to report, and on which day should it have been read? Why is reading it early — even on the pre-planned final day, if you'd been checking daily and cherry-picking — still a problem if the PM already saw (and was anchored by) the day-6 number?

4. **Estimate how often this would happen by chance.** This dataset was simulated with **zero true difference** between arms (both had the same underlying return rate — verify this by comparing the final day-14 rates, which should be nearly identical). Given that days 1, 2, and 6 all independently dipped below p = 0.05 purely from sampling noise, what does that tell you about the real false-positive rate of "check daily, stop at the first p < 0.05" compared to the nominal 5%? (You don't need to derive the exact inflated rate mathematically here — Lecture 3 gives you the intuition; state it in your own words with reference to this example.)

5. **Rewrite the monitoring protocol.** In 5–8 bullet points, write the rule Loopline's experimentation team should adopt so this can't happen again — covering: when the team is and isn't allowed to look at the p-value, what they *should* monitor daily (hint: not the primary metric's p-value), and what to do if leadership demands an early read.

## Expected results (spot checks)

- Task 1 → your recomputed p-values should match the table exactly (or within floating-point rounding) — if they don't, you likely built the cumulative counts wrong (e.g., using per-day counts instead of running totals).
- Task 3 → the honest conclusion is **no significant difference** (p ≈ 0.86 at the full, pre-planned n); the day-6 "kill it" call was a false positive from peeking, not a real finding. There is nothing wrong with the consolidated digest design based on this data.
- Task 4 → across just 14 independent daily looks, three of them (days 1, 2, 6) crossed p < 0.05 under a true null — a rate far higher than 5%, and exactly the mechanism Lecture 3 §1 describes.

## Done when…

- [ ] `exercise-03.py` reproduces the table and confirms the logged p-values.
- [ ] Every one of the PM's four Slack messages has a named mistake and mechanism in your write-up.
- [ ] You state clearly that the honest, full-duration result is a null result — and that reporting the day-6 number instead would have led Loopline to wrongly kill a feature that (per this data) does no harm.
- [ ] Your rewritten protocol (Task 5) has a concrete answer for "what do we do if leadership wants results tomorrow" — not just "don't peek."

## Stretch

- The PM's day-1 panic ("treatment's tanking!") came from a sample of only ~266 total sessions. Using the sample-size formula from Lecture 2, what MDE would you need to be chasing for n≈266 total (~133/arm) to even be an appropriately sized look? Compare that to the test's actual designed MDE (3 points) — is 266 sessions anywhere close to enough to draw a conclusion from, regardless of what the p-value says?
- Find one real published example (a blog post, conference talk, or case study from a company's engineering blog) of a team publicly admitting they had to walk back an experiment result due to peeking or a related trap. Summarize what happened in 3–4 sentences and link it in your submission — evidence this isn't a hypothetical mistake.

## Submission

Commit `exercise-03.py` and your write-up (Tasks 2, 3, 4, 5) to your portfolio under `c44-week-07/exercise-03/`.
