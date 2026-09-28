# Mini-Project — Answer 15 Sales Questions With Pivots + Pivot Charts

> Answer 15 real business questions about Crunch Outfitters' first half of 2025 using **only** pivot tables and pivot charts built from the `Transactions` Table. Every question requires at least one grouped period, a percentage breakdown, or a chart — this is the week's capstone, and it's built to force you through the full toolkit, not just the easy parts.

**Estimated time:** 2.5–3 hours, best done Saturday after the exercises and challenges.

Unlike Challenge 1 (fast, single-number answers), this mini-project asks you to actually **present** each answer — a pivot, a chart where specified, and a sentence of interpretation a sales director could read without opening the workbook. That's the real shape of analytics work: nobody hands you a finished chart to admire, they hand you a raw export and a list of questions, and your value is the whole pipeline from data to a trustworthy, presentable answer.

---

## Deliverable

A dedicated area of your `crunch-week7` workbook (a `Mini-Project` sheet group, or one sheet per question — your call, as long as it's navigable) containing:

1. **15 pivot tables**, one per question, each clearly labeled with the question it answers.
2. **At least 8 pivot charts** (specified per-question below — some questions require a chart, some don't, but the total across the project must be at least 8).
3. `report.md` (or a `Report` sheet) — for each of the 15 questions: the answer in one to two sentences, referencing the actual numbers.
4. `notes.md` — a short reflection (see the end).

Everything runs against the `Transactions` Table from the [week README](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/README.md). Note whether you built this in Excel, Google Sheets, or both.

---

## The 15 questions

### A. Grouped periods (quarters and months)

1. **Chart required.** Group `OrderDate` by Quarter and build a bar chart comparing Q1 vs. Q2 revenue. By how much did Q2 outperform Q1, in both dollars and percent?
2. **Chart required.** Build a monthly revenue **line chart**. Camping shows a strong seasonal spike in one specific month, followed by a sharp drop the next. Which month peaked, and by how much (dollars and %) did the following month fall?
3. **Chart required.** Build a **running total** line chart of monthly revenue (Show Values As → Running Total In). In which month did cumulative H1 revenue first cross the halfway point of the full six-month total?
4. Build a pivot comparing monthly **order count** to monthly **average order value**. In the single strongest revenue month, was the lead driven more by *more orders* or by *bigger orders*? Support your answer with both numbers.

### B. Percentage breakdowns

5. **Chart required.** Build a Category-by-revenue pivot with Show Values As → % of Grand Total, and chart it as a sorted bar chart. Which category would you recommend for increased marketing budget next quarter, and why — cite its % share?
6. **Chart required.** Build a Region-in-Rows, Channel-in-Columns pivot with Show Values As → % of Row Total, and chart it as a 100% stacked column. Which region is the most Online-dependent, by percentage — and which is the least?
7. Within the **West** region specifically, build a % of Row Total breakdown by Category. Which single category dominates West's revenue mix, and what's its share?
8. Build a % of Grand Total pivot for the top 5 individual products (filter to the top 5 by revenue). Which single product contributes the largest share of total H1 revenue, and what is that share?

### C. Rank, calculated fields, and distributions

9. **Chart required.** Build a sales-rep revenue **ranking** pivot (Show Values As → Rank Largest to Smallest) and chart it as a sorted bar chart. What's the dollar gap between the #1 rep and the #8 (last-place) rep?
10. Add a calculated field `RevenuePerUnit = TotalRevenue/Units`, broken out by Category. Which category has the **lowest** revenue per unit sold, and would you flag it for a pricing review?
11. **Chart required.** Using the `Units` binning from Exercise 2, build a bar chart (histogram) of order-size distribution. What's the most common order-size bucket, and how many orders fall in it?

### D. Filtered and multi-dimension views

12. **Chart required.** Filter the pivot to the **Wholesale channel only**, then break it out by Region and chart it. Which region's Wholesale channel looks like the best candidate for expansion, based on current revenue?
13. Build a two-level pivot: `Region` in Rows, `Channel` nested inside, Sum of `TotalRevenue` in Values. Without changing any settings, does the region ranking (by total revenue) match the ranking you found back in Challenge 1? State yes/no and why that's expected.
14. Compare Online's average order value to Wholesale's average order value across the whole dataset. Which channel has a higher average order — and does that surprise you given Online has by far the most total revenue?

### E. Executive summary

15. **Chart required.** Of all the charts you built in this mini-project, pick the **one** you'd put on slide 1 of the H1 business review if you could only show a single chart. Justify your choice in 3–4 sentences, referencing at least two specific numbers from elsewhere in this project.

---

## Milestones

Pace yourself; don't try to do all 15 in one sitting.

- **Milestone 1 (45 min):** Questions 1–4 (grouped periods). Get comfortable with Quarter/Month grouping and running totals again before moving on.
- **Milestone 2 (45 min):** Questions 5–8 (percentage breakdowns). This is where Show Values As earns its keep.
- **Milestone 3 (45 min):** Questions 9–11 (rank, calculated fields, distribution).
- **Milestone 4 (30–45 min):** Questions 12–14 (filters and multi-dimension views).
- **Milestone 5 (15–20 min):** Question 15 (executive summary) + `notes.md` reflection.

---

## Rules

- **Every chart must be a pivot chart** — built directly from a pivot table (PivotChart in Excel; a chart sourced from the pivot's output in Sheets) — not a static chart pointing at a manually copy-pasted range.
- **At least 8 of the 15 questions must include a chart** (marked "Chart required" above); you're welcome to chart more than the minimum.
- **Every percentage answer must come from Show Values As**, not a manually typed division formula — that's the entire point of this week's toolkit.
- **State your pivot configuration** for each question in `report.md` (which fields, which zones, which grouping/Show Values As setting) so every answer is rebuildable by someone else.
- **Follow Lecture 3's readability rules** on every chart: zero baseline on bar/column charts, a title that states the finding, no unnecessary legends, no 3D.

---

## Rubric

| Criterion | Weight | "Great" looks like |
|-----------|------:|--------------------|
| Correctness | 35% | All 15 answers are numerically right, verified against a rebuildable pivot |
| Chart quality | 25% | All required charts present, built as true pivot charts, following Lecture 3's readability rules |
| Percentage/grouping technique | 20% | Show Values As and date/number grouping used correctly, not faked with manual formulas |
| Interpretation | 10% | `report.md` states the answer in words with real numbers, not just a screenshot |
| Executive summary (Q15) | 10% | A genuinely defensible single-chart choice, justified with specific numbers |

---

## Reflection (`notes.md`, ~200 words)

1. Which question forced you to combine the most techniques (grouping + calculated field + Show Values As, say) — walk through how you built it.
2. Where did Count and Sum (or Average and Sum) disagree in this project, and which one turned out to matter more for the business question being asked?
3. Which chart type felt like it did the most work with the least effort — i.e., communicated the most for the amount of setup it took?
4. If Crunch Outfitters gave you a second half of the year's data tomorrow, which of your 15 pivots would you keep exactly as-is (because a Table source auto-expands them), and which would need manual rework?

---

## Why this matters

This mini-project is the shape of real analytics and BI work: someone hands you a raw export and a list of business questions, and your value is turning each one into a correct, presentable, chartable answer — fast. Fifteen questions across quarters, percentages, ranks, calculated fields, and filtered views is enough repetition that pivot configuration should start to feel like a small, fixed vocabulary you reach for automatically, the same way `WHERE` and `GROUP BY` become automatic in SQL. Keep this workbook — Week 8 takes several of these exact pivots and charts and assembles them into a single interactive dashboard screen.

When done: save your work, then take the [quiz](20-数据与工具/20-1%20Excel/20-1-0%20Excel专业课程（English）/curriculum/week-07-pivot-tables-and-charts/quiz.md) and start [Week 8 — Dashboards & visualization](../../week-08-dashboards-and-visualization/).
