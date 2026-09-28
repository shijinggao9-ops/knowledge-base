# Lecture 2 — LET & Readable Mega-Formulas

> **Duration:** ~2 hours. **Outcome:** You can take a long, repetitive formula and refactor it with `LET` so every sub-expression has a name and is computed once — and you can generate structured or randomized arrays with `SEQUENCE` and `RANDARRAY` and combine them with the spill tools from Lecture 1.

Nest a `FILTER` inside a `SORT` inside a `UNIQUE` a few times and you'll notice a problem: the same sub-expression — `Orders!D2:D31="North"`, say — starts appearing two, three, four times in a single formula, because you need it in the filter condition *and* somewhere else in the same formula. Every repetition is a place a typo can sneak in, a place the engine recalculates the same thing again, and a place a teammate reading your formula has to re-derive what it means. `LET` fixes all three at once.

## 1. The problem, concretely

Say you want: for **Shipped** orders only, the total revenue, but only if that total exceeds $1,000 — otherwise show `"Below threshold"`. Without `LET`:

```excel
=IF(SUM(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")) > 1000,
    SUM(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")),
    "Below threshold")
```

`FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")` — the exact same sub-expression — appears **twice**. That's not just ugly; the engine genuinely recomputes it twice, and if you ever need to tweak the filter condition (say, add a region filter), you have to remember to change it in both places or the formula silently drifts out of sync with itself.

## 2. `LET` — name it once, use it everywhere

```excel
=LET(
    shipped_total, SUM(FILTER(Orders!I2:I31, Orders!J2:J31="Shipped")),
    IF(shipped_total > 1000, shipped_total, "Below threshold")
)
```

`LET(name1, value1, [name2, value2, ...], calculation)` — pairs of `name, value`, then a final expression that gets to use every name you defined. `shipped_total` is computed **once**, then reused as many times as you want inside the final calculation, both for readability and because the engine genuinely only evaluates it once no matter how many times the name appears afterward.

**Rules that matter:**

- The **last argument** is always the calculation that gets returned — everything before it is name/value pairs.
- Names can't collide with cell references — `LET(A1, 5, A1*2)` is invalid because `A1` already means something. Pick a name like `qty` or `shipped_total` instead.
- **Later names can reference earlier names** in the same `LET` — this is the whole point:

```excel
=LET(
    shipped, FILTER(Orders!A2:J31, Orders!J2:J31="Shipped"),
    sorted_shipped, SORT(shipped, 9, -1),
    top5, TAKE(sorted_shipped, 5),
    top5
)
```

Read top to bottom: `shipped` is defined first (the filtered rows), `sorted_shipped` builds on `shipped` (sorts it), `top5` builds on `sorted_shipped` (takes the first 5), and the final line just returns `top5`. Each step is one clear English-ish name — this is a genuinely different reading experience from the single 80-character nested version, even though it computes the identical result.

```mermaid
flowchart LR
  A["shipped = FILTER(Orders, Status='Shipped')"] --> B["sorted_shipped = SORT(shipped, 9, -1)"]
  B --> C["top5 = TAKE(sorted_shipped, 5)"]
  C --> D["return top5"]
```
*Each LET name builds on the one before it, evaluated once and reused by name.*

## 3. `LET` is also a performance tool, not just cosmetic

Every time a named sub-expression appears more than once in a formula *without* `LET`, the calculation engine recomputes it from scratch each time it's referenced. On a small 30-row table like `Orders`, you'll never notice. On a real dataset with tens of thousands of rows and several repeated `FILTER`/`SORT` calls, re-deriving the same intermediate array three or four times inside one cell is a measurable slowdown — and it compounds if that formula gets copied down or across many cells. `LET` computes each named value exactly once per formula evaluation, however many times its name is referenced afterward. Naming things isn't just for humans reading the formula; it's genuinely faster.

## 4. `SEQUENCE` — generating structured arrays

```excel
=SEQUENCE(10)                        ' a column of 1 through 10
=SEQUENCE(5, 2)                      ' 5 rows × 2 columns, filled 1–10 row by row
=SEQUENCE(12, 1, 1, 1)               ' 12 rows, starting at 1, stepping by 1 — same as SEQUENCE(12)
=SEQUENCE(30, 1, 3001, 1)            ' a column of the 30 OrderIDs, 3001 through 3030, without retyping them
```

`SEQUENCE(rows, [columns], [start], [step])`. A common use: a rank column next to a sorted spill, generated instead of typed:

```excel
=LET(
    ranked, SORT(FILTER(Orders!C2:I31, Orders!J2:J31="Shipped"), 7, -1),
    HSTACK(SEQUENCE(ROWS(ranked)), ranked)
)
```

