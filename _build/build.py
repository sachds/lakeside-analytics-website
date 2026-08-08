#!/usr/bin/env python3
"""Render both Lakeside Analytics builds from one content model.

Two skins share an information architecture and every word of copy; only the
class names and page chrome differ. Running this is the only supported way to
edit either site's structure — hand-editing one build would let them drift.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import (NAV, STUDIES, CASES, ALSO_BUILT, PRACTICES, SHAPES,
                     STATS, METHOD, ABOUT, CONTACT, KINDS, LEDES)

LIGHT = "/Users/sachin/Developer/lakeside-analytics-website"
DARK  = "/Users/sachin/Developer/lakeside-analytics-dark"

MARK = ('<svg class="mark" width="%d" height="%d" viewBox="0 0 20 20" fill="none" aria-hidden="true">'
        '<circle cx="10" cy="6.4" r="3.4" stroke="currentColor" stroke-width="1.5"/>'
        '<path d="M3 13.2h14M5 16.2h10" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>')

EMAIL = CONTACT["email"]


# ---------------------------------------------------------------- shared bits

def nav_links(current, cls_a=""):
    out = []
    for label, href in NAV:
        cur = ' aria-current="page"' if href == current else ""
        out.append(f'      <a href="{href}"{cur}>{label}</a>')
    out.append(f'      <a href="mailto:{EMAIL}">Contact</a>')
    return "\n".join(out)


def head(skin, title, desc, canonical, extra=""):
    if skin == "dark":
        links = ('<meta name="theme-color" content="#0F1210">\n'
                 '<link rel="preload" as="font" type="font/woff2" href="fonts/SourceSerif4-var.woff2" crossorigin>\n'
                 '<link rel="stylesheet" href="tokens.css">\n<link rel="stylesheet" href="styles.css">')
    else:
        links = '<link rel="stylesheet" href="styles.css">'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://lakesideanalytics.io/{canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://lakesideanalytics.io/{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
{links}{extra}
</head>
<body>
"""


def header(skin, current):
    if skin == "dark":
        return f"""
<a class="skip" href="#main">Skip to content</a>

<header class="nav">
  <div class="container nav-inner">
    <a class="wordmark" href="/">
      {MARK % (18, 18)}
      Lakeside Analytics
    </a>
    <nav class="nav-links" aria-label="Primary">
{nav_links(current)}
    </nav>
  </div>
</header>

<main id="main">
"""
    return f"""
<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/">
      {MARK % (20, 20)}
      Lakeside Analytics
    </a>
    <nav class="nav" aria-label="Primary">
{nav_links(current)}
    </nav>
  </div>
</header>

<main id="main">
"""


def contact_section(skin, title=None, sub=None):
    t = title or CONTACT["title"]
    s = sub or CONTACT["sub"]
    if skin == "dark":
        return f"""
  <section class="contact">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> Contact</p>
      <div class="head-rule"></div>
      <h2>{t}</h2>
      <p class="sub">{s}</p>
      <a class="mailto" href="mailto:{EMAIL}">{EMAIL}</a>
      <p class="contact-meta">brooklyn, new york &middot; practice established 2021</p>
    </div>
  </section>
"""
    return f"""
  <section>
    <div class="wrap">
      <div class="callout cta">
        <span class="eyebrow">Contact</span>
        <h2>{t}</h2>
        <p>{s}</p>
        <div class="btn-row">
          <a class="btn" href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
    </div>
  </section>
"""


