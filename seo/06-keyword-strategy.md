# Cupboard Centre — Keyword Map (Stage A3 output)

Built from `matrix/NEW_CC.csv` (the newer, fuller pull — 181 rows) with `OLD_CC.csv`
filling gaps. Every number below is read straight from the matrix, not typed by hand.

**Files:** `04-keyword-map-per-page.csv` (the map) · `05-rejected-keywords.csv` (37 rejections with reasons)

---

## Two things to settle first

### 1. Don't divide search volume by 12

`sv` from Search Atlas is **already the average monthly searches** — it's derived from 12
months of data, not a 12-month total. Dividing by 12 would understate everything by 12×.

It also wouldn't change a single decision: dividing every number by the same constant
leaves the ranking order identical. So `kitchen cupboards` = **22,200 searches/month**.

### 2. Mpumalanga vs Nelspruit — a flag before we commit

You've asked to target Mpumalanga instead of Nelspruit. Worth knowing what the data says:

| Term | Volume |
|---|---|
| `kitchen cupboards nelspruit` | **50** (KD 9) |
| `cupboard centre nelspruit` | **10** |
| `diy cupboards in mpumalanga` | **0** |
| every other town/province term | **0** |

Nelspruit is the *only* local modifier with measurable demand. Dropping it entirely would
forfeit that, and their Google Business Profile is anchored there.

**My recommendation:** use both, in different jobs — **Mpumalanga** as the region wording
in body copy and on the service-areas page (it honestly reflects the wider trading area),
**Nelspruit** retained in the homepage title and GBP-aligned spots. You lose nothing and
gain the broader positioning. Say the word if you'd rather go Mpumalanga-only and I'll
apply it as specified.

Either way: per the framework, service pages stay **region-neutral** (they serve the whole
province) — only the homepage and location pages carry a place name.

---

## Three structural recommendations

These need your yes/no before I write any metadata.

**A. Split `bedroom-bathroom-cabinetry` into two pages.**
One page can't own both. `bathroom cabinets` is 9,900 @ KD 8 and `bedroom cupboards` is
2,900 @ KD 3 — together the second- and fourth-best opportunities on the site, currently
competing with each other on one URL.

**B. Restore a dedicated kitchen gallery page.**
You were right that the old site had a page per gallery. `/gallery-designs-of-kitchen-cupboard`
was the **most internally-linked page on the old site (127 links)** and
`designs of kitchen cupboard` is 3,600 @ KD 28. We merged all five galleries into one
`gallery.html` and lost that. Browse intent is genuinely different from service intent, so
it doesn't cannibalise the kitchen service page.

**C. Add an office & reception desks page.**
`office desks` is **8,100 @ KD 8** and `reception desks` is **1,600 @ KD 3** — and they
genuinely build both (they're all over the custom-cabinetry gallery). Right now these sit
buried as secondaries. This is the single biggest untapped opportunity in the set.

---

## The map — primary keyword per page

Ordered by opportunity (volume ÷ difficulty). Full detail incl. secondaries in `04-*.csv`.

| Page | Primary keyword | Vol/mo | KD | Opp |
|---|---|---:|---:|---:|
| `kitchen-units` | **kitchen cupboards** | 22,200 | 6 | 3700 |
| `bathroom-cabinets` *(new, split)* | **bathroom cabinets** | 9,900 | 8 | 1238 |
| `office-reception-desks` *(new)* | **office desks** | 8,100 | 8 | 1013 |
| `bedroom-cupboards` *(new, split)* | **bedroom cupboards** | 2,900 | 3 | 967 |
| `index` (home) | **diy cupboards** | 2,400 | 14 | 171 |
| `melamine-doors-quartz-countertops` | **quartz countertops** | 2,900 | 19 | 153 |
| `diy-units` | **flat pack cupboards** | 390 | 3 | 130 |
| `gallery-kitchen` *(restore)* | **designs of kitchen cupboard** | 3,600 | 28 | 129 |
| `custom-cabinetry` | **shopfitting** | 590 | 5 | 118 |
| `product-flat-pack-wardrobe` | **flat pack wardrobe** | 110 | 5 | 22 |
| `cupboard-installation` | **kitchen cupboard installation** | 170 | 42 | 4 |

**Total addressable volume across targeted primaries: ~53,500 searches/month.**

**No chase** (deliberately): `services` and `gallery` demoted to overviews so they can't
compete with the pages beneath them; `service-areas` kept for coverage but not chased
(all town terms read 0 — local intent is won on the Google Business Profile);
`about` / `contact` / `get-a-quote` / `faq` support conversion, not head terms;
`cart` is noindex.

### Why the homepage keeps "diy cupboards"

The old homepage title was *"Nelspruit's Best DIY Cupboard Solutions"* and the hero led on
DIY cupboards — it already ranks there. A2's **keep-as-is rule** says don't over-optimise a
working page, so the homepage keeps that term and the brand name. It's deliberately *not*
reused on `diy-units`, which takes `flat pack cupboards` instead — that's how we avoid the
two pages eating each other.

---

## What I rejected, and why

37 terms, each with a reason, in `05-rejected-keywords.csv`. You were right to push on
relevance — the biggest numbers in the file are the worst targets:

| Rejected | Vol | Why |
|---|---:|---|
| `chest of drawer` | **33,100** | Retail-furniture intent — people buying loose furniture, not built-in cupboards. Highest volume in the whole set and still wrong. |
| `quote request` | **12,100** | Searchers want quote *templates/software*. Nothing to do with cupboards. |
| `kitchen cabinets` | 6,600 | KD 78 — hardest term in the set, and "cupboards" is the SA phrasing. |
| `nelspruit` | 27,100 | Bare geography, no commercial intent. |
| `walk in closet` | 1,000 | KD 80, US phrasing. |
| `wall racks` | 110 | Not a product line — your call, agreed. |
| `bathroom remodeling`, `home renovation`, `kitchen renovation` | — | Not their service. They build cabinetry; they don't remodel. |
| `cart`, `checkout`, `review items`, `secure checkout`, `finalize selection` | — | Utility pages. Agreed. |
| `christmas holidays` | 170 | Seasonal leftover from the old stuffing. |
| all 4 `builders warehouse …` | 30–140 | Competitor brand — unwinnable, and the traffic wants Builders Warehouse. |
| `cupboard warehouse` | 320 | Competitor navigational, despite the tempting KD 6. |

Two useful near-misses worth naming, because they look like rejections but aren't:
`bathroom cabinetry` (9,900 @ **KD 48**) was dropped in favour of `bathroom cabinets`
(same 9,900 @ **KD 8**); `reception desk` singular reads KD 48 while the plural
`reception desks` is KD 3 for identical volume. Same traffic, a fraction of the fight.

---

## Data-quality note

The two pulls disagree on difficulty for **31 keywords**, several dramatically —
`bathroom cabinets` KD 61.6 → 8, `office desks` 33 → 8, `kitchen cupboard design` 53 → 4,
`quote request` 6 → 51. I've used the **newer NEW_CC pull** throughout. Worth a spot-check
in Search Atlas on the four pages where the swing changes the call, before we build on it.

---

## Next

This is the A3 exit gate: **confirm the map + the three structural decisions (A/B/C) and
the Mpumalanga/Nelspruit call**, and I'll write the full A4 spec — every title, meta
description, H1, H2 skeleton and intro paragraph, per page, with each keyword landing once
and naturally. No stuffing; the old keyword set is guidance, not a template.
