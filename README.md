# lakesideanalytics.io

Marketing site for Lakeside Analytics. Plain static HTML/CSS, no build step, served by
GitHub Pages — the same arrangement as `lakecode.ai`.

## Structure

```
index.html      Home — featured study, stats, latest research, work, method
writing.html    Insights & research — all 13 articles + the DAIS talk, typed and dated
work.html       Client work — Mercedes, Capital One, Molson Coors + tools without write-ups
services.html   Services — four practices + engagement model
about.html      About — the practice, background, education
404.html        Not-found page
styles.css      The whole design system. One file, CSS custom properties.
_build/         Page generator. See below — do NOT hand-edit the HTML.
```

## The HTML is generated

Both this build and the dark build (`../lakeside-analytics-dark`) render from one
content model, so their copy cannot drift apart. Edit `_build/content.py`, then:

```bash
python3 _build/build.py
```

That rewrites all six pages in **both** repos. Hand-editing the HTML works until the next
regeneration silently reverts it.

`_build/content.py` holds every study, case, practice, and stat. Each figure in it traces
to a published source; if you add one, check it against the linked article first.

## Local preview

```bash
python3 -m http.server 4321
```

Then open <http://localhost:4321>.

## Design notes

All color, spacing, and type values live as custom properties in `:root` at the top of
`styles.css`, with a `prefers-color-scheme: dark` block overriding them. Light and dark
both ship — change a token once and both themes follow. There are no external font or
script requests, so the site loads with a single CSS round-trip.

Conventions worth keeping:

- **One accent.** Lake teal (`--accent`), used for primary buttons, the mark, and link
  hover. Everything else is the neutral ramp. Adding a second accent will make the site
  look generic fast.
- **`.eyebrow`** — mono, uppercase, letterspaced — labels every section.
- **`.grid`** auto-fits to 3 columns; **`.grid-2`** is for four-card sections so they lay
  out 2×2 instead of 3 plus an orphan.
- Claims in the copy are tied to published work. If you add a metric, it should trace to
  something on the writing page.

## Hosting

**Cloudflare Pages**, project `lakeside-analytics`.

Deploy from this directory:

```bash
wrangler pages deploy . --project-name lakeside-analytics --branch main
```

Live at `lakeside-analytics.pages.dev`. Cloudflare serves extensionless URLs
(`/services`, `/writing`) and 308-redirects the `.html` forms to them; `404.html` is
picked up automatically as the not-found page.

There is no `CNAME` file — that is a GitHub Pages artifact. Custom domains are attached
to the Pages project, not committed to the repo.

### Custom domain

`lakesideanalytics.io` is registered at **Squarespace**; DNS currently runs on the legacy
Google Domains nameservers (`ns-cloud-d*.googledomains.com`). Cloudflare Pages cannot
serve an apex domain unless the zone is on Cloudflare, because that provider has no
ALIAS/ANAME support at the apex — so the nameservers have to move.

The zone also carries Google Workspace email (5 MX, SPF, and a `google._domainkey` DKIM
split across 3 DNS chunks) plus a `sachin` CNAME for the portfolio. All of it must be
recreated on Cloudflare *before* the nameserver switch or mail breaks.

GitHub Pages was tried first and abandoned: the `pages-build-deployment` job never got a
runner. Pages is now disabled on this repo and its domain claim released.
