# -*- coding: utf-8 -*-
"""Cupboard Centre static-site generator.
Replicates the Website B conversion framework (section sequence, forms, trust
components) with Cupboard Centre brand, content and photography."""
import json, os, re

OUT = os.path.join(os.path.dirname(__file__), '..')   # repo root
POOL = json.load(open(os.path.join(os.path.dirname(__file__), '..', '_extract', 'images_pool.json')))
IMG_MAP = json.load(open(os.path.join(os.path.dirname(__file__), '..', '_extract', 'img_map.json')))

# ---------------------------------------------------------------- brand / config
SITE   = "Cupboard Centre"
PHONE  = "084 683 7467"
TEL    = "0846837467"
WA     = "27793057321"           # WhatsApp - a DIFFERENT number to the call line
WA_DISP= "079 305 7321"          # WhatsApp, display format
EMAIL  = "info@cupboardcentre.co.za"
ADDR   = "Point S Building, Lower Level, Cnr Silva Street &amp; Old Pretoria Rd, Mbombela, 1200"
ADDR_Q = "Cupboard+Centre,+Old+Pretoria+Rd,+Mbombela,+1200"
FB     = "https://www.facebook.com/profile.php?id=61565764388558"
IG     = "https://www.instagram.com/cupboardcentre_diy"
TT     = "https://www.tiktok.com/@cupboardcentre_cc3"
GMAP   = "https://maps.google.com/maps?q=%s&z=15&output=embed" % ADDR_Q

# ---------------------------------------------------------------- image helpers
def _photos(page, kind='jpeg'):
    out=[]
    for u,meta in POOL.items():
        if meta['page']==page:
            out.append((u, meta['alt']))
    return out

KITCHEN  = _photos('gallery-designs-of-kitchen-cupboard.html')
BEDROOM  = _photos('gallery-bedroom-cupboards.html')
BATHROOM = _photos('gallery-bathroom-cabinetry.html')
CUSTOM   = _photos('gallery-custom-cabinetry.html')
DIY      = _photos('gallery-diy-units.html')
MELAMINE = [ (u,a) for u,a in _photos('melamine-doors-quartz-countertops.html') ]
INSTALL  = _photos('cupboard-installation.html') + _photos('kitchen-units.html')
GENERAL  = [ (u,a) for u,a in _photos('index.html') if u.lower().endswith(('.jpeg','.jpg')) ]
PRODUCT  = _photos('shop.html') + _photos('cc1.html')

def img(lst, i, alt_default=""):
    if not lst:
        return ("", alt_default)
    u,a = lst[i % len(lst)]
    return (IMG_MAP.get(u, u), (a or alt_default).replace('&amp;','&'))

def esc(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

# ---------------------------------------------------------------- SVG snippets
SVG_PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8c1.4 2.8 3.8 5.2 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.4.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.4c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.4 0 .8-.2 1l-2.2 2.2z"></path></svg>'
SVG_MAIL  = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2zm0 2v.4l8 5 8-5V6H4zm16 12V8.8l-7.5 4.7c-.3.2-.7.2-1 0L4 8.8V18h16z"></path></svg>'
SVG_PIN   = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"></path></svg>'
SVG_FB    = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.5 21v-7h2.3l.4-2.8h-2.7V9.3c0-.8.2-1.3 1.4-1.3h1.4V5.6C15.4 5.5 14.7 5.4 13.9 5.4c-2 0-3.4 1.2-3.4 3.5v1.9H8v2.8h2.5V21z"></path></svg>'
SVG_IG    = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5"></rect><circle cx="12" cy="12" r="3.8"></circle><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor" stroke="none"></circle></svg>'
SVG_CLOCK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5.2l3.2 1.9"/></svg>'
SVG_TT    = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 0 1-2.59 2.5 2.59 2.59 0 0 1 0-5.18c.27 0 .53.04.77.12v-3.2a5.76 5.76 0 0 0-.77-.05A5.72 5.72 0 0 0 4.14 15.3 5.72 5.72 0 0 0 9.86 21a5.72 5.72 0 0 0 5.72-5.72V9.01a7.35 7.35 0 0 0 4.28 1.37V7.3a4.28 4.28 0 0 1-3.26-1.48z"></path></svg>'
SVG_YT    = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 12s0-3.2-.4-4.7c-.2-.9-.9-1.5-1.7-1.7C19.4 5.2 12 5.2 12 5.2s-7.4 0-8.9.4c-.8.2-1.5.8-1.7 1.7C1 8.8 1 12 1 12s0 3.2.4 4.7c.2.9.9 1.5 1.7 1.7 1.5.4 8.9.4 8.9.4s7.4 0 8.9-.4c.8-.2 1.5-.8 1.7-1.7.4-1.5.4-4.7.4-4.7zM9.8 15.3V8.7l6.2 3.3z"></path></svg>'
SVG_WA    = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.5 15.2L2 22l4.9-1.4A10 10 0 1 0 12 2zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 1 1 12 20zm4.4-5.6c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.6.1s-.7.8-.8 1c-.2.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.2-.4.2-.4.6-1.2.1-.2 0-.4 0-.5s-.6-1.4-.8-1.9c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3c-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.2.8 3 .6.5-.1 1.4-.6 1.6-1.1.2-.6.2-1 .1-1.1s-.2-.2-.4-.3z"></path></svg>'
SVG_SHIELD= '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5 6.5 4.7v6.8c0 4.6 3.4 8.6 5.5 9.8 2.1-1.2 5.5-5.2 5.5-9.8V4.7L12 2.5z" fill="none" stroke="#ff5d5d" stroke-width="2.6"></path><path d="M12 2.5 6.5 4.7v6.8c0 4.6 3.4 8.6 5.5 9.8V2.5z" fill="#ff5d5d"></path></svg>'
# generic service icons
IC = {
 'install':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 21l2.6-.5 8.4-8.4-2.1-2.1-8.4 8.4z"/><path d="M13 11l3.8-3.8a2.7 2.7 0 0 0 0-3.8l-.9.9-1.9 1.9-.9.9"/><circle cx="16.5" cy="6.2" r=".6" fill="currentColor" stroke="none"/></svg>',
 'kitchen':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="2.5"/><path d="M12 3.5v17M3.5 12h17"/><circle cx="8.8" cy="8" r=".8" fill="currentColor" stroke="none"/><circle cx="15.2" cy="8" r=".8" fill="currentColor" stroke="none"/></svg>',
 'bed':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="3.5" width="16" height="17" rx="2.5"/><path d="M12 3.5v17"/><path d="M9.4 8.5v4M14.6 8.5v4"/></svg>',
 'bath':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 12.5h16v1.6a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5z"/><path d="M8 12.5V7.6a2.6 2.6 0 0 1 2.6-2.6H12"/><path d="M7 19l-1 2M18 19l1 2"/><circle cx="12.5" cy="5" r=".8" fill="currentColor" stroke="none"/></svg>',
 'door':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5.5" y="3" width="13" height="18" rx="2.2"/><circle cx="15" cy="12" r="1.1" fill="currentColor" stroke="none"/></svg>',
 'quartz':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 8.5h18l-2.2 3.2H5.2z"/><path d="M5.2 11.7V19M18.8 11.7V19M5.2 19h13.6"/></svg>',
 'custom':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M14 6l4 4"/><path d="M4.4 19.6 6 15.8 8.2 18z" fill="currentColor" stroke="none"/></svg>',
 'diy':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 8.2v7.6a1.9 1.9 0 0 1-1 1.6l-7 3.8a1.9 1.9 0 0 1-1.8 0l-7-3.8A1.9 1.9 0 0 1 3 15.8V8.2a1.9 1.9 0 0 1 1-1.6l7-3.8a1.9 1.9 0 0 1 1.8 0l7 3.8A1.9 1.9 0 0 1 21 8.2z"/><path d="m3.5 7.3 8.5 4.7 8.5-4.7M12 22V12"/></svg>',
 'ruler':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2.5" y="6" width="19" height="12" rx="3"/><circle cx="8" cy="12" r="3.3"/><circle cx="8" cy="12" r="1" fill="currentColor" stroke="none"/><path d="M14 9.2v2M16.5 9.2v2M19 9.2v2"/></svg>',
 'hinge':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="4" width="6.5" height="16" rx="1.8"/><rect x="13.5" y="4" width="6.5" height="16" rx="1.8"/><circle cx="12" cy="8" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="16" r="1.1" fill="currentColor" stroke="none"/></svg>',
 'calendar':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12.5" r="8.5"/><path d="M12 8v4.5l3 2"/><path d="M12 2.2v1.6"/></svg>',
 'truck':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="1.5" y="6.5" width="13" height="9.5" rx="1.8"/><path d="M14.5 9.5h3.2l2.8 3.2V16h-6z"/><circle cx="6" cy="18" r="2.1"/><circle cx="17.3" cy="18" r="2.1"/></svg>',
 'check':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="9" r="5.5"/><path d="M8.4 13 7 22l5-2.9L17 22l-1.4-9"/><circle cx="12" cy="9" r="2" fill="currentColor" stroke="none"/></svg>',
 'wallet':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12.6 2.6A2 2 0 0 0 11.2 2H4.5A2.5 2.5 0 0 0 2 4.5v6.7a2 2 0 0 0 .6 1.4l8.7 8.7a2.4 2.4 0 0 0 3.4 0l6.6-6.6a2.4 2.4 0 0 0 0-3.4z"/><circle cx="7.4" cy="7.4" r="1.7" fill="currentColor" stroke="none"/></svg>',
 'target':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.6" fill="currentColor" stroke="none"/></svg>',
 'eye':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.6-6.8 10-6.8S22 12 22 12s-3.6 6.8-10 6.8S2 12 2 12z"/><circle cx="12" cy="12" r="3.2"/><circle cx="12" cy="12" r="1" fill="currentColor" stroke="none"/></svg>',
 'drop':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5c4 5 6.5 7.7 6.5 11a6.5 6.5 0 0 1-13 0c0-3.3 2.5-6 6.5-11z"/><path d="M9 15.2a2.6 2.6 0 0 0 2.5 2.3"/></svg>',
 'layout':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2.5"/><path d="M3 9.5h18M9.5 9.5V21"/><rect x="4.6" y="4.6" width="3.2" height="3.2" rx=".7" fill="currentColor" stroke="none"/></svg>',
 'gem':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 3h14l3 6-10 12L2 9z"/><path d="M2 9h20M9 3 7 9l5 12 5-12-2-6"/></svg>',
 'pin':'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5a7 7 0 0 0-7 7c0 5 7 12.5 7 12.5s7-7.5 7-12.5a7 7 0 0 0-7-7z"/><circle cx="12" cy="9.4" r="2.4" fill="currentColor" stroke="none"/></svg>',
}

print("gen.py config loaded. Category counts:",
      "kitchen",len(KITCHEN),"bedroom",len(BEDROOM),"bathroom",len(BATHROOM),
      "custom",len(CUSTOM),"diy",len(DIY),"melamine",len(MELAMINE),
      "install",len(INSTALL),"general",len(GENERAL),"product",len(PRODUCT))

# ============================================================ shared components
FONTS = "https://fonts.googleapis.com/css2?family=Montserrat:wght@600;700&family=Open+Sans:wght@400;500;600;700&family=Poppins:wght@500;600;700&display=swap"

# nav service dropdown
SERVICES = [
    ("Complete Installation", "cupboard-installation.html"),
    ("DIY Kitchen Units", "kitchen-units.html"),
    ("Bedroom Cupboards", "bedroom-cupboards.html"),
    ("Bathroom Cabinets", "bathroom-cabinets.html"),
    ("Melamine Doors &amp; Quartz Countertops", "melamine-doors-quartz-countertops.html"),
    ("Shopfitting &amp; Custom Cabinetry", "custom-cabinetry.html"),
    ("Office &amp; Reception Desks", "office-reception-desks.html"),
    ("DIY Units &amp; Flat-Packs", "diy-units.html"),
    ("All Services", "services.html"),
]


SITE_URL = "https://www.cupboardcentre.co.za"

def sch_breadcrumb(trail):
    """trail: list of (name, path) ending with the current page."""
    items = []
    for i, (name, path) in enumerate(trail, 1):
        items.append('{"@type":"ListItem","position":%d,"name":%s,"item":"%s%s"}'
                     % (i, json.dumps(name.replace('&amp;','&')), SITE_URL, path))
    return '{"@type":"BreadcrumbList","itemListElement":[%s]}' % ",".join(items)

def sch_service(name, desc, path):
    return ('{"@type":"Service","name":%s,"description":%s,"url":"%s%s",'
            '"serviceType":%s,'
            '"provider":{"@type":"HomeAndConstructionBusiness","name":"Cupboard Centre","@id":"%s/"},'
            '"areaServed":[%s]}'
            % (json.dumps(name.replace('&amp;','&')), json.dumps(desc.replace('&amp;','&')),
               SITE_URL, path, json.dumps(name.replace('&amp;','&')), SITE_URL,
               ",".join('{"@type":"City","name":"%s"}' % t for t in
                        ["Nelspruit","Mbombela","White River","Hazyview","Barberton","Sabie","Malelane"])))

def sch_faq(pairs):
    qs = ",".join('{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
                  % (json.dumps(q.replace('&amp;','&')), json.dumps(a.replace('&amp;','&')))
                  for q, a in pairs)
    return '{"@type":"FAQPage","mainEntity":[%s]}' % qs

def head(title, desc, canonical, og_img, schema=None, local_business=False, preload=None):
    # canonical must byte-match what the server serves: extensionless, no index.html
    if canonical.endswith('/index.html'): canonical = canonical[:-10]
    elif canonical.endswith('.html'):     canonical = canonical[:-5]
    subnav = "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in SERVICES)
    ld = (
      '{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",'
      '"name":"Cupboard Centre","image":"%s","@id":"https://www.cupboardcentre.co.za/",'
      '"url":"https://www.cupboardcentre.co.za/","telephone":"+27846837467",'
      '"email":"%s",'
      '"openingHours":["Mo-Th 07:00-17:00","Fr 07:00-16:30","Sa 07:30-13:30"],'
      '"address":{"@type":"PostalAddress","streetAddress":"Point S Building, Lower Level, Cnr Silva Street & Old Pretoria Rd","addressLocality":"Mbombela","addressRegion":"Mpumalanga","postalCode":"1200","addressCountry":"ZA"},'
      '"areaServed":[{"@type":"City","name":"Nelspruit"},{"@type":"City","name":"Mbombela"},{"@type":"City","name":"White River"}],'
      '"sameAs":["%s","%s","%s"]}' % (og_img, EMAIL, FB, IG, TT)
    )
    # LocalBusiness belongs on the homepage and contact page only; every other page
    # carries the schema that describes what THAT page is.
    nodes = ([ld] if local_business else []) + list(schema or [])
    if not nodes:
        nodes = ['{"@context":"https://schema.org","@type":"WebPage","name":%s,"url":"%s"}'
                 % (json.dumps(title.replace('&amp;','&')), canonical)]
    ld = ('{"@context":"https://schema.org","@graph":[%s]}' % ",".join(nodes)) if len(nodes) > 1 else nodes[0]
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Cupboard Centre">
<link rel="canonical" href="{canonical}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cupboard Centre">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_img}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="assets/css/fonts.css">
<link rel="stylesheet" href="assets/css/styles.css">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" href="/assets/images/favicon.png" type="image/png" sizes="500x500">
<link rel="apple-touch-icon" href="/assets/images/apple-touch-icon.png">
{preload}
<script type="application/ld+json">{ld}</script>
</head>
<body>
""".format(title=title, desc=desc, canonical=canonical, og_img=og_img, fonts=FONTS,
           subnav=subnav, ld=ld,
           preload='{preload}')

def logo(href="index.html", dark_bg=False):
    if dark_bg:
        return ('<a class="logo" href="%s" aria-label="Cupboard Centre home">'
                '<img class="logo-img flogo-black" src="assets/images/photos/66db6af75f06f55b858a6efc.png" alt="Cupboard Centre" width="200" height="52"></a>') % href
    return ('<a class="logo" href="%s" aria-label="Cupboard Centre home">'
            '<img class="logo-img" src="assets/images/photos/66db6af75f06f55b858a6efc.png" alt="Cupboard Centre" width="200" height="52"></a>') % href

def header(active="", cart=False):
    def a(label, href):
        return '<li><a href="%s">%s</a></li>' % (href, label)
    subnav = "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in SERVICES)
    m_subnav = subnav
    cart_svg = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                '<circle cx="9" cy="20.5" r="1.5"/><circle cx="18" cy="20.5" r="1.5"/>'
                '<path d="M2.5 3h2.2l2.3 12a1.6 1.6 0 0 0 1.6 1.3h8.9a1.6 1.6 0 0 0 1.6-1.3L21 6.5H6.2"/></svg>')
    return """<div class="topbar"><div class="wrap">
  <div class="ti-left">
    <span class="ti-avail"><span class="ti-dot"></span>Open &amp; ready to help with your project</span>
    <a href="tel:{tel}"><strong>Call {phone}</strong></a>
    <ul class="ti-social">
      <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">{s_wa}</a></li>
      <li><a href="{fb}" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{s_fb}</a></li>
      <li><a href="{ig}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{s_ig}</a></li>
    </ul>
  </div>
