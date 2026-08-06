# lakesideanalytics.io

Marketing site for Lakeside Analytics. Plain static HTML/CSS, no build step, served by
GitHub Pages — the same arrangement as `lakecode.ai`.

## Structure

```
index.html      Home — positioning, four practices, how we work, selected work, CTA
services.html   Services — the four practices in detail + engagement model
writing.html    Writing — published work (Capital One Software, Plotly, Databricks SME)
404.html        Not-found page (GitHub Pages serves this automatically)
styles.css      The whole design system. One file, CSS custom properties.
favicon.svg
CNAME           Custom domain for GitHub Pages
.nojekyll       Skip Jekyll processing
robots.txt / sitemap.xml
```

There is no framework, no `node_modules`, and no build. Edit the HTML, commit, push —
GitHub Pages redeploys in about a minute.

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

GitHub Pages, custom domain `lakesideanalytics.io`.

DNS for the domain is on **Google Domains** nameservers (`ns-cloud-d*.googledomains.com`),
not Cloudflare. The records GitHub Pages needs:

| Type  | Name  | Value                                                    |
|-------|-------|----------------------------------------------------------|
| A     | `@`   | `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` |
| CNAME | `www` | `sachds.github.io.`                                       |

Both were already in place before this site existed.

`sachin.lakesideanalytics.io` is a separate GitHub Pages site from the
`sachds/lakesideanalytics-website` repo. It is unaffected by this one — different
subdomain, different repo.

### Enabling Pages on a fresh clone

Settings → Pages → Source: `main` / root, then set the custom domain to
`lakesideanalytics.io` and wait for the certificate to provision (usually minutes; up to
an hour). Tick **Enforce HTTPS** once it is available.
