# Assembling the Product Story

Every week of this course taught you one link in a chain. This lecture is about the chain itself — what makes eleven separate artifacts (a discovery brief, a JTBD map, a problem statement, a PRD, a RICE table, a roadmap, an events schema, a funnel query, an experiment design, a launch plan, a pricing model) add up to *one story* instead of eleven unrelated homework assignments sitting in a folder. That distinction is the entire point of a capstone, and it is also, not coincidentally, the entire point of being a product manager: your job is rarely to be the smartest person in any single room — it's to be the person who can hold the whole chain in their head and show everyone else how the links connect.

## 1. The five-act product narrative

Every coherent zero-to-one product story — real or fictional, yours or a case study you'll read on the job — follows the same five acts. You've done each one at least once this course; this week you do all five in sequence, on one idea, without a professor pre-supplying any of the inputs.

| Act | Question it answers | Course week(s) that taught it | Artifact it produces |
|-----|---------------------|-------------------------------|-----------------------|
| **1. Discover** | Who has this problem, and how do we know it's real? | Week 2 (user research), Week 3 (problem framing) | A discovery brief with evidence, not opinion |
| **2. Spec** | What, precisely, are we building to solve it? | Week 4 (PRDs) | A PRD with scope, non-goals, and success metrics |
| **3. Prioritize** | Given limited capacity, what ships first? | Week 5 (RICE, WSJF, Kano, roadmapping) | A scored backlog and a Now/Next/Later roadmap |
| **4. Measure** | Once it's live, did it actually work? | Week 6 (SQL metrics), Week 7 (experimentation) | An instrumented dashboard and/or an experiment result |
| **5. Launch & grow** | How do we tell the world, and then keep it growing? | Week 8 (UX), Week 9 (GTM), Week 10 (pricing/growth) | A positioning statement, a rollout plan, a pricing/growth model |

Notice what's *not* in this table: Week 1 (foundations) and Week 11 (AI/LLM product management) aren't acts — they're lenses you apply *inside* every act. Week 1's PM vocabulary (JTBD, personas, the build/measure/learn loop) is how you talk about all five acts. Week 11's AI-feature judgment (when an LLM feature is the right bet, how to scope and eval one, what "good enough" means for a probabilistic feature) is a filter you run over Acts 2–5 *if and only if* your capstone idea actually calls for an AI feature — plenty of good zero-to-one products don't, and forcing one in because "it's the AI-era course" is exactly the kind of solution-first thinking Week 3 taught you to distrust.

The single biggest mistake in a rushed capstone is **treating the five acts as independent boxes to check** rather than a chain where each act's output is the next act's input. A PRD that doesn't trace back to a specific line in the discovery brief is fiction with a template. A roadmap whose top item isn't the PRD's stated MVP scope is a to-do list, not a roadmap. A dashboard that measures something other than the PRD's stated success metric is measuring the wrong thing beautifully. Coherence isn't a nice-to-have on top of the five acts — it's the only thing that makes them worth doing in order at all.

```mermaid
flowchart LR
  A["Discover"] --> B["Spec"]
  B --> C["Prioritize"]
  C --> D["Measure"]
  D --> E["Launch and grow"]
```
*Each act's output becomes the next act's input - a chain, not five independent boxes to check.*

## 2. Loopline's arc, read as one story

You've been building Loopline's product story for eleven weeks without necessarily seeing it as one story. Read it that way now — this is the exact shape your own capstone narrative should take, compressed.

**Act 1 — Discover (Weeks 2–3).** Loopline started from a research finding, not a feature idea: small remote teams were losing track of who-owns-what across five different tools, and the JTBD that kept surfacing was "help me see, in one glance, what my team is stuck on" — not "give me a prettier task list." That distinction — a job to be done, not a feature request — is what let Week 3 frame a validated problem ("teams lack a single, trusted view of blocked work") instead of a solution dressed as a problem ("we should build a Kanban board").

