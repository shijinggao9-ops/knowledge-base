# Mini-Project — The Capstone: Zero to One

**Estimated time:** 6.5 hours (Saturday's block, plus Sunday polish time from the schedule).

## Brief

This is the deliverable the entire course has been building toward. You are not starting from a blank page today — you're assembling and finishing the pieces you wrote in Exercises 1–3 and Challenges 1–2 into one coherent document that tells your capstone idea's full story: discover, spec, prioritize, measure, experiment, launch. A real hiring manager, or a real internal stakeholder panel, should be able to read this single document and understand exactly what you'd build, why, how you'd know if it worked, and what you'd do next.

If you've been keeping up with the exercises and challenges, most of the writing is already done. Today's job is **assembly, coherence-auditing, and finishing** — not drafting from zero.

## Requirements

Produce one primary document, `c44-week-12/mini-project/capstone-product-story.md`, structured as follows:

### 1. Executive summary (150–250 words)
One paragraph a busy executive could read alone and understand the whole story: the problem, the MVP, the launch result (honest, both signals), and the ask. Write this **last**, after everything else is finished — a summary written first tends to describe the idea you *wish* you'd built rather than the one your evidence actually supports.

### 2. Discovery (pull from Exercise 1)
Your discovery brief, lightly edited for a stakeholder audience rather than a classroom exercise — trim anything that was scaffolding for the exercise itself (task numbers, "Done when" references) and keep the problem statement, evidence, JTBD, sizing, and risks.

### 3. Spec and roadmap (pull from Exercise 2)
Your PRD's Problem, Goals, Non-goals, User Stories, and Success Metric sections, plus your Now/Next/Later roadmap with the RICE/WSJF reasoning for at least your top 3 items visible (not the full raw table required, but the reasoning behind your key calls must be legible to a reader who wasn't in the room when you scored them).

### 4. Instrumentation and results (pull from Exercise 3)
Your event schema (the `CREATE TABLE` statements, or a clean summary of the columns and what they capture), and your dashboard's key findings — presented as the coherent-story paragraph from Exercise 3's Part B, Task 4, not as a raw dump of every query result.

### 5. Experiment (pull from Challenge 1)
Your experiment plan's hypothesis, design choice, sample-size reasoning, guardrails, and pre-registered decision rule — condensed to the essentials a stakeholder needs, not the full working document.

### 6. Launch narrative and defense (pull from Challenge 2)
Your full five-part launch narrative, plus at least 3 of your 5 defense Q&A answers (choose the 3 that best demonstrate you can defend a real trade-off under pressure).

### 7. Coherence self-audit
Run Lecture 1 Section 3's five-point checklist against your OWN capstone, in writing, one sentence per checkbox: does the PRD cite the discovery brief, does the Now bucket trace to the PRD, does the dashboard measure the PRD's stated metric, does the experiment's decision rule match the dashboard's metric, does the next bet trace to evidence. If any answer is "not quite," say so honestly and fix it before submitting — a self-audit that finds nothing wrong on the first pass usually means it wasn't run rigorously.

## Deliverables

- [ ] `capstone-product-story.md` — the assembled document, sections 1–7 above, all present and in order.
- [ ] All five source files from Exercises 1–3 and Challenges 1–2 still committed in their own folders (the assembled document references them; it doesn't replace them).
- [ ] A `README.md` in `c44-week-12/mini-project/` (can be brief) linking to `capstone-product-story.md` and stating, in one sentence, your capstone idea — this is the file a portfolio visitor sees first.

## Grading rubric (self-check before submitting)

| Dimension | What "meets the bar" looks like |
|-----------|-----------------------------------|
| **Coherence** | Every section traces to the section before it — no orphaned artifacts (Lecture 1's audit, Section 7 above, passes honestly). |
| **Evidence discipline** | Every claim about the market, the users, or the results is sourced to something specific — a cited competitor, a query result, a named number — not asserted. |
| **Honesty about the result** | Section 4 and Section 6 report the real mixed signal from your dashboard, not a cleaned-up version. A capstone with zero bad news is a tell, not a strength (Lecture 1, Section 5). |
| **SQL, never a spreadsheet** | The instrumentation section shows real `CREATE TABLE`/`SELECT` work — no data-as-a-grid anywhere in the pipeline. |
| **A real, falsifiable next bet** | The next-quarter bet has a specific action, metric+threshold, and decision date — not "we'll keep iterating." |

## Stretch goals

- **Build a live 1-page HTML or Markdown-rendered summary** of your dashboard's key numbers (a simple table or a hand-built chart description is fine — this course doesn't require a BI tool) that you could screen-share in 60 seconds during a real interview.
- **Record a 5-minute pitch** covering the executive summary and the launch narrative's five parts, timed — practicing the actual verbal delivery of Challenge 2's stretch goal, but for the finished, polished version.
- **Run your coherence self-audit on a classmate's capstone** (if you're working through this course with others) and compare notes — a second reader almost always finds an orphaned artifact the author missed, which is exactly why real PM work goes through review before a launch readout, not just before code ships.

## Submission

Commit the full `c44-week-12/mini-project/` folder, including `capstone-product-story.md` and its `README.md`, to your portfolio. This is the file to link first if anyone — a hiring manager, a mentor, a future employer — asks to see your work from this course.