def footer(skin):
    links = "\n".join(f'        <a href="{h}">{l}</a>' for l, h in NAV)
    if skin == "dark":
        return f"""
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <strong>Lakeside Analytics</strong>
        Data platforms and AI systems, engineered with evidence.
      </div>
      <div class="footer-links">
        <a href="/">Home</a>
{links}
        <a href="mailto:{EMAIL}">{EMAIL}</a>
      </div>
    </div>
    <div class="colophon">
      <span>&copy; 2026 Lakeside Analytics</span>
      <span>Every number on this site carries a venue and a date. If a figure is not in a published piece, it does not appear here.</span>
      <span>Product names and marks belong to their respective owners; their use does not imply endorsement.</span>
    </div>
  </div>
</footer>

</body>
</html>
"""
    return f"""
</main>

<footer class="site-footer">
  <div class="wrap">
    <div>&copy; 2026 Lakeside Analytics. All rights reserved.</div>
    <div class="footer-links">
      <a href="/">Home</a>
{links}
      <a href="mailto:{EMAIL}">{EMAIL}</a>
    </div>
  </div>
  <div class="wrap colophon">
    Every number on this site carries a venue and a date. If a figure is not in a
    published piece, it does not appear here. Product names and marks belong to their
    respective owners.
  </div>
</footer>

</body>
</html>
"""


def lede(key):
    a, b = LEDES[key]
    return f'<strong>{a}</strong>{b}'


def filter_bar(kinds):
    """Filter pills, the BCG insights-index pattern. Progressive enhancement:
    with JS off every card stays visible and the bar simply does nothing."""
    pills = "\n".join(
        f'        <button class="pill" type="button" data-kind="{k}">{k}</button>'
        for k in kinds)
    return f"""      <div class="filters" role="group" aria-label="Filter by type">
        <button class="pill is-on" type="button" data-kind="all">All <span class="pill-n">{len(STUDIES)}</span></button>
{pills}
      </div>
"""


FILTER_JS = """<script>
(function () {
  var bar = document.querySelector('.filters');
  if (!bar) return;
  var cards = Array.prototype.slice.call(document.querySelectorAll('[data-kind-of]'));
  bar.addEventListener('click', function (e) {
    var b = e.target.closest('.pill');
    if (!b) return;
    var k = b.dataset.kind;
    bar.querySelectorAll('.pill').forEach(function (p) { p.classList.toggle('is-on', p === b); });
    cards.forEach(function (c) {
      c.hidden = !(k === 'all' || c.dataset.kindOf === k);
    });
  });
})();
</script>
"""


def sec_head(skin, ix, eyebrow, h2, sub=None):
    subhtml = f'\n        <p class="sub">{sub}</p>' if sub else ""
    if skin == "dark":
        return f"""      <div class="section-head">
        <p class="eyebrow"><span class="ix">{ix}</span> {eyebrow}</p>
        <div class="head-rule"></div>
        <h2>{h2}</h2>{subhtml}
      </div>
"""
    subl = f'\n        <p>{sub}</p>' if sub else ""
    return f"""      <div class="section-intro prose">
        <span class="eyebrow">{eyebrow}</span>
        <h2>{h2}</h2>{subl}
      </div>
"""


# ---------------------------------------------------------------- components

def insight_card(skin, s):
    """Card anatomy borrowed wholesale from BCG's insights index:
    category chip, then TYPE + full date, then headline, then dek."""
    role = f' &middot; {s["role"]}' if s.get("role") else ""
    cls = "icard" if skin == "dark" else "icard"
    return f"""
        <a class="{cls}" href="{s['url']}" data-kind-of="{s['kind']}">
          <span class="icard-chip">{s['kind']}</span>
          <span class="icard-meta">{s['full']} &middot; {s['venue']}{role}</span>
          <span class="icard-title">{s['title']}</span>
          <span class="icard-desc">{s['desc']}</span>
        </a>
"""


def study_card(skin, s, i):
    role = f' &middot; {s["role"]}' if s.get("role") else ""
    meta = f'{s["kind"]} &middot; {s["date"]} &middot; {s["venue"]}{role}'
    if skin == "dark":
        return f"""
        <article class="study">
          <div class="index num">{i:02d}</div>
          <div>
            <p class="date-line"><span class="kind">{s['kind']}</span> {s['date']} &middot; {s['venue']}{role}</p>
            <h3><a href="{s['url']}">{s['title']}</a></h3>
            <p class="finding">{s['desc']}</p>
          </div>
        </article>
"""
    return f"""
        <li class="entry">
          <div class="entry-meta">
            <span class="kind">{s['kind']}</span>
            <span>{s['date']}</span>
            <span class="entry-role">{s['venue']}</span>
          </div>
          <div>
            <h3><a href="{s['url']}">{s['title']}</a></h3>
            <p>{s['desc']}</p>
          </div>
        </li>
"""