</div></div>
<header class="mainheader"><div class="wrap">
  {logo}
  <nav aria-label="Primary"><ul class="nav">
    <li><a href="index.html">Home</a></li>
    <li class="has-sub"><a href="services.html">Services</a><ul class="subnav">{subnav}</ul></li>
    <li><a href="shop.html">Shop</a></li>
    <li><a href="gallery.html">Gallery</a></li>
    <li><a href="about.html">About</a></li>
    <li><a href="blog.html">Blog</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul></nav>
  <div class="hdr-right">
    <a class="nav-cart" href="cart.html" aria-label="View cart">{cart_svg}<span class="cart-count" data-cart-count hidden>0</span></a>
    <span class="nav-cta"><a href="get-a-quote.html">Get a Free Quote</a></span>
    <a class="hdr-call" href="tel:{tel}" aria-label="Call us now">{s_ph}<span>Call Now</span></a>
    <button class="hamburger" aria-label="Menu" aria-expanded="false">☰</button>
  </div>
</div>
<div class="mobile-menu"><ul>
  <li><a href="index.html">Home</a></li>
  <li class="m-has-sub"><button class="m-sub-toggle" aria-expanded="false">Services <span class="m-caret">▾</span></button>
    <ul class="m-subnav">{m_subnav}</ul></li>
  <li><a href="shop.html">Shop</a></li>
  <li><a href="gallery.html">Gallery</a></li>
  <li><a href="about.html">About</a></li>
  <li><a href="blog.html">Blog</a></li>
  <li><a href="contact.html">Contact</a></li>
  <li><a href="cart.html">Cart</a></li>
  <li><a href="get-a-quote.html">Get a Free Quote</a></li>
  <li><a href="tel:{tel}">Call {phone}</a></li>
  <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp Us</a></li>
</ul></div>
</header><main id="main">
""".format(tel=TEL, phone=PHONE, wa=WA, fb=FB, ig=IG, s_fb=SVG_FB, s_ig=SVG_IG, s_wa=SVG_WA,
           s_ph=SVG_PHONE, logo=logo(), subnav=subnav, m_subnav=m_subnav, cart_svg=cart_svg)

# ---- lead form (used in hero, cta band, quote page) ----
def lead_form(title="Request Your Free Quote", note="We’ll call you back once we receive your form.", btn="Get My Free Quote", project=True):
    opts = ["Get a Free Quote","DIY Cupboards &amp; Flat-Packs","Kitchen Units","Bedroom Cupboards",
            "Bathroom Cabinetry","Melamine Doors","Quartz Countertops","Custom Cabinetry &amp; Shopfitting",
            "Installation","Other"]
    o = "".join("<option>%s</option>" % x for x in opts)
    projopts = "".join("<option>%s</option>" % x for x in ["New build","Renovation / replacement","DIY (self-assemble)","Full supply &amp; install"])
    proj = ('<select class="field full" aria-label="Project Type" data-role="project" required><option value="">Project Type</option>%s</select>' % projopts) if project else ''
    return """<form class="lead-form" data-lead>
      <h2 class="lf-title">{title}</h2>
      <span class="form-note">{note}</span>
      <div class="grid2">
        <input class="field" placeholder="Your Name" required aria-label="Your Name" data-role="name">
        <input class="field" type="tel" placeholder="Phone Number" required aria-label="Phone Number" data-role="phone" inputmode="tel" pattern="^(\\+?27|0)[\\s\\-().]*\\d(?:[\\s\\-().]*\\d){{8}}$" title="Enter a 10-digit SA number (e.g. 082 123 4567) or +27 followed by 9 digits.">
        <input class="field full" type="email" placeholder="Email Address" required aria-label="Email Address" data-role="email">
        <select class="field full" aria-label="How Can We Help?" data-role="service" required><option value="">How Can We Help?</option>{o}</select><input type="text" class="field full" placeholder="Please specify" data-role="service_other" style="display:none">
        {proj}<input class="field full" placeholder="Suburb / Area" aria-label="Suburb / Area" data-role="suburb" required><textarea class="field full" placeholder="Tell us what you need (optional)" aria-label="Brief message (optional)" data-role="message"></textarea>
      </div>
      <label class="lead-consent" style="display:flex;gap:10px;align-items:flex-start;margin:14px 0 0;font-size:.85rem;line-height:1.4;cursor:pointer;text-align:left"><input type="checkbox" data-role="consent" checked style="margin-top:3px;flex:0 0 auto;width:16px;height:16px;cursor:pointer"><span>I agree to be contacted by Cupboard Centre about my enquiry. See our <a href="privacy-policy.html" style="text-decoration:underline">Privacy Policy</a>.</span></label>
      <p style="margin:14px 0 0"><button type="submit" class="btn btn-green btn-arrow" style="width:100%">{btn}</button></p>
    </form>""".format(title=title, note=note, o=o, proj=proj, btn=btn)

# ---- reviews section (reusable) ----
REVIEWS = [
 ("Trish Pearce","Google Review","5.0","I had a dressing table made and a cupboard fitted. I paid on Tuesday and they fitted on Thursday. They were amazing, the staff were very polite and professional. I am very happy and I recommend this company and their work.",True),
 ("Fortune Ngomane","Google Review","5.0","Recommended!!",False),
 ("Marinda De Clercq","Google Review","5.0","Left Cupboard Centre a 5-star rating.",False),
 ("Paul Stander","Google Review","5.0","Left Cupboard Centre a 5-star rating.",False),
]
GREV = '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.611 20.083H42V20H24v8h11.303c-1.649 4.657-6.08 8-11.303 8-6.627 0-12-5.373-12-12s5.373-12 12-12c3.059 0 5.842 1.154 7.961 3.039l5.657-5.657C34.046 6.053 29.268 4 24 4 12.955 4 4 12.955 4 24s8.955 20 20 20 20-8.955 20-20c0-1.341-.138-2.65-.389-3.917z"></path><path fill="#FF3D00" d="M6.306 14.691l6.571 4.819C14.655 15.108 18.961 12 24 12c3.059 0 5.842 1.154 7.961 3.039l5.657-5.657C34.046 6.053 29.268 4 24 4 16.318 4 9.656 8.337 6.306 14.691z"></path><path fill="#4CAF50" d="M24 44c5.166 0 9.86-1.977 13.409-5.192l-6.19-5.238C29.211 35.091 26.715 36 24 36c-5.202 0-9.619-3.317-11.283-7.946l-6.522 5.025C9.505 39.556 16.227 44 24 44z"></path><path fill="#1976D2" d="M43.611 20.083H42V20H24v8h11.303c-.792 2.237-2.231 4.166-4.087 5.571l6.19 5.238C36.971 39.205 44 34 44 24c0-1.341-.138-2.65-.389-3.917z"></path></svg>'
FREV = '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#1877F2" d="M24 4C12.95 4 4 12.95 4 24c0 9.98 7.31 18.25 16.88 19.75V29.78h-5.08V24h5.08v-4.41c0-5.02 2.99-7.79 7.56-7.79 2.19 0 4.48.39 4.48.39v4.92h-2.52c-2.49 0-3.26 1.54-3.26 3.12V24h5.55l-.89 5.78h-4.66v13.97C36.69 42.25 44 33.98 44 24 44 12.95 35.05 4 24 4z"></path></svg>'

def review_slide(rv):
    who, plat, score, quote, clamp = rv
    src = FREV if 'Facebook' in plat else GREV
    lab = 'Facebook review' if 'Facebook' in plat else 'Google review'
    clampcls = ' rev-clamp' if clamp else ''
    toggle = '<button type="button" class="rev-toggle">Read more</button>' if clamp else ''
    initial = who.strip()[0]
    av = ('<span class="rev-avatar" aria-hidden="true" style="display:flex;align-items:center;justify-content:center;'
          'font-family:\'Poppins\',sans-serif;font-weight:700;color:#fff;background:var(--green)">%s</span>' % initial)
    return ('<div class="rev-slide"><article class="rev-card%s">'
            '<span class="rev-source" role="img" aria-label="%s">%s</span>'
            '<div class="rev-stars">★★★★★ <span class="rev-score">%s</span></div>'
            '<p class="rev-quote">&ldquo;%s&rdquo;</p>%s'
            '<div class="rev-meta">%s<span class="rev-id"><span class="rev-who">%s</span>'
            '<span class="rev-platform">%s</span></span></div></article></div>'
            ) % (clampcls, lab, src, score, quote, toggle, av, who, plat)

def reviews_section(bg="bg-navy-slate"):
    slides = "".join(review_slide(r) for r in REVIEWS)
    dots = "".join('<button class="cdot%s" aria-label="Go to review page %d"></button>' % ((' active' if i==0 else ''), i+1) for i in range(max(1, -(-len(REVIEWS)//3))))
    return """<section id="reviews" class="section {bg}"><div class="wrap">
  <div class="reviews-head"><span class="eyebrow">What Clients Say</span>
  <h2 class="reviews-score">Loved by Homes &amp; <span class="g2">Contractors</span></h2>
  <p>A 5.0 rating from our Google reviews, real feedback from Cupboard Centre customers across Nelspruit and Mbombela.</p></div>
  <div class="review-carousel" data-carousel>
    <button class="carousel-arrow prev" data-prev aria-label="Previous reviews">‹</button>
    <div class="carousel-viewport"><div class="carousel-track" data-track>{slides}</div></div>
    <button class="carousel-arrow next" data-next aria-label="Next reviews">›</button>
  </div>
  <div class="carousel-dots" data-dots>{dots}</div>
  <div class="review-links">
    <a class="btn btn-outline" href="{fb}" target="_blank" rel="noopener noreferrer"><span class="rl-ico">{frev}</span>See Our Facebook Reviews</a>
    <a class="btn btn-outline" href="{ig}" target="_blank" rel="noopener noreferrer"><span class="rl-ico">{ig_ico}</span>Follow Us on Instagram</a>
  </div>
</div></section>
""".format(bg=bg, slides=slides, dots=dots, fb=FB, ig=IG, frev=FREV, ig_ico=SVG_IG)

MARQUEE_ITEM = ('<span class="mq-item"><img class="mq-logo flogo-white" '
                'src="assets/images/photos/66db6af75f06f55b858a6efc.png" alt="" aria-hidden="true" '
                'width="180" height="46" loading="lazy" decoding="async"></span>')
def marquee():
    return '<div class="marquee marquee-dark" aria-hidden="true"><div class="marquee-track">%s</div></div>\n' % (MARQUEE_ITEM*16)

# trusted supplier / partner brands (real logos sourced from each brand)
PARTNERS = [
    ("PG Bison",       "assets/images/photos/partners/pg-bison.png",       "https://pgbison.co.za",       "p-green"),
    ("Wood4U",         "assets/images/photos/partners/wood4u.png",         "https://wood4u.co.za",        ""),
    ("Eezi Quartz",    "assets/images/photos/partners/eezi-quartz.png",    "https://www.eeziquartz.co.za",""),
    ("Sonae Arauco",   "assets/images/photos/partners/sonae-arauco.svg",   "https://www.sonaearauco.com", ""),
    ("FHD, Fitting &amp; Handle Distributors", "assets/images/photos/partners/fhd.png", "https://fhd.co.za", ""),
    ("National Edging","assets/images/photos/partners/national-edging.png","https://www.nationaledging.co.za",""),
]
def partners_band():
    cards=""
    for name, src, href, cls in PARTNERS:
        c = " "+cls if cls else ""
        cards += ('<a class="partner-card" href="%s" target="_blank" rel="noopener noreferrer" '
                  'title="%s"><img class="partner-logo%s" src="%s" alt="%s logo" loading="lazy" '
                  'decoding="async"></a>') % (href, name, c, src, name)
    return """<section id="partners" class="section partners-band"><div class="wrap section-center">
  <span class="eyebrow eyebrow-rule">In Partnership With Our Trusted Partners</span>
  <div class="partner-grid">%s</div>
</div></section>
""" % cards

def cta_form():
    return """<section id="cta-form" class="cta-band"><div class="cta-panel">
  <div>
    <span class="eyebrow">Free, No-Obligation Quote</span>
    <h2>Get Your Free Cupboard Quote Today</h2>
    <p>No pressure, no obligation, just honest advice and a clear written quote. Tell us about your space and we’ll get straight back to you.</p>
    <p class="btn-row" style="margin-top:18px"><a class="btn btn-ghost" href="tel:{tel}">Call {phone}</a> <a class="btn btn-ghost" href="https://wa.me/{wa}" target="_blank" rel="noopener">WhatsApp Us</a></p>
  </div>
  {form}
</div></section>
""".format(tel=TEL, phone=PHONE, wa=WA, wa_disp=WA_DISP, form=lead_form(project=False))

def footer():
    svc = "".join('<li><a href="%s">%s</a></li>' % (h, t) for t, h in SERVICES[:6])
    return """</main><footer class="footer"><div class="wrap">
  <div class="footer-cols">
    <div>
      {logo}
      <h2 class="h4" style="margin-top:18px">About Us</h2>
      <p>For over 25 years, Cupboard Centre has supplied and installed top-quality DIY and custom cupboards, kitchens, bedrooms, bathrooms, melamine doors and quartz countertops, for homes and businesses across Mpumalanga.</p>
    </div>
    <div><h2 class="h4">Our Services</h2><ul>{svc}</ul></div>
    <div><h2 class="h4">Quick Links</h2><ul>
      <li><a href="shop.html">Online Shop</a></li>
      <li><a href="gallery.html">Gallery</a></li>
      <li><a href="about.html">About Us</a></li>
      <li><a href="faq.html">FAQ</a></li>
      <li><a href="blog.html">Blog</a></li>
      <li><a href="get-a-quote.html">Get a Free Quote</a></li>
      <li><a href="service-areas.html">Service Areas</a></li>
    </ul></div>
    <div><h2 class="h4">Get In Touch</h2>
      <ul class="fcontact">
        <li><a href="tel:{tel}"><span class="fc-ico">{s_ph}</span><span>{phone}</span></a></li>
        <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener"><span class="fc-ico">{s_wa}</span><span>WhatsApp {wa_disp}</span></a></li>
        <li><a href="mailto:{email}"><span class="fc-ico">{s_ml}</span><span>{email}</span></a></li>
        <li><a href="https://maps.google.com/maps?q={addrq}" target="_blank" rel="noopener"><span class="fc-ico">{s_pin}</span><span>Point S Building, Cnr Silva St, Mbombela</span></a></li>
        <li class="fhours"><span class="fc-ico">{s_clock}</span><span>Mon&ndash;Thu 07:00&ndash;17:00 · Fri 07:00&ndash;16:30<br>Sat 07:30&ndash;13:30 · Sun closed</span></li>
      </ul>
      <ul class="fsocial">
        <li><a href="{fb}" target="_blank" rel="noopener noreferrer" aria-label="Facebook">{s_fb}</a></li>
        <li><a href="{ig}" target="_blank" rel="noopener noreferrer" aria-label="Instagram">{s_ig}</a></li>
        <li><a href="{tt}" target="_blank" rel="noopener noreferrer" aria-label="TikTok">{s_tt}</a></li>
        <li><a href="https://wa.me/{wa}" target="_blank" rel="noopener noreferrer" aria-label="WhatsApp">{s_wa}</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">© 2026 Cupboard Centre. All Rights Reserved. | Nelspruit &amp; Mbombela’s DIY &amp; custom cupboard specialists. | <a href="privacy-policy.html">Privacy Policy</a> · <a href="sitemap.html">Sitemap</a></div>
</div></footer>
<script src="assets/js/app.js" defer></script>
</body>
</html>""".format(logo=logo(dark_bg=True), svc=svc, tel=TEL, phone=PHONE, wa=WA, email=EMAIL, addrq=ADDR_Q,
                  s_ph=SVG_PHONE, s_wa=SVG_WA, s_ml=SVG_MAIL, s_pin=SVG_PIN, wa_disp=WA_DISP,
                  s_clock=SVG_CLOCK,
                  fb=FB, ig=IG, tt=TT, s_fb=SVG_FB, s_ig=SVG_IG, s_tt=SVG_TT)

def page_hero(current, eyebrow, h1, subtitle="", cta=True, trail=None, bg_img=None, prefix=""):
    cr = '<a href="%sindex.html">Home</a>' % prefix
    for label, href in (trail or []):
        cr += '<span class="sep">›</span><a href="%s%s">%s</a>' % (prefix, href, label)
    cr += '<span class="sep">›</span><span class="cur">%s</span>' % current
    sub = '<p style="max-width:46em;margin:0 auto">%s</p>' % subtitle if subtitle else ''
    ctab = ''  # sub-page heroes carry no button (removed per request)
    # every sub-page hero carries a photo behind a red overlay (like cupboardcentre.co.za)
    if bg_img is None:
        bg_img = img(GENERAL, 0)[0]
    overlay = "linear-gradient(rgba(20,14,15,0.34) 0%,rgba(20,14,15,0.5) 60%,rgba(20,14,15,0.62) 100%)"
    style = ('padding:76px 0;background:%s,url(%s);background-size:cover;background-position:center' % (overlay, bg_img))
    return """<section class="page-hero" style="{style}"><div class="wrap section-center text-white">
  <nav class="crumbs" aria-label="Breadcrumb">{cr}</nav>
  <span class="eyebrow">{eyebrow}</span><h1 style="color:#fff">{h1}</h1>{sub}{ctab}
