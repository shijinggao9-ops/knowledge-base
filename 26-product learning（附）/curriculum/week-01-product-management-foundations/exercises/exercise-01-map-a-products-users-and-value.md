# Exercise 1 — Map a Product's Users and Value

**Goal:** Take everything from Lecture 2 — segments, personas, JTBD, value proposition — and apply the full chain to a real product you actually use. By the end, you can look at any app on your phone and produce this analysis in under 20 minutes.

**Estimated time:** 60–75 minutes.

## Setup

Pick a real product you use at least weekly and know reasonably well. Good choices: a note-taking app, a fitness tracker, a food-delivery app, a work tool (Slack, Notion, Linear), a banking app. Avoid picking something you've never actually used — you need real behavior to reason from, not a marketing page.

Write your answers in a file `product-map.md`.

## Tasks

1. **Name the product and one sentence on what it is.** No marketing copy — describe it the way you'd explain it to a friend who's never heard of it.

2. **Identify 2–3 segments.** Who uses this product, grouped by observable traits (role, context, technical sophistication, etc.)? For each segment, list 2–3 defining traits. *(Reminder: a segment is not yet a job — resist describing what they want here, just who they are.)*

3. **Pick one segment and build a lightweight persona.** Give them a name, 3–4 concrete traits, and one sentence on their situation when they'd open this product. Every trait must be something you could plausibly observe about a real person — not invented backstory.

4. **Write a JTBD statement for your persona**, using the template from Lecture 2:
   > When **[situation]**, I want to **[functional job]**, so I can **[expected outcome]**.

   Then answer, in one sentence each: what's the *functional* layer of this job, what's the *emotional* layer, and is there a *social* layer (there isn't always one — say so if not)?

5. **Run the "is this a disguised feature request?" test** on your own JTBD statement from Task 4. Does it describe a durable outcome independent of any specific tool? If you find yourself naming a button or a screen, push "why" at least once more and rewrite it.

6. **Build the pains/gains → pain relievers/gain creators table** from Lecture 2, with at least 2 rows in each column, specific to your persona's job.

7. **Write one sentence of "value proposition"** that a stranger could read and understand exactly what the product does about which pain — no slogans ("helps you stay organized" is banned; name the specific behavior).

## Expected outcome (self-check)

- Your JTBD statement (Task 4) should **not** contain the product's own name or any of its feature names. If it does, you've described the solution, not the job.
- Your pain relievers and gain creators (Task 6) should each name a **specific, checkable product behavior** — something you could point at in the actual app.
- A friend who has never used the product should be able to read your Task 7 sentence and understand exactly what problem it solves for whom — without needing to have seen the app.

## Done when…

- [ ] `product-map.md` has all 7 tasks answered.
- [ ] Task 4's JTBD statement survives the disguised-feature-request test from Task 5 (or was rewritten until it does).
- [ ] Task 6's table has at least 2 rows per column, each specific and checkable.
- [ ] You could explain your persona (Task 3) to someone else in 30 seconds without reading off the page.

## Stretch

- Build a second JTBD statement for a *different* segment of the same product (Task 2). Compare: does the product serve both jobs well, or is it clearly optimized for one at the expense of the other?
- Find one feature in the product that does **not** map to any row in your pains/gains table. Is it dead weight, or does it reveal a job you missed?

## Submission

Commit `product-map.md` to your portfolio under `c44-week-01/exercise-01/`.
