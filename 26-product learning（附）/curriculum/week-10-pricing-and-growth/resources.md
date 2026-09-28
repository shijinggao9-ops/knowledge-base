# Week 10 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install first

This week's modeling gets real — a subscription book, a growth-loop event log, and a channel comparison, all queried and then projected forward in pandas. Make sure both engines and the Python stack are ready before Lecture 3.

- **SQLite 3.35+** — the zero-setup engine; ships on macOS and most Linux already: <https://www.sqlite.org/download.html>. Check with `sqlite3 --version`.
- **PostgreSQL 16+** — the course's primary engine: <https://www.postgresql.org/download/> · macOS: [Postgres.app](https://postgresapp.com/) is the easiest. Linux: `sudo apt install postgresql` / `sudo dnf install postgresql-server`. Windows: the EDB installer.
- **Python 3.10+ with pandas**, required this week (not optional, unlike some earlier weeks): `pip install pandas sqlalchemy psycopg2-binary` — <https://pandas.pydata.org/docs/getting_started/install.html>
- **A plain Markdown editor** — anything works (VS Code, Obsidian, even a plain text editor). Most of this week's deliverables are Markdown files plus the `.sql`/`.py` scripts you write along the way.

## Required reading (this week's core)

- **Patrick Campbell / ProfitWell (now Paddle), "The Ultimate Guide to SaaS Pricing":** <https://www.paddle.com/resources/saas-pricing-guide>
  *Why: the clearest practitioner-level walkthrough of pricing models and packaging mechanics — read before Lecture 1.*
- **Van Westendorp Price Sensitivity Meter (methodology overview):** <https://en.wikipedia.org/wiki/Van_Westendorp%27s_Price_Sensitivity_Meter>
  *Why: the exact four-question method used in Lecture 1, Section 4 and Exercise 1's stretch goal.*
- **Andrew Chen, "Growth Loops are the New Funnels":** <https://andrewchen.com/growth-loops-are-the-new-funnels/>
  *Why: the essay that popularized the loop-vs-funnel distinction this week's Lecture 2 is built on — read before Lecture 2.*
- **Reforge, "Growth Loops":** <https://www.reforge.com/blog/growth-loops>
  *Why: a deeper practitioner breakdown of the four loop types and how to instrument them, extending Lecture 2's coverage.*
- **ChartMogul, "MRR — Monthly Recurring Revenue":** <https://chartmogul.com/metrics/mrr/>
  *Why: the clean, canonical vocabulary (MRR, ARPU, churn types) used throughout Lecture 3 — read before Lecture 3.*

## Reference (keep in tabs)

- **Openview Partners, "SaaS Pricing Strategy":** <https://openviewpartners.com/blog/saas-pricing-strategy/>
  *Why: a second practitioner take on tiering and packaging, useful cross-reference for Exercise 1.*
- **SaaS Capital, "What is a Good Churn Rate?":** <https://www.saas-capital.com/blog-posts/what-is-a-good-churn-rate-for-saas-companies/>
  *Why: benchmark context for reading the 13.3% logo churn rate in this week's `subscriptions` data.*
- **Dave McClure, "Startup Metrics for Pirates" (AARRR):** <https://500.co/startup-metrics/>
  *Why: the original funnel framework referenced in Lecture 2, Section 7, for contrast with loop thinking.*
- **Brian Balfour, "The Never Ending Road to Retention":** <https://www.reforge.com/blog/retention>
  *Why: on why retention itself behaves like a compounding growth lever, extending this week's loop math to a fourth loop type.*
- **pandas documentation, "Essential Basic Functionality":** <https://pandas.pydata.org/docs/user_guide/basics.html>
  *Why: reference for the DataFrame operations used in Lecture 3, Section 5 and the mini-project's `growth-model.py`.*

## Practice beyond this week's exercises

- **Any real SaaS pricing page** — Slack, Notion, Datadog, Linear, Figma are all good, varied examples.
  *Why: essential for Homework Problem 1's pricing-page audit; the more real pages you dissect, the faster tiering patterns become obvious on sight.*
- **A subscription you personally pay for**
  *Why: the anchor for Homework Problem 4's self-administered Van Westendorp drill — the method lands differently once you've run it on yourself.*

## Deeper background (optional this week)

- **Patrick Campbell, "Pricing Page Teardown" series (ProfitWell/Paddle blog archive):** search Paddle's resources hub for current teardown posts.
  *Why: dozens of real, dissected pricing pages if Homework Problem 1 leaves you wanting more reps.*
- **Reforge, "North Star Metrics":** <https://www.reforge.com/blog/north-star-metrics> (also cited in Week 1)
  *Why: revisit it now that Loopline's North Star (Weekly Active Teams) has real pricing and growth models pointed at it.*

## Glossary

| Term | Definition |
|------|------------|
| **Seat-based pricing** | Price scales with the number of users inside an account; fits products whose value scales with headcount. |
| **Usage-based pricing** | Price scales with a metered unit of consumption (API calls, storage, compute); fits when cost-to-serve tracks usage. |
| **Freemium** | A fully functional free tier alongside a paid tier unlocked by a value threshold; fits products with strong network/viral effects. |
| **Packaging** | The decision of how many tiers exist and what's gated into each, independent of the underlying pricing model. |
| **Value-metric gate** | A tier boundary defined by something the customer directly experiences and would agree justifies the price step. |
| **Anchoring** | The effect where an early-seen price (e.g., a top tier) shapes how reasonable a later price (e.g., the middle tier) appears. |
| **Van Westendorp Price Sensitivity Meter** | A four-question interview method for finding an acceptable price range without asking a single, biased direct-price question. |
| **Growth loop** | A cycle where a user action produces output that becomes the next cycle's input — self-reinforcing, unlike a funnel. |
| **Funnel** | A linear sequence of steps where input always has to come from outside the system. |
| **k-factor (viral coefficient)** | Invites per active user × invite-to-new-active-user conversion rate; the expected number of new active users each active user produces through a loop. |
| **Cycle time** | How long one loop iteration takes, from an existing user's action to the new user becoming active enough to repeat it. |
| **MRR (Monthly Recurring Revenue)** | Total recurring revenue normalized to a monthly figure, computed off net (post-discount) price. |
| **ARPU (Average Revenue Per User/seat)** | MRR divided by total active seats/users — the blended average price actually being paid. |
| **Logo churn** | The share of accounts (regardless of size) that cancel in a period. |
| **Revenue churn** | The share of MRR lost to cancellations in a period — weighted by account size, unlike logo churn. |
| **Risk-adjusted projection** | A revenue forecast that discounts naive projected revenue by an explicit, stated probability of churn per segment or price-change bracket. |
| **North Star metric** | The single metric a team treats as the best proxy for durable product value (Loopline's: Weekly Active Teams). |

---

*Broken link? Open an issue or PR.*
