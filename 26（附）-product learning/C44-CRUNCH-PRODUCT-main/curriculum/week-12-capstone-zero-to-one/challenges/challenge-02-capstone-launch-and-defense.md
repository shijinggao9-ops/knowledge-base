# Challenge 2 — Launch the Capstone and Defend the Bets

**Goal:** Write your full five-part launch narrative (Lecture 3's structure) using your own dashboard results from Exercise 3, then answer five planted, adversarial stakeholder questions modeled on Lecture 3 Section 3's four pushback shapes — in writing, as if you were in the room.

**Estimated time:** 150 minutes.

## The scenario

Your capstone MVP has "launched" (hypothetically — using your Exercise 3 synthetic dashboard as the launch data) and you're presenting the readout to a stakeholder panel: a CFO who cares about cost and return, a Growth lead who cares about the metric trend and what's next, and your own VP of Product who cares about whether the original bet was sound. All three will ask hard, specific questions, and none of them will accept a vague answer.

## Part A — The launch narrative (60 min)

Write `c44-week-12/challenge-02/launch-narrative.md` in Lecture 3 Section 2's exact five-part structure:

1. **The problem, in one sentence, with its evidence** — pulled from your discovery brief.
2. **What we built, and what we deliberately didn't** — pulled from your PRD's scope and non-goals.
3. **Did it work — the honest number** — pulled directly from your Exercise 3 dashboard's summary paragraph. Report both the healthy signal and the actual problem, in that order, exactly as Lecture 2 Section 3 modeled.
4. **What we learned, as a specific, falsifiable hypothesis** — your best explanation for *why* the dashboard shows what it shows, stated precisely enough that it could be wrong.
5. **The next-quarter bet** — using Lecture 3 Section 4's three-part structure exactly: a specific action, a specific metric and threshold, a specific decision date. This should connect directly to Challenge 1's experiment plan — the bet you're proposing here should be the experiment you designed there, or a clearly related one.

Keep it tight — 400–600 words. A launch narrative that rambles past this length usually means Section 3 (the honest number) is burying the real finding under hedging language instead of stating it plainly.

## Part B — Defend the bets (90 min)

Answer each of these five planted questions in writing, 3–5 sentences each, in `c44-week-12/challenge-02/defense-qa.md`. Each is modeled directly on one of Lecture 3 Section 3's four pushback shapes — name which shape you're answering at the top of each response.

1. **"Why did you build [your MVP's core feature] instead of [one of your roadmap's other Now/Next items]? That other item had more requests behind it."** Answer using your actual RICE/WSJF scores from Exercise 2 — cite the real numbers, not a general justification.

2. **"Your [primary metric] number looks weak. Why should we keep investing instead of cutting this?"** Reframe using your metric tree, the way Lecture 3 Section 3 modeled for AI Task Summaries — name what IS healthy in your dashboard, and be specific about why the weak number is diagnosable rather than fatal (or, honestly, argue that it might actually be fatal, if your own data suggests that — a defense that overclaims confidence it doesn't have is worse than one that admits a real limit).

3. **"Isn't your sample too small / too short / too novelty-driven to mean anything?"** Answer honestly using your actual synthetic dataset's size and observation window from Exercise 3 — name the real limitation, and name what would resolve it (this should connect to Challenge 1's experiment design).

4. **"What did this cost, and was it worth it?"** Use your roadmap's job-size/effort estimate from Exercise 2, and connect it back to the RICE or WSJF score that justified building it.

5. **A question you invent yourself** — the sharpest, most uncomfortable question a real stakeholder could ask about YOUR specific idea, that isn't already covered by questions 1–4. Write it, then answer it. (If you can't think of an uncomfortable question about your own capstone, that's worth noticing — it usually means you haven't looked hard enough at your own weakest evidence from Exercise 1's risk assessment.)

## Expected outcome

A launch narrative and a defense document that, together, read like a real stakeholder readout — specific numbers, honest limitations, and a next bet with a real decision date, not a polished summary that avoids every hard question by staying vague.

## Done when…

- [ ] The launch narrative follows the five-part structure exactly, in order, at the target length.
- [ ] Section 3 (did it work) reports the honest number, not just the flattering one, and reports the healthy signal first per Lecture 3's ordering guidance.
- [ ] The next-quarter bet has a specific action, a specific metric+threshold, and a specific decision date — all three, not two out of three.
- [ ] Each of the five Q&A answers names which pushback shape it's answering, and cites a real number or artifact from your own capstone work (RICE/WSJF score, dashboard result, sample size) rather than a generic response.
- [ ] Question 5 is a genuinely uncomfortable question you invented yourself, not a restatement of one of the first four.

## Stretch

Record yourself (audio or video, 3–5 minutes, not required to submit anywhere public) actually delivering the launch narrative out loud, then answering one of the five planted questions live, unscripted, using only your written notes as reference — not reading verbatim. Notice where you stumble; that's usually the exact spot where your written answer was relying on vague language to paper over a gap in your evidence. Revise `defense-qa.md` based on what you find.

## Submission

Commit `launch-narrative.md` and `defense-qa.md` to your portfolio under `c44-week-12/challenge-02/`.
