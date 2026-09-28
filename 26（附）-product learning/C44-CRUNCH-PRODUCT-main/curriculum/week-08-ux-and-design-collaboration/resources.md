# Week 8 — Resources

Free, public, no signup unless noted. Read the "required" set; treat the rest as reference you dip into when a specific question comes up.

## Install / set up first

- **PostgreSQL 16+ or SQLite 3.35+** — same requirement as every SQL-touching week in this course. See [C33 · Crunch SQL's resources](../../../C33-CRUNCH-SQL/curriculum/week-01-relational-model-and-select/resources.md) for install steps if you haven't already. SQLite is the fastest path if this is your first setup.
- **A contrast checker** — [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/), free, browser-based, no signup. Used in Lecture 3 and Exercise 3's accessibility pass.
- **WAVE** — [wave.webaim.org](https://wave.webaim.org/), free automated accessibility scanner, works on any public URL or as a browser extension. Used in Homework Problem 4.
- **Chrome DevTools Lighthouse** — built into Chrome (F12 → Lighthouse tab), free, includes an accessibility audit alongside performance/SEO. No install needed if you have Chrome.

## Required reading (this week's core)

- **Nielsen Norman Group — "10 Usability Heuristics for User Interface Design":**
  <https://www.nngroup.com/articles/ten-usability-heuristics/>
  *Why: the canonical list this whole week's heuristic-evaluation method is built on.*
- **Nielsen Norman Group — "Why You Only Need to Test with 5 Users":**
  <https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/>
  *Why: the original research behind Lecture 2's central claim — read it once, you'll cite it for the rest of your career.*
- **Nielsen Norman Group — "Thinking Aloud: The #1 Usability Tool":**
  <https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/>
  *Why: the technique your Exercise 2 sessions depend on — moderator behavior matters as much as the tasks you write.*
- **W3C — "Web Content Accessibility Guidelines (WCAG) 2.1 Overview":**
  <https://www.w3.org/WAI/standards-guidelines/wcag/>
  *Why: the source document behind every accessibility claim this week makes — skim the overview, don't try to read the full spec.*

## Reference (keep in tabs)

- **Nielsen Norman Group — "How to Conduct a Heuristic Evaluation":** <https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/>
  *Why: the step-by-step method behind Exercise 1 and Exercise 3.*
- **Nielsen Norman Group — "Severity Ratings for Usability Problems":** <https://www.nngroup.com/articles/how-to-rate-the-severity-of-usability-problems/>
  *Why: the 0–4 scale used throughout this week, explained in more depth.*
- **Nielsen Norman Group — "Moderated vs. Unmoderated Usability Testing":** <https://www.nngroup.com/articles/moderated-unmoderated-usability-testing/>
  *Why: when to graduate from Exercise 2's moderated sessions to a scaled unmoderated approach.*
- **W3C — "Understanding the Four Principles of Accessibility" (POUR):** <https://www.w3.org/WAI/WCAG21/Understanding/intro#understanding-the-four-principles-of-accessibility>
  *Why: the four-bucket mental model Lecture 3 uses to sort every accessibility finding.*
- **WebAIM — "Contrast and Color Accessibility":** <https://webaim.org/articles/contrast/>
  *Why: the practical, non-legalese explanation of *why* the 4.5:1 ratio exists and how to hit it.*
- **Nielsen Norman Group — "Design Critiques: Encourage a Positive Culture to Improve Products":** <https://www.nngroup.com/articles/design-critiques/>
  *Why: running a critique session well, beyond just the I Like / I Wish / What If structure.*

## Practice beyond this week's exercises

- **A11y Project — "Checklist":** <https://www.a11yproject.com/checklist/>
  *Why: a free, community-maintained, practical accessibility checklist — less formal than the WCAG spec, faster to scan.*
- **Baymard Institute — free articles on checkout UX:** <https://baymard.com/blog>
  *Why: real, research-backed teardowns of e-commerce and checkout friction — the closest free analog to Loopline's checkout flow this week, from real audited products.*
- **Mermaid Live Editor** — <https://mermaid.live/>
  *Why: paste this week's Mermaid flow-diagram snippets in and see them rendered instantly, no install.*

## Glossary

| Term | Definition |
|------|------------|
| **User flow** | The sequence of screens and actions a person moves through to accomplish one goal. |
| **Friction** | Anything that makes a step harder, slower, or scarier than it needs to be — not automatically bad, but always worth judging. |
| **Heuristic evaluation** | A structured review of an interface against a checklist (Nielsen's 10) to find likely usability problems without a user test. |
| **Severity rating** | Nielsen's 0–4 scale rating how serious a usability problem is, from cosmetic (1) to catastrophic (4). |
| **Think-aloud protocol** | Asking a test participant to narrate their thoughts continuously while working, revealing their mental model in real time. |
| **Goal-based task** | A usability-test instruction that states the user's goal without leaking the UI steps to reach it. |
| **5-user rule** | Nielsen's finding that ~5 participants in a usability test typically surface ~85% of a flow's usability problems. |
| **Moderated / unmoderated testing** | Moderated: you watch live and can probe. Unmoderated: participants record themselves alone, reviewed later. |
| **I Like / I Wish / What If** | A critique framework: name what's working, name a specific grounded problem, propose a direction as a question. |
| **WCAG** | Web Content Accessibility Guidelines — the W3C's standard for accessible web content, with A/AA/AAA conformance levels. |
| **POUR** | WCAG's four principles: Perceivable, Operable, Understandable, Robust. |
| **Contrast ratio** | A measure of how distinguishable text is from its background; WCAG AA requires 4.5:1 for normal text, 3:1 for large text. |
| **Trade-off framework (impact/cost/risk/reversibility)** | The four inputs this course uses to make and defend a ship-now-vs-fix-first decision. |

---

*Broken link? Open an issue or PR.*