def case_lead(skin, c):
    v, l = c["lead"]
    return f"""        <div class="case-lead">
          <span class="lead-val">{v}</span>
          <span class="lead-label">{l}</span>
        </div>
"""


def case_block(skin, c, full=False):
    body = "\n".join(f"            <p>{p}</p>" for p in (c["body"] if full else c["body"][-1:]))
    n = len(c["measures"])
    if skin == "dark":
        ms = "\n".join(f"""          <div class="measure">
            <span class="m-val">{v}</span>
            <span class="m-label">{l}</span>
          </div>""" for v, l in c["measures"])
        return f"""
      <article class="case">
""" + case_lead(skin, c) + f"""        <div class="case-head">
          <span class="case-mark">{c['client']}</span>
          <span>{c['scope']}</span>
          <span class="case-role">{c['years']}</span>
        </div>
        <div class="case-grid">
          <h3>{c['title']}</h3>
          <div class="case-body">
{body}
            <p class="prov">{c['prov']}</p>
          </div>
        </div>
        <div class="measures{' m-2' if n == 2 else ''}">
{ms}
        </div>
      </article>
"""
    ms = "\n".join(f"""            <li>
              <span class="m-figure">{v}</span>
              <span class="m-label">{l}</span>
            </li>""" for v, l in c["measures"])
    return f"""
      <article class="engagement">
""" + case_lead(skin, c) + f"""        <div class="engagement-who">
          <strong>{c['client']}</strong>
          {c['scope']}
          <br>{c['years']}
        </div>
        <div class="engagement-body">
          <h3>{c['title']}</h3>
{body}
          <ul class="measures">
{ms}
          </ul>
          <p class="provenance">{c['prov']}</p>
        </div>
      </article>
"""


def stats_block(skin):
    if skin == "dark":
        items = "\n".join(f"""        <div class="stat">
          <span class="s-val num">{v}</span>
          <span class="s-label">{l}</span>
        </div>""" for v, l in STATS)
        return f'      <div class="stats">\n{items}\n      </div>\n'
    items = "\n".join(f"""      <div class="stat">
        <span class="figure">{v}</span>
        <span class="label">{l}</span>
      </div>""" for v, l in STATS)
    return f'  <div class="wrap">\n    <div class="stats">\n{items}\n    </div>\n  </div>\n'


def shapes_block(skin, items):
    if skin == "dark":
        inner = "\n".join(f"""        <div class="shape">
          <span class="term">{t}</span>
          <h3>{h}</h3>
          <p>{b}</p>
        </div>""" for t, h, b in items)
        return f'      <div class="shapes">\n{inner}\n      </div>\n'
    inner = "\n".join(f"""        <article class="card">
          <span class="num">{t}</span>
          <h3>{h}</h3>
          <p>{b}</p>
        </article>""" for t, h, b in items)
    return f'      <div class="grid">\n{inner}\n      </div>\n'


def wrap_open(skin):
    return '    <div class="container">' if skin == "dark" else '    <div class="wrap">'


# ---------------------------------------------------------------- pages

