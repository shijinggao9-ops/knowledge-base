# Challenge 1 — Answer 15 Questions With Pivots

**Time:** ~90 minutes. **Difficulty:** Medium. **These have right answers — check yours.**

## The scenario

You're the analyst at Crunch Outfitters. The sales director drops by with a list of 15 questions about the first half of 2025, asked the way real stakeholders ask questions — fast, in plain English, one after another, expecting a number back within a minute or two of each one. Your job: build (or reuse/reconfigure) a pivot table for each question and read off the answer. Unlike Challenge 2, these questions have objectively correct answers — your job is accuracy and speed, not judgment.

## Your task

For each question:

1. Build or reconfigure a pivot table against the `Transactions` Table to answer it.
2. Write the answer as a single sentence in `challenge-01.md` (or a `Notes` sheet), e.g., "North generated the most revenue at $8,666.93."
3. Note which pivot **zone configuration** you used (which fields in Rows/Columns/Values/Filters, which aggregation, any grouping or Show Values As) — one short line per question is enough.

You do not need 15 separate pivot tables — many of these questions can be answered by reconfiguring the same one or two pivots. Part of the skill this challenge builds is recognizing when you can reuse a pivot versus when you genuinely need a new configuration.

## The 15 questions

1. What is total revenue across all 86 transactions?
2. How many orders were placed in total?
3. Which region generated the most revenue, and how much?
4. Which product category has the highest **total revenue**?
5. Which product category has the most **orders** (by count) — is it the same category as Q4?
6. What is the average order value company-wide?
7. Which sales channel has the highest **average** order value?
8. What percentage of total revenue came from the Camping category?
9. Which month had the lowest revenue, and which had the highest?
10. What is the cumulative (running total) revenue through the end of March (Q1)?
11. Which sales rep ranks #1 by total revenue? Which ranks last?
12. Within the North region specifically, what percentage of its revenue came through the Online channel?
13. Which region relies most heavily on the Wholesale channel, in dollar terms?
14. What is the single largest individual order in the dataset — which region, which rep, which product, and for how much?
15. Using a calculated field for revenue-per-unit (`TotalRevenue / Units`), which product category has the highest revenue per unit sold?

## Constraints

- Every answer must come from a pivot table you can point to — no manually scanning the raw 86 rows and eyeballing a total. The whole point of this week is that the pivot does the counting.
- State the pivot configuration for each answer (Rows/Columns/Values/Filters/grouping used), not just the final number — a number with no traceable configuration isn't trustworthy the way a rebuildable pivot is.
- Round dollar answers to 2 decimal places; round percentages to 1 decimal place.

## Hints

<details>
<summary>On Q5 vs Q4 (count vs. sum)</summary>

Build one pivot with `Category` in Rows and **both** `OrderID` (Count) and `TotalRevenue` (Sum) in Values, side by side. You'll be able to answer both Q4 and Q5 from the same pivot, and directly see whether they agree.

</details>

<details>
<summary>On Q15 (calculated field)</summary>

See Lecture 2 §3. The calculated field divides the **group's total** revenue by the **group's total** units — not an average of each row's per-unit price. Build it once, drop it into Values on a `Category`-in-Rows pivot, and sort descending.

</details>

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Correctness | Numbers don't match a rebuildable pivot | All 15 answers are numerically correct |
| Traceability | Just a number, no configuration noted | Each answer states which fields/zones/aggregation produced it |
| Efficiency | A brand-new pivot built from scratch for every single question | Reuses and reconfigures pivots where the same shape answers multiple questions |
| Precision | Inconsistent rounding, mismatched category names | Consistent rounding; category/region names copied exactly as they appear in the data |

## Answer key

<details>
<summary>Reveal after attempting</summary>

1. **$27,494.99** total revenue.
2. **86** orders.
3. **North**, **$8,666.93**.
4. **Camping**, **$8,535.29** total revenue.
5. **Apparel**, **21 orders** — not the same category as Q4. Apparel has the most orders but Camping generates more revenue because camping gear costs more per item.
6. **$319.71** average order value (27,494.99 / 86).
7. **Online**, average order **$331.00** (vs. Retail $305.72, Wholesale $306.65).
8. **31.0%** of total revenue came from Camping (8,535.29 / 27,494.99).
9. **February** lowest ($1,896.26); **May** highest ($6,666.61).
10. **$11,108.09** cumulative through March (Jan 2,959.38 + Feb 1,896.26 + Mar 6,252.45).
11. **Jack Rivera** ranks #1 ($6,353.65); **Nadia Osei** ranks last ($1,501.40).
12. **≈64.1%** of North's revenue came through Online ($5,555.50 of $8,666.93).
13. **West** relies most on Wholesale in dollar terms — **$3,014.32**.
14. Order **1061**: **South** region, rep **Tom Baker**, product **Alpine 2-Person Tent**, **$1,319.94** (6 units, no discount, via Online).
15. **Footwear** has the highest revenue per unit at **≈$125.76/unit** (5,785.04 / 46), narrowly ahead of Camping (≈$118.55/unit) and Electronics (≈$116.98/unit).

</details>

## Submission

Keep `challenge-01.md` (or your `Notes` sheet) in your `crunch-week7` workbook, with all 15 answers and their pivot configurations noted.
