# Week 9 — Go-to-Market & Launch

> **Goal:** by Sunday you can write a positioning statement that survives a skeptical VP of Sales, choose a launch tier and channel mix that matches the actual risk of what you're shipping, build a cross-functional launch checklist nothing falls through, and stand up a SQL launch dashboard that tells you — with data, not vibes — whether a phased rollout is working or needs to stop.

Welcome back to **C44 · Crunch Product**. You've spent eight weeks getting a feature *right*: discovering the problem (Weeks 2–3), specifying it (Week 4), prioritizing it against everything else (Week 5), proving it out with analytics and experiments (Weeks 6–7), and getting the design into shippable shape (Week 8). None of that matters if nobody knows the feature exists, the wrong audience hears about it, or a rollout goes sideways and nobody notices until support is on fire. This week is about the last mile: **turning a built feature into a launched one, safely and measurably.**

We continue the running example: **Loopline**, the fictional team task-management app. Recall from Week 5's backlog that **Guest & External Collaborator Access** — the ability to invite an external client, contractor, or partner into a specific project without giving them a full seat — was blocking **three signed enterprise deals** (Anchor Bank, Northwind Logistics, BrightPath Health) and depended on the audit log work shipping first for the security review. Both are now built. Engineering has a working, tested version behind a feature flag. **It is launch week.** This is exactly the moment where a strong PM earns their seat at the table: not by writing more code, but by deciding *who hears about this, in what order, through what channels, and how you'll know — in hours, not weeks — if something is wrong.*

## Learning objectives

By the end of this week, you will be able to:

- **Write** a positioning statement using the segment/need/category/differentiator template, and translate it into a messaging house — pillars, feature-to-benefit mapping, and proof points — for more than one target segment.
- **Choose** a launch tier (internal, private beta, limited GA, full GA) and a channel mix that matches the actual technical, security, and brand **risk** of what's shipping — not the size of the team's excitement.
- **Build** a cross-functional launch checklist spanning product, engineering, marketing, sales, support, and legal/security, with named owners and go/no-go gates.
- **Instrument** a rollout with feature flags and phased exposure, and **define launch success metrics in SQL** — activation funnels, ticket rates, and time-to-detect — before the first customer sees the feature.
- **Set rollback criteria in advance** — the specific, numeric thresholds that trigger a pause or rollback — and use a SQL query, not a hallway conversation, to decide when they're crossed.
- **Plan a rollout from beta to general availability**, and **write a recovery plan** for a launch that hits real trouble mid-rollout.

## Standards this week meets

| Bar | What this week is measured against |
| --- | --- |
| University | `MGT 4570` — develop a go-to-market plan: positioning and messaging for named segments, channel selection, and launch readiness across functions. |
| Industry | Run the launch: pick the tier that matches the actual risk, own the cross-functional checklist, and set the numeric rollback thresholds before the first customer sees the feature. |
| Beyond the bar | The rollback criterion is a query rather than a hallway conversation, and the week traces a real launch incident through it from detection to recovery — `lecture-notes/03-instrumented-rollouts.md` |

## Prerequisites

- Weeks 1–8 — this week assumes you can read a JTBD statement (Week 3), a PRD (Week 4), a RICE/Kano-scored backlog (Week 5), a funnel query (Week 6), and an experiment readout (Week 7) without re-explanation. We reuse the **Guest & External Collaborator Access** feature from Week 5's backlog as this week's launch subject.
- PostgreSQL 16+ **or** SQLite 3.35+ installed. Everything here runs unchanged on either; SQLite is the zero-setup fallback. Install steps are in [`resources.md`](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/resources.md).
- **No spreadsheets as a launch tracker.** A launch checklist, a rollout schedule, and a success dashboard are structured, queryable data — rows with owners, dates, statuses, and thresholds. We model all of it in **SQL and/or Python (pandas)**, never in a spreadsheet used as a system of record. A spreadsheet is a fine way to *print* a checklist for a meeting; it is not where the data about your launch should live, because it can't be joined, audited, or queried under pressure at 2 a.m. when a rollout is going wrong. Spreadsheets as a tool are taught separately in [C41 Crunch Excel](../../../C41-CRUNCH-EXCEL/).

## Set up the seed data (do this first)

Every lecture, exercise, challenge, and the mini-project this week works against the same rollout of **Guest & External Collaborator Access** across 24 Loopline customer orgs. Create the tables once.

**SQLite (fastest to start):**