def page_index(skin):
    featured = STUDIES[0]
    s = head(skin, "Lakeside Analytics — Data platforms and AI systems, engineered with evidence",
             "Benchmark studies, production agents, and data applications on Databricks and Snowflake. Every recommendation traces to a published number.",
             "")
    s += header(skin, "")

    hero_cls = "hero"
    lede_html = lede("index")

    if skin == "dark":
        s += f"""
  <section class="{hero_cls}">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> Independent data platform consultancy</p>
      <h1>Data platforms and AI systems, engineered with evidence.</h1>
      <p class="lede">{lede_html}</p>

      <a class="feature" href="{featured['url']}">
        <span class="feature-kind">{featured['kind']}</span>
        <span class="feature-meta">{featured['date']} &middot; {featured['venue']}</span>
        <span class="feature-title">{featured['title']}</span>
        <span class="feature-desc">{featured['desc']}</span>
        <span class="feature-cta">Read the study &rarr;</span>
      </a>

{stats_block(skin)}    </div>
  </section>
"""
    else:
        s += f"""
  <section class="{hero_cls}">
    <div class="wrap">
      <span class="eyebrow">Independent data platform consultancy</span>
      <h1>Data platforms and AI systems, engineered with evidence.</h1>
      <p class="lede">{lede_html}</p>

      <a class="feature" href="{featured['url']}">
        <span class="feature-kind">{featured['kind']}</span>
        <span class="feature-meta">{featured['date']} &middot; {featured['venue']}</span>
        <span class="feature-title">{featured['title']}</span>
        <span class="feature-desc">{featured['desc']}</span>
        <span class="feature-cta">Read the study &rarr;</span>
      </a>
    </div>
  </section>

{stats_block(skin)}"""

    # latest research
    s += f"""
  <section{' class="band"' if skin == 'light' else ''}>
{wrap_open(skin)}
{sec_head(skin, '01', 'Insights &amp; research', 'The measurements, in public.', 'Thirteen articles and a conference talk. Every number dated, every venue named.')}"""
    s += '      <div class="igrid igrid-3">\n' + "".join(insight_card(skin, x) for x in STUDIES[1:4]) + "      </div>\n"
    s += f"""      <div class="btn-row">
        <a class="btn {'btn-quiet' if skin == 'dark' else 'btn-ghost'}" href="writing.html">Explore all research &rarr;</a>
      </div>
    </div>
  </section>
"""

    # selected work
    s += f"""
  <section>
{wrap_open(skin)}
{sec_head(skin, '02', 'Work', 'Systems built and measured at production scale.', 'Named where the work is already public — through a conference talk, an article title, or a byline.')}"""
    s += "".join(case_block(skin, c) for c in CASES)
    s += f"""      <div class="btn-row">
        <a class="btn {'btn-quiet' if skin == 'dark' else 'btn-ghost'}" href="work.html">See client work &rarr;</a>
      </div>
    </div>
  </section>
"""

    # method
    s += f"""
  <section{' class="band"' if skin == 'light' else ''}>
{wrap_open(skin)}
{sec_head(skin, '03', 'Method', 'Measure, then architect, then leave the proof behind.', 'Most platform decisions get made on vendor documentation and what worked somewhere else. The result is architecture built on assumptions nobody tested.')}"""
    s += shapes_block(skin, METHOD)
    s += "    </div>\n  </section>\n"

    s += contact_section(skin)
    s += footer(skin)
    return s


def page_writing(skin):
    s = head(skin, "Insights &amp; research — Lakeside Analytics",
             "Thirteen published articles and a conference talk on Databricks and Snowflake benchmarking, agent architecture, and large-scale analytics applications.",
             "writing.html")
    s += header(skin, "writing.html")
    lede_html = lede("writing")
    if skin == "dark":
        s += f"""
  <section class="hero">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> Insights &amp; research</p>
      <h1>The measurements, in public.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section>
    <div class="container">
"""
        s += filter_bar(KINDS)
        s += '      <div class="igrid">\n'
        s += "".join(insight_card(skin, x) for x in STUDIES)
        s += "      </div>\n    </div>\n  </section>\n"
    else:
        s += f"""
  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">Insights &amp; research</span>
      <h1>The measurements, in public.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
""" + filter_bar(KINDS) + """      <div class="igrid">
"""
        s += "".join(insight_card(skin, x) for x in STUDIES)
        s += "      </div>\n    </div>\n  </section>\n"

    s += contact_section(skin, "Want this kind of measurement on your own platform?",
                         "The method behind these articles is the one we bring to client engagements.")
    s += footer(skin).replace("</body>", FILTER_JS + "</body>")
    return s