</div></section>
""".format(style=style, cr=cr, eyebrow=eyebrow, h1=h1, sub=sub, ctab=ctab)

import re as _re
def clean_urls(html):
    """Internal links -> root-relative and extensionless (/about, not about.html).

    The old Wix site served extensionless URLs, so this keeps the new site on the
    same URL shape and removes a whole class of redirects. Root-relative also makes
    the link correct from any directory depth (e.g. /blog/post)."""
    def fix(m):
        href = m.group(1)
        if href.startswith(('http://', 'https://', '#', 'tel:', 'mailto:', '//')):
            return m.group(0)
        path = href.lstrip('./')
        while path.startswith('../'):
            path = path[3:]
        path = path[:-5] if path.endswith('.html') else path
        return 'href="/"' if path in ('index', '') else 'href="/%s"' % path
    return _re.sub(r'href="([^"]+\.html)"', fix, html)

def use_webp(html):
    """Point every <img>/background at the .webp twin when one exists on disk."""
    def swap(m):
        pre, path, post = m.group(1), m.group(2), m.group(3)
        webp = _re.sub(r'\.(jpe?g|png)$', '.webp', path, flags=_re.I)
        disk = webp.lstrip('./')
        while disk.startswith('../'): disk = disk[3:]
        return pre + webp + post if os.path.exists(os.path.join(OUT, disk)) else m.group(0)
    html = _re.sub(r'(src=")([^"]+\.(?:jpe?g|png))(")', swap, html, flags=_re.I)
    html = _re.sub(r'(url\()([^)"\']+\.(?:jpe?g|png))(\))', swap, html, flags=_re.I)
    return html


def responsive_img(u, alt, cls="", extra=""):
    """Gallery grid image: 700px thumb by default, full file for retina + lightbox.

    `u` arrives as the original .jpg/.png path (the webp swap runs later in write()),
    so derive both variants from the base name here."""
    base = _re.sub(r'\.(jpe?g|png|webp)$', '', u)
    full, sm = base + '.webp', base + '-sm.webp'
    def on_disk(x): return os.path.exists(os.path.join(OUT, x.lstrip('/')))
    if on_disk(full) and on_disk(sm):
        return ('<img src="%s" srcset="%s 700w, %s 1600w"'
                ' sizes="(max-width:700px) 100vw, (max-width:1000px) 50vw, 33vw"'
                ' data-full="%s" alt="%s"%s%s loading="lazy" decoding="async">'
                % (sm, sm, full, full, alt, (' class="%s"' % cls) if cls else '', extra))
    return '<img src="%s" alt="%s"%s%s loading="lazy" decoding="async">' % (u, alt, (' class="%s"' % cls) if cls else '', extra)

HOME_HERO = "assets/images/photos/66f6cc2b52153310a558a6b1.webp"  # .hero-panel bg in styles.css

def add_hero_preload(html):
    """Preload the page-hero background: it is the LCP element and, being a CSS
    url(), is only discovered after CSS parses. Derived from the emitted markup so
    the preload URL always byte-matches the request. Pages without a hero image
    (the homepage hero is plain white) get no preload."""
    m = _re.search(r'class="page-hero"[^>]*style="[^"]*url\(([^)]+)\)', html)
    hero_url = m.group(1) if m else (HOME_HERO if 'class="hero-panel"' in html else None)
    if not hero_url:
        return html.replace('{preload}\n', '').replace('{preload}', '')
    tag = '<link rel="preload" as="image" href="%s" fetchpriority="high">' % hero_url
    return html.replace('{preload}', tag, 1).replace('{preload}', '')

def write(name, html):
    html = add_hero_preload(use_webp(clean_urls(html)))
    path = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w').write(html)
    return len(html)

print("components loaded OK")

# ============================================================ blog data
BLOG = [
 ("choosing-the-perfect-kitchen-units","A Complete Guide to Choosing the Perfect Kitchen Units",
  "The quest for the perfect kitchen units often hits a snag when it comes to selecting units that blend function with style. Here’s how to get it right.",
  "Kitchens", KITCHEN,
  [("Start with how you actually use your kitchen","Before you fall in love with a finish, map how you cook, store and move. The best kitchen units are planned around the ‘work triangle’ between your sink, stove and fridge, with the cupboards and drawers you reach for most placed within easy reach. At Cupboard Centre we start every kitchen with this conversation, because layout drives everything else."),
   ("Choose a door finish that suits your life","Melamine doors are hard-wearing, easy to clean and available in dozens of colours and wood-grains, ideal for busy family kitchens. For a more premium look, add a quartz countertop and soft-close hinges. We’ll show you real samples so you can see and feel the difference before you commit."),
   ("Don’t forget storage that works harder","Deep drawers for pots, built-in spice racks, a dedicated appliance garage and a proper pantry column turn an ordinary kitchen into one that’s a pleasure to use. Custom or DIY, we size every unit to your space so nothing is wasted."),
   ("DIY or fully installed?","If you’re handy, our pre-cut, pre-drilled DIY kitchen units arrive labelled and ready to assemble, a big saving. Prefer to leave it to us? Our team measures, builds and installs the whole kitchen for you. Either way, the quality is the same.")]),
 ("durable-quartz-countertops","The Ultimate Guide to Durable Quartz Countertops",
  "Tired of countertops that can’t stand up to daily use? We unveil why quartz outperforms granite and concrete, and how to choose the right slab.",
  "Countertops", KITCHEN,
  [("Why quartz has become the countertop of choice","Quartz is an engineered stone, natural quartz crystals bound with resin, which makes it exceptionally hard, non-porous and consistent in colour. Unlike natural stone, it doesn’t need sealing, resists stains and scratches, and shrugs off the daily grind of a working kitchen."),
   ("Quartz vs granite vs melamine tops","Granite is beautiful but porous and needs regular sealing. Melamine tops are affordable and versatile. Quartz sits at the premium end: the low-maintenance durability of stone with a flawless, uniform finish. We stock Eazi Quartz and can match it to your doors."),
   ("Caring for your quartz top","Simply wipe with warm soapy water, no harsh chemicals or abrasive pads needed. Use a board for chopping and a trivet for very hot pots, and your quartz will look showroom-fresh for decades."),
   ("Getting the right fit","A countertop is only as good as its template and installation. Our team measures precisely and installs cleanly, so your joins are tight and your overhangs correct.")]),
 ("granite-countertops-for-your-home","Timeless Elegance: Granite Countertops for Your Home",
  "Granite brings natural character to a kitchen or bathroom. Here’s what to know about choosing, sealing and living with a granite surface.",
  "Countertops", KITCHEN,
  [("The natural beauty of granite","No two granite slabs are alike. That natural variation, the flecks, veins and depth of colour, gives every kitchen a one-of-a-kind centrepiece that engineered surfaces can’t quite replicate."),
   ("What to expect from natural stone","Granite is heat-resistant and hard-wearing, but because it’s porous it should be sealed on installation and re-sealed periodically. Done right, it’s a surface that lasts a lifetime."),
   ("Pairing granite with the right cabinetry","Warm wood-grain melamine doors, crisp white units or bold dark cabinetry, granite works with all of them. We’ll help you balance the tones so your countertop and cupboards feel like one design.")]),
 ("expert-solutions-for-shop-fitting","Retail Transformation: Expert Solutions for Shop Fitting",
  "The right shop fitting turns floor space into sales. See how custom counters, display units and storage are built to work as hard as you do.",
  "Custom & Shopfitting", CUSTOM,
  [("Shop fitting that sells","Your counters, shelving and display units are silent salespeople. We design and build retail fittings that guide customers, showcase stock and make the most of every square metre, all finished in hard-wearing materials that survive heavy trading."),
   ("Built for your brand and your space","From reception desks and service counters to modular storage and back-of-house cabinetry, everything is made to measure. Choose finishes and colours that match your brand, and we’ll handle the build and installation."),
   ("Durable where it counts","Retail takes a beating. We specify robust melamine, quality edging and soft-close hardware so your fittings still look sharp years down the line.")]),
]

NEW_POSTS = [
 ("how-to-install-kitchen-cupboards","How to Install Kitchen Cupboards: A Step-by-Step Guide",
  "Fitting your own kitchen units is very doable if you get the first two steps right. Here is the order we work in, and the mistakes that cost people a weekend.",
  "Kitchens", KITCHEN,
  [("Check the walls before you check the cupboards",
    "Almost no wall in a real house is straight, level or square, and almost every installation problem traces back to that. Before anything comes out of a box, run a long spirit level along the floor and up the walls and find your high point and your worst bulge. If the floor drops 15&nbsp;mm across a four-metre run, you need to know that now, not when the last unit refuses to line up with the first."),
   ("Set a datum line and work from it",
    "Draw one level pencil line right around the room at the height of the top of your base units, measured up from the highest point of the floor. Every unit gets set to that line, and the gaps that result at the bottom get hidden by the plinth. This single step is the difference between a run of cupboards that reads as one clean line and one that visibly wanders."),
   ("Hang the wall units first, not the base units",
    "It feels backwards, but fitting the wall cupboards while the floor is still clear saves a lot of awkward reaching over base units. Find the studs or use proper cavity fixings rated well above the loaded weight of the cupboard, hang the rail, and check each unit against your datum line as you go. Join neighbouring units to each other before you fully tighten them to the wall."),
   ("Level, shim and join the base units",
    "Set each base unit on its legs, bring it up to the datum line, and pack behind it where the wall bows. Clamp adjoining units together, check the fronts are flush, then screw them to each other through the side panels. Cupboards that are joined to each other stay in line; cupboards that are only screwed to the wall drift apart over time."),
   ("Leave doors and drawers until last",
    "Fit the carcasses, get your countertop templated, and only then hang doors and fit drawer fronts. Modern soft-close hinges adjust in three directions, so budget an unhurried hour at the end purely for adjustment. Consistent gaps between doors are what make a kitchen look professionally fitted, and they are almost entirely down to that final hour."),
   ("When it is worth handing it over",
    "DIY makes sense for a straightforward run of units on sound walls. It makes less sense where you are cutting into a quartz top, moving plumbing or electrics, or working around an awkward corner that needs a scribed filler. Our pre-cut, pre-drilled units are built for self-assembly, and if you would rather not do the fitting, our own installers will measure, build and fit the whole kitchen for you.")]),

 ("cost-of-built-in-cupboards-south-africa","What Do Built-In Cupboards Cost in South Africa?",
  "Quotes for built-in cupboards vary enormously, and it is rarely obvious why. Here is what actually drives the price, and how to compare two quotes fairly.",
  "Buying Guides", BEDROOM,
  [("Why two quotes for the same cupboard differ so much",
    "Built-in cupboards are priced per running metre of finished cabinetry, but that headline number hides four separate decisions: the board, the doors, the internal layout and the hardware. Two companies can quote the same metre and mean very different things by it. Understanding the four levers is what lets you tell a genuinely cheaper quote from one that has simply left things out."),
   ("Board and finish is the biggest single lever",
    "Standard white melamine-faced board is the most affordable route and is perfectly good for a wardrobe interior. Wood-grain and textured finishes cost more, and moisture-resistant board for a bathroom or scullery costs more again. Doors move the price most of all, because a plain slab door and a routed or high-gloss door are different products even when the carcass behind them is identical."),
   ("Size matters less than layout",
    "A long, uninterrupted run of cupboards is cheaper per metre than a short one, because the fixed costs of measuring, delivery and installation get spread further. What pushes the price up is complexity: corners that need scribing, angled ceilings, bulkheads, and internal fittings like shoe racks, drawer stacks and pull-out rails. A simple wardrobe with a rail and a shelf is a fraction of the cost of the same width fitted out fully."),
   ("Hardware is where cheap cupboards give themselves away",
    "Hinges and drawer runners are the parts you touch every day and the first parts to fail. Soft-close hinges and quality runners add to the quote and are the single best place not to economise, because replacing failed hardware later costs more than specifying it properly at the start. We fit soft-close as standard rather than listing it as an upgrade, which is worth checking when you compare quotes."),
   ("DIY flat-pack is the biggest saving available",
    "Buying pre-cut, pre-drilled units and assembling them yourself removes the labour from the quote entirely, and labour is a meaningful share of any installed price. Our flat-pack wardrobe with woody-look doors, three doors, two drawers, hanging rail and all hardware included, is R8&nbsp;999. If you are comfortable with a screwdriver and a spirit level, that is the cheapest honest way to fit out a bedroom."),
   ("How to compare two quotes properly",
    "Ask both suppliers the same four questions: what board and thickness, what door finish, what hinges and runners, and what is included in the internals. Then check whether delivery, installation and removal of the old units are in or out. A quote that looks 20% cheaper very often turns out to be quoting a thinner board, standard hinges or a bare interior. We give a clear written quote with the specification on it, free and with no obligation, so you have something concrete to compare against.")]),

 ("cupboard-materials-guide","Cupboard Materials Explained: What to Choose and Where",
  "Melamine, moisture-resistant board, solid wood, quartz, edging. A plain-language guide to cupboard materials and which one belongs in which room.",
  "Buying Guides", MELAMINE,
  [("Melamine-faced board does most of the work",
    "The overwhelming majority of built-in cupboards in South African homes are melamine-faced chipboard, and for good reason. The melamine surface is fused to the board under heat and pressure, which makes it hard-wearing, easy to wipe clean and completely colour-stable. It comes in dozens of plain colours and wood-grains, and a good wood-grain melamine is close enough to timber that most people cannot tell at arm’s length."),
   ("Moisture-resistant board for bathrooms and sculleries",
    "Standard chipboard and steam are a poor combination. In a bathroom, a scullery or under a sink, moisture-resistant board is worth the difference: it is manufactured to swell far less when it does get wet, which is what stops a vanity from bulging at the bottom edge after a year. Pair it with a non-porous top and properly sealed edges and a bathroom unit will outlast the tiles."),
   ("Solid wood and veneer",
    "Solid timber and wood veneer give a depth of grain that no printed finish quite matches, and they can be sanded and refinished years later. The trade-offs are cost, weight, and the fact that timber moves with humidity, so doors need seasonal adjustment. It is a considered choice for a feature piece rather than the default for a whole house."),
   ("Countertops: quartz, granite and melamine tops",
    "Quartz is engineered stone, natural quartz bound with resin, which makes it non-porous, consistent in colour and effectively maintenance-free. Granite is natural, so every slab is unique, but it is porous and needs sealing on installation and periodically after. Melamine tops are the budget option and perform well away from heavy heat and standing water. We supply Eazi Quartz alongside melamine tops, so you can match the top to the room rather than to a catalogue."),
   ("Edging is the detail that decides how long it lasts",
    "The board is only as durable as its edges. An exposed or thinly edged panel will absorb moisture and chip, and it is the first thing to go on a cheap cupboard. Properly applied edging on every visible edge, matched to the face, is not glamorous and it is exactly what separates cabinetry that still looks good in ten years from cabinetry that does not."),
   ("Matching the material to the room",
    "In practice: hard-wearing melamine for kitchens and bedrooms, moisture-resistant board wherever there is water, quartz where the surface takes daily abuse, and timber where you want a feature. If you are unsure, come into the Mbombela showroom and handle the samples. Seeing a wood-grain next to a gloss under real light settles the question far faster than any guide can.")]),
]

BLOG = BLOG + NEW_POSTS

BLOG_TITLE = {
 "how-to-install-kitchen-cupboards":       "How to Install Kitchen Cupboards",
 "cost-of-built-in-cupboards-south-africa":"Cost of Built-In Cupboards in South Africa",
 "cupboard-materials-guide":               "Cupboard Materials Explained",
 "choosing-the-perfect-kitchen-units":  "Kitchen Cupboard Design Ideas",
 "durable-quartz-countertops":          "Quartz vs Granite Countertops",
 "granite-countertops-for-your-home":   "Granite Countertops Guide",
 "expert-solutions-for-shop-fitting":   "Shop Fitting Ideas for Retail",
}
BLOG_IMG = {
 "how-to-install-kitchen-cupboards":("assets/images/photos/66f49878d1853e7db04197b9.jpg","Kitchen cupboard carcasses part-way through installation"),
 "cost-of-built-in-cupboards-south-africa":("assets/images/photos/6702dc253cd54697fb1f4ef6.jpg","Built-in cupboards with drawers and a timber top"),
 "cupboard-materials-guide":("assets/images/photos/6705945712e1ca6563958611.jpg","Quartz slab alongside white melamine cupboard units"),
 "choosing-the-perfect-kitchen-units":("assets/images/photos/6702dc273cd5463db01f4ef8.jpg","Fitted kitchen with white wall and base cupboard units and a gas hob"),
 "durable-quartz-countertops":("assets/images/photos/66f6cc2b52153310a558a6b1.jpg","Durable quartz countertop on a custom Cupboard Centre island"),
 "granite-countertops-for-your-home":("assets/images/photos/6702dc251b48d6576329d1e9.jpg","Natural stone countertop with high-gloss built-in cabinetry"),
 "expert-solutions-for-shop-fitting":("assets/images/photos/6702dc1ed6cf170e3edf4b2a.jpg","Custom retail reception counter and shopfitting"),
}
def blog_image(slug, imgs):
    return BLOG_IMG.get(slug, img(imgs,1))

def post_card(p):
    slug,title,excerpt,cat,imgs,body = p
    u,a = blog_image(slug, imgs)
    return ('<div class="post-card"><a href="blog/{slug}.html" style="display:block" aria-label="{t}">'
            '<div class="pc-img" style="background-image:url({u})"></div></a>'
            '<div class="pc-body"><span class="eyebrow" style="margin-bottom:6px">{cat}</span>'
            '<h3><a href="blog/{slug}.html">{t}</a></h3><p>{ex}</p>'
            '<a class="more" href="blog/{slug}.html">Read more<span class="sr-only">: {t}</span></a></div></div>'
            ).format(slug=slug,t=title,u=u,cat=cat,ex=excerpt)

# ============================================================ svc cards
def svc_card(title, href, icon, imgtuple):
    u,a = imgtuple
    return ('<a class="svc-card" href="{href}"><div class="svc-img"><img src="{u}" alt="{a}" width="214" height="214" loading="lazy" decoding="async"></div>'
            '<div class="svc-body"><span class="svc-badge">{icon}</span>'
            '<h2 class="svc-title h4">{t}</h2></div></a>').format(href=href,u=u,a=esc(a) if a else title,icon=icon,t=title)

HOME_SVCS = [
  ("Complete Installation","cupboard-installation.html",IC['install'],img(INSTALL,0,"Professional cupboard installation")),
  ("DIY Kitchen Units","kitchen-units.html",IC['kitchen'],img(KITCHEN,2,"DIY kitchen units")),
  ("Bedroom Cupboards","bedroom-cupboards.html",IC['bed'],img(BEDROOM,0,"Built-in bedroom cupboards")),
  ("Bathroom Cabinets","bathroom-cabinets.html",IC['bath'],img(BATHROOM,1,"Bathroom vanity cabinetry")),
  ("Melamine Doors","melamine-doors-quartz-countertops.html",IC['door'],("assets/images/photos/66f6cb03e1628294c2d7168d.jpg","Wood-grain melamine kitchen with quartz island")),
  ("Quartz Countertops","melamine-doors-quartz-countertops.html",IC['quartz'],img(KITCHEN,5,"Quartz countertops")),
  ("Custom Cabinetry &amp; Shopfitting","custom-cabinetry.html",IC['custom'],img(CUSTOM,0,"Custom cabinetry and shopfitting")),
  ("DIY Units &amp; Flat-Packs","diy-units.html",IC['diy'],img(DIY,0,"DIY flat-pack units")),
]

def work_carousel():
    picks = [
      ("assets/images/photos/6702dc2501848c80ac744433.jpg","Custom wood-grain kitchen with island and glass display cabinets"),
      ("assets/images/photos/6702dc1e01848c97a8744427.jpg","Modern grey kitchen with a large island and induction hob"),
      ("assets/images/photos/6702dc281e07d901a5811b87.jpg","Custom curved reception desk shopfitting"),
      ("assets/images/photos/6702dc1f01848c135a74442c.jpg","Fitted office reception counter and workstation"),
      ("assets/images/photos/6702dc2501848c074b744439.jpg","Bright fitted kitchen with breakfast bar and bar stools"),
      ("assets/images/photos/6702dc2001848c4c9674442e.jpg","Bathroom vanity with a stone top and vessel basin"),
    ]
    slides=""
    for i,(u,a) in enumerate(picks):
        slides += ('<button class="work-slide%s" type="button" data-i="%d"><img src="%s" alt="%s" width="400" height="300" loading="lazy" decoding="async"></button>'
                   % ((' is-active' if i==0 else ''), i, u, esc(a) if a else "Cupboard Centre project"))
    dots="".join('<button class="cdot%s" aria-label="Go to project %d"></button>'%((' active' if i==0 else ''),i+1) for i in range(len(picks)))
    return """<section id="gallery" class="section bg-navy-slate"><div class="wrap section-center">
  <span class="eyebrow">Our Work</span><h2>Spaces We Have Transformed</h2>
  <div class="work-carousel" data-work>
    <button class="carousel-arrow prev" data-work-prev aria-label="Previous project">‹</button>
    <div class="work-viewport"><div class="work-track" data-work-track>{slides}</div></div>
    <button class="carousel-arrow next" data-work-next aria-label="Next project">›</button>
  </div>
  <div class="carousel-dots" data-work-dots>{dots}</div>
  <p style="margin-top:24px"><a class="btn btn-green btn-arrow" href="gallery.html">See More Images</a></p>
