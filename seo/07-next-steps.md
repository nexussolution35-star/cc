# What's next — SEO roadmap

## Where we are

Stages **A2 (old-site audit)**, **A3 (keyword map)** and **A4 (metadata & copy)** are done,
plus most of the **B1 technical** list. A **B2-style verification** passes clean on all 27
pages: no duplicate titles/descriptions/canonicals, every title ≤60, every description
120–170, one H1 and one `<main>` per page, canonical == og:url, all JSON-LD valid, zero
broken internal links.

## No Search Console — what that actually changes

It removes a blocker rather than creating one. The *keep-as-is* rule exists to stop you
over-optimising a page that already ranks; with no GSC on either site there is no such
evidence, so the keyword map is the best available basis and we've built on it. Nothing is
waiting on data any more.

But it makes one thing urgent: **the client currently has no measurement at all.** That is
the top of the list below.

---

## 1. Set up the measurement stack (do this before cutover)

| Tool | Why | When |
|---|---|---|
| **Google Search Console** | Zero visibility today. Verify the **www** property (the format the old site is indexed on). Submit `sitemap.xml` the moment the domain cuts over. | Now / at launch |
| **Google Business Profile** | **The single highest-ROI item.** Every town keyword reads 0 volume, so local intent is *not* won on-page — it's won in the map pack. They already have real Google reviews. Claim, complete, categorise, add photos, keep NAP identical to the site footer. | Now |
| **GA4** | Conversion baseline for the quote form and calls. | At launch |

The old site's numbers become the reporting baseline — same metrics, same period length.

## 2. Finish the launch path (framework Parts C)

- **C1 Port** to the production host, keeping real path routing, per-route metadata and
  server-rendered content.
- **C2 URL format & primary domain** — pick **www** to match what's indexed, then prove it:
  redirect chain, trailing-slash behaviour, and served URL == canonical == sitemap entry.
- **C3** notify the back-end lane to wire the forms and chat widget.
- **C4 Lovable-only passes** — the image pass is **already done** (below); still to run:
  favicon check, accessibility audit fixes, and the host's own SEO diagnostic.
- **C5 Post-launch monitoring** — weekly for the first month, then monthly. ~70% indexed at
  two weeks with no errors is healthy; only 404s and errors are action items.

**At cutover, swap `robots.txt`.** The preview is deliberately serving `Disallow: /` so it
can't compete with the client's live site. The production `robots.txt` in the repo (allow-all,
references the sitemap) must replace it — a staging block that survives to production is the
classic launch-killer.

## 3. Content — where the remaining upside is

The money pages are now mapped and optimised. The next real gains:

- **Bulk out the two thin service pages.** `cupboard-installation` and `shop` carry the least
  copy and the weakest targets.
- **Blog is only 4 posts**, and two of them target near-zero volume. Worth commissioning
  against the informational terms that *do* have demand:
  `how to install kitchen cupboards` (50 @ KD 13), `kitchen cupboard design ideas` (90 @ KD 30),
  `cost of built in cupboards south africa` (20 @ KD 3, transactional intent).
- **Re-run the matrix in ~90 days.** The two pulls already disagreed on difficulty for 31
  keywords; treat KD as directional, not precise.

---

## Already banked this pass

**URL format — the fix that mattered most.** Everything is now root-relative and
extensionless (`/about`, not `/about.html`), matching the shape the old Wix site served:

- **10 of 27 old URLs are now preserved exactly and need no redirect at all** — including the
  three most-linked pages on the old site: `/gallery-designs-of-kitchen-cupboard` (127 internal
  links), `/shop` (121) and `/kitchen-units` (95).
- Redirects fell from 26 → **17**; high-risk URLs from 16 → **8**.
- `.html` variants 301 to the extensionless URL, so the same content is never on two URLs.

**Schema**, page-appropriate rather than blanket: LocalBusiness on home + contact only,
`Service` on the 8 service pages, `FAQPage` on the 9 pages with a visible FAQ (generated from
the same data the page renders, so markup and copy can't drift), `BreadcrumbList` on 23 deep
pages, `BlogPosting` on the 4 posts, `Product` on the product page. All valid.

**Image pass**, done early rather than left to the host: 119 images converted to WebP and
700px thumbnails generated for the gallery grids, served via `srcset` with the full file
reserved for retina and the lightbox.

| Page | Before | After |
|---|---:|---:|
| `/gallery` | 6.71 MB | **1.49 MB** (−78%) |
| `/gallery-designs-of-kitchen-cupboard` | 4.12 MB | **0.81 MB** (−80%) |
| `/` | 2.15 MB | **1.37 MB** (−36%) |

Still to do on images: hero images should be `fetchpriority="high"` and *not* lazy-loaded —
worth confirming the LCP image didn't end up lazy after the port.
