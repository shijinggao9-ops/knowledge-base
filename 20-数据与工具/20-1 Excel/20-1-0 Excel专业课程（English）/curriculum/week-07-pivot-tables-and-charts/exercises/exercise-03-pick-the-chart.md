# Exercise 3 — Pick the Right Chart

**Goal:** Practice matching a chart type to a question, building both standalone and pivot charts, and applying the readability rules from Lecture 3 (zero baseline, sorted bars, direct titles, no chart-junk).

**Estimated time:** 45 minutes.

## Setup

Continue in `crunch-week7`. Create a new sheet named `Ex3-Charts` for this exercise's work. You'll build on top of pivots from Exercises 1 and 2 — feel free to rebuild them fresh here if that's cleaner.

## Tasks

For each question below: (a) state which chart type you'll use and why in one sentence, (b) build the pivot that feeds it, (c) build the pivot chart, (d) apply at least one readability fix from Lecture 3 (zero baseline, sort by value, a title that states the finding, or removing an unnecessary legend/gridline).

1. **"Which region sold the most?"** *(Comparison of 4 discrete categories at a single point in time.)*

2. **"Is revenue trending up or down across the six months?"** *(Change over a continuous time axis.)*

3. **"What's each category's share of total revenue?"** — build this **twice**: once as a pie chart, once as a sorted bar chart. Time yourself (roughly) answering "which is bigger, Footwear or Electronics" from each. Write one sentence on which was faster and why.

4. **"How does channel mix differ across regions?"** *(Part-to-whole comparison across 4 groups — a job no single pie chart can do alone.)*

5. **"What's the shape of order sizes — are most orders small, medium, or large?"** *(Use your binned `Units` pivot from Exercise 2, Task 3, as a histogram-style bar chart.)*

## Expected result (spot checks)

- Task 1 → your bar/column chart's tallest bar is North.
- Task 2 → your line chart visibly dips in February and peaks in May.
- Task 3 → your bar chart should let you answer "which is bigger" almost instantly; the pie chart should take noticeably longer, especially between two similarly-sized wedges like Footwear (21.0%) and Electronics (24.7%).
- Task 4 → West's chart segment for Wholesale should be visibly larger than North's, East's, or South's Wholesale segments.

## Done when…

- [ ] Five charts exist on `Ex3-Charts`, each preceded by your one-sentence "which chart type and why."
- [ ] Every chart has a title that states a finding, not just a generic field-name label.
- [ ] Every bar/column chart's y-axis starts at zero.
- [ ] Task 3's written comparison (pie vs. bar) is filled in.
- [ ] At least 2 of the 5 charts are true **pivot charts** (built via PivotChart / Insert Chart from a pivot), not static charts pointing at a copy-pasted range.

## Stretch

- Take any one chart you built and deliberately break two of Lecture 3's rules (truncate the y-axis, add a 3D effect, swap in a legend where a direct label would work better). Screenshot or describe both versions side by side and write two sentences on which specific comparisons got harder to make in the "broken" version.
- Build a chart with a filter control wired to it (Excel: a Slicer connected to the pivot; Sheets: a filter on the source or pivot) so a viewer could switch the region shown without touching the underlying pivot fields. (This is a preview of Week 8's dashboard work — don't worry if it takes some trial and error.)

## Submission

Keep `Ex3-Charts` in your `crunch-week7` workbook — no separate file needed, but be ready to walk through your chart choices if asked in review.