</div></section>
""".format(slides=slides,dots=dots)

# home FAQ + why-accordion content
WHY_ITEMS = [
 ("25+ Years of Cupboard Expertise","Over two-and-a-half decades supplying and installing cupboards across Mpumalanga, 1028+ projects and counting."),
 ("Custom &amp; DIY Under One Roof","From flat-pack DIY kits you assemble yourself to fully custom, installed cabinetry, whatever suits your budget and skill."),
 ("Quality Materials, Quality Hardware","Hard-wearing melamine, Eazi Quartz tops and soft-close hinges and runners as standard, not as an upsell."),
 ("Free, No-Obligation Quotes","We give you a clear, written, no-obligation quote up front, so you know exactly what to expect before any work begins."),
 ("Expert Installation Team","Prefer it done for you? Our installers fit kitchens, wardrobes and vanities cleanly and on schedule."),
]
FAQ_ITEMS = [
 ("Do you supply DIY cupboards as well as installed units?","Yes. You can order pre-cut, pre-drilled DIY flat-pack units to assemble yourself, or let our team supply and install a complete custom solution, kitchens, bedrooms and bathrooms."),
 ("Which areas do you cover?","Our showroom is in Mbombela (Nelspruit) and we install across the Lowveld, Nelspruit, White River, Hazyview and surrounds. Our DIY flat-pack units are delivered nationwide."),
 ("Can you make cupboards to my exact measurements?","Absolutely. Custom cabinetry is our speciality. We measure your space and build units to fit precisely, with the finishes, colours and hardware you choose."),
 ("Do you offer quartz and melamine countertops?","Yes, we supply and fit Eazi Quartz countertops and a wide range of melamine tops and doors to match your cabinetry."),
 ("How do I get a quote?","Send us your measurements or your plans, or pop into the showroom. Call 084 683 7467, WhatsApp 079 305 7321, or fill in the quote form and we’ll come back to you with a clear, written quote."),
]

def accordion(items, cls="faq-list"):
    inner="".join('<div class="faq-item"><h2 class="faq-q h4">%s</h2><div class="faq-a"><p>%s</p></div></div>'%(q,a) for q,a in items)
    return '<div class="%s">%s</div>'%(cls,inner)

AREA_CHIPS = [("Nelspruit","service-areas.html"),("Mbombela","service-areas.html"),("White River","service-areas.html"),
              ("Hazyview","service-areas.html"),("Barberton","service-areas.html"),("Sabie","service-areas.html"),
              ("Malelane","service-areas.html")]
def link_chips(chips, pin=True):
    inner=""
    for t,h in chips:
        p = '<span class="chip-pin">%s</span>'%SVG_PIN if pin else ''
        inner+='<a href="%s">%s%s</a>'%(h,p,t)
    return '<div class="link-chips">%s</div>'%inner

print("blog + home helpers loaded")

# ============================================================ HOME PAGE
def build_home():
    hero_u,_ = img(GENERAL,0)
    about_u = "assets/images/photos/67028368d6cf1745c3def33d.jpg"  # the Cupboard Centre team
    commit_u = "assets/images/photos/6701c754fbe4fd1483bcbd50.jpg"  # Cupboard Centre premises + team
    h  = head("DIY &amp; Custom Cupboards Nelspruit | Cupboard Centre",
              "DIY cupboards and custom cabinetry from Cupboard Centre, Nelspruit. Kitchens, wardrobes, bathroom cabinets and quartz tops, supplied and installed. Free quote.",
              "https://www.cupboardcentre.co.za/", hero_u, local_business=True)
    h += header("home")
    # 1. HERO
    h += """<section id="hero" class="hero"><div class="hero-panel">
  <div class="hero-content">
    <span class="hero-eyebrow">{shield}Nelspruit &amp; Mbombela · 25+ Years of Cupboards</span>
    <h1>Nelspruit's Best Choice For <span class="sub">DIY &amp; Custom Cupboard Solutions</span></h1>
    <p>A one-stop shop for cupboards, from custom kitchens, bedroom &amp; bathroom cabinetry and quartz countertops to pre-cut DIY flat-packs delivered to your door. Supply, delivery and expert installation.</p>
    <div class="review-badges"><a class="review-badge" href="{fb}" target="_blank" rel="noopener noreferrer"><span class="rb-logo">{grev}</span><span class="rb-text"><span class="rb-score">5.0 <span class="rb-stars">★★★★★</span></span><span class="rb-label">Google Reviews</span></span></a><a class="review-badge" href="{fb}" target="_blank" rel="noopener noreferrer"><span class="rb-logo">{frev}</span><span class="rb-text"><span class="rb-score">5.0 <span class="rb-stars">★★★★★</span></span><span class="rb-label">Facebook Reviews</span></span></a></div>
    <div class="hero-sub-claims"><span>Custom &amp; DIY</span><span>Free Quote</span><span>Nationwide Delivery</span></div>
  </div>
  <div class="hero-form-col">{form}</div>
</div></section>
""".format(shield=SVG_SHIELD, fb=FB, grev=GREV, frev=FREV, form=lead_form())
    # 1b. TRUSTED PARTNERS
    h += partners_band()
    # 2. REVIEWS
    h += reviews_section("bg-navy-slate")
    # 3. ABOUT
    h += """<section id="about" class="section bg-navy"><div class="wrap">
  <div class="section-center about-banner"><h2 class="about-banner-title">We Are <span class="g2">Cupboard Centre</span></h2></div>
  <div class="about-card">
    <div class="about-img" style="background-image:url({about_u});background-size:cover;background-position:center 42%"></div>
    <div class="about-panel">
      <span class="about-eyebrow">A Local Team. A Lasting Standard.</span>
      <h3 class="about-heading">Cupboards Done <span class="g2">Properly</span></h3>
      <p>For over 25 years, Cupboard Centre has been Nelspruit’s go-to for cupboard solutions. Come to us with an idea and we’ll bring a complete solution, we specialise in DIY cupboard kits you can design, build and install yourself, as well as fully custom, professionally fitted cabinetry. With efficient turnaround times, you get exactly what you need without the wait.</p>
      <a class="btn btn-ghost" href="about.html">Learn More About Us</a>
    </div>
  </div>
</div></section>
""".format(about_u=about_u)
    # 4. SERVICES
    cards="".join(svc_card(t,h2,ic,im) for t,h2,ic,im in HOME_SVCS)
    h += """<section id="services" class="section bg-navy-slate"><div class="wrap section-center">
  <span class="eyebrow">What We Do</span><h2>Everything For Your Cupboards, One Team</h2>
  <p style="max-width:50em;margin:0 auto 34px">From a full custom kitchen to a single DIY flat-pack wardrobe, kitchens, bedrooms, bathrooms, doors and countertops, tailored to your space and budget.</p>
  <div class="svc-grid">{cards}</div>
  <p class="btn-row" style="margin-top:30px;justify-content:center"><a class="btn btn-green btn-arrow" href="services.html">Explore All Services</a> <a class="btn btn-outline" href="shop.html">Shop DIY Online</a></p>
</div></section>
""".format(cards=cards)
    # 5. WHY (commit-panel)
    h += """<section id="why" class="section bg-navy"><div class="wrap">
  <div class="commit-panel">
    <div class="commit-left">
      <span class="eyebrow">Why Clients Pick Us</span>
      <h2>The Cupboard Centre <span class="g2">Difference</span></h2>
      <div class="commit-acc">{acc}</div>
    </div>
    <div class="commit-right"><!--commit-right-->
      <div class="commit-img" style="background-image:url({commit_u})"></div>
      </div>
  </div>
</div></section>
""".format(acc="".join('<div class="faq-item"><h2 class="faq-q h4">%s</h2><div class="faq-a"><p>%s</p></div></div>'%(q,a) for q,a in WHY_ITEMS), commit_u=commit_u)
    # fix: commit accordion uses faq-item markup
    # 6. WORK carousel
    h += work_carousel()
    # 7. PROCESS
    steps=[("Get in Touch","Call, WhatsApp or send your measurements for a clear, tailored cupboard solution suited to your space and budget."),
           ("Plan &amp; Quote","We confirm your sizes and finishes and prepare a written plan and quote, with no obligation."),
           ("Build &amp; Deliver","We manufacture your units to spec and deliver, pre-cut and labelled for DIY, or ready for our installers."),
           ("Install &amp; Enjoy","Our team fits everything cleanly and on schedule, or supports your DIY build every step of the way.")]
    ps="".join('<div class="proc-step"><div class="proc-num">%d</div><h2 class="h4">%s</h2><p>%s</p></div>'%(i+1,t,d) for i,(t,d) in enumerate(steps))
    h += """<section id="process" class="section bg-navy"><div class="wrap section-center">
  <span class="eyebrow">How It Works</span><h2>Our Simple Process</h2>
  <div class="proc-grid">{ps}</div>
</div></section>
""".format(ps=ps)
    # 8. OFFERS
    h += """<section id="offers" class="section bg-navy-slate"><div class="wrap">
  <div class="offer-cta">
    <span class="eyebrow offer-eyebrow">Our Offer</span>
    <h2>Get a Free, No-Obligation Quote</h2>
    <p class="offer-line"><span class="offer-ico">{ph}</span>Call <a href="tel:{tel}">{phone}</a> or WhatsApp us, we’ll help you plan your cupboards and send a clear written quote, free and on your schedule.</p>
    <a class="btn btn-navy btn-arrow" href="#cta-form" data-scroll="cta-form">Get My Free Quote</a>
  </div>
</div></section>
""".format(ph=SVG_PHONE, tel=TEL, phone=PHONE)
    # 9. BLOG
    pc="".join(post_card(p) for p in BLOG[:3])
    h += """<section id="blog" class="section bg-navy"><div class="wrap section-center">
  <span class="eyebrow">From the Blog</span><h2>Cupboard &amp; Kitchen Tips</h2>
  <div class="blog-grid" style="margin-top:34px">{pc}</div>
  <p style="margin-top:30px"><a class="btn btn-green btn-arrow" href="blog.html">See All Articles</a></p>
</div></section>
""".format(pc=pc)
    # 10. FAQ
    h += """<section id="faq" class="section bg-navy"><div class="wrap">
  <div class="section-center"><span class="eyebrow">Questions?</span><h2>Frequently Asked Questions</h2></div>
  <div style="margin-top:34px">{faq}</div>
</div></section>
""".format(faq=accordion(FAQ_ITEMS))
    # 11. SERVICE AREA
    h += """<section id="service-area" class="section bg-navy"><div class="wrap">
  <div class="area-split">
    <div class="area-text">
      <span class="eyebrow">Where We Work</span><h2>Serving Nelspruit, Mbombela &amp; the Lowveld</h2>
      <p>Our showroom is in Mbombela (Nelspruit) and we supply and install cupboards across the Lowveld. Prefer DIY? Our pre-cut, labelled flat-pack units are delivered nationwide.</p>
      {chips}
      <p style="margin-top:22px"><a class="btn btn-green btn-arrow" href="service-areas.html">All Service Areas</a></p>
    </div>
    <div class="area-map">
      <iframe src="{gmap}" loading="lazy" title="Cupboard Centre showroom in Mbombela" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </div>
</div></section>
""".format(chips=link_chips(AREA_CHIPS), gmap=GMAP)
    # 12. CTA + 13. marquee + footer
    h += cta_form()
    h += marquee()
    h += footer()
    return h

n = write("index.html", build_home())
print("index.html:", n, "bytes")

# ============================================================ SERVICE PAGES
def area_split_txt(eyebrow,h2,paras,img_tuple,included=None,reverse=False,bg="bg-navy"):
    u,a=img_tuple
    inc=""
    if included:
        inc='<ul class="included-grid" style="margin-top:18px">%s</ul>'%("".join('<li>%s</li>'%x for x in included))
    ptxt="".join('<p>%s</p>'%p for p in paras)
    rc=' reverse' if reverse else ''
    return """<section class="section {bg}"><div class="wrap"><div class="area-split{rc}">
    <div class="area-text"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{ptxt}{inc}
      <p style="margin-top:22px"><a class="btn btn-green btn-arrow" href="#cta-form" data-scroll="cta-form">Get My Free Quote</a></p></div>
    <div class="area-map" style="min-height:420px"><img src="{u}" alt="{a}" style="width:100%;height:100%;min-height:420px;object-fit:cover;border-radius:var(--r-card);box-shadow:var(--shadow-panel)" loading="lazy"></div>
  </div></div></section>
""".format(bg=bg,rc=rc,eyebrow=eyebrow,h2=h2,ptxt=ptxt,inc=inc,u=u,a=esc(a) if a else h2)

def pill_section(eyebrow,h2,sub,tags,bg="bg-navy-slate"):
    t="".join("<span>%s</span>"%x for x in tags)
    subh='<p style="max-width:46em;margin:6px auto 0;color:var(--muted)">%s</p>'%sub if sub else ''
    return """<section class="section {bg}"><div class="wrap"><div class="section-center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{subh}</div>
  <div class="pill-tags">{t}</div></div></section>
