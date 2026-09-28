# Challenge 1 — Trim a Bloated PRD to Its Non-Goals

**Time:** ~90 minutes. **Difficulty:** Medium-hard. **No single right answer.**

## The scenario

You've just inherited a draft PRD from a well-meaning but scope-happy colleague on the Loopline team. It was written after a single brainstorm session and never trimmed. Engineering has already flagged, informally, that it reads like "at least three sprints of work pretending to be one feature." Your VP wants a buildable v1 by end of next sprint — roughly one-fifth of what's drafted here. Your job: cut it down, and write the non-goals section that makes the cut *stick* instead of quietly creeping back in during planning.

## The draft PRD (as received)

```markdown
# PRD: Team Activity Insights

## Context
Managers have said, in various conversations, that they'd like "more
visibility" into how their team is doing. This feature gives them that.

## Goals
1. Show a real-time activity feed of everything happening across the team's tasks.
2. Show a weekly digest email summarizing team velocity, blockers, and wins.
3. Add a "team health score" that combines velocity, stuck-task rate, and
   overdue-task rate into a single 0–100 number.
4. Let managers configure custom alert rules (e.g., "notify me if any
   task sits untouched for more than N hours" with a manager-chosen N).
5. Add a leaderboard showing which team members closed the most tasks
   this week, visible to the whole team.
6. Build an AI-generated natural-language summary of "what happened on
   your team this week" that managers can read in 30 seconds.

## Requirements
(none written yet — "we'll figure out stories once the goals are locked")

## Success metrics
- Managers love it (measure via NPS survey after launch).
- Increased engagement with the manager dashboard.
```

## Your task

In `challenge-01.md`:

1. **Diagnose the document.** In 3–5 sentences, explain what's wrong with this draft as a PRD — not just "it's too big," but *why* it's too big (hint: look at how many genuinely different jobs-to-be-done are bundled into "Goals," and look hard at the success metrics section too).

2. **Pick exactly ONE goal to ship as v1.** State which of the six you'd keep, and defend it in 3–4 sentences using what you know from Weeks 1–3: which goal serves the clearest, most validated JTBD? Which one could plausibly ship correctly, with real edge cases handled, inside one sprint? (There's a decent case for more than one goal — defend your specific choice, including why you didn't pick the next-best option.)

3. **Write the non-goals section** for your trimmed v1 PRD. Every one of the five goals you *didn't* pick becomes a non-goal — but a lazy non-goals section just repeats the list. For each, write one clause of *why* it's deferred (too unscoped as written, depends on data that doesn't exist yet, is a genuinely separate feature, needs a product decision not yet made, etc. — vary your reasons; don't write the same justification five times).

4. **Fix the success metrics section.** "Managers love it (measured via NPS)" is not a real success metric for a specific feature — explain in two sentences why, then write 2–3 real, falsifiable success metrics for the ONE goal you kept, in the style of Lecture 1's Stuck Task Alerts example (tie each to a specific, nameable event or query, even if you're inventing plausible event names since this feature doesn't have real instrumentation yet).

5. **Write 2–3 requirements** (user stories, no full acceptance criteria needed for this challenge) for your trimmed v1, run each through the INVEST test from Lecture 2 in one line each.

## Constraints

- Your final v1 scope must be small enough that you could plausibly defend "one sprint" to a skeptical engineering lead — if your kept scope still smells like three features, cut further.
- You may **not** simply pick goal #1 (the activity feed) by default because it's listed first — read all six and make a reasoned choice; a strong answer sometimes picks a less "obvious" goal for a well-argued reason.
- Don't invent new goals — trim from the six given. The skill here is subtraction, not creativity.

## Hints

<details>
<summary>On which goal is actually easiest to validate against Weeks 1–3</summary>

Go back to Week 1's value-proposition table: "surfaces blockers... so nothing is silently forgotten" and "a 2-minute Monday view... walking into the sync already knowing the answer." Which of the six goals most directly serves that *already-validated* job, versus which ones are net-new, unvalidated bets (the leaderboard and the AI summary, in particular, have no stated evidence behind them anywhere in this draft)?

</details>

<details>
<summary>On the "team health score" and "AI summary" goals specifically</summary>

Both of these bundle *multiple* underlying decisions that haven't been made (what weights make up a health score? what does the AI summarize from, given the feature has no data yet?). A goal that secretly depends on several unmade decisions is a sign it's not one goal — it's several, wearing a trenchcoat.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Diagnosis | "It's too big" | Names the specific structural problem (bundled JTBDs, no requirements, unfalsifiable metrics) |
| Scope choice | Picks arbitrarily or picks everything "phased" | One goal, defended with a specific, evidence-based reason |
| Non-goals | Repeats the same justification five times | Varied, specific reasons per deferred goal |
| Metrics | Keeps "managers love it" | Concrete, event-backed, falsifiable metrics |
| Requirements | Vague feature bullets | Real stories that pass INVEST |

## Submission

Commit `challenge-01.md` to your portfolio under `c44-week-04/challenge-01/`.