def page_work(skin):
    s = head(skin, "Client work — Lakeside Analytics",
             "Case studies from Mercedes, Capital One Software, and Molson Coors — trillion-row visualization, published benchmark programs, and warehouse-backed planning applications.",
             "work.html")
    s += header(skin, "work.html")
    lede_html = lede("work")
    if skin == "dark":
        s += f"""
  <section class="hero">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> Work</p>
      <h1>Systems built and measured at production scale.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section>
    <div class="container">
"""
    else:
        s += f"""
  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">Work</span>
      <h1>Systems built and measured at production scale.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
"""
    s += "".join(case_block(skin, c, full=True) for c in CASES)
    s += "    </div>\n  </section>\n"

    items = "\n".join(f"""        <div class="shape">
          <h3>{n}</h3>
          <p>{d}</p>
        </div>""" for n, d in ALSO_BUILT)
    grid_cls = "shapes shapes-2" if skin == "dark" else "grid grid-2"
    inner = items if skin == "dark" else "\n".join(f"""        <article class="card">
          <h3>{n}</h3>
          <p>{d}</p>
        </article>""" for n, d in ALSO_BUILT)
    s += f"""
  <section{' class="band"' if skin == 'light' else ''}>
{wrap_open(skin)}
{sec_head(skin, '02', 'Also built', 'Tools and applications without public write-ups.', 'Listed plainly, without metrics — there is no published source to cite for these.')}      <div class="{grid_cls}">
{inner}
      </div>
    </div>
  </section>
"""
    s += contact_section(skin)
    s += footer(skin)
    return s


def page_services(skin):
    s = head(skin, "Services — Lakeside Analytics",
             "Databricks and Snowflake platform architecture, compute benchmarking and cost optimization, custom analytics applications, and AI agents on the data platform.",
             "services.html")
    s += header(skin, "services.html")
    lede_html = lede("services")
    if skin == "dark":
        s += f"""
  <section class="hero">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> Services</p>
      <h1>Four practices. Each ends in something running.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section>
    <div class="container">
"""
        for p in PRACTICES:
            scope = "\n".join(f"            <li>{x}</li>" for x in p["scope"])
            s += f"""
      <article class="practice">
        <div>
          <p class="practice-idx"><span class="ix">{p['num']}</span> &middot; {p['area']}</p>
          <h3>{p['title']}</h3>
        </div>
        <div class="practice-body">
          <p>{p['body']}</p>
          <ul class="scope">
{scope}
          </ul>
        </div>
      </article>
"""
    else:
        s += f"""
  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">Services</span>
      <h1>Four practices. Each ends in something running.</h1>
      <p class="lede">{lede_html}</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
"""
        for p in PRACTICES:
            scope = "\n".join(f"            <li>{x}</li>" for x in p["scope"])
            s += f"""
      <article class="service">
        <div class="service-index">{p['num']} / {p['area']}</div>
        <div class="service-body">
          <h3>{p['title']}</h3>
          <p>{p['body']}</p>
          <ul class="checklist">
{scope}
          </ul>
        </div>
      </article>
"""
    s += "    </div>\n  </section>\n"

    s += f"""
  <section{' class="band"' if skin == 'light' else ''}>
{wrap_open(skin)}
{sec_head(skin, '02', 'Engagement model', 'Three ways to start.')}"""
    s += shapes_block(skin, SHAPES)
    s += "    </div>\n  </section>\n"
    s += contact_section(skin, "Describe the problem — that&rsquo;s enough to start.",
                         "A paragraph about what your platform is doing, or should be doing, is plenty for a first conversation. We will tell you honestly if it isn&rsquo;t work we should take.")
    s += footer(skin)
    return s