""".format(bg=bg,eyebrow=eyebrow,h2=h2,subh=subh,t=t)

def feature_section(eyebrow,h2,feats,bg="bg-navy"):
    cards=""
    for ic,ft,fp in feats:
        cards+='<div class="feature-card"><span class="fc-ico">%s</span><h2 class="h4">%s</h2><p>%s</p></div>'%(IC.get(ic,IC['check']),ft,fp)
    return """<section class="section {bg}"><div class="wrap section-center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>
  <div class="feature-grid">{cards}</div></div></section>
""".format(bg=bg,eyebrow=eyebrow,h2=h2,cards=cards)

def process_section(eyebrow="How It Works",h2="Our Simple Process",bg="bg-navy-slate"):
    steps=[("Get in Touch","Call, WhatsApp or send your measurements for a tailored solution and a clear, written quote."),
           ("Plan &amp; Quote","We confirm your sizes and finishes and prepare a written plan and quote, with no obligation."),
           ("Build &amp; Deliver","We manufacture to spec and deliver, pre-cut and labelled for DIY, or ready for our installers."),
           ("Install &amp; Enjoy","Our team fits everything cleanly and on schedule, or supports your DIY build all the way.")]
    ps="".join('<div class="proc-step"><div class="proc-num">%d</div><h2 class="h4">%s</h2><p>%s</p></div>'%(i+1,t,d) for i,(t,d) in enumerate(steps))
    return '<section class="section %s"><div class="wrap section-center"><span class="eyebrow">%s</span><h2>%s</h2><div class="proc-grid" style="margin-top:30px">%s</div></div></section>\n'%(bg,eyebrow,h2,ps)

RELATED = [("Complete Installation","cupboard-installation.html"),("DIY Kitchen Units","kitchen-units.html"),
           ("Bedroom Cupboards","bedroom-cupboards.html"),
           ("Bathroom Cabinets","bathroom-cabinets.html"),
           ("Office &amp; Reception Desks","office-reception-desks.html"),
           ("Melamine Doors &amp; Quartz Countertops","melamine-doors-quartz-countertops.html"),
           ("Custom Cabinetry &amp; Shopfitting","custom-cabinetry.html"),("All Services","services.html")]
def related_section(current):
    chips=[(t,h) for t,h in RELATED if h!=current]
    inner="".join('<a href="%s">%s</a>'%(h,t) for t,h in chips)
    return """<section class="section bg-navy"><div class="wrap section-center"><span class="eyebrow">Explore</span><h2>Related Services</h2>
  <div class="link-chips" style="margin-top:24px">%s</div></div></section>
"""%inner
def areas_section():
    return """<section class="section bg-navy-slate"><div class="wrap section-center"><span class="eyebrow">Where We Work</span><h2>Serving Nelspruit, Mbombela &amp; the Lowveld</h2>
  <p style="max-width:42em;margin:6px auto 0;color:var(--muted)">From our Mbombela showroom we supply and install across the Lowveld, with DIY flat-packs delivered nationwide.</p>
  %s</div></section>
"""%link_chips(AREA_CHIPS)

# ============================================================ editorial-flow helpers
def accent(h):
    """Wrap the trailing part of a heading in a red accent span."""
    if ',' in h:
        a,b = h.rsplit(',',1); return '%s, <span class="g2">%s</span>'%(a.strip(), b.strip())
    w = h.split()
    if len(w) > 2: return ' '.join(w[:-2]) + ' <span class="g2">' + ' '.join(w[-2:]) + '</span>'
    return '<span class="g2">%s</span>'%h

def esplit(eyebrow, h2_html, paras, img_tuple, bullets=None, reverse=False, bg="bg-navy", cta=None, subhead=None):
    u,a = img_tuple
    body = ''
    if subhead: body += '<p style="font-weight:700;color:var(--heading);font-family:\'Poppins\',sans-serif;margin-bottom:.4em">%s</p>'%subhead
    for i,p in enumerate(paras):
        body += '<p%s>%s</p>'%(' class="area-lead"' if i==0 and not subhead else '', p)
    if bullets:
        body += '<ul class="included-grid">%s</ul>'%''.join('<li>%s</li>'%b for b in bullets)
    if cta:
        label,href = cta
        ds = ' data-scroll="cta-form"' if href == '#cta-form' else ''
        body += '<p style="margin-top:22px"><a class="btn btn-green btn-arrow" href="%s"%s>%s</a></p>'%(href, ds, label)
    eyeb = '<span class="eyebrow">%s</span>'%eyebrow if eyebrow else ''
    return """<section class="section {bg}"><div class="wrap"><div class="area-split{rc}">
    <div class="area-text">{eyeb}<h2>{h2}</h2>{body}</div>
    <div class="area-fig"><img src="{u}" alt="{a}" loading="lazy" decoding="async"></div>
  </div></div></section>
""".format(bg=bg, rc=(' reverse' if reverse else ''), eyeb=eyeb, h2=h2_html, body=body, u=u, a=esc(a) if a else "Cupboard Centre cabinetry")

def bigstats(items, bg="bg-navy-slate"):
    cells = ''
    for n,l in items:
        base = n.rstrip('+%'); suf = n[len(base):]
        cells += '<div class="stat"><span class="n">%s<sup>%s</sup></span><span class="l">%s</span></div>'%(base, suf, l)
    return '<section class="section %s"><div class="wrap"><div class="bigstats">%s</div></div></section>\n'%(bg, cells)

def statement(html, bg="bg-navy-slate"):
    return '<section class="section %s"><div class="wrap"><div class="statement"><h2>%s</h2></div></div></section>\n'%(bg, html)

def faq_section(eyebrow, h2, items, bg="bg-navy-slate"):
    return '<section class="section %s"><div class="wrap"><div class="section-center"><span class="eyebrow">%s</span><h2>%s</h2></div><div style="margin-top:34px">%s</div></div></section>\n'%(bg, eyebrow, h2, accordion(items))

SVC_CARDS = [
 ("Complete Installation","Full supply and fitting of kitchens, wardrobes and cabinetry across the Lowveld.","cupboard-installation.html", img(INSTALL,2)),
 ("DIY Kitchen Units","Pre-cut, ready-to-assemble kitchen units, delivered to your door.","kitchen-units.html", img(KITCHEN,3)),
 ("Bedroom Cupboards","Built-in wardrobes and walk-in closets, made to measure.","bedroom-cupboards.html", img(BEDROOM,4)),
 ("Bathroom Cabinets","Vanities and bathroom storage in moisture-resistant board.","bathroom-cabinets.html", img(BATHROOM,1)),
 ("Office &amp; Reception Desks","Custom office desks, reception counters and office storage.","office-reception-desks.html", img(CUSTOM,4)),
 ("Melamine Doors &amp; Quartz Countertops","Hard-wearing doors and premium Eazi Quartz tops.","melamine-doors-quartz-countertops.html", img(MELAMINE,0)),
 ("Custom Cabinetry &amp; Shopfitting","Bespoke cabinetry for homes, offices and shops.","custom-cabinetry.html", img(CUSTOM,1)),
 ("DIY Units &amp; Flat-Packs","Flat-pack units for every room, delivered nationwide.","diy-units.html", img(DIY,0)),
]
def services_carousel(current, eyebrow="Explore", h2=None, intro=None, bg="bg-navy"):
    h2 = h2 or accent("More of What We Do")
    cards = [c for c in SVC_CARDS if c[2] != current]
    cc = ''
    for t,d,href,imt in cards:
        u,a = imt
        cc += ('<a class="hscroll-card" href="%s"><div class="hs-img"><img src="%s" alt="%s" loading="lazy" decoding="async"></div>'
               '<div class="hs-body"><h3>%s</h3><p>%s</p><span class="hs-more">Learn more &rarr;</span></div></a>'
               )%(href, u, esc(a) if a else t, t, d)
    introp = '<p style="max-width:46em;margin:6px auto 0;color:var(--muted)">%s</p>'%intro if intro else ''
    return """<section class="section {bg}"><div class="wrap">
  <div class="section-center"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2>{introp}</div>
  <div class="hscroll-wrap">
    <div class="hscroll">{cc}</div>
    <div class="hscroll-nav"><button data-hs-prev aria-label="Scroll left">&lsaquo;</button><button data-hs-next aria-label="Scroll right">&rsaquo;</button></div>
  </div>
