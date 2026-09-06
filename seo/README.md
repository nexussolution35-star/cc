# Cupboard Centre — SEO Foundation (Stage A2 + A3)

Worked against the **SEO Specialist Copilot Master Prompt v2.0**. This folder covers
**A2 (old-site audit)** and the **A3 candidate list**. It deliberately stops short of
final metadata (A4) — see *Why no rewrites yet* below.

## Files

| File | What it is |
|---|---|
| `01-old-site-keywords.csv` | Every keyword the old Wix site declared (164 rows / 102 unique), with its page, URL, old title, whether that page had a meta description, duplication flag, intent, and the new page it maps to. |
| `02-keyword-opportunities.csv` | The **Search Atlas candidate list** (198 rows): brand, core services, `[service] services` variants, service+town, town coverage, category/product, informational, plus every legacy term re-listed for re-testing. |
| `03-url-migration-map.csv` | All 27 old URLs → new URLs, with old internal-link counts and ranking risk. |
| `04-keyword-map-per-page.csv` | The confirmed map: primary + secondaries per page, with volume, difficulty and opportunity. |
| `05-rejected-keywords.csv` | 37 rejected terms, each with a one-line reason. |
| `06-keyword-strategy.md` | The A3 write-up: structural recommendations, the map, rejections. |
| `matrix/OLD_CC.csv`, `matrix/NEW_CC.csv` | Raw Search Atlas exports. |
| `redirects.htaccess` / `redirects.nginx.conf` | Server configs generated from the map. |
| `/_redirects` (repo root) | Netlify / Cloudflare Pages / Lovable format. |

All three CSVs have **empty `search_volume` and `keyword_difficulty` columns**. That is
intentional — Rule 5: *"a keyword without volume + difficulty + intent is not research,
it is a guess."* Those columns get filled from Search Atlas, then the `decision` /
`verdict` column gets set.

---

## What the old site was actually doing

**1. It was keyword stuffing — confirmed, with numbers.**
All 19 pages carried a `<meta name="keywords">` tag. Google has ignored that tag since
2009; it contributed nothing. Worse, **62 of 164 keyword entries were duplicates of terms
already claimed on another page** — the textbook cannibalisation signal. Examples:
`custom cabinetry` appears on 5 pages, `quartz countertops` on 4, `cupboard installation`
on 4. No page could win a term that four other pages were also claiming.

**2. 16 of 19 pages had NO meta description.** Only `bedroom-and-bathroom-cabinetry`,
`contact-us` and `melamine-doors-quartz-countertops` had one. Google was writing its own
snippets for 84% of the site.

**3. Multiple H1s on every page** — Wix junk. `about-us` had **18 H1 tags**. The old
site was effectively ranking on `<title>` alone.

**4. Stale terms are still in the keyword set** — the homepage lists `Christmas Holidays`.

**5. Competitor-brand terms.** The blog page targeted `builders warehouse built in kitchen
cupboards`, `diy kitchen cupboards builders warehouse` etc. These are competitor
navigational terms — very hard to win, and the traffic converts poorly. Flagged for
rejection in the CSV; the decision is the specialist's after the matrix.

## What our new site already fixes

| Item | Old | New |
|---|---|---|
| Meta descriptions | 3 / 19 | **24 / 24** |
| Meta keywords tag | 19 / 19 (dead weight) | **0** — correctly omitted |
| H1 per page | 2–18 | **exactly 1** on all 24 |
| Canonicals | present, but homepage canonical → `/home-cc` | present, homepage → `/` |
| `sitemap.xml` | — | **added** (23 URLs, priorities set) |
| `robots.txt` | — | **added** (production version, references sitemap) |

---

## ⚠️ The one thing that will break rankings: every URL changed

The old Wix site served **extensionless** URLs (`/about-us`). The new static site serves
`.html` (`/about.html`). The host does serve clean URLs — `/kitchen-units` resolves — so
pages whose **slug is unchanged** are already safe. But **renamed** pages 404 today:

```
/about-us      → 404      /contact-us  → 404
/home-cc       → 404      /gallery-*   → 404
```

**16 URLs are HIGH risk** (55+ internal links each on the old site). The worst:

| Old URL | Links | New | 
|---|---|---|
| `/home-cc` | 145 | `/` |
| `/gallery-designs-of-kitchen-cupboard` | 127 | `/gallery.html` |
| `/shop` | 121 | `/shop.html` |
| `/gallery-custom-cabinetry` | 118 | `/custom-cabinetry.html` |
| `/about-us` | 98 | `/about.html` |

`/home-cc` matters most: it was the **canonical URL of the old homepage** (a Wix quirk),
so it is the homepage URL Google has indexed.

**Nothing is lost as long as the 26 redirects in `_redirects` ship with the site.** They
are generated from the migration map, so the two cannot drift apart.

---

## Notes on the current preview

The preview at `cupboard-centre-preview.surge.sh` serves `User-agent: * / Disallow: /`
(Surge's default). **That is correct for now** — it stops the preview competing with the
client's live site for the same content. I have therefore **kept `robots.txt` out of the
preview deploy** while shipping it in the repo for production.

Per Rule 7's robots corollary, the staging block **must not survive to production** — at
cutover the repo's `robots.txt` becomes the live one.

---

## Why no title/description rewrites yet

The framework is explicit that A4 (metadata & copy) comes **after** the keyword map is
confirmed, and that keywords without their matrix are guesses. Rewriting titles now would
be repeating the old site's mistake with better prose.

Equally important — A2's *keep-as-is* rule: **pages that already rank must keep their URL,
wording and intent untouched**; over-optimising a working page is a listed failure mode. I
cannot tell which pages rank without **Google Search Console data**, which is the one input
I don't have.

### Next actions

1. **Pull GSC data** (last 12 months, page + query) → tells us the keep-as-is list. This is
   the blocker for A4.
2. **Run the 198 candidates through Search Atlas** → fill volume + difficulty.
3. I then build the per-page keyword map (primary + 2–3 secondaries, no two pages sharing a
   primary) and write every title, description, H1 and intro — the A4 spec.

**Primary domain:** the old site is indexed on **www** (the apex redirects every route to
the homepage — itself a defect). Our canonicals already use `https://www.cupboardcentre.co.za`,
which matches. Worth confirming against GSC before cutover.
