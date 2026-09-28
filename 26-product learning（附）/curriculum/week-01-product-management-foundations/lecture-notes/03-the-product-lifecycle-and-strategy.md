# Lecture 3 — The Product Lifecycle and Strategy

> **Duration:** ~2 hours. **Outcome:** You can name a product's lifecycle stage, explain why that stage determines which metric matters most, run the value / viability / feasibility / usability (VVF+U) lens on an idea, and read a metrics dashboard to infer — with evidence — the strategic bet a team is making.

A feature that's a brilliant bet for a two-year-old startup can be a wasteful distraction for a ten-year-old market leader, and vice versa — not because either team has worse judgment, but because they're in different lifecycle stages with different constraints and different jobs to do *as a business*. This lecture gives you the map.

## 1. The product lifecycle — five stages

Every product moves (or dies trying to move) through a rough sequence. Stages aren't strict calendar phases — a mature product can spin up a brand-new discovery effort for a new segment — but at any given moment, most of a product's energy sits in one stage, and that stage should set the agenda.

| Stage | Central question | What "winning" looks like | Typical primary metric |
|-------|-------------------|----------------------------|--------------------------|
| **1. Discovery / inception** | Is there a real, painful, sizable problem here? | A validated problem, evidenced by real user behavior, not just opinions | Number of validated problem interviews; qualitative signal strength |
| **2. Validation / early growth** | Do enough people want *this specific solution* enough to keep using it? | Early users activate and come back without heavy hand-holding | Activation rate; week-1/week-4 retention |
| **3. Growth** | Can we scale acquisition and retention together, profitably? | New user growth compounds; retention holds as the user base scales | New signups, WAU/MAU ratio (stickiness), growth rate |
| **4. Maturity** | Can we defend and extend the business, since raw growth has slowed? | Revenue and retention are stable or grow slowly; expansion revenue and efficiency matter more than new logos | Net revenue retention (NRR), churn rate, margin |
| **5. Decline / sunset** | Should we invest, hold, or wind this down deliberately? | A clear, honest decision — sometimes "kill it well" is the best outcome | Revenue trend, cost to serve vs. revenue, migration/off-boarding completion |

Two things trip people up about this table:

- **Stage is diagnosed from evidence, not vibes or company age.** A five-year-old company can launch a genuinely new product line that's back in stage 1 for that line, while its core product sits in stage 4. Diagnose the *product* (or even the *feature area*), not just the company.
- **The "right" metric changes by stage — chasing the wrong one is a classic, expensive mistake.** A stage-1 product chasing MAU growth before it has validated the problem is optimizing a number that will collapse the moment marketing spend stops. A stage-4 product chasing raw signups while ignoring churn is filling a leaking bucket. Lecture 3's whole point: **the stage tells you which metric to trust.**

```mermaid
flowchart LR
  A["Discovery"] --> B["Validation"]
  B --> C["Growth"]
  C --> D["Maturity"]
  D --> E["Decline"]
```
*A product moves through five lifecycle stages, and the stage in play sets which metric actually matters.*

## 2. Reading stage from a metrics dashboard — worked example

Say you're handed Loopline's dashboard for the last six weeks:

| Week | New signups | Activation rate | WAU/MAU | NRR |
|------|------------:|-----------------:|--------:|-----:|
| 1 | 420 | 61% | 0.71 | — |
| 2 | 455 | 59% | 0.72 | — |
| 3 | 480 | 57% | 0.70 | — |
| 4 | 510 | 54% | 0.69 | 101% |
| 5 | 525 | 52% | 0.68 | 100% |
| 6 | 540 | 49% | 0.67 | 99% |

What's the story? New signups are climbing steadily — someone would love to point at that line and declare victory. But look at activation rate: it's falling every single week, and NRR has slipped under 100%, meaning **existing accounts are shrinking faster than they're expanding.** This is a growth-stage product where the top of the funnel is healthy but the *engine underneath it is degrading* — more people are walking in the door, and a shrinking share of them are finding value once inside. A team that only tracked signups would report a "great quarter." A team reading the whole table sees a product whose growth is being propped up by acquisition spend while the product experience itself is quietly eroding — which is exactly the kind of thing that stops being fixable once it's been true for two quarters instead of six weeks.

This is the core discipline of this lecture: **a single metric moving in a good direction proves nothing. A stage-appropriate metric read alongside its neighbors tells you the truth.** Exercise 3 gives you a fuller, twelve-week version of this exact table (as a real, queryable dataset — see the data-tooling note below) and asks you to do this diagnosis yourself, with evidence.

> **Why this table lives in a database, not a spreadsheet.** The moment metrics data needs to be stored, filtered, or joined against other tables (which cohort signed up which week, which plan tier, which segment) — the durable, correct home for it is a real table you can query, not a spreadsheet tab someone will eventually break with a stray sort. This course stores and queries data with **SQL (PostgreSQL/SQLite) and Python/pandas**, always — spreadsheets are covered separately, as a presentation surface, in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/). You'll see this pattern every week analytics comes up.

## 3. The value / viability / feasibility / usability (VVF+U) lens

Before any idea earns a spot on a roadmap, it should survive four independent questions. Miss any one of them and you get a specific, predictable kind of failure:

