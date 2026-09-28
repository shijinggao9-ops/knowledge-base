# Challenge 1 — Parse Inconsistent Addresses

**Time:** ~60 minutes. **Difficulty:** Medium-hard. **No single formula solves every row.**

## The scenario

A colleague hands you a column of customer addresses scraped from several different sources over several years — a web form, a support ticket system, and an old CSV nobody remembers the origin of. They all *look* like addresses, but they don't share one consistent shape: different delimiter styles, some with apartment numbers, some international, some with extra whitespace. This is deliberately the hardest parsing problem this week, because real address data genuinely is this messy — there is no clean textbook format to rely on, and part of the skill is recognizing when a fully general formula isn't realistic and a documented judgment call is the right answer instead.

## Build the data

Add a new sheet, `Challenge 1`. Type this exactly as shown, including irregular spacing where present:

| RawAddress |
|---|
| 123 Main St, Austin, TX 78701 |
| 45 Elm Avenue Apt 4B, Seattle, WA 98101-2345 |
| 789 Oak Blvd, Toronto, ON M4B 1B3 |
| 1600 Pennsylvania Ave NW, Washington, DC 20500 |
| 22 Rue de la Paix, Paris, France, 75002 |
| 10 Downing Street, London, UK SW1A 2AA |
|  500  Fifth Ave , New York , NY  10110 |

Row 1 is your header (`RawAddress`).

## Your task

Build four output columns — `Street`, `City`, `Region`, `PostalCode` — that parse as much of each row correctly as a reasonable, general formula can manage.

### Step 1 — Start with the clean cases

Rows 1, 2, 4, and 7 all follow a recognizable `Street, City, Region PostalCode` pattern once whitespace is trimmed. Use `TEXTSPLIT` on `", "` (or chained `FIND`/`MID`, your choice) to get `Street` and `City` for these rows, then split the last piece (`"TX 78701"`) on the space to separate `Region` from `PostalCode`. Watch for:

- Row 2's postal code has a `-2345` suffix (ZIP+4) — decide whether `PostalCode` should include it or not, and be consistent.
- Row 4's street (`"1600 Pennsylvania Ave NW"`) has no internal comma, but does have an internal space in the street name itself — make sure your split doesn't accidentally cut the street short.
- Row 7 has irregular extra spaces throughout (`" 500  Fifth Ave , New York , NY  10110"`) — `TRIM` every extracted piece.

### Step 2 — Handle the ones that break the pattern

- **Row 3** (`"789 Oak Blvd, Toronto, ON M4B 1B3"`) — the Canadian postal code (`M4B 1B3`) contains a **space in the middle of itself**, which breaks a naive "split the last piece on space" approach for `Region`/`PostalCode` (you'd get `Region: ON M4B`, `PostalCode: 1B3` — wrong). Fix this specifically: after splitting off the last comma-piece, the *first* space-separated token is `Region`, and **everything after it** is `PostalCode` — not just the last token.
- **Row 5** (`"22 Rue de la Paix, Paris, France, 75002"`) — this one has **four** comma-separated pieces, not three (`Street, City, Country, PostalCode`) — a different shape than every other row. A formula tuned for exactly 3 pieces will misparse this one. Decide: do you special-case it, or accept a documented wrong/partial result for this row? Either is acceptable — but you must state which, and why.
- **Row 6** (`"10 Downing Street, London, UK SW1A 2AA"`) — the UK postcode `SW1A 2AA` has an internal space **and** shares its piece with the country code `UK`, three tokens jammed into what your other rows treat as two (`Region PostalCode`). Same judgment call as Row 5.

### Step 3 — Document your judgment calls

In a `Challenge 1 — Notes` text block (a `Notes` sheet, a comment, or a markdown file — your choice), answer:

1. Which rows did your general formula parse *correctly* with no special-casing?
2. Which rows did you special-case, and what specifically made them different from the "normal" shape?
3. For Rows 5 and 6 (4-piece and space-embedded postal codes) — did you build a fully general formula, hard-code an exception, or leave the result acceptably wrong? Defend your choice — there's no penalty for "I accepted a wrong result here and here's why that's a reasonable tradeoff for 2 rows out of 7," as long as it's stated, not hidden.
4. If this were 50,000 rows instead of 7, would your approach still be practical? What would you do differently at that scale (hint: this is a preview of why Week 5's data-cleaning/validation tools, and eventually Week 11's Power Query, exist — some messes are worse fixed with formulas than with a proper ETL step).

## How success is judged

| Signal | Weak answer | Strong answer |
|--------|-------------|----------------|
| Coverage | Only the 4 clean rows parsed; others left entirely blank with no comment | All 7 rows attempted; failures are deliberate and documented, not silent |
| Technique | Every row hand-typed after "eyeballing" it | Formula-driven for every row you claim to have solved generally |
| Robustness | Row 3's Canadian postcode silently truncated with no acknowledgment | Row 3 either fixed correctly or the truncation explicitly called out as a known gap |
| Judgment | No notes; grader has to guess what you intended | All Step 3 questions answered with real specifics, not generic statements |

## Submission

Keep the `Challenge 1` sheet (with your four parsed columns) and your notes in the workbook.