def page_about(skin):
    a = ABOUT
    s = head(skin, "About — Lakeside Analytics",
             "Lakeside Analytics is the consulting practice of Sachin Seth, a data platform architect working on Databricks and Snowflake since 2021.",
             "about.html")
    s += header(skin, "about.html")
    body = "\n".join(f"        <p>{p}</p>" for p in a["body"])
    facts = "\n".join(f"""          <div class="fact">
            <span class="fact-k">{k}</span>
            <span class="fact-v">{v}</span>
          </div>""" for k, v in a["facts"])
    ed = a["education"]
    venues = "".join(f"<li>{v}</li>" for v in a["venues"])

    if skin == "dark":
        s += f"""
  <section class="hero">
    <div class="container">
      <p class="eyebrow"><span class="ix">&#8212;</span> About</p>
      <h1>A practice built on measurement.</h1>
      <p class="lede">{lede("about")}</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="about-grid">
        <div class="about-body">
{body}
        </div>
        <aside class="about-facts">
{facts}
        </aside>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
{sec_head(skin, '02', 'Background', 'Education and byline.')}      <div class="about-grid">
        <div class="about-body">
          <h3 class="ed-degree">{ed['degree']}</h3>
          <p class="ed-school">{ed['school']} &middot; {ed['years']}</p>
          <p>{ed['note']}</p>
        </div>
        <aside class="about-facts">
          <div class="fact">
            <span class="fact-k">Published at</span>
            <ul class="venue-list">{venues}</ul>
          </div>
        </aside>
      </div>
    </div>
  </section>
"""
    else:
        s += f"""
  <section class="hero">
    <div class="wrap">
      <span class="eyebrow">About</span>
      <h1>A practice built on measurement.</h1>
      <p class="lede">{lede("about")}</p>
    </div>
  </section>

  <section style="padding-top:0">
    <div class="wrap">
      <div class="about-grid">
        <div class="about-body prose">
{body}
        </div>
        <aside class="about-facts">
{facts}
        </aside>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap">
{sec_head(skin, '02', 'Background', 'Education and byline.')}      <div class="about-grid">
        <div class="about-body prose">
          <h3 class="ed-degree">{ed['degree']}</h3>
          <p class="ed-school">{ed['school']} &middot; {ed['years']}</p>
          <p>{ed['note']}</p>
        </div>
        <aside class="about-facts">
          <div class="fact">
            <span class="fact-k">Published at</span>
            <ul class="venue-list">{venues}</ul>
          </div>
        </aside>
      </div>
    </div>
  </section>
"""
    s += contact_section(skin)
    s += footer(skin)
    return s


def page_404(skin):
    s = head(skin, "Page not found — Lakeside Analytics", "", "404.html")
    s = s.replace('<meta name="description" content="">', '<meta name="robots" content="noindex">')
    s += header(skin, "")
    open_ = wrap_open(skin)
    s += f"""
  <section class="hero">
{open_}
      {'<p class="eyebrow"><span class="ix">&#8212;</span> 404</p>' if skin == 'dark' else '<span class="eyebrow">404</span>'}
      <h1>That page isn&rsquo;t here.</h1>
      <p class="lede">The link may be out of date. Everything on this site lives under one of the sections below.</p>
      <div class="btn-row">
        <a class="btn" href="/">Home</a>
        <a class="btn {'btn-quiet' if skin == 'dark' else 'btn-ghost'}" href="writing.html">Insights</a>
        <a class="btn {'btn-quiet' if skin == 'dark' else 'btn-ghost'}" href="work.html">Work</a>
      </div>
    </div>
  </section>
"""
    s += footer(skin)
    return s


PAGES = {
    "index.html": page_index,
    "writing.html": page_writing,
    "work.html": page_work,
    "services.html": page_services,
    "about.html": page_about,
    "404.html": page_404,
}

if __name__ == "__main__":
    for skin, root in (("light", LIGHT), ("dark", DARK)):
        for name, fn in PAGES.items():
            open(os.path.join(root, name), "w", encoding="utf-8").write(fn(skin))
        print(f"{skin:5s} -> {root}  ({len(PAGES)} pages)")