| Lens | Question | Fails as... |
|------|----------|-------------|
| **Value** | Do users actually want this — does it address a real pain or gain from Lecture 2's map? | A feature nobody asked for and nobody adopts |
| **Viability** | Does this work for the *business* — revenue, cost, legal, brand, strategy? | A feature users love that bankrupts or legally exposes the company |
| **Feasibility** | Can we actually build this with the time, tech, and skills we have? | An eternally-delayed project, or a rushed, broken version |
| **Usability** | Can the people it's for actually figure out how to use it? | A powerful feature nobody discovers or completes |

This is a deliberate extension of the classic three-lens model (value/viability/feasibility, popularized by Marty Cagan and IDEO's design-thinking work) — usability is added as its own explicit check because "valuable and feasible" ideas routinely die from being *un-discoverable* or *too confusing to complete*, which is a different failure than "not valuable" or "not buildable."

### Worked example: should Loopline build an AI auto-summarizer for stand-ups?

Someone on the team proposes: "Let's add an AI feature that reads all of a team's task comments overnight and writes a stand-up summary." Run the lens:

- **Value:** Does this map to a real pain from our value-prop table? Partially — "spends 30 minutes every Monday manually compiling status" is a real, evidenced pain. An AI summary attacks that directly. **Passes, with a named pain it maps to.**
- **Viability:** What does this cost to run (LLM inference at scale), and does it fit the pricing tier it would ship in? If it's only viable on the highest-priced tier, does that tier have enough of the target segment (engineering managers, our persona) to matter? Needs a real cost model before greenlighting — **not yet resolved.**
- **Feasibility:** Do we have the data pipeline to reliably pull the right comments per team, and can we hit a quality bar where the summary doesn't say something embarrassingly wrong in front of a user's own boss? **Feasible, but nontrivial — needs an eval process, not a demo.**
- **Usability:** Will managers trust an AI-written summary enough to actually read it instead of skimming manually anyway — and will they know how to correct it when it's wrong? **Untested — this is a discovery question, not an engineering one.**

Verdict: value looks real, but viability and usability are **open questions, not blockers** — which means the honest next step is a small, cheap validation (a prototype in front of five real managers, and a rough cost model), not a full build and not an outright kill. That's the practical output of the VVF+U lens: it rarely gives you a clean yes/no on the first pass. It tells you **which specific question to answer next**, and in what order, before you commit real engineering time.

### A pattern: which lens usually fails first, by lifecycle stage

- **Discovery-stage products** most often fail on **value** — the problem wasn't real or wasn't painful enough.
- **Growth-stage products** most often fail on **usability** — the value is real but the path to it is too confusing to scale past early adopters who'll push through friction.
- **Mature products** most often fail on **viability** — a feature that's technically great and usable but doesn't move revenue, retention, or cost enough to justify its maintenance burden for years to come.

This isn't a law of nature, but it's a useful prior: when you're stuck deciding which lens to interrogate hardest, ask what stage you're in first.

## 4. Strategy is a bet, made explicit

"Strategy" gets treated as a mystical executive activity. Stripped down, a product strategy is just: **given our stage and our constraints, here is the specific bet we're making about where value will come from next, and here is the metric that will tell us if we're right.** A strategy that doesn't name a metric isn't a strategy — it's an aspiration.

For a growth-stage Loopline seeing the activation decline from Section 2, a real strategic bet might read:

> "We believe activation is falling because the redesigned onboarding added friction for our core segment (mid-size software teams), not because the product is losing overall appeal. We're betting that removing the mandatory calendar-connect step recovers activation to ≥65% within two weeks. If it doesn't, the problem is upstream of onboarding and we need new discovery work, not another UI tweak."

Notice the shape: a **claim**, a **reason to believe it**, a **specific bet**, and a **falsification condition**. That last part — being willing to say what would prove you wrong — is what separates a strategy from a slogan. "We're doubling down on AI" is not a strategy by this definition. "We're betting that an AI stand-up summary saves managers 20+ minutes a week, measured by time-to-first-glance and week-4 retention of the feature; if adoption is under 15% after a month, we pull it" is.

## 5. Check yourself

- Name the five lifecycle stages and, for each, the central question it's trying to answer.
- In the six-week Loopline table (Section 2), why is "new signups are climbing" not, by itself, good news? What two other numbers changed the story?
- Walk the AI-summarizer example through all four VVF+U lenses in your own words. Which lens is the real blocker right now — and what's the cheapest way to resolve it?
- Why does this course store metrics data in SQL tables instead of a spreadsheet? What breaks about a spreadsheet as data grows — joins across cohorts, tiers, or segments?
- Write one strategic bet, in the claim/reason/bet/falsification-condition shape, for a product you use. What would have to happen for you to say the bet failed?

You now have the full toolkit for Week 1: the role (Lecture 1), the user and the job (Lecture 2), and the stage and the bet (Lecture 3). The exercises put all three to work against real data and a real product of your choosing.

## Further reading

- **Marty Cagan, "Product Vision vs. Product Strategy" (SVPG):** <https://www.svpg.com/product-vision-vs-strategy/>
- **Dan Olsen, "The Lean Product Playbook" (product-market fit framing):** <https://leanproductplaybook.com/>
- **Reforge, "North Star Metrics" (overview article):** <https://www.reforge.com/blog/north-star-metrics>
- **IDEO, "Design Thinking: Desirability, Feasibility, Viability":** <https://www.ideou.com/blogs/inspiration/how-to-balance-desirability-feasibility-and-viability-to-drive-innovation>