```bash
sqlite3 loopline_launch.db
```

**PostgreSQL:**

```bash
createdb loopline_launch
psql loopline_launch
```

Then paste this into the shell (unchanged on both engines):

```sql
-- Customer orgs eligible for the Guest & External Collaborator Access rollout.
-- Eligible = Team or Business plan (Guest Access is not on the Free tier).
CREATE TABLE orgs (
    org_id       INTEGER PRIMARY KEY,
    org_name     TEXT    NOT NULL,
    segment      TEXT    NOT NULL,   -- 'SMB' | 'Mid-Market' | 'Enterprise'
    plan_tier    TEXT    NOT NULL,   -- 'Team' | 'Business'
    region       TEXT    NOT NULL,
    deal_status  TEXT                -- 'blocked_on_guest_access' | NULL
);

INSERT INTO orgs (org_id, org_name, segment, plan_tier, region, deal_status) VALUES
-- The 3 signed enterprise deals this launch unblocks (private beta, wave 1)
(1,  'Anchor Bank',            'Enterprise',  'Business', 'US-East',  'blocked_on_guest_access'),
(2,  'Northwind Logistics',    'Enterprise',  'Business', 'US-Cent',  'blocked_on_guest_access'),
(3,  'BrightPath Health',      'Enterprise',  'Business', 'US-West',  'blocked_on_guest_access'),
-- Friendly design partners (private beta, wave 1) — agencies live and breathe external collaborators
(4,  'Fenwick & Co',           'Mid-Market',  'Business', 'US-East',  NULL),
(5,  'Ridgeline Creative',     'SMB',         'Team',     'US-West',  NULL),
(6,  'Solstice Studio',        'SMB',         'Team',     'EU',       NULL),
(7,  'Harbor Consulting',      'Mid-Market',  'Business', 'US-East',  NULL),
(8,  'Vantage Partners',       'Mid-Market',  'Business', 'EU',       NULL),
-- Limited GA, 25% of the remaining eligible base (wave 2)
(9,  'Redline Studios',        'SMB',         'Team',     'US-West',  NULL),
(10, 'Cobalt Analytics',       'Mid-Market',  'Business', 'US-Cent',  NULL),
(11, 'Juniper & James',        'SMB',         'Team',     'EU',       NULL),
(12, 'Fairmount Realty',       'Mid-Market',  'Business', 'US-East',  NULL),
(13, 'Blue Anchor Media',      'SMB',         'Team',     'US-West',  NULL),
(14, 'Prairie Digital',        'Mid-Market',  'Business', 'US-Cent',  NULL),
(15, 'Silverline Legal',       'Enterprise',  'Business', 'US-East',  NULL),
(16, 'Wavecrest Agency',       'SMB',         'Team',     'EU',       NULL),
-- Full GA, remaining base (wave 3) — includes Cascade Freight, this week's incident case study
(17, 'Cascade Freight',        'Enterprise',  'Business', 'US-Cent',  NULL),
(18, 'Meridian Capital',       'Enterprise',  'Business', 'US-East',  NULL),
(19, 'Thistle & Co',           'SMB',         'Team',     'US-West',  NULL),
(20, 'Northgate Builders',     'Mid-Market',  'Business', 'US-Cent',  NULL),
(21, 'Palmetto Studio',        'SMB',         'Team',     'US-East',  NULL),
(22, 'Ironclad Insurance',     'Enterprise',  'Business', 'US-West',  NULL),
(23, 'Rowan Freelance Collective', 'SMB',     'Team',     'EU',       NULL),
(24, 'Beacon Nonprofit',       'Mid-Market',  'Business', 'US-East',  NULL);

-- When each org's feature flag was turned on, and which rollout phase they belong to.
CREATE TABLE rollout_exposures (
    exposure_id      INTEGER PRIMARY KEY,
    org_id            INTEGER NOT NULL REFERENCES orgs(org_id),
    phase             TEXT    NOT NULL,  -- 'beta' | 'ga_25' | 'ga_100'
    flag_enabled_at   TIMESTAMP NOT NULL
);

INSERT INTO rollout_exposures (exposure_id, org_id, phase, flag_enabled_at) VALUES
(1,1,'beta','2026-02-02 09:00'),(2,2,'beta','2026-02-02 09:00'),(3,3,'beta','2026-02-02 09:15'),
(4,4,'beta','2026-02-02 09:15'),(5,5,'beta','2026-02-03 10:00'),(6,6,'beta','2026-02-03 10:00'),
(7,7,'beta','2026-02-03 10:30'),(8,8,'beta','2026-02-04 11:00'),
(9,9,'ga_25','2026-02-16 09:00'),(10,10,'ga_25','2026-02-16 09:00'),(11,11,'ga_25','2026-02-16 09:30'),
(12,12,'ga_25','2026-02-17 10:00'),(13,13,'ga_25','2026-02-17 10:00'),(14,14,'ga_25','2026-02-18 11:00'),
(15,15,'ga_25','2026-02-18 11:00'),(16,16,'ga_25','2026-02-19 09:00'),
(17,17,'ga_100','2026-03-02 09:00'),(18,18,'ga_100','2026-03-02 09:00'),(19,19,'ga_100','2026-03-02 09:30'),
(20,20,'ga_100','2026-03-02 10:00'),(21,21,'ga_100','2026-03-03 09:00'),(22,22,'ga_100','2026-03-03 09:15'),
(23,23,'ga_100','2026-03-03 10:00'),(24,24,'ga_100','2026-03-04 09:00');

-- Every guest invitation sent since each org's flag turned on.
CREATE TABLE guest_invitations (
    invite_id       INTEGER PRIMARY KEY,
    org_id           INTEGER NOT NULL REFERENCES orgs(org_id),
    invited_at       TIMESTAMP NOT NULL,
    guest_email      TEXT    NOT NULL,
    accepted_at      TIMESTAMP,          -- NULL = never accepted the invite
    first_action_at  TIMESTAMP           -- NULL = accepted but never did anything as a guest
);

INSERT INTO guest_invitations (invite_id, org_id, invited_at, guest_email, accepted_at, first_action_at) VALUES
(1,1,'2026-02-02 14:00','counsel@outside-firm.com','2026-02-02 15:30','2026-02-02 16:10'),
(2,1,'2026-02-05 10:00','auditor@thirdparty.com','2026-02-05 12:00','2026-02-06 09:00'),
(3,2,'2026-02-03 09:00','ops@carrierco.com','2026-02-03 11:00',NULL),
(4,2,'2026-02-10 09:00','driver-lead@carrierco.com','2026-02-10 09:40','2026-02-10 14:00'),
(5,3,'2026-02-02 13:00','clinician@partnerclinic.org','2026-02-02 20:00','2026-02-03 08:00'),
(6,3,'2026-02-04 09:00','billing@partnerclinic.org',NULL,NULL),
(7,4,'2026-02-02 11:00','client@bigbrand.com','2026-02-02 11:45','2026-02-02 12:30'),
(8,4,'2026-02-06 11:00','client2@bigbrand.com','2026-02-06 13:00','2026-02-06 13:20'),
(9,4,'2026-02-09 11:00','client3@otherbrand.com','2026-02-09 15:00',NULL),
(10,5,'2026-02-03 12:00','freelancer@indie.dev','2026-02-03 12:20','2026-02-03 12:40'),
(11,6,'2026-02-03 15:00','client@studioclient.com','2026-02-04 08:00','2026-02-04 09:00'),
(12,7,'2026-02-03 16:00','partner@consultfirm.io',NULL,NULL),
(13,8,'2026-02-05 10:00','vendor@vantagevendor.com','2026-02-05 10:30','2026-02-05 11:00'),
(14,9,'2026-02-17 09:00','client@redlineclient.com','2026-02-17 10:00',NULL),
(15,10,'2026-02-16 10:00','contractor@cobaltvendor.io','2026-02-16 14:00','2026-02-17 09:00'),
(16,11,'2026-02-17 11:00','freelancer@juniperclient.com',NULL,NULL),
(17,12,'2026-02-18 09:00','broker@fairmountpartner.com','2026-02-18 12:00','2026-02-18 13:00'),
(18,13,'2026-02-18 10:00','client@blueanchorclient.com','2026-02-19 09:00',NULL),
(19,14,'2026-02-19 10:00','client@prairiedigital-client.com','2026-02-19 11:00','2026-02-19 15:00'),
(20,15,'2026-02-19 09:00','cocounsel@outsidefirm2.com','2026-02-19 09:45','2026-02-19 10:00'),
(21,15,'2026-02-20 09:00','expert@expertwitness.com','2026-02-20 10:00',NULL),
(22,16,'2026-02-20 11:00','client@wavecrestclient.com','2026-02-20 15:00','2026-02-21 09:00'),
(23,17,'2026-03-02 10:00','carrier@cascadepartner.com','2026-03-02 11:00','2026-03-02 11:30'),
(24,17,'2026-03-03 09:00','broker2@cascadepartner.com','2026-03-03 09:30','2026-03-03 10:00'),
(25,17,'2026-03-03 14:00','dispatch@othercascadeco.com','2026-03-03 14:20','2026-03-03 14:45'),
(26,18,'2026-03-02 11:00','advisor@meridianlp.com','2026-03-02 12:00',NULL),
(27,19,'2026-03-03 09:00','client@thistleclient.com','2026-03-03 10:00','2026-03-03 10:30'),
(28,20,'2026-03-03 10:00','sub@northgatesub.com','2026-03-03 12:00','2026-03-04 09:00'),
(29,21,'2026-03-04 09:00','client@palmettoclient.com',NULL,NULL),
(30,22,'2026-03-04 10:00','adjuster@ironcladpartner.com','2026-03-04 11:00','2026-03-04 11:20'),
(31,23,'2026-03-04 11:00','client@rowanclient.com','2026-03-04 13:00','2026-03-04 13:15'),
(32,24,'2026-03-05 09:00','donor-liaison@beaconpartner.org','2026-03-05 10:00',NULL);

-- Support tickets opened while the rollout was live, whether or not they turn out
-- to be about Guest Access. Realistic launch data is noisy on purpose.
CREATE TABLE support_tickets (
    ticket_id     INTEGER PRIMARY KEY,
    org_id         INTEGER NOT NULL REFERENCES orgs(org_id),
    opened_at      TIMESTAMP NOT NULL,
    category       TEXT    NOT NULL,   -- see values below
    severity       TEXT    NOT NULL    -- 'low' | 'medium' | 'high' | 'critical'
);

INSERT INTO support_tickets (ticket_id, org_id, opened_at, category, severity) VALUES
(1,1,'2026-02-03 10:00','guest_access_confusion','low'),
(2,4,'2026-02-07 09:00','guest_access_confusion','low'),
(3,4,'2026-02-10 14:00','unrelated_billing','low'),
(4,7,'2026-02-04 11:00','guest_access_confusion','medium'),
(5,8,'2026-02-06 09:00','guest_access_confusion','low'),
(6,9,'2026-02-18 10:00','guest_access_confusion','low'),
(7,10,'2026-02-17 15:00','guest_access_permission_question','medium'),
(8,12,'2026-02-19 10:00','guest_access_confusion','low'),
(9,14,'2026-02-20 09:00','unrelated_perf','low'),
(10,15,'2026-02-21 11:00','guest_access_confusion','medium'),
(11,17,'2026-03-03 16:40','guest_access_permission_bug','critical'),
(12,17,'2026-03-03 17:10','guest_access_permission_bug','critical'),
(13,18,'2026-03-04 09:00','guest_access_confusion','low'),
(14,20,'2026-03-04 13:00','guest_access_confusion','low'),
(15,22,'2026-03-04 15:00','guest_access_permission_question','medium'),
(16,23,'2026-03-05 10:00','guest_access_confusion','low');
```

