# Challenge 1 — Diagnose a Sudden Funnel Drop in SQL

**Time:** ~75–90 minutes. **Difficulty:** Medium–Hard. **The bug is real and specific — find it with SQL, not by guessing.**

## The scenario

It's mid-March 2025. Loopline's CEO drops into the team's weekly metrics review and says: "Overall signup-to-activation looks fine this quarter, but something felt off in mid-February — support got a few tickets about people not being able to get going after they made a workspace. Can you look at the funnel and tell me if that's real, and if so, exactly when and where?"

You have the full `events` table. You do **not** have the engineering deploy log, the support ticket text, or anyone's memory of what shipped. All you have is the data — which is exactly the situation you'll be in most of the time this happens for real. Your job: find the anomaly, name the specific week and the specific funnel step, quantify how bad it was relative to normal, and write a one-paragraph diagnosis a CEO could act on.

## Your task

Produce a file `diagnosis.md` containing:

1. **The method.** The SQL query (or queries) you used to slice the funnel by cohort week — Lecture 2 §6 gave you the exact pattern; you're applying it here for real, without knowing in advance which week or step is broken.
2. **The finding.** Which cohort week, which specific step-to-step conversion, and by how much it deviates from the other seven weeks (give both the anomalous week's rate and a baseline — e.g. "the other 7 weeks average X%, this week is Y%").
3. **Ruled-out alternatives.** At least one other explanation you checked and rejected before concluding it's a product bug — e.g., "is this cohort just small enough that the drop is noise, not signal?" or "did visitor volume also drop that week, meaning it's a traffic issue, not a conversion issue?" Show the query that ruled each one out.
4. **The diagnosis paragraph.** Three to five sentences, written for the CEO: what happened, when, roughly how many users it affected, and what you'd ask engineering to check first.

## Constraints

- Start from the funnel-by-cohort-week query pattern in Lecture 2 §6 — don't reinvent it, extend it.
- Look at **every** step-to-step transition, not just the one the CEO hinted at ("couldn't get going after making a workspace") — confirm that hint is actually where the data points, rather than assuming it and confirming your own bias.
- Quantify magnitude, not just direction. "Conversion dropped" is not a finding; "conversion dropped from a 60–100% baseline to 20% for one week, affecting roughly 4 of 5 users in that week's workspace-created group" is a finding.
- Small cohorts are noisy — Lecture 3 §2 already told you this. Part of your job is judging whether the anomaly you find is *too small a sample to trust*, or genuinely stands out even accounting for that. Say which, and why.

## Hints

<details>
<summary>Where to start looking</summary>

You already have the exact query shape you need — it's the last code block in Lecture 2 (§6), computing `workspace_created → task_created` conversion by cohort week. Run it as-is first. Then run the *same pattern* for every other step-to-step pair in the funnel (`landing → signup_started`, `signup_started → signup_completed`, `signup_completed → workspace_created`, `task_created → task_completed`) before concluding which single transition is the outlier — the CEO's hint narrows your search, it shouldn't replace your own check.

</details>

<details>
<summary>On ruling out "is this just noise"</summary>

Every cohort here is small (3–12 registered users). One useful gut-check: how many *other* weeks have a step-to-step conversion rate below 50%? If the anomalous week is the *only* week below 50% and every other week clusters 60–100%, that's a much stronger signal than "the numbers wiggle around a bit." Compute the average and the range of the non-anomalous weeks and compare.

</details>

<details>
<summary>On ruling out "was it a traffic problem, not a conversion problem"</summary>

Check whether `landing_page_view` volume for that same cohort week is unusually low or high compared to neighboring weeks. If visitor volume looks normal but the *rate* at one specific step craters, that points at something inside the product for that step, not an acquisition/traffic issue — those are different root causes with different fixes.

</details>

## How success is judged

| Signal | Weak submission | Strong submission |
|---|---|---|
| Method | Eyeballs the raw event rows for patterns | Runs the systematic funnel-by-cohort-week query across every step |
| Precision | "Something looks off in February" | Names the exact cohort week and exact step-to-step transition |
| Magnitude | States direction only ("it dropped") | States the anomalous rate *and* the baseline rate, with the query that produced both |
| Skepticism | Reports the first thing that looks weird | Checks and reports at least one ruled-out alternative (noise, traffic) |
| Communication | Dumps SQL output on the CEO | Ends with a plain-English, three-to-five-sentence diagnosis paragraph |

## Submission

Commit `diagnosis.md` (plus any `.sql` files you used) to your portfolio under `c44-week-06/challenge-01/`.