**Act 2 — Spec (Week 4).** The PRD scoped an MVP around exactly that JTBD: a stuck-task view, with an explicit non-goal list (no time tracking, no billing, no mobile app in v1) that kept the team from drowning the validated problem in unrelated feature work. The PRD's one success metric was framed before a line of code shipped: "percentage of teams with at least one task marked stuck who resolve it within 48 hours."

**Act 3 — Prioritize (Week 5).** The backlog that followed — `guest_external_access`, `audit_log_compliance`, `dark_mode`, `ai_task_summaries`, and others — got scored on RICE and WSJF, not gut feel. `dark_mode` had 1,800 forum upvotes (a loud, real signal) and still ranked near the bottom, because loud isn't the same as urgent or impactful — a lesson that only exists because the team measured Reach honestly instead of substituting "how many people asked" for "how much this matters." `guest_external_access` ranked low on RICE (narrow initial reach: 20 teams) and #1 on WSJF, because three signed deals had closing dates riding on it — WSJF's Time Criticality component saw the urgency that RICE structurally couldn't.

**Act 4 — Measure (Weeks 6–7).** Once `guest_external_access` shipped, Week 6 didn't ask "does it feel like it's working" — it queried the actual `events` table: a real activation funnel, real weekly retention cohorts, a real DAU/MAU stickiness number. Week 7 went further: instead of shipping the redesigned onboarding flow to everyone and hoping, the team ran an A/B test, pre-registered a decision rule, and only rolled out once the experiment — not a stakeholder's opinion — said it worked.

**Act 5 — Launch & grow (Weeks 8–10).** Design turned the validated flow into real screens (Week 8). GTM turned the shipped feature into a phased, instrumented rollout with a kill switch and a named owner for the pause decision (Week 9) — and that instrumentation is *why* the team caught Cascade Freight's spike in critical support tickets within 48 hours of exposure instead of two weeks later. Once live, Week 10 asked the money question the earlier acts had deliberately deferred: does the flat $12/seat price still make sense now that Loopline has SSO and audit logs that only enterprise buyers value, and is the guest-invite flow — originally a feature, not a growth bet — actually a growth loop worth investing in on its own terms?

Read end to end, that's not eleven separate weeks of homework. It's one company's product story, and every act's output became the next act's input. That's the standard your own capstone is held to this week — not "did you do five things," but "does output of Act *n* visibly become the input of Act *n+1*."

## 3. Auditing a story for coherence

Before you write a word of your own capstone, run this checklist against Loopline's story above — you should be able to answer "yes, and here's where" to every line. Then hold your own capstone to the same bar as you write it.