</div></section>
""".format(bg=bg, eyebrow=eyebrow, h2=h2, introp=introp, cc=cc)

def service_faq(short):
    return [
     ("Do you supply %s on their own, or fully installed?"%short.lower(),
      "Both. You can order supply-only, including DIY flat-packs to assemble yourself, or let our team measure, build and install everything for you."),
     ("Can you make it to my exact sizes?",
      "Yes, custom sizes are our speciality. Send us your measurements or visit the showroom and we will build to fit your space precisely."),
     ("Do you deliver outside Nelspruit?",
      "Our installation teams cover Nelspruit, Mbombela and the wider Lowveld, and our pre-cut DIY units are delivered nationwide, flat-packed and protected."),
     ("How do I get a price?",
      "Call 084 683 7467, WhatsApp 079 305 7321, or use the quote form below and we will come back to you with a clear, written quote."),
    ]

TOWNS_LINE = ("We supply, deliver and install across Nelspruit, Mbombela, White River, "
              "Hazyview, Barberton, Sabie and Malelane.")

SERVICE_PAGES = {
 "cupboard-installation.html": dict(
   title="Kitchen Cupboard Installation | Cupboard Centre",
   desc="Professional kitchen cupboard installation, built-in wardrobes and bathroom vanities, measured, manufactured and fitted by our own team. Get a free quote today.",
   eyebrow="Our Services", h1="Kitchen Cupboard Installation",
   subtitle="Professional supply and installation of kitchens, wardrobes and cabinetry across Mpumalanga.",
   intro_h="Installation Done Right, First Time",
   intro=["Come to us with an idea and leave with a complete solution. Our installation team handles everything, measuring, manufacturing and fitting, so your new cupboards go in cleanly, level and built to last.",
          "Whether it’s a full custom kitchen, built-in bedroom wardrobes or a bathroom vanity, we manage the whole project with efficient turnaround times and a tidy site at the end of every job.",
          TOWNS_LINE],
   included=["Accurate measuring &amp; planning","Kitchen &amp; scullery installation","Built-in bedroom wardrobes","Bathroom vanities &amp; storage","Countertop supply &amp; fitting","Soft-close hinges &amp; runners"],
   img_cat=INSTALL, img_i=2,
   offer_eyebrow="What We Install", offer_h="Every Room, One Team",
   offer_sub="From a single wardrobe to a whole home or office, professionally fitted.",
   offer_tags=["Kitchens","Sculleries","Bedroom Wardrobes","Bathroom Vanities","TV &amp; Wall Units","Office Cupboards","Shop Fittings","Laundry Units"],
   feats=[("ruler","Precision Measured","We measure every wall, corner and service point so your units fit the space exactly."),
          ("hinge","Quality Hardware","Soft-close hinges and runners, quality edging and hard-wearing melamine as standard."),
          ("calendar","Clean, On-Schedule Fitting","Experienced installers who work neatly, protect your home and finish on time.")]),

 "kitchen-units.html": dict(
   title="Kitchen Cupboards &amp; DIY Kitchen Units | Cupboard Centre",
   desc="Kitchen cupboards built to your space, plus pre-cut DIY kitchen units you assemble yourself. Factory-direct prices, delivered nationwide. Get a free quote.",
   eyebrow="Our Services", h1="Kitchen Cupboards &amp; DIY Kitchen Units",
   subtitle="Kitchen cupboards made to measure, or pre-cut, pre-drilled kitchen units you can assemble yourself.",
   intro_h="Kitchen Units to Suit Your Budget",
   intro=["Our DIY kitchen units arrive pre-cut, edged and drilled, labelled and ready to assemble over a weekend, a serious saving without cutting corners on quality.",
          "Prefer a turnkey kitchen? We’ll design, manufacture and install the whole thing, complete with melamine or quartz tops, soft-close everything and the storage you actually need.",
          TOWNS_LINE],
   included=["Base &amp; wall units in standard sizes","Custom sizes on request","Melamine &amp; quartz countertops","Soft-close hinges &amp; drawer runners","Built-in oven &amp; hob provision","Delivered nationwide"],
   img_cat=KITCHEN, img_i=3,
   offer_eyebrow="What You Can Order", offer_h="Build the Kitchen You Want",
   offer_sub="Mix and match units, finishes and tops to design a kitchen around how you cook.",
   offer_tags=["Base Units","Wall Units","Tall / Pantry Units","Corner Units","Drawer Stacks","Oven Housings","Sink Units","Islands"],
   feats=[("diy","Easy DIY Assembly","Pre-cut, labelled and drilled, with a bit of DIY know-how you’ll have it together in a weekend."),
          ("wallet","Factory-Direct Value","Buying direct from the manufacturer means showroom quality at DIY prices."),
          ("truck","Delivered to Your Door","Flat-packed and protected for delivery anywhere in South Africa.")]),

 "bedroom-cupboards.html": dict(
   title="Bedroom Cupboards &amp; Built-In Wardrobes | Cupboard Centre",
   desc="Bedroom cupboards and built-in wardrobes made to measure, with hanging space, drawers and shoe storage designed around your room. Get a free quote today.",
   eyebrow="Our Services", h1="Bedroom Cupboards &amp; Built-In Wardrobes",
   subtitle="Built-in wardrobes, walk-in closets and bedroom cupboards, custom-made to fit your space and style.",
   intro_h="Storage That Fits Your Life",
   intro=["From floor-to-ceiling built-in wardrobes with hanging space, shelving, drawers and shoe racks, to sliding-door robes and walk-in closets, we design bedroom cupboards around the way you live.",
          "Choose your finishes, handles and internal layout, mirrors, LED lighting, soft-close drawers, and we’ll build and install it to a flawless fit.",
          TOWNS_LINE],
   included=["Built-in &amp; walk-in wardrobes","Chest of drawers &amp; shelving","Mirror &amp; sliding doors","Shoe storage &amp; accessories","Bedside cabinets","DIY wardrobe kits"],
   img_cat=BEDROOM, img_i=4,
   offer_eyebrow="What We Build", offer_h="Bedrooms, Beautifully Organised",
   offer_sub="Every wardrobe is made to measure for a seamless, wall-to-wall fit.",
   offer_tags=["Built-in Wardrobes","Walk-in Closets","Sliding-Door Robes","Chest Drawers","Bedside Cabinets","Shoe Storage","Shelving","Linen Cupboards"],
   feats=[("ruler","Made to Measure","Every unit is built to your exact dimensions, no wasted space, no awkward gaps."),
          ("layout","Your Style, Your Layout","Finishes, handles, lighting and internal fittings chosen by you."),
          ("hinge","Quality Hardware","Soft-close drawers and runners as standard, not as an upsell.")]),

 "bathroom-cabinets.html": dict(
   title="Bathroom Cabinets &amp; Vanities | Cupboard Centre",
   desc="Bathroom cabinets and vanities built to measure, in moisture-resistant board with quartz tops. Floating units, mirror cabinets and storage. Get a free quote.",
   eyebrow="Our Services", h1="Bathroom Cabinets &amp; Vanities",
   subtitle="Bathroom cabinets, vanities and storage, made to measure in moisture-resistant board with quartz tops.",
   intro_h="Bathroom Storage Built to Last",
   intro=["A bathroom is a hard place for cabinetry. We build vanities and bathroom cabinets in moisture-resistant board, topped with non-porous quartz, so they handle steam, splashes and daily use without swelling or staining.",
          "Floating vanities, double basins, mirror cabinets and tall storage columns, all sized to your bathroom and finished in the colours and handles you choose.",
          TOWNS_LINE],
   included=["Vanity units &amp; double basins","Floating &amp; floor-standing options","Quartz &amp; melamine tops","Mirror cabinets","Tall storage columns","Waterproof board options"],
   img_cat=BATHROOM, img_i=1,
   offer_eyebrow="What We Build", offer_h="Vanities &amp; Bathroom Storage",
   offer_sub="Made to measure for a seamless fit around plumbing and tiling.",
   offer_tags=["Vanity Units","Double Basins","Floating Vanities","Mirror Cabinets","Storage Columns","Under-Basin Units","Quartz Tops","Waterproof Board"],
   feats=[("drop","Water-Smart Bathrooms","Moisture-resistant boards and quartz tops built to handle a busy bathroom."),
          ("ruler","Fits Around Plumbing","We measure to your existing pipework and tiling so the unit sits flush and level."),
          ("gem","Premium Surfaces","Non-porous quartz tops that resist stains, scratches and daily wear.")]),

 "melamine-doors-quartz-countertops.html": dict(
   title="Quartz Countertops &amp; Melamine Doors | Cupboard Centre",
   desc="Eazi Quartz countertops and hard-wearing melamine cupboard doors, cut to size and fitted. The fastest way to transform a kitchen. Get a free quote today.",
   eyebrow="Our Services", h1="Quartz Countertops &amp; Melamine Doors",
   subtitle="Premium Eazi Quartz countertops and affordable, hard-wearing melamine doors to finish your cupboards perfectly.",
   intro_h="The Finishing Touch That Lasts",
   intro=["Doors and tops make or break a cupboard. Our Eazi Quartz countertops add a premium, non-porous, stain-resistant surface, while our melamine doors come in dozens of colours and wood-grains, tough, easy to clean and great value.",
          "Replacing tired doors or kitchen countertops is one of the fastest, most affordable ways to transform a kitchen. We supply on their own or as part of a full installation.",
          TOWNS_LINE],
   included=["Eazi Quartz countertops","Melamine countertops","Melamine doors, many colours","Wood-grain &amp; solid finishes","Cut-to-size service","Soft-close hinges included"],
   img_cat=MELAMINE, img_i=0,
   offer_eyebrow="What We Supply", offer_h="Doors &amp; Tops for Every Style",
   offer_sub="Refresh an existing kitchen or finish a new one with surfaces that last.",
   offer_tags=["Eazi Quartz Tops","Melamine Tops","Kitchen Cupboard Doors","Wood-grain Finishes","Solid Colours","Splashbacks","Cut-to-Size","Soft-Close Hinges"],
   feats=[("gem","Premium Quartz","Non-porous, scratch- and stain-resistant, and virtually maintenance-free."),
          ("door","Tough &amp; Affordable","Melamine resists knocks, moisture and daily wear, and it’s kind to your budget."),
          ("ruler","Cut to Your Sizes","Doors and tops cut precisely to your measurements for a clean, professional fit.")]),

 "custom-cabinetry.html": dict(
   title="Shopfitting &amp; Custom Cabinetry | Cupboard Centre",
   desc="Shopfitting and custom cabinetry for retail and business, shop counters, display units and made-to-measure storage, designed and installed. Get a free quote.",
   eyebrow="Our Services", h1="Shopfitting &amp; Custom Cabinetry",
   subtitle="Shop counters, display units and bespoke cabinetry for retail, hospitality and business premises.",
   intro_h="Built for Your Space and Your Brand",
   intro=["Your counters, shelving and display units are silent salespeople. We design and build retail shopfitting that guides customers, showcases stock and makes the most of every square metre, finished in hard-wearing materials that survive heavy trading.",
          "Tell us the look, the function and the budget, and we’ll handle design, manufacture and installation, from a single service counter to a complete retail fit-out.",
          TOWNS_LINE],
   included=["Shop counters &amp; displays","Retail fit-outs","Service &amp; till counters","Display shelving","Stockroom storage","Custom cabinetry to order"],
   img_cat=CUSTOM, img_i=1,
   offer_eyebrow="What We Build", offer_h="Custom Solutions for Home &amp; Business",
   offer_sub="No two projects are the same, everything is designed and built to order.",
   offer_tags=["Shop Counters","Display Units","Retail Fit-outs","Till Counters","Stockroom Storage","Entertainment Units","Home Offices","Custom Cabinetry"],
   feats=[("custom","Designed With You","We turn your idea, sketch or Pinterest board into a buildable, made-to-measure design."),
          ("check","Expert Craftsmanship","Skilled cabinetmakers and quality materials for a finish that impresses."),
          ("wallet","Priced to Your Brief","Custom doesn’t have to mean expensive, we build to your budget and priorities.")]),

 "office-reception-desks.html": dict(
   title="Office Desks &amp; Reception Desks | Cupboard Centre",
   desc="Custom office desks, reception desks and office cupboards built to measure for your workspace, designed, manufactured and installed. Get a free quote today.",
   eyebrow="Our Services", h1="Office Desks &amp; Reception Desks",
   subtitle="Custom office desks, reception counters and office cupboards, built to measure for the way your team works.",
   intro_h="Workspaces Built to Measure",
   intro=["A desk bought off a shelf rarely fits the room. We design and build office desks, reception desks and workstations to your exact floor plan, with cable management, storage and finishes chosen to match your brand.",
          "From a single home-office desk to a full commercial reception counter and matching office cupboards, we handle design, manufacture and installation.",
          TOWNS_LINE],
   included=["Custom office desks","Reception &amp; service counters","Workstations &amp; pods","Office cupboards &amp; storage","Filing &amp; credenza units","Cable management built in"],
   img_cat=CUSTOM, img_i=4,
   offer_eyebrow="What We Build", offer_h="Desks, Counters &amp; Office Storage",
   offer_sub="Designed around your floor plan, your team and your brand.",
   offer_tags=["Office Desks","Reception Desks","Workstations","Office Cupboards","Filing Units","Credenzas","Boardroom Tables","Home Offices"],
   feats=[("layout","Planned To Your Floor","We work to your floor plan so desks, storage and walkways actually fit."),
          ("custom","Finished In Your Brand","Colours, edging and detailing chosen to match your corporate identity."),
          ("hinge","Built For Daily Use","Commercial-grade board, edging and hardware that stands up to office wear.")]),

 "diy-units.html": dict(
   title="Flat Pack Cupboards &amp; DIY Units | Cupboard Centre",
   desc="Flat pack cupboards and DIY units, pre-cut, edged, drilled and labelled with all hardware included. Delivered nationwide. Order online or get a free quote.",
   eyebrow="Our Services", h1="Flat Pack Cupboards &amp; DIY Units",
   subtitle="Ready-to-assemble flat pack cupboards delivered to your door, the smart, affordable way to kit out any room.",
   intro_h="DIY Cupboards, Done Properly",
   intro=["Our flat pack cupboards are the same quality we install, pre-cut, edged, drilled and labelled, with all the hardware included. Follow the guide and you’ll have solid, professional-looking cupboards in place over a weekend.",
          "Kitchens, bedrooms, bathrooms and floor units in a range of standard sizes, with custom sizes on request. Everything is flat-packed and protected for safe delivery nationwide.",
          TOWNS_LINE],
   included=["Floor units in standard widths","Base &amp; wall kitchen units","Wardrobe &amp; storage kits","All hardware &amp; fittings included","Assembly guide provided","Custom sizes on request"],
   img_cat=DIY, img_i=0,
   offer_eyebrow="What You Can Order", offer_h="Flat-Packs for Every Room",
   offer_sub="Pick your units and sizes, we cut, pack and deliver.",
   offer_tags=["Floor Units","Kitchen Units","Wardrobe Kits","Drawer Units","Bathroom Units","Shelving","Corner Units","Custom Sizes"],
   feats=[("diy","Assemble It Yourself","Clear labelling and included hardware make assembly straightforward and satisfying."),
          ("wallet","Biggest Savings","DIY is the most affordable way to fit out a room without compromising on quality."),
          ("truck","Nationwide Delivery","Flat-packed, protected and delivered wherever you are in South Africa.")]),
}

def build_service(fname, d):
    cat=d['img_cat']; i=d['img_i']
    og,_=img(cat,i)
    # keep &amp; encoded - a raw & in <title>/<meta> is invalid HTML
    title = d.get('title') or ("%s | Cupboard Centre" % d['h1'])
    desc  = d.get('desc')  or d['subtitle']
    slug = "/" + fname[:-5]
    faqs = service_faq(d['h1'].replace('&amp;','&'))
    h = head(title, desc, "https://www.cupboardcentre.co.za/%s"%fname, og,
             schema=[sch_service(d['h1'], desc, slug),
                     sch_breadcrumb([("Home","/"),("Services","/services"),(d['h1'], slug)]),
                     sch_faq(faqs)])
    h += header(cart=True)
    h += page_hero(d['h1'], d['eyebrow'], d['h1'], d['subtitle'], trail=[("Services","services.html")], bg_img=img(cat,i)[0])
    # 1 — intro: image left, text right
    h += esplit("Overview", accent(d['intro_h']), d['intro'], img(cat,i),
                reverse=True, bg="bg-navy", cta=("Get a Free Quote","#cta-form"))
    # 2 — quality + two-column checklist: text left, image right
    h += esplit(d['offer_eyebrow'], accent(d['offer_h']), [d['offer_sub']], img(cat,i+1),
                bullets=d['included'], reverse=False, bg="bg-navy-slate")
    # 3 — horizontal carousel of the other services
    h += services_carousel(fname, eyebrow="Explore",
                           intro="One team for every cupboard. Browse the rest of what we do.", bg="bg-navy")
    # 4 — FAQ accordion (white cards on the grey section)
    h += faq_section("Questions", accent(d['h1'] + ", Answered"), faqs, bg="bg-navy-slate")
    h += cta_form()
    h += marquee()
    h += footer()
    return h

for fname,d in SERVICE_PAGES.items():
    print(fname, write(fname, build_service(fname,d)), "bytes")

# ============================================================ SERVICES HUB
def build_services_hub():
    og,_=img(KITCHEN,0)
    h=head("Our Services | Cupboard Centre",
           "Everything Cupboard Centre does: kitchen cupboards, bedroom and bathroom cabinetry, quartz tops, shopfitting, office desks and DIY flat-packs. Get a free quote.",
           "https://www.cupboardcentre.co.za/services.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Services","/services")])])
    h+=header()
    h+=page_hero("Services","What We Do","Cupboards For Every Room &amp; Budget",
                 "From fully installed custom kitchens to DIY flat-packs delivered to your door, one team for every cupboard.", bg_img=img(KITCHEN,0)[0])
    cards="".join(svc_card(t,h2,ic,im) for t,h2,ic,im in HOME_SVCS)
    h+="""<section class="section bg-navy"><div class="wrap section-center"><span class="eyebrow">Our Services</span><h2>One Team For Every Cupboard</h2>
  <p style="max-width:50em;margin:0 auto 34px">Whatever the room and whatever the budget, we supply, deliver and install cupboards built to last.</p>
  <div class="svc-grid">%s</div></div></section>
"""%cards
    # difference commit panel
    h+="""<section class="section bg-navy-slate"><div class="wrap"><div class="commit-panel">
    <div class="commit-left"><span class="eyebrow">Why Clients Pick Us</span><h2>The Cupboard Centre <span class="g2">Difference</span></h2>
      <div class="commit-acc">%s</div></div>
    <div class="commit-right"><div class="commit-img" style="background-image:url(%s)"></div>
      </div>
  </div></div></section>
"""%("".join('<div class="faq-item"><h2 class="faq-q h4">%s</h2><div class="faq-a"><p>%s</p></div></div>'%(q,a) for q,a in WHY_ITEMS), img(INSTALL,0)[0])
    h+=process_section("How It Works","Our Simple Process","bg-navy")
    h+=reviews_section("bg-navy-slate")
    h+=areas_section()
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("services.html", write("services.html", build_services_hub()), "bytes")

# ============================================================ ABOUT
def build_about():
    og,_=img(KITCHEN,4)
    h=head("About Cupboard Centre | 25+ Years in Mpumalanga",
           "For over 25 years Cupboard Centre has supplied and installed DIY &amp; custom cupboards across Mpumalanga, 1028+ projects, 50+ corporate clients, 100% satisfaction.",
           "https://www.cupboardcentre.co.za/about.html", og,
           schema=[sch_breadcrumb([("Home","/"),("About","/about")])])
    h+=header(cart=True)
    h+=page_hero("About Us","Our Story","Your Trusted DIY &amp; Custom Cupboard Experts",
                 "Over 25 years designing, building and installing cupboards for homes and businesses across Mpumalanga.", bg_img=img(KITCHEN,4)[0])
    # A — craftsmanship (image left, text right)
    h+=esplit("Our Story", accent("Built on Craftsmanship, Driven by Detail"),
        ["Cupboard Centre began with a simple idea: give Mpumalanga homeowners and builders beautifully made cupboards without the premium-showroom mark-up. What started as a passion for quality cabinetry has grown into a trusted Nelspruit name for custom and DIY cupboards.",
         "Over more than 25 years we have grown through word of mouth, referrals and repeat customers rather than trends and shortcuts. Kitchens, bedrooms, bathrooms, doors and countertops, all built to last."],
        img(KITCHEN,0), reverse=True, bg="bg-navy")
    # stats row
    h+=bigstats([("25+","Years of Experience"),("1028+","Projects Completed"),("50+","Corporate Clients"),("100%","Customer Satisfaction")], bg="bg-navy-slate")
    # B — experience / detail + bullets (text left, image right)
    h+=esplit("Why We're Different", accent("Experience You Can See in Every Detail"),
        ["Cupboard Centre is proudly local and owner-run. We combine traditional cabinetmaking values with modern materials and machinery, so every unit is finished to a standard we are happy to put our name on."],
        img(INSTALL,2),
        bullets=["Quality materials &amp; hardware","Custom &amp; DIY under one roof","Soft-close as standard","Expert local installation","Nationwide flat-pack delivery","Honest, written quotes"],
        reverse=False, bg="bg-navy", subhead="This is what sets us apart:")
    # statement
    h+=statement('Locally made cupboards, <span class="muted">built to last a lifetime.</span>', bg="bg-navy-slate")
    # C — designed around real living + bullets (image left, text right)
    h+=esplit("Our Approach", accent("Designed Around Real Living"),
        ["A cupboard should work as hard as it looks good. We plan every layout around how you actually live and store, then build it to fit your space exactly, with the finishes and hardware you choose."],
        img(BEDROOM,4),
        bullets=["Layouts that fit your space","Practical, everyday storage","Finishes chosen by you","Hard-wearing, easy-clean materials"],
        reverse=True, bg="bg-navy", subhead="Where function meets finish.")
    h+=reviews_section("bg-navy-slate")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("about.html", write("about.html", build_about()), "bytes")

# ============================================================ CONTACT
def contact_form():
    opts=["Get a Quote","DIY Cupboards","Kitchen Units","Bedroom Cupboards","Bathroom Cabinetry","Melamine Doors","Quartz Countertops","Custom Cabinetry","Installation","Other"]
    o="".join("<option>%s</option>"%x for x in opts)
    return """<div class="contact-form"><span class="eyebrow" style="color:var(--green)">Send Us A Message</span><h2>Request a Free Quote</h2>
      <form data-lead style="margin-top:16px"><div class="grid2 contact-grid2">
        <input class="field" placeholder="Full Name" required aria-label="Full Name" data-role="name">
        <input class="field" type="tel" placeholder="Phone Number" required aria-label="Phone Number" data-role="phone" inputmode="tel" pattern="^(\\+?27|0)[\\s\\-().]*\\d(?:[\\s\\-().]*\\d){8}$" title="Enter a 10-digit SA number or +27 followed by 9 digits.">
        <input class="field full" type="email" placeholder="Email Address" required aria-label="Email Address" data-role="email">
        <input class="field full" placeholder="Suburb / Area" aria-label="Suburb / Area" data-role="suburb" required>
        <select class="field full" aria-label="How Can We Help?" data-role="service" required><option value="">How Can We Help?</option>%s</select><input type="text" class="field full" placeholder="Please specify" data-role="service_other" style="display:none">
        <textarea class="field full" placeholder="Tell us about your project, sizes or any questions you have..." aria-label="Message" data-role="message"></textarea>
        <label class="lead-consent" style="display:flex;gap:10px;align-items:flex-start;margin:14px 0 0;font-size:.85rem;line-height:1.4;cursor:pointer;text-align:left"><input type="checkbox" data-role="consent" checked style="margin-top:3px;flex:0 0 auto;width:16px;height:16px;cursor:pointer"><span>I agree to be contacted by Cupboard Centre about my enquiry. See our <a href="privacy-policy.html" style="text-decoration:underline">Privacy Policy</a>.</span></label>
        <div class="full"><button class="btn btn-green btn-arrow" type="submit" style="width:100%%">Send Message</button></div>
      </div></form></div>"""%o

def build_contact():
    og,_=img(GENERAL,1)
    h=head("Contact Cupboard Centre | Nelspruit &amp; Mbombela",
           "Contact Cupboard Centre in Mbombela (Nelspruit). Call 084 683 7467, WhatsApp us or visit our showroom. Free quotes on DIY &amp; custom cupboards.",
           "https://www.cupboardcentre.co.za/contact.html", og, local_business=True,
           schema=[sch_breadcrumb([("Home","/"),("Contact","/contact")])])
    h+=header()
    h+=page_hero("Contact Us","Get In Touch","Contact Us", cta=False, bg_img=img(GENERAL,1)[0])
    h+="""<section class="section bg-navy"><div class="wrap"><div class="contact-grid">
    %s
    <div class="contact-info">
      <h3>Visit Our Showroom</h3>
      <div class="info-row">Point S Building, Lower Level,<br>Cnr Silva Street &amp; Old Pretoria Rd,<br>Mbombela (Nelspruit), 1200</div>
      <h3>Call or WhatsApp</h3>
      <div class="info-row"><a href="tel:%s">%s</a></div>
      <div class="info-row"><a href="https://wa.me/%s" target="_blank" rel="noopener">WhatsApp us &raquo;</a></div>
      <h3>Email</h3>
      <div class="info-row"><a href="mailto:%s">%s</a></div>
      <h3>Business Hours</h3>
      <div class="info-row">Mon &ndash; Thu: 07:00 &ndash; 17:00<br>Fri: 07:00 &ndash; 16:30<br>Sat: 07:30 &ndash; 13:30<br>Sun: Closed</div>
      <p style="margin-top:16px"><a class="btn btn-blue btn-arrow" href="service-areas.html">View Our Service Areas</a></p>
    </div>
  </div></div></section>