Sanity checks — these should print `24`, `24`, `32`, and `16`:

```sql
SELECT COUNT(*) FROM orgs;
SELECT COUNT(*) FROM rollout_exposures;
SELECT COUNT(*) FROM guest_invitations;
SELECT COUNT(*) FROM support_tickets;
```

Notice what's already baked into this data on purpose: tickets 11 and 12 are **`critical`** severity, **`guest_access_permission_bug`**, both from **Cascade Freight** (org 17), both opened within 30 minutes of each other on the afternoon of `2026-03-03` — the second day of the `ga_100` wave. That is not noise. That is a rollout in the middle of going wrong, and Lecture 3, Exercise 3, and Challenge 2 all come back to it. Everything else — the low/medium confusion tickets scattered across beta and `ga_25` — is normal launch friction, the kind you expect and don't panic about.

**Python setup**, for the launch dashboard work in Lecture 3 and the mini-project:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install pandas sqlalchemy psycopg2-binary   # psycopg2-binary only needed if you're on Postgres
```

## Weekly schedule

The schedule below adds up to approximately **28 hours** (the course's full-time pace). Treat it as a target, not a stopwatch.

| Day | Focus | Lectures | Exercises | Challenges | Quiz/Read | Homework | Mini-Project | Daily Total |
|-----------|------------------------------------------------|---------:|----------:|-----------:|----------:|---------:|-------------:|------------:|
| Monday | Positioning statements and messaging houses | 2h | 1h | 0h | 0.5h | 1h | 0h | 4.5h |
| Tuesday | Messaging practice; feature-benefit-proof maps | 0h | 1.5h | 0h | 0.5h | 1h | 0h | 3h |
| Wednesday | Launch tiers, risk, and channel selection | 2h | 1.5h | 1h | 0.5h | 1h | 0h | 6h |
| Thursday | Feature flags, rollback criteria, SQL dashboards | 2h | 1.5h | 1h | 0.5h | 1h | 1h | 7h |
| Friday | Challenges: risky launch plan, bad-launch recovery | 0h | 0h | 1h | 0.5h | 1h | 1.5h | 4h |
| Saturday | Mini-project (full GTM & launch plan) | 0h | 0h | 0h | 0h | 0h | 2.5h | 2.5h |
| Sunday | Quiz + review | 0h | 0h | 0h | 1h | 0h | 0h | 1h |
| **Total** | | **6h** | **4.5h** | **3h** | **3.5h** | **5h** | **5h** | **28h** |

## How to navigate this week

Work top to bottom. Each piece assumes the ones above it.

| # | File | What's inside | ~Time |
|--:|------|---------------|------:|
| 1 | [lecture-notes/01-positioning-and-messaging.md](01-positioning-and-messaging.md) | Positioning statement template, differentiation, messaging houses, feature-to-benefit-to-proof mapping | 2h |
| 2 | [lecture-notes/02-launch-tiers-and-channels.md](02-launch-tiers-and-channels.md) | Launch tiers matched to risk, channel selection, cross-functional coordination and RACI | 2h |
| 3 | [lecture-notes/03-instrumented-rollouts.md](03-instrumented-rollouts.md) | Feature flags, phased GA, SQL launch dashboards, rollback criteria — with the Cascade Freight incident | 2h |
| 4 | [exercises/exercise-01-write-a-positioning-statement.md](exercise-01-write-a-positioning-statement.md) | Write positioning statements for two Guest Access segments and a feature-benefit-proof table | 1.5h |
| 5 | [exercises/exercise-02-build-a-launch-checklist.md](exercise-02-build-a-launch-checklist.md) | Build a cross-functional launch checklist with owners and go/no-go gates | 1.5h |
| 6 | [exercises/exercise-03-define-launch-success-in-sql.md](exercise-03-define-launch-success-in-sql.md) | Write the SQL queries that define and measure launch success and detect the Cascade Freight incident | 1.5h |
| 7 | [challenges/challenge-01-plan-a-risky-launch.md](challenge-01-plan-a-risky-launch.md) | Plan a phased rollout for a genuinely risky feature (AI Task Summaries) | 1.5h |
| 8 | [challenges/challenge-02-recover-from-a-bad-launch.md](challenge-02-recover-from-a-bad-launch.md) | Write the recovery plan for the Cascade Freight permission bug, live | 1.5h |
| 9 | [mini-project/README.md](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/mini-project/README.md) | Write a full go-to-market and launch plan for a v1 feature | 2.5h |
| 10 | [homework.md](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/homework.md) | Extra practice, spread across the week | 5h |
| 11 | [quiz.md](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/quiz.md) | 15 self-check questions + answer key | 1h |
| 12 | [resources.md](26-product%20learning（附）/curriculum/week-09-go-to-market-and-launch/resources.md) | Official/primary-source reading on positioning, launches, flags, and postmortems | — |

## By the end of this week you can…

- Write a positioning statement that names a specific segment, a specific need, and a specific differentiator — and explain why "for everyone" positioning is really positioning for no one.
- Pick a launch tier and channel mix by reasoning about blast radius, reversibility, and support cost, not by copying last quarter's launch plan.
- Produce a launch checklist a stakeholder can actually run a go/no-go meeting from, with named owners per function.
- Write the SQL that turns "is the launch working?" from a feeling into a query result, and set rollback thresholds before you need them — not while support is already escalating.
- Recognize a launch going wrong from data (not from a Slack fire), and write a calm, structured recovery plan instead of panicking in public.

## Up next

[Week 10 — Pricing & growth](../week-10-pricing-and-growth/) — once a feature is live and adopted, the next question is what it's worth, and how it compounds.

---

*Part of the Code Crunch Worldwide open curriculum · GPL-3.0 · If you find errors, please open an issue or PR.*