- [ ] **Does the PRD cite a specific finding from the discovery brief**, not just a restated problem? (Loopline's PRD cites the "one glance, what's stuck" JTBD directly — not a generic "users want visibility.")
- [ ] **Does every item in the roadmap's "Now" bucket trace to the PRD's stated MVP scope**, or did something unscoped sneak in because it was easy or someone senior asked for it?
- [ ] **Does the dashboard measure the PRD's stated success metric**, not a metric that happened to be easy to query? (A team that specs "48-hour stuck-task resolution rate" and then reports "total tasks created" measured the wrong thing well.)
- [ ] **Does the experiment's decision rule reference the same metric as the dashboard**, so a "win" in the experiment and a "win" on the dashboard mean the same thing?
- [ ] **Does the launch narrative's "what's next" bet trace back to something the metrics or the experiment actually showed**, rather than being a generic "we'll keep iterating"?

A story fails this audit in a specific, recognizable way: an **orphaned artifact** — a PRD nobody can trace to research, a roadmap item nobody can trace to the PRD, a metric nobody can trace to a stated goal, a "next bet" nobody can trace to evidence. Orphaned artifacts are the single most common reason a portfolio piece — capstone or otherwise — reads as "assignment completed" instead of "product judgment demonstrated." A hiring manager skimming your capstone will find the seams if they exist; this audit is how you find them first.

## 4. Choosing your capstone idea

You need an idea by the end of today. Three constraints make the difference between a capstone you can actually finish this week and one that stalls on Wednesday:

1. **Scope it to fit in a week, on purpose.** Your capstone MVP should be small enough to fully spec, prioritize, and (hypothetically) instrument in the time you have — think "one core JTBD, one platform, one primary user segment," not "a platform that does five things for three audiences." A too-big idea produces a shallow version of all five acts; a right-sized idea produces a genuinely deep version of all five. Shallow-and-broad loses to deep-and-narrow every time a hiring manager reads it.
2. **Pick something you can generate honest evidence for**, even without real users. You will not run real user interviews this week — that's not the point of a one-week capstone. But you should be able to write a discovery brief grounded in *plausible, specific* evidence: your own experience with the problem, a genuinely existing competitor's reviews (real product, real complaints, cited), a forum thread you can point to, a friend or colleague's actual described pain. "I assume people want this" is not evidence. "Here are four 1-star reviews of [real competitor product] complaining about exactly this gap, and here's why I believe our approach solves it differently" is.
3. **Make sure it has a real metric.** If you can't articulate, before writing the PRD, roughly what event stream would prove the MVP worked or didn't — you've picked an idea that's still a vibe, not a product. Circle back to Week 3's problem-framing discipline before moving on.

Three example capstone ideas at the right scope (don't copy these verbatim — the exercise checks that your idea has its own specific evidence, not a reskin of one of these):

- **A shared grocery list app for roommates that auto-splits recurring costs** — narrow JTBD ("stop arguing about who bought the last thing of dish soap"), one platform (mobile), one segment (co-living young adults), an obvious event stream (item added, item purchased, cost split confirmed).
- **A waiting-room check-in kiosk for small dental/vet clinics that cuts front-desk paperwork time** — narrow JTBD, B2B, small enough scope to spec in a week, a clear metric (average check-in time, front-desk error rate).
- **A "one screen" habit-tracking app for a single, specific habit category** (not a general habit tracker — pick one: hydration, medication adherence, or practice-instrument streaks) — narrow enough that the discovery brief can cite real, specific competitor complaints about existing general-purpose habit apps being too broad.

Write your idea, in one sentence, at the top of a new file: `c44-week-12/00-capstone-idea.md`. You'll expand it into a full discovery brief in Exercise 1 — but the one-sentence commitment now is what keeps Tuesday's PRD from drifting into a different idea than Monday's discovery brief covered. That drift — silently changing your idea mid-week — is the single fastest way to produce a capstone with an orphaned Act 2.

## 5. What "coherent" does *not* mean

Coherence is not the same as "everything goes perfectly" or "every metric is good news." Loopline's own story has a real setback baked into it — the guest-invite rollout paused after a support-ticket spike, and this week's AI Task Summaries launch (Lecture 2) shows strong trial and weak retention, not a clean win. Both are still coherent stories, because the response to the setback traces logically from the evidence: pause, investigate, fix, resume with a kill switch already proven to work is a coherent Act 5, even though it isn't a triumphant one. A capstone that reports only good news, with no setback, no ambiguous number, and no hard trade-off, usually means the student picked metrics that couldn't fail — which is its own tell, and not a flattering one. Real zero-to-one stories have a rough patch. Yours should too; the skill this week measures is how you read and respond to it, not whether you avoided it.

## 6. What comes next

Lecture 2 builds the "measure" act concretely — you'll work through the AI Task Summaries dataset from the README, choose its North Star, and write the SQL that reveals the strong-trial-weak-retention story summarized above. Lecture 3 builds the "launch & grow" act's communication layer — how you present that exact kind of ambiguous, half-good result to a room that wants a clean answer. Exercises 1–3 and Challenges 1–2 build your own capstone's five acts, piece by piece, so that by Saturday's mini-project you're assembling files you've already written — not starting from a blank page a second time.
