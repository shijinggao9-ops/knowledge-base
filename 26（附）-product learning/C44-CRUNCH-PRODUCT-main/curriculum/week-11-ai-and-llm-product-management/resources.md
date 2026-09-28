# Week 11 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up. Provider pricing and specific model names move fast — treat any dollar figure anywhere in this week's lectures as illustrative, and check the current pricing page before committing a real budget.

## Install first

This week's data work is three small seed tables — ready-made queries, no new tooling category beyond what earlier weeks already set up.

- **SQLite 3.35+** — the zero-setup engine; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **PostgreSQL 16+** — the course's primary engine since Week 6: <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **Python 3.10+ with pandas**: `pip install pandas sqlalchemy psycopg2-binary` — <https://pandas.pydata.org/docs/getting_started/install.html>
- **A plain Markdown editor** — anything works (VS Code, Obsidian, even a plain text editor). This week's written deliverables are all Markdown files in your portfolio.

## Required reading (this week's core)

- **Anthropic — "Building Effective AI Agents":** <https://www.anthropic.com/research/building-effective-agents>
  *Why: the clearest short statement of when a model-driven approach earns its complexity versus a simpler deterministic system — read before Lecture 1.*
- **Hamel Husain — "Your AI Product Needs Evals":** <https://hamel.dev/blog/posts/evals/>
  *Why: the practitioner essay this course's eval methodology is closest to in spirit — read before Lecture 2.*
- **OWASP — "LLM Top 10":** <https://owasp.org/www-project-top-10-for-large-language-model-applications/>
  *Why: the standard reference for prompt injection and the other failure modes Lecture 3's safety guardrails address.*
- **Google — "People + AI Guidebook":** <https://pair.withgoogle.com/guidebook/>
  *Why: Google's design-pattern reference for human-in-the-loop AI product design, covering the same four-pattern spectrum Lecture 3 Section 2 walks through, in more visual depth.*

## Reference (keep in tabs)

- **OpenAI — "A Practical Guide to Building Agents":** <https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf>
  *Why: a second vendor's take on scoping and guardrail-ing an LLM-backed feature, useful to compare against Anthropic's framing.*
- **OpenAI — "Evals" documentation:** <https://platform.openai.com/docs/guides/evals>
  *Why: a concrete, vendor-provided implementation of the golden-set + grading pattern from Lecture 2, if you want to see a production tool built around the same idea.*
- **Anthropic — "Building evals and test cases":** <https://docs.claude.com/en/docs/test-and-evaluate/develop-tests>
  *Why: a second worked walkthrough of eval-set construction, useful alongside Hamel Husain's essay.*
- **Eugene Yan — "Task-Specific LLM Evals that Do and Don't Work":** <https://eugeneyan.com/writing/llm-evaluators/>
  *Why: a grounded, skeptical look at where LLM-as-judge grading (Lecture 2, Section 3) actually holds up and where it doesn't.*
- **OpenAI — "Safety best practices":** <https://platform.openai.com/docs/guides/safety-best-practices>
  *Why: a vendor checklist that overlaps heavily with Lecture 3's safety-guardrail section — good for cross-checking your own guardrail table.*
- **Anthropic — "Responsible Scaling Policy":** <https://www.anthropic.com/news/anthropics-responsible-scaling-policy>
  *Why: shows how safety-guardrail thinking scales from a single feature (this week's scope) up to an entire frontier model program — useful context, not something you need to replicate.*

## Practice beyond this week's exercises

- **A real changelog or release-notes page from any AI-featured product you use** — search "[product name] AI feature release notes."
  *Why: essential raw material for Homework Problem 5's product comparison — you're looking for public evidence of scope, HITL design, and guardrails.*
- **Any public model provider's pricing page** (search "[provider] API pricing")
  *Why: ground Lecture 1 Section 5's cost/latency/quality triangle in real, current numbers rather than this week's illustrative figures — useful for Challenge 2's arithmetic.*

## Deeper background (optional this week)

- **Clayton Christensen, "The Innovator's Dilemma"** (book)
  *Why: the Week 1 resource list flagged this book as relevant again here — a useful lens on why "add the trendy new technology" pressure (this week's opening scenario) hits every incumbent product team eventually, and why disciplined scoping is the actual differentiator, not the technology itself.*
- **Cal Newport, "A Skeptical Take on the AI Revolution"** (essay/talk, widely available) — search the title.
  *Why: a deliberately contrarian read to hold up against this week's material — a healthy habit before writing an AI feature spec is being able to argue the "don't build it" side of the fit checklist convincingly, not just the "yes, build it" side.*

## Glossary

| Term | Definition |
|------|------------|
| **Deterministic feature** | Same input always produces the same, exactly-specifiable output. |
| **Probabilistic feature** | Same input can produce different, still-plausible outputs across calls — the defining property of an LLM-backed feature. |
| **Fit checklist** | The five-question test (Lecture 1) for whether a feature genuinely needs an LLM rather than rules, classic ML, or nothing. |
| **Build vs. buy (for AI)** | The choice between a rules engine, a classic trained ML model, prompting a foundation model API, or fine-tuning one. |
| **Cost/latency/quality triangle** | The three-way tradeoff every model-tier choice makes; optimizing two typically costs you the third. |
| **Human-in-the-loop (HITL)** | Any design where a human reviews, confirms, or gates a model's output before it takes effect; ranges from suggest-only to full autonomy. |
| **Golden eval set** | A fixed, reusable set of input cases with rubrics, used to score a feature's output quality repeatably. |
| **Rubric** | A specific, checkable description of what a good output looks like for a given eval case. |
| **LLM-as-judge** | Using a second model call to grade a first model's output against a rubric, at a scale human grading can't match. |
| **Offline evaluation** | Running the golden eval set against a candidate prompt/model version before shipping. |
| **Online evaluation** | Monitoring real production outputs and user feedback after shipping. |
| **Hallucination** | A model stating something false or invented with the same fluent confidence as a true statement. |
| **Guardrail** | A concrete, testable control against a specific failure mode — hallucination, cost, or misuse — not a general monitoring promise. |
| **Prompt injection** | An attempt, via user input, to override a model's original instructions or extract information it shouldn't reveal. |
| **Kill switch** | A single flag that disables an AI feature immediately, without a deploy, falling back to a manual/deterministic path. |

---

*Broken link? Open an issue or PR.*