"""%(contact_form(), TEL, PHONE, WA, EMAIL, EMAIL)
    # map card
    h+="""<section class="section bg-navy-slate"><div class="wrap"><div class="section-center"><span class="eyebrow">Find Us</span><h2>Our Showroom</h2></div>
  <div class="branch-maps" style="grid-template-columns:1fr;max-width:960px">
    <div class="branch-map-card">
      <iframe src="%s" loading="lazy" title="Cupboard Centre showroom map" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <div class="bm-body"><h3>Cupboard Centre, Mbombela</h3><p>Point S Building, Lower Level, Cnr Silva Street &amp; Old Pretoria Rd, Mbombela, 1200<br><a href="tel:%s">%s</a></p></div>
    </div>
  </div></div></section>
"""%(GMAP,TEL,PHONE)
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("contact.html", write("contact.html", build_contact()), "bytes")

# ============================================================ GALLERY
def build_gallery():
    og,_=img(KITCHEN,0)
    h=head("Project Gallery | Cupboard Centre",
           "Browse completed Cupboard Centre projects, custom kitchens, built-in bedroom cupboards, bathroom vanities, quartz countertops and shopfitting across Mpumalanga.",
           "https://www.cupboardcentre.co.za/gallery.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Gallery","/gallery")])])
    h+=header()
    h+=page_hero("Gallery","Our Work","Spaces We Have Transformed",
                 "A selection of custom and DIY cupboard projects we’ve designed, built and installed.", bg_img=img(KITCHEN,0)[0])
    cats=[("all","All"),("kitchen","Kitchens"),("bedroom","Bedrooms"),("bathroom","Bathrooms"),("custom","Custom &amp; Shopfitting"),("diy","DIY Units")]
    filt="".join('<button data-filter="%s"%s>%s</button>'%(c,(' class="active"' if c=="all" else ''),l) for c,l in cats)
    # build items
    def items(lst,cat,n):
        out=""
        for i in range(min(n,len(lst))):
            u,a=img(lst,i,cat+" project")
            cap=('<figcaption>%s</figcaption>'%esc(a)) if a and a!=cat+" project" else ''
            out+='<figure class="g-item" data-cat="%s">%s%s</figure>'%(cat,responsive_img(u,esc(a) if a else cat),cap)
        return out
    grid = items(KITCHEN,"kitchen",12)+items(BEDROOM,"bedroom",10)+items(BATHROOM,"bathroom",8)+items(CUSTOM,"custom",10)+items(DIY,"diy",6)
    h+="""<section class="section bg-navy"><div class="wrap">
  <div class="gallery-filters">%s</div>
  <div class="gallery-grid">%s</div>
  <p class="section-center" style="margin-top:34px"><a class="btn btn-outline" href="gallery-designs-of-kitchen-cupboard.html">See All Kitchen Cupboard Designs</a> <a class="btn btn-green btn-arrow" href="#cta-form" data-scroll="cta-form">Start Your Project</a></p>
</div></section>
"""%(filt,grid)
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("gallery.html", write("gallery.html", build_gallery()), "bytes")

# ---- dedicated kitchen-designs gallery (restores the old, most-linked URL) ----
def build_kitchen_gallery():
    og,_=img(KITCHEN,0)
    h=head("Designs of Kitchen Cupboard: Photo Gallery | Cupboard Centre",
           "Browse real designs of kitchen cupboard projects we have built and installed, wood-grain, gloss and quartz-topped kitchens. Get a free quote on yours.",
           "https://www.cupboardcentre.co.za/gallery-designs-of-kitchen-cupboard.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Gallery","/gallery"),("Designs of Kitchen Cupboard","/gallery-designs-of-kitchen-cupboard")])])
    h+=header()
    h+=page_hero("Kitchen Designs","Kitchen Gallery","Designs of Kitchen Cupboard",
                 "Real kitchen cupboard designs we have measured, manufactured and fitted across Mpumalanga.",
                 trail=[("Gallery","gallery.html")], bg_img=img(KITCHEN,0)[0])
    def items(lst,cat,n,start=0):
        out=""
        for i in range(start,min(start+n,len(lst))):
            u,a=img(lst,i,"kitchen cupboard design")
            cap=('<figcaption>%s</figcaption>'%esc(a)) if a and a!="kitchen cupboard design" else ''
            out+='<figure class="g-item" data-cat="%s">%s%s</figure>'%(cat,responsive_img(u,esc(a) if a else cat),cap)
        return out
    h+="""<section class="section bg-navy"><div class="wrap section-center">
  <span class="eyebrow">Kitchen Cupboard Designs</span>
  <h2>Every Kitchen Here Was Built To Fit</h2>
  <p style="max-width:52em;margin:0 auto 30px">From wood-grain melamine and high-gloss doors to quartz-topped islands, these are kitchen cupboard designs we have built for real homes. Use them for ideas, then tell us about your space.</p>
  <div class="gallery-grid">%s</div>
  <p style="margin-top:34px"><a class="btn btn-green btn-arrow" href="kitchen-units.html">See Kitchen Cupboards &amp; Units</a></p>
</div></section>
"""%(items(KITCHEN,"kitchen",24))
    h+=faq_section("Questions", accent("Kitchen Cupboard Designs, Answered"),
                   [("What kitchen cupboard designs are most popular right now?",
                     "Wood-grain melamine with a contrasting quartz top is the most requested look, followed by plain white or grey gloss doors with handleless or slim-line handles. We will show you real samples so you can see and feel the finish before you decide."),
                    ("Can you build a kitchen from a design I have seen?",
                     "Yes. Bring a photo, a sketch or a Pinterest board and we will work out how to build it for your space and budget, then measure, manufacture and install it."),
                    ("Do you design the layout as well as build it?",
                     "We do. We plan the layout around how you actually cook and store things, the work triangle between sink, stove and fridge, then size every unit to your walls.")],
                   bg="bg-navy-slate")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("gallery-designs-of-kitchen-cupboard.html",
      write("gallery-designs-of-kitchen-cupboard.html", build_kitchen_gallery()), "bytes")

# ============================================================ SERVICE AREAS
def build_service_areas():
    og,_=img(GENERAL,2)
    h=head("Cupboards in Nelspruit &amp; Mbombela | Cupboard Centre",
           "Cupboard Centre installs cupboards across Nelspruit, Mbombela, White River, Hazyview, Barberton, Sabie and Malelane, with DIY flat-packs delivered nationwide.",
           "https://www.cupboardcentre.co.za/service-areas.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Service Areas","/service-areas")])])
    h+=header()
    h+=page_hero("Service Areas","Where We Work","Serving Nelspruit, Mbombela &amp; Beyond",
                 "Installation across the Lowveld from our Mbombela showroom, and DIY flat-pack delivery nationwide.", bg_img=img(GENERAL,2)[0])
    towns=["Nelspruit","Mbombela","White River","Hazyview","Barberton","Sabie","Malelane","Kaapmuiden","Kanyamazane","Nsikazi","Karino","Rocky's Drift"]
    tp="".join("<span>%s</span>"%t for t in towns)
    h+="""<section class="section bg-navy"><div class="wrap"><div class="area-split">
    <div class="area-text"><span class="eyebrow">Local Coverage</span><h2>Towns We Cover Across the Lowveld</h2>
      <p>Our showroom and workshop are in Mbombela (Nelspruit), and our installation teams cover the surrounding Lowveld. Not local? Our pre-cut, labelled DIY flat-pack units are delivered anywhere in South Africa.</p>
      <div class="pill-tags" style="justify-content:flex-start;margin-top:18px">%s</div>
      <p style="margin-top:22px"><a class="btn btn-green btn-arrow" href="#cta-form" data-scroll="cta-form">Get My Free Quote</a></p></div>
    <div class="area-map"><iframe src="%s" loading="lazy" title="Cupboard Centre service area" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div></div></section>
"""%(tp,GMAP)
    h+=feature_section("How We Serve You","Local Install, Nationwide DIY",[
       ("install","Local Installation","Full supply-and-install across Nelspruit, Mbombela, White River, Hazyview and the wider Lowveld."),
       ("truck","Nationwide DIY Delivery","Flat-packed, pre-cut units delivered to your door anywhere in South Africa."),
       ("ruler","Remote Measuring Help","Not nearby? Send us your measurements and we’ll help you plan and order the right units."),
    ],bg="bg-navy-slate")
    h+="""<section class="section bg-navy"><div class="wrap"><div class="section-center"><span class="eyebrow">Find Us</span><h2>Our Showroom</h2></div>
  <div class="branch-maps" style="grid-template-columns:1fr;max-width:960px">
    <div class="branch-map-card"><iframe src="%s" loading="lazy" title="Cupboard Centre showroom" referrerpolicy="no-referrer-when-downgrade"></iframe>
      <div class="bm-body"><h3>Cupboard Centre, Mbombela</h3><p>Point S Building, Lower Level, Cnr Silva Street &amp; Old Pretoria Rd, Mbombela, 1200<br><a href="tel:%s">%s</a></p></div></div>
  </div></div></section>
"""%(GMAP,TEL,PHONE)
    h+=reviews_section("bg-navy-slate")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("service-areas.html", write("service-areas.html", build_service_areas()), "bytes")

# ============================================================ FAQ
FAQ_FULL = FAQ_ITEMS + [
 ("What’s the difference between DIY and installed cupboards?","DIY units arrive pre-cut, edged, drilled and labelled with all hardware included for you to assemble. Installed means we handle everything, measuring, manufacturing and professional fitting. The quality of the units is identical; you choose how hands-on you want to be."),
 ("How long does a project take?","DIY orders are typically ready within a few working days. Custom, installed projects depend on scope, we’ll give you a clear timeline with your quote. We’re known for efficient turnaround."),
 ("Do you offer soft-close hinges and drawers?","Yes, soft-close hinges and drawer runners come standard on our cabinetry, not as an extra."),
 ("Can you match a colour or finish I already have?","In most cases, yes. Bring a photo or sample and we’ll match the melamine finish or countertop as closely as possible from our range."),
 ("Do you supply countertops separately?","Yes. We supply and fit Eazi Quartz and melamine countertops on their own or as part of a full kitchen."),
 ("How do I pay and do you take deposits?","We’ll set out payment terms clearly in your quote. Custom projects usually start with a deposit to secure your order and materials."),
]
def build_faq():
    og,_=img(GENERAL,3)
    h=head("Cupboard Questions Answered | Cupboard Centre",
           "Answers to common questions about Cupboard Centre's DIY and custom cupboards, ordering, delivery, installation, finishes, countertops and quotes.",
           "https://www.cupboardcentre.co.za/faq.html", og,
           schema=[sch_faq(FAQ_ITEMS), sch_breadcrumb([("Home","/"),("FAQ","/faq")])])
    h+=header()
    h+=page_hero("FAQ","Questions?","Frequently Asked Questions",
                 "Everything you need to know about ordering, delivery and installation.", bg_img=img(GENERAL,3)[0])
    h+="""<section class="section bg-navy"><div class="wrap">%s</div></section>
"""%accordion(FAQ_FULL)
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("faq.html", write("faq.html", build_faq()), "bytes")

# ============================================================ BLOG + POSTS
def build_blog():
    og,_=img(KITCHEN,1)
    h=head("Blog | Cupboard Centre, Cupboard, Kitchen &amp; Countertop Tips",
           "Expert advice on kitchens, cupboards, countertops and DIY from Cupboard Centre, guides to help you plan, choose and build the perfect cabinetry.",
           "https://www.cupboardcentre.co.za/blog.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Blog","/blog")])])
    h+=header()
    h+=page_hero("Blog","Insights","Cupboard &amp; Kitchen Tips",
                 "Guides and advice to help you plan, choose and get the most from your cupboards.", bg_img=img(KITCHEN,1)[0])
    pc="".join(post_card(p) for p in BLOG)
    h+="""<section class="section bg-navy"><div class="wrap">
  <div class="section-center"><span class="eyebrow">Guides &amp; Advice</span><h2>Cupboard, Kitchen &amp; Countertop Guides</h2></div>
  <div class="blog-grid" style="margin-top:30px">%s</div></div></section>
"""%pc
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("blog.html", write("blog.html", build_blog()), "bytes")

def build_post(p):
    slug,title,excerpt,cat,imgs,body = p
    og = blog_image(slug, imgs)[0]
    post_schema = ('{"@type":"BlogPosting","headline":%s,"description":%s,"image":"%s/%s",'
                   '"author":{"@type":"Organization","name":"Cupboard Centre"},'
                   '"publisher":{"@type":"Organization","name":"Cupboard Centre"},'
                   '"mainEntityOfPage":"%s/blog/%s"}'
                   % (json.dumps(title.replace('&amp;','&')),
                      json.dumps(excerpt.replace('&amp;','&')), SITE_URL, og, SITE_URL, slug))
    h=head(BLOG_TITLE.get(slug, title) + " | Cupboard Centre", excerpt,
           "https://www.cupboardcentre.co.za/blog/%s.html"%slug, og,
           schema=[post_schema,
                   sch_breadcrumb([("Home","/"),("Blog","/blog"),(title,"/blog/"+slug)])])
    # header/footer use relative paths, from /blog/ we need ../ prefix
    hd=header().replace('href="','href="../').replace('href="../#','href="#').replace('href="../http','href="http').replace('href="../tel:','href="tel:').replace('href="../mailto:','href="mailto:').replace('src="assets','src="../assets')
    h=h.replace('href="assets/css/styles.css"','href="../assets/css/styles.css"')
    h=h.replace('href="assets/images/favicon.png"','href="../assets/images/favicon.png"')
    h+=hd
    # page hero with blog trail (fix links for subdir)
    ph=page_hero(title,"Insights",title,cta=False,trail=[("Blog","blog.html")],bg_img='../'+img(imgs,1)[0],prefix="../")
    h+=ph
    hero_u = '../'+blog_image(slug, imgs)[0]
    secs=""
    for i,(sh,sp) in enumerate(body):
        secs+='<h2>%s</h2><p>%s</p>'%(sh,sp)
    h+="""<section class="section bg-navy"><div class="wrap"><div class="article-body">
    <p><span class="eyebrow">%s</span></p>
    <img src="%s" alt="%s" style="width:100%%;border-radius:var(--r-card);box-shadow:var(--shadow-card);margin:0 0 26px" loading="lazy">
    <p style="font-size:18px;color:var(--heading)"><strong>%s</strong></p>
    %s
    <div style="background:#f4f5f7;border-radius:var(--r-card);padding:26px 28px;margin-top:30px">
      <h3 style="margin-top:0">Ready to start your project?</h3>
      <p style="margin-bottom:14px">Cupboard Centre supplies and installs custom and DIY cupboards across Nelspruit and the Lowveld, with delivery nationwide. Get a free, no-obligation quote today.</p>
      <a class="btn btn-green btn-arrow" href="../get-a-quote.html">Get a Free Quote</a>
    </div>
  </div></div></section>
"""%(cat,hero_u,esc(title),excerpt,secs)
    # cta + marquee + footer with ../ fix
    cf=cta_form().replace('href="privacy-policy.html"','href="../privacy-policy.html"')
    h+=cf
    h+=marquee().replace('src="assets','src="../assets')
    ft=footer().replace('href="','href="../').replace('href="../http','href="http').replace('href="../tel:','href="tel:').replace('href="../mailto:','href="mailto:').replace('href="../#','href="#').replace('src="assets','src="../assets')
    h+=ft
    return h
for p in BLOG:
    print("blog/%s.html"%p[0], write("blog/%s.html"%p[0], build_post(p)), "bytes")

# ============================================================ GET A QUOTE
def build_quote():
    og,_=img(GENERAL,0)
    h=head("Get a Free Quote | Cupboard Centre, DIY &amp; Custom Cupboards",
           "Get a free, no-obligation quote from Cupboard Centre on DIY or custom cupboards, kitchens, wardrobes, doors and countertops. Free, with no obligation.",
           "https://www.cupboardcentre.co.za/get-a-quote.html", og,
           schema=[sch_breadcrumb([("Home","/"),("Get a Quote","/get-a-quote")])])
    h+=header()
    h+=page_hero("Get a Free Quote","Free &amp; No-Obligation","Get Your Free Cupboard Quote", cta=False, bg_img=img(KITCHEN,7)[0])
    benefits=[("wallet","Best Value, Guaranteed","Factory-direct pricing on DIY and custom cupboards, quality that beats the big retailers."),
              ("ruler","Planning &amp; Advice","We help you plan the right units and finishes, with a clear written quote and no pressure."),
              ("truck","Delivery &amp; Installation","Nationwide DIY delivery, or full supply-and-install across the Lowveld."),
              ("check","25+ Years’ Experience","Over a thousand completed projects for homes and businesses across Mpumalanga.")]
    bl="".join('<li style="display:flex;gap:12px;align-items:flex-start;margin-bottom:16px"><span style="flex:0 0 auto;width:42px;height:42px;border-radius:50%%;background:var(--green);color:#fff;display:flex;align-items:center;justify-content:center">%s</span><span><strong style="display:block;color:var(--heading);font-family:\'Poppins\',sans-serif">%s</strong><span style="font-size:14px">%s</span></span></li>'%(IC.get(ic,IC['check']),t,d) for ic,t,d in benefits)
    h+="""<section class="section bg-navy"><div class="wrap"><div class="contact-grid">
    <div>
      <span class="eyebrow">Why Cupboard Centre</span><h2>Honest Advice, Clear Pricing</h2>
      <p>Tell us about your project, a room, a rough size, or just an idea, and we’ll come back with a clear, written quote. No obligation, no pressure.</p>
      <ul style="list-style:none;margin-top:22px">%s</ul>
      <p class="btn-row" style="margin-top:8px"><a class="btn btn-outline" href="tel:%s">Call %s</a> <a class="btn btn-outline" href="https://wa.me/%s" target="_blank" rel="noopener">WhatsApp Us</a></p>
    </div>
    %s
  </div></div></section>
