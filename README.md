# Cupboard Centre — Website

A rebuilt, conversion-focused static website for **Cupboard Centre**, Nelspruit &
Mbombela's DIY & custom cupboard specialists.

The site is **self-hosted static HTML/CSS/JS** — no build step or framework is
required to run it. Upload the files to any static host (or open `index.html`
locally) and it works.

## What this is

The previous Cupboard Centre site was structurally weak. This rebuild keeps
**Cupboard Centre's brand** (red / charcoal / white, logo, content, photography)
but rebuilds the **structure and conversion architecture** on the proven
section framework of a high-converting reference site.

Every page follows the reference framework's **exact section sequence** — no
sections removed, merged, reordered or simplified — including:

- Sticky utility bar + header with services mega-menu and persistent CTAs
- Hero with lead-capture form, trust badges and sub-claims
- Social-proof review carousel
- "We Are Cupboard Centre" about band
- Services grid (image cards)
- "The Difference" dark accordion panel with credibility badge
- "Spaces We Have Transformed" project carousel
- 4-step process
- Offer / free-quote CTA panel
- Blog teasers
- FAQ accordion
- Service-area map + town chips
- Full-width lead-capture CTA band
- Brand marquee + 4-column footer with contact + trust strip

Service, about, contact, gallery, service-areas, FAQ, blog, quote, shop, privacy
and sitemap pages each mirror the reference framework's structure for that page
type, adapted to Cupboard Centre's products and copy.

## Pages

| Page | File |
|------|------|
| Home | `index.html` |
| Services hub | `services.html` |
| Complete Installation | `cupboard-installation.html` |
| DIY Kitchen Units | `kitchen-units.html` |
| Bedroom & Bathroom Cabinetry | `bedroom-bathroom-cabinetry.html` |
| Melamine Doors & Quartz Countertops | `melamine-doors-quartz-countertops.html` |
| Custom Cabinetry & Shopfitting | `custom-cabinetry.html` |
| DIY Units & Flat-Packs | `diy-units.html` |
| About | `about.html` |
| Contact | `contact.html` |
| Get a Free Quote | `get-a-quote.html` |
| Online Shop | `shop.html` |
| Gallery | `gallery.html` |
| Service Areas | `service-areas.html` |
| FAQ | `faq.html` |
| Blog + 4 articles | `blog.html`, `blog/*.html` |
| Privacy Policy | `privacy-policy.html` |
| Sitemap | `sitemap.html` |

## Structure

```
index.html, *.html            Top-level pages
blog/*.html                   Blog articles
assets/css/styles.css         Design system (brand tokens + all components)
assets/js/app.js              Interactions (menu, carousels, accordions,
                              gallery filters + lightbox, forms)
assets/images/photos/         Bundled Cupboard Centre photography
build/generate.py             Reference generator used to produce the pages
```

## Brand

- **Primary red** `#e81e2c`  ·  **charcoal/black** `#211a1b`  ·  **white**
- Headings: Poppins · Body: Open Sans · Labels: Montserrat (Google Fonts)

## Notes for the developer

- **Images** are bundled locally under `assets/images/photos/` so the site is
  fully self-contained and reliable — no hot-linking to third-party CDNs.
- **Forms** (`data-lead`) currently show a friendly success confirmation on the
  front end. Wire the `submit` handler in `assets/js/app.js` to your email
  service / CRM (e.g. an endpoint or form provider) to receive enquiries.
- **Google Maps** embeds point at the Mbombela showroom address; they render on
  any normal host (they may appear blank in restricted sandbox previews).
- **Contact details** (phone `084 683 7467`, `info@cupboardcentre.co.za`,
  Facebook, Instagram, WhatsApp, showroom address) are set in the footer,
  header and contact page — update in `build/generate.py` (or directly in the
  HTML) if they change.
- `build/generate.py` is included for transparency; it was run against the
  original site captures to generate these pages and is not needed to host the
  site.
