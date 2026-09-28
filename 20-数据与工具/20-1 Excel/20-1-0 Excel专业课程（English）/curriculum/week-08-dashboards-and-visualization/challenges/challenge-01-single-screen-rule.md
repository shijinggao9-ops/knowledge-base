# Challenge 1 — Fit It All on One Screen

**Time:** ~60 min. **Requires:** the completed Exercise 1–3 dashboard (skeleton, connected slicers/timeline, live KPI tiles).

## The constraint

Your dashboard from the exercises works. This challenge adds a hard, **measured** constraint on top of "works": the entire dashboard — title, all four KPI tiles, all three charts, the filter zone — must be fully visible with **zero scrolling, in either direction**, at:

- **Window size:** 1366×768 pixels (a common budget/older laptop resolution — smaller than the 1440×900+ most people develop on).
- **Zoom level:** 100% (no cheating by zooming out to 70% to make more fit — that's not how a viewer will actually open the file).
- **Ribbon/toolbar visible** — don't measure against a maximized, chrome-free full-screen view; measure against how the app actually looks when someone opens it normally.

## Steps

1. Resize your application window (or, if you can't resize below your monitor's native resolution, use `View → Zoom` combined with a ruler/measurement check against a 1366×768 reference — the goal is realism about a smaller screen, however you simulate it) to the target size.
2. Look at your dashboard at that size. List, honestly, **everything that doesn't fit** — a chart clipped at the edge, a KPI tile wrapping to two lines, a slicer panel pushed off-screen.
3. For each item on that list, make one of these three decisions, and write down which one you made and why:
   - **Cut it entirely** — it wasn't earning its space against the governing question from Lecture 1 (this is often the *right* answer, not a failure — dashboards that keep everything usually fail this constraint for a reason).
   - **Resize/compress it** — shrink a chart, tighten a KPI tile's padding, merge two smaller charts' zones — without losing the information it was there to convey.
   - **Replace it with something more compact** — e.g., swap a full bar chart for a sparkline (Lecture 3) if the full chart's precision wasn't actually needed at dashboard-glance scale.
4. Rebuild the dashboard against the constraint using those decisions. Re-measure. Repeat until it genuinely fits with no scrolling.
5. Re-run all four slicer/timeline tests from Exercise 2, Part C, and the full test pass from Exercise 3, Part F — the constraint pass must not have broken any live-filtering behavior.

## Deliverable

The resized `Dashboard` sheet itself, plus a short `single-screen-notes.md` (150-250 words) listing:

1. What you cut entirely, and why it didn't survive the "does this help answer the governing question" test.
2. What you resized/compressed, and what you specifically did to preserve its meaning at the smaller size.
3. One thing you were tempted to cut but decided to keep, and why you think it earned its space.

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Fits the constraint | 35% | Genuinely no scrolling at 1366×768, 100% zoom — verified, not estimated |
| Still functionally correct | 30% | All slicer/timeline/KPI tests from the exercises still pass after resizing |
| Cutting discipline | 20% | Choices are justified against the governing question, not arbitrary |
| Write-up clarity | 15% | The three required points are answered specifically, with real reasoning |

## Why this matters

Every real dashboard eventually meets someone on a smaller screen, an older laptop, or a projector at a meeting — and "it looked fine on my monitor" is not a standard a dashboard survives contact with. This challenge forces the actual skill from Lecture 1's single-screen rule: making hard content choices under a real constraint, not designing in a vacuum and hoping it fits later.
