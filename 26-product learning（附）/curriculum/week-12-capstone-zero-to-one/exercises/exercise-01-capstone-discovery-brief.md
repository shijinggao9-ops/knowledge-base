# Exercise 1 — Write the Capstone Discovery Brief

**Goal:** Turn your one-sentence capstone idea into a discovery brief with real, specific, sourced evidence behind it — the Act 1 artifact that every later act of your capstone must trace back to.

**Estimated time:** 90 minutes.

## Setup

You should already have `c44-week-12/00-capstone-idea.md` with your one-sentence idea from Lecture 1, Section 4. If you don't have one yet, write it now — one sentence, right-sized (a single JTBD, a single platform, a single primary segment), before starting this exercise.

Create `c44-week-12/exercise-01/discovery-brief.md`.

## Tasks

Write each section below. Target 500–800 words total — this is a brief, not a thesis; Week 3's problem-framing discipline (be precise, not exhaustive) applies here exactly as it did there.

1. **The problem statement**, in Week 3's format: *[Segment] struggles to [job to be done] because [root cause], which costs them [quantified or clearly-scoped impact].* Every bracket must be filled with something specific — no bracket may contain a vague placeholder like "users" (name the segment precisely) or "a lot of time" (estimate a number, even roughly, and say how you estimated it).

2. **The evidence**, three distinct sources. Real evidence, not invented: your own direct experience with the problem (be specific about the situation, not "I've noticed this before"); at least one **real, existing competitor or adjacent product**, with a specific complaint you can point to (an actual review, an actual forum post, an actual feature gap you can name — cite what it is, even if you're paraphrasing rather than quoting); and one more source of your choosing (a friend or colleague's specific described experience, a spec of a real analogous product's public roadmap, published usage stats for the problem space). "I assume this is true" is not evidence and will not pass review.

3. **The JTBD**, in Week 1/2's functional + emotional + social format: *When [situation], I want to [motivation], so I can [expected outcome].* Write it once, precisely — this is the sentence your PRD will cite word-for-word in Exercise 2.

4. **Opportunity sizing**, a rough but reasoned estimate of how many people have this problem and how you'd know. You don't need real market research — you need a *defensible chain of reasoning* (e.g., "the U.S. has ~2.1M small dental/vet clinics [cite a real, findable public number]; assume 15% use paper check-in and would consider switching, based on [your reasoning] — that's a ~315K clinic addressable segment"). Show your math, not just a final number.

5. **Risk assessment**, one sentence each on desirability risk (will anyone actually want this — what's your weakest evidence point from Task 2?), feasibility risk (what's technically hard about building it, even at MVP scope?), and viability risk (is there a plausible path to this making money or otherwise justifying the investment?).

## Expected outcome

A discovery brief that a skeptical classmate could read cold and understand: exactly who has this problem, exactly what evidence you have that it's real (and how strong or weak that evidence honestly is), exactly what the JTBD is, a defensible size estimate, and an honest read on the three biggest risks — not a brief that only reports the reasons the idea is good.

## Done when…

- [ ] The problem statement has no vague brackets — segment, JTBD, root cause, and impact are all specific.
- [ ] All three evidence sources are distinct, and at least one references a real, named, existing product or public source (not invented).
- [ ] The JTBD sentence is written in the full functional + emotional + social format, not abbreviated.
- [ ] The opportunity sizing shows its reasoning chain, not just a final number.
- [ ] The risk assessment names a genuine weakness in your own evidence — not a token risk that isn't really a risk (e.g., "risk: someone else might build this too" is not a real desirability/feasibility/viability risk in the Week 3 sense).
- [ ] You can explain, in one sentence, which single piece of evidence you'd most want to strengthen if you had one more week — and why that one, not another.

## Stretch

Write a fourth evidence source: a **falsification attempt**. Actively look for a reason your problem statement might be wrong — a competitor that already solved this well, a sign that the segment doesn't actually care as much as you assumed, a reason the "root cause" you named might not be the real one. Report what you found, even if it complicates your brief. A discovery brief that survives an honest attempt to falsify it is far more convincing than one that never tried.

## Submission

Commit `discovery-brief.md` to your portfolio under `c44-week-12/exercise-01/`.