`HSTACK(array1, array2, ...)` glues arrays together side by side (there's a `VSTACK` for stacking vertically). `ROWS(ranked)` counts however many rows `ranked` spilled into — combined with `SEQUENCE`, that produces a rank number `1, 2, 3, ...` that automatically matches however many Shipped orders exist, with no hard-coded row count anywhere in the formula.

## 5. `RANDARRAY` — generating randomized arrays

```excel
=RANDARRAY(5)                              ' 5 random decimals between 0 and 1
=RANDARRAY(5, 1, 1, 100)                   ' 5 random decimals between 1 and 100
=RANDARRAY(5, 1, 1, 100, TRUE)             ' 5 random WHOLE numbers between 1 and 100
```

`RANDARRAY([rows], [columns], [min], [max], [integer])`. Two honest use cases: generating disposable test data while building a formula (fill a scratch range with `RANDARRAY(30,1,10,500,TRUE)` to stress-test a `SORT`/`FILTER` combo before pointing it at real data), and Monte-Carlo-style what-if sketches (Week 9's Scenario Manager territory, but quick and disposable). **`RANDARRAY` recalculates every time the sheet recalculates** — including just opening the file — so never build a formula that depends on a `RANDARRAY` value staying fixed; if you need a "frozen" random sample, generate it, then paste-special as values.

## 6. Putting it together: a readable "report cell"

The kind of formula this week is building toward — filtered, sorted, ranked, all in one cell, all readable:

```excel
=LET(
    src, Orders!A2:J31,
    is_shipped, INDEX(src, 0, 10) = "Shipped",
    shipped_rows, FILTER(src, is_shipped),
    sorted_rows, SORT(shipped_rows, 9, -1),
    top5, TAKE(sorted_rows, 5),
    ranked, HSTACK(SEQUENCE(ROWS(top5)), top5),
    ranked
)
```

`INDEX(src, 0, 10)` — a `0` for the row argument means "every row," so this pulls the entire 10th column (`Status`) out of `src` without a separate range reference. Every named step reads as a sentence: source, is it shipped, the shipped rows, sorted, the top 5, ranked. Compare that to writing the equivalent as one unbroken nested expression — same answer, radically different to maintain six months from now.

## 7. Google Sheets

`LET` was added to Google Sheets in 2022 with **identical syntax** to Excel — same name/value pairing, same rule about the final calculation argument. `SEQUENCE` and `RANDARRAY` are both natively supported in Sheets as well, with matching arguments. `HSTACK`/`VSTACK`/`TAKE`/`CHOOSEROWS` are also present in current Sheets. If a formula in this lecture doesn't work in your Sheets file, the most likely cause isn't a missing function — it's an old cached version of Sheets; refresh the tab.

## 8. Check yourself

- What's the difference between what goes in `LET`'s middle arguments versus its final argument?
- Rewrite `=SUM(FILTER(A:A,B:B="x"))*2 - SUM(FILTER(A:A,B:B="x"))` using `LET` so the filtered sum is computed once.
- Why is `LET(A1, 5, A1*2)` invalid?
- What does `SEQUENCE(12,1,2026,1)` produce, conceptually, if you fed it into a date-formatted column?
- Why should you never rely on a specific value from `RANDARRAY` staying the same between two recalculations?
- In the "report cell" example, why is `INDEX(src, 0, 10)` used instead of just writing `Orders!J2:J31` directly?

If those feel automatic, Lecture 3 takes the next step: instead of naming values inside one formula, you'll name a whole **reusable formula** — your own function — with `LAMBDA`.

## Further reading

- **Microsoft — `LET` function:** <https://support.microsoft.com/en-us/office/let-function-34842dd8-b92b-4d3f-b325-b8b8f9908999>
- **Microsoft — `SEQUENCE` function:** <https://support.microsoft.com/en-us/office/sequence-function-57467a98-57e0-4817-9f14-2eb78519ca90>
- **Microsoft — `RANDARRAY` function:** <https://support.microsoft.com/en-us/office/randarray-function-21261e55-3bec-4885-86a6-8b0a47fd4d33>
- **Microsoft — `HSTACK`/`VSTACK` functions:** <https://support.microsoft.com/en-us/office/hstack-function-9d1a2ac6-458b-414a-960d-8577f0d4b90a>
- **Google — `LET` function:** <https://support.google.com/docs/answer/12475830>
- **Google — `SEQUENCE` function:** <https://support.google.com/docs/answer/10218653>
- **Google — `RANDARRAY` function:** <https://support.google.com/docs/answer/10251762>