"""%(bl,TEL,PHONE,WA,lead_form("Request Your Free Quote","We’ll call you back once we receive your form.","Get My Free Quote"))
    h+=process_section("How It Works","From Quote to Complete","bg-navy-slate")
    h+=reviews_section("bg-navy")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("get-a-quote.html", write("get-a-quote.html", build_quote()), "bytes")

# ============================================================ SHOP
# --- single in-stock product ---
def _prod_photo():
    for i in range(len(PRODUCT)):
        u,a=img(PRODUCT,i)
        if u.endswith('.jpg'): return u
    return img(PRODUCT,0)[0]
PROD = dict(
    id="flat-pack-wardrobe",
    name="Flat-Pack Wardrobe, Woody Doors",
    price=8999, price_disp="R8 999", was="R12 999",
    short="3-door, 2-drawer flat-pack wardrobe with woody-look melamine doors, a hanging rail and custom internal storage. Pre-cut, edged, drilled and labelled, ready to assemble.",
    img=_prod_photo(),
    gallery=[img(BEDROOM,7)[0], img(BEDROOM,2)[0]],
    features=["3 doors + 2 drawers","Woody-look melamine finish","Hanging rail &amp; adjustable shelves",
              "Soft-close hinges included","All hardware &amp; assembly guide included","Delivered nationwide, flat-packed"],
)

def add_cart_attrs(p):
    return ('data-id="%s" data-name="%s" data-price="%d" data-price-disp="%s" data-img="%s"'
            % (p['id'], p['name'], p['price'], p['price_disp'], p['img']))

def build_shop():
    p=PROD
    h=head("Shop Pre-Assembled &amp; Flat Pack Cupboards | Cupboard Centre",
           "Buy Cupboard Centre flat-pack and pre-assembled cupboards online, pre-cut, edged and drilled with all hardware included. Delivered nationwide.",
           "https://www.cupboardcentre.co.za/shop.html", p['img'],
           schema=[sch_breadcrumb([("Home","/"),("Shop","/shop")])])
    h+=header(cart=True)
    h+=page_hero("Shop","Online Shop","Shop DIY Cupboards",
                 "DIY flat-pack cupboards, delivered to your door, nationwide.", bg_img=img(KITCHEN,3)[0])
    wasx=' <span class="was">%s</span>'%p['was'] if p['was'] else ''
    h+="""<section class="section bg-navy"><div class="wrap">
  <div class="section-center" style="margin-bottom:26px"><span class="eyebrow">In Stock</span><h2>DIY Cupboards, Ready to Order</h2>
  <p style="max-width:46em;margin:6px auto 0;color:var(--muted)">Looking for custom kitchens, bedrooms or bathrooms? <a href="get-a-quote.html" style="color:var(--cc-red);font-weight:700">Get a free quote</a> and we’ll build to your space.</p></div>
  <div style="max-width:360px;margin:0 auto">
    <div class="img-card" style="display:flex;flex-direction:column">
      <a class="ic-img" href="product-{id}.html" style="display:block"><img src="{img}" alt="{name}" loading="lazy" decoding="async"></a>
      <div style="padding:20px 22px;display:flex;flex-direction:column;flex:1">
        <h3 style="font-size:18px;color:var(--heading);margin:0 0 6px"><a href="product-{id}.html">{name}</a></h3>
        <p style="font-size:14px;flex:1">{short}</p>
        <p class="price" style="margin:6px 0 12px">{price}{wasx}</p>
        <div class="btn-row" style="gap:10px">
          <button class="btn btn-green" data-add-cart {attrs} style="flex:1">Add to Cart</button>
          <a class="btn btn-outline" href="product-{id}.html" style="flex:1">View</a>
        </div>
      </div></div>
  </div>
</div></section>
""".format(id=p['id'], img=p['img'], name=p['name'], short="3 doors, 2 drawers, woody-look melamine, custom internal storage.", price=p['price_disp'], wasx=wasx, attrs=add_cart_attrs(p))
    h+=feature_section("Why Shop With Us","DIY Made Easy",[
      ("truck","Nationwide Delivery","Flat-packed, protected and delivered to your door anywhere in South Africa."),
      ("diy","Assembly Ready","Pre-cut, edged, drilled and labelled with all hardware included."),
      ("wallet","Factory-Direct Prices","Buy straight from the manufacturer and save without losing quality."),
    ],bg="bg-navy-slate")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("shop.html", write("shop.html", build_shop()), "bytes")

def build_product():
    p=PROD
    h=head("%s | Cupboard Centre"%p['name'].replace('&amp;','&'),
           "Flat pack wardrobe with woody melamine doors, 3 doors and 2 drawers. Pre-cut, edged and drilled with all hardware included. Delivered nationwide.",
           "https://www.cupboardcentre.co.za/product-%s.html"%p['id'], p['img'],
           schema=[('{"@type":"Product","name":%s,"description":%s,"image":"%s/%s",'
                    '"brand":{"@type":"Brand","name":"Cupboard Centre"},'
                    '"offers":{"@type":"Offer","priceCurrency":"ZAR","price":"%d",'
                    '"availability":"https://schema.org/InStock","url":"%s/product-%s"}}'
                    % (json.dumps(p['name'].replace('&amp;','&')),
                       json.dumps(p['short'].replace('&amp;','&')), SITE_URL, p['img'],
                       p['price'], SITE_URL, p['id'])),
                   sch_breadcrumb([("Home","/"),("Shop","/shop"),(p['name'],"/product-"+p['id'])])])
    h+=header(cart=True)
    h+=page_hero(p['name'],"Shop",p['name'],cta=False,trail=[("Shop","shop.html")],bg_img=img(KITCHEN,3)[0])
    thumbs="".join('<button class="pd-thumb" data-src="%s"><img src="%s" alt="" loading="lazy"></button>'%(g,g) for g in [p['img']]+p['gallery'])
    feats="".join('<li>%s</li>'%f for f in p['features'])
    wasx=' <span class="was">%s</span>'%p['was'] if p['was'] else ''
    wamsg = "Hi Cupboard Centre, I'd like to order the %s (%s). Is it in stock?"%(p['name'].replace('&amp;','&'), p['price_disp'])
    import urllib.parse as _u
    wa_href="https://wa.me/%s?text=%s"%(WA,_u.quote(wamsg))
    h+="""<section class="section bg-navy"><div class="wrap">
  <div class="product-detail">
    <div class="pd-media">
      <div class="pd-main"><img src="{img}" alt="{name}" data-pd-main></div>
      <div class="pd-thumbs">{thumbs}</div>
    </div>
    <div class="pd-info">
      <span class="eyebrow">DIY Wardrobe, In Stock</span>
      <h2 style="font-size:30px;margin:.1em 0 .3em">{name}</h2>
      <p class="price" style="font-size:26px;margin:0 0 14px">{price}{wasx}</p>
      <p>{short}</p>
      <ul class="included-grid" style="grid-template-columns:1fr;margin:16px 0 22px">{feats}</ul>
      <div class="pd-buy">
        <div class="qty-box"><button type="button" data-qty-dec aria-label="Decrease">−</button><input type="number" min="1" value="1" data-qty aria-label="Quantity"><button type="button" data-qty-inc aria-label="Increase">+</button></div>
        <button class="btn btn-green btn-arrow" data-add-cart {attrs} style="flex:1">Add to Cart</button>
      </div>
      <p style="margin-top:14px"><a class="btn btn-outline" href="{wa}" target="_blank" rel="noopener">Order via WhatsApp</a> <a class="btn btn-outline" href="cart.html">View Cart</a></p>
      <p style="font-size:13px;color:var(--muted);margin-top:14px">Prices include the flat-pack unit and hardware. Delivery is quoted on checkout by area. Need a custom size? <a href="get-a-quote.html" style="color:var(--cc-red);font-weight:700">Request a quote</a>.</p>
    </div>
  </div>
</div></section>
""".format(img=p['img'],name=p['name'],price=p['price_disp'],wasx=wasx,short=p['short'],feats=feats,thumbs=thumbs,attrs=add_cart_attrs(p),wa=wa_href)
    h+=reviews_section("bg-navy-slate")
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("product-%s.html"%PROD['id'], write("product-%s.html"%PROD['id'], build_product()), "bytes")

def build_cart():
    h=head("Your Cart | Cupboard Centre","Review the DIY cupboard units in your Cupboard Centre cart, adjust quantities and send your order enquiry straight through to our Mbombela team.",
           "https://www.cupboardcentre.co.za/cart.html", PROD['img'])
    h+=header(cart=True)
    h+=page_hero("Cart","Shop","Your Cart",cta=False,trail=[("Shop","shop.html")],bg_img=img(KITCHEN,3)[0])
    h+="""<section class="section bg-navy"><div class="wrap">
  <div data-cart-root>
    <div class="cart-empty" data-cart-empty>
      <p style="font-size:18px;color:var(--heading);font-family:'Poppins',sans-serif;font-weight:700;margin-bottom:6px">Your cart is empty</p>
      <p style="color:var(--muted);margin-bottom:18px">Browse our DIY cupboards and add something to get started.</p>
      <a class="btn btn-green btn-arrow" href="shop.html">Go to Shop</a>
    </div>
    <div class="cart-body" data-cart-body hidden>
      <div class="cart-items" data-cart-items></div>
      <div class="cart-summary">
        <div class="cart-total-row"><span>Subtotal</span><strong data-cart-total>R0</strong></div>
        <p style="font-size:13px;color:var(--muted);margin:6px 0 16px">Delivery is quoted by area once you send your enquiry. No payment is taken online.</p>
        <button class="btn btn-green btn-arrow" data-cart-checkout style="width:100%">Send Order Enquiry via WhatsApp</button>
        <p style="margin-top:10px"><a class="btn btn-outline" href="shop.html" style="width:100%">Continue Shopping</a></p>
      </div>
    </div>
  </div>
</div></section>
"""
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("cart.html", write("cart.html", build_cart()), "bytes")

# ============================================================ PRIVACY
def build_privacy():
    h=head("Privacy Policy | Cupboard Centre","How Cupboard Centre collects, uses, stores and protects the personal information you share with us through our website, forms and enquiries.",
           "https://www.cupboardcentre.co.za/privacy-policy.html", img(GENERAL,0)[0])
    h+=header()
    h+=page_hero("Privacy Policy","Legal","Privacy Policy", cta=False, bg_img=img(GENERAL,0)[0])
    secs=[("Who We Are","Cupboard Centre (“we”, “us”, “our”) supplies and installs DIY and custom cupboards from our showroom at Point S Building, Lower Level, Cnr Silva Street &amp; Old Pretoria Rd, Mbombela, 1200. You can reach us on 084 683 7467 or at info@cupboardcentre.co.za."),
      ("Information We Collect","When you submit an enquiry or quote request, we collect the details you provide, such as your name, phone number, email address, suburb/area and information about your project. We may also collect basic, anonymous usage data through our website."),
      ("How We Use Your Information","We use your information to respond to your enquiry, prepare quotes, arrange delivery or installation, and keep you updated about your project. With your consent, we may occasionally send you relevant offers or news. We do not sell your personal information."),
      ("Sharing Your Information","We only share your information where necessary to deliver our services, for example with delivery partners, or where required by law. We take reasonable steps to ensure any third parties protect your information."),
      ("Data Security &amp; Retention","We take reasonable technical and organisational measures to protect your personal information and retain it only for as long as needed to provide our services and meet legal obligations."),
      ("Your Rights","You may request access to, correction of, or deletion of your personal information, and you may withdraw consent to marketing at any time by contacting us on info@cupboardcentre.co.za."),
      ("Cookies","Our website may use cookies and similar technologies to improve your experience and understand how the site is used. You can control cookies through your browser settings."),
      ("Changes to This Policy","We may update this policy from time to time. The latest version will always be available on this page."),
      ("Contact Us","For any privacy questions or requests, contact us on 084 683 7467 or info@cupboardcentre.co.za.")]
    body="".join('<h2>%s</h2><p>%s</p>'%(t,b) for t,b in secs)
    h+='<section class="section bg-navy-slate"><div class="wrap"><div class="article-body">%s</div></div></section>\n'%body
    h+=marquee(); h+=footer()
    return h
print("privacy-policy.html", write("privacy-policy.html", build_privacy()), "bytes")

# ============================================================ SITEMAP
def build_sitemap():
    h=head("Sitemap | Cupboard Centre","Every page on the Cupboard Centre website in one place, our cupboard services, project galleries, online shop, guides and contact details.",
           "https://www.cupboardcentre.co.za/sitemap.html", img(GENERAL,0)[0])
    h+=header()
    h+=page_hero("Sitemap","Sitemap","Sitemap", cta=False, bg_img=img(GENERAL,0)[0])
    groups=[("Main",[("Home","index.html"),("About Us","about.html"),("Contact","contact.html"),("Get a Free Quote","get-a-quote.html"),("Online Shop","shop.html"),("Product: Flat-Pack Wardrobe","product-flat-pack-wardrobe.html"),("Cart","cart.html"),("Gallery","gallery.html"),("FAQ","faq.html"),("Service Areas","service-areas.html")]),
            ("Services",[("All Services","services.html")]+[(t.replace('&amp;','&'),hh) for t,hh in SERVICES[:-1]]),
            ("Blog",[("Blog","blog.html")]+[(p[1],"blog/%s.html"%p[0]) for p in BLOG]),
            ("Legal",[("Privacy Policy","privacy-policy.html")])]
    cols=""
    for title,links in groups:
        li="".join('<li><a href="%s">%s</a></li>'%(hh,t) for t,hh in links)
        cols+='<div><h2 class="h4" style="color:var(--heading)">%s</h2><ul style="list-style:none">%s</ul></div>'%(title,li)
    h+="""<section class="section bg-navy"><div class="wrap"><div class="footer-cols" style="gap:36px">%s</div></div></section>
"""%cols
    # style the sitemap links
    h+='<style>section .footer-cols li a{color:var(--blue)!important;display:inline-block;padding:5px 0}section .footer-cols li a:hover{color:var(--green)!important}</style>'
    h+=cta_form(); h+=marquee(); h+=footer()
    return h
print("sitemap.html", write("sitemap.html", build_sitemap()), "bytes")

# ============================================================ sitemap.xml / robots.txt / _redirects
SITE = "https://www.cupboardcentre.co.za"

# priority + change frequency by page role
SITEMAP_PAGES = [
    ("",                                       "1.0", "weekly"),
    ("services.html",                          "0.9", "monthly"),
    ("cupboard-installation.html",             "0.9", "monthly"),
    ("kitchen-units.html",                     "0.9", "monthly"),
    ("bedroom-cupboards.html",                 "0.9", "monthly"),
    ("bathroom-cabinets.html",                 "0.9", "monthly"),
    ("office-reception-desks.html",            "0.9", "monthly"),
    ("gallery-designs-of-kitchen-cupboard.html","0.8", "monthly"),
    ("melamine-doors-quartz-countertops.html", "0.9", "monthly"),
    ("custom-cabinetry.html",                  "0.9", "monthly"),
    ("diy-units.html",                         "0.9", "monthly"),
    ("shop.html",                              "0.8", "weekly"),
    ("product-flat-pack-wardrobe.html",        "0.7", "weekly"),
    ("gallery.html",                           "0.7", "monthly"),
    ("service-areas.html",                     "0.7", "monthly"),
    ("about.html",                             "0.6", "yearly"),
    ("contact.html",                           "0.7", "yearly"),
    ("get-a-quote.html",                       "0.8", "yearly"),
    ("faq.html",                               "0.6", "monthly"),
    ("blog.html",                              "0.6", "weekly"),
    ("sitemap.html",                           "0.3", "yearly"),
    ("privacy-policy.html",                    "0.2", "yearly"),
]
# NOINDEX list (per SEO spec): cart is a utility page, excluded from the sitemap.
NOINDEX = ["cart.html"]

def build_sitemap_xml():
    from datetime import date
    today = date.today().isoformat()
    urls = list(SITEMAP_PAGES) + [("blog/%s.html" % p[0], "0.5", "monthly") for p in BLOG]
    body = ""
    for loc, pri, freq in urls:
        loc = loc[:-5] if loc.endswith('.html') else loc
        body += ("  <url>\n    <loc>%s/%s</loc>\n    <lastmod>%s</lastmod>\n"
                 "    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>\n"
                 % (SITE, loc, today, freq, pri))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % body)

def build_robots():
    return ("# Production robots.txt for cupboardcentre.co.za\n"
            "User-agent: *\n"
            "Allow: /\n\n"
            "# Utility pages, no search value\n"
            "Disallow: /cart\n\n"
            "Sitemap: %s/sitemap.xml\n" % SITE)

print("sitemap.xml", write("sitemap.xml", build_sitemap_xml()), "bytes")
print("robots.txt", write("robots.txt", build_robots()), "bytes")

print("\nALL PAGES GENERATED.")
