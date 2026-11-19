# CLAUDE.md — elikesbikes.com

Project context and conventions for AI-assisted development on this site.
Revision: 2026-11-18 (elegance pass inside the Interstellar theme; see Revision history at the end). Previous: 2026-11-09 (static/mcc/avatars: MCC Discord post pictures).

---

## What This Site Is

Personal website for Emmanuel Loaiza (tars) — a homelab nerd, tech content creator, and cyclist.
Live at: **https://elikesbikes.com**

Stack: **Hugo** (v0.151.0 extended) + **Blowfish theme** (v2.90.0, Go module) + **Cloudflare Workers** (via Wrangler)

**Repo location:** `~/devops/projects/elikesbikes.com` (git repo lives here since 2026-10-25;
`~/devops/github/elikesbikes.com` is a stale copy without `.git`).

**Remotes:** `origin` fetches from GitHub and pushes to BOTH
`github.com/elikesbikes/elikesbikes.com` (primary — Cloudflare builds from it) and
`gitlab.home.elikesbikes.com/ecloaiza/elikesbikes.com` (secondary mirror). Commit with
`gacp_elikesbikes "message"`; Claude Code hooks auto-commit after edits.

**Every commit here is a production deploy, and the hooks commit on their own.** A PostToolUse hook
(after each Edit/Write to a file in this folder) and a Stop hook (when any Claude session on this machine
ends a turn) run `gacp_elikesbikes`, which pushes `main`, which Cloudflare builds and publishes. So:

- **Never run `hugo server` or `hugo` inside this folder while working.** Both write into `public/`, which
  is still tracked, and the next hook pushes it. On 2026-11-18 a preview server did exactly that: commit
  3d8f583 put dev-server pages (localhost URLs, livereload) into the tracked `public/` (production was not
  affected, Cloudflare rebuilds from source).
- **Multi-file changes: work in a copy, land once.** `rsync -a --exclude .git --exclude public` the repo to
  a scratch folder, edit and preview there (`hugo server --renderToMemory`), then copy the finished files
  back with one shell command that ends in `gacp_elikesbikes "message"`. One commit, one deploy, nothing
  half-finished live.

---

## Look: Interstellar console theme (dark only)

The site uses the owner's "Interstellar" theme, shared with MCC/Cooper. Never invent a new look.

- Tokens: bg `#06080b` · panel `#161a21` · raised `#212731` · border `#2b313b` · accent amber `#f0a23b`
  (dim `#b87723`) · data blue `#9fc4e8` · teal `#5fb3a1` · text `#e6e8ec` · muted `#8a909c`.
- Type: **Inter** for prose; **IBM Plex Mono** uppercase + wide tracking for labels, dates, tags, nav, buttons.
- Wordmark `ELIKESBIKES` in amber mono with glow (site title, styled by CSS).
- Faint amber/blue radial glows (a fixed, viewport-sized `body::before` layer, so they never show the edge
  of Blowfish's 1280px column); blurred fixed header; cards lift + amber border and glow on hover.
- Details added 2026-11-18, all in `custom.css`: the header sits on the same column as the page content at
  every width; the current section is underlined in the nav; section labels are an amber dash, the label
  and a hairline that fades out; the rule under a page title starts with a short amber segment; page
  content rises in once on load (off under `prefers-reduced-motion`); long text is capped near 68 characters.

Where it lives:

| File | Purpose |
|---|---|
| `assets/css/schemes/interstellar.css` | Blowfish color scheme (neutral/primary/secondary ladders → Interstellar) |
| `assets/css/custom.css` | Everything else: tokens, fonts, Blowfish overrides, all component classes |
| `layouts/partials/extend-head.html` | Google Fonts (Inter, IBM Plex Mono), theme-color, forces `dark` class |
| `layouts/partials/extend-footer.html` | Tiny script: sets `aria-current` on the nav links of the current section (Blowfish renders no active state) |
| `config/_default/params.toml` | `colorScheme = "interstellar"`, `defaultAppearance = "dark"`, switcher off |

**No inline styles in layouts.** Use the classes in `custom.css` (`.page`, `.page-head`, `.card`,
`.card-title`, `.pill`, `.btn`, `.btn-row`, `.section-head`, `.mono`, `.when`, grids `.grid-videos` etc.).
Helper tokens next to the theme colors: `--prose` (body copy), `--hairline` (dividers inside a surface),
`--glow` (accent as `r, g, b` for `rgba()`), `--ease-out`. Blowfish's utilities are in `@layer utilities`,
so plain rules in `custom.css` already win; add `!important` only where Blowfish uses it too.

---

## Project Structure

```
config/_default/
  config.toml           baseURL, title ("elikesbikes"), theme
  hugo.toml             outputs (home JSON for search), taxonomies, related
  languages.en.toml     author name/headline/bio/links — single source for the headline
  menus.en.toml         Videos · Resources (Homelab, Tutorials, Linux Dotfiles) · Tags · About
  params.toml           Blowfish params (scheme, appearance, search, header, footer)

assets/
  css/custom.css, css/schemes/interstellar.css
  icons/*.svg           Simple Icons SVGs (youtube, github, discord, strava, trainerroad)
  images/profile.jpg    Source photo; Hugo crops/resizes to webp via profile-image.html

data/
  social.yaml           Social links (name, handle, url, icon, color) for home + about
  resources.yaml        Repo metadata used by scripts

content/
  _index.md             Home: bio body + recent_project frontmatter
  about/_index.md       About (layout in layouts/about/list.html)
  videos/<slug>/index.md  youtube_id, tags, description (scripts/fetch_youtube.ym)
  resources/<repo>/_index.md  type: "repo" pages (+ tutorials/docker-compose subpage)
  search/_index.md      layout: "search" (required by Blowfish search)

layouts/
  index.html            Home: hero (avatar, name, headline, stats), bio, social chips, recent project
                        (picture beside the words; stacked under 820px), latest 3 videos
  404.html              "Page not found" in the site's look (Cloudflare serves it: wrangler.toml not_found_handling)
  videos/list.html      Header + video grid
  videos/single.html    Embedded player (youtube-nocookie), tags link to /tags/
  repo/list.html        Repo header, tech pills, GitHub button, folder grid
  resources/list.html   Repo cards
  about/list.html       Hero + bio sections (label column beside the text) + social tiles
  _default/list.html    Generic list (rows)
  _default/terms.html   /tags/ as pill cloud with counts
  _default/term.html    /tags/<tag>/ reuses the video grid
  partials/
    video-card.html     One video card (maxresdefault thumb with hqdefault fallback)
    social-links.html   Renders data/social.yaml ("chips" or "cards" variant)
    headline.html       Author headline split on " · " into spans: one line on wide screens, one phrase per line on phones
    extend-footer.html  Marks the current section in the nav (aria-current)
    brand-icon.html     Inlines assets/icons/<name>.svg with optional color/size
    profile-image.html  Processed avatar (Fill, webp, 1x/2x)
    favicons.html       Favicon override (Blowfish checks for this partial first)
    extend-head.html    Fonts + dark lock

static/                 favicons, images/projects/*.svg (recent project thumbnails, drawn in the Interstellar
                        palette; shown through <img>, so text inside them falls back to the system monospace)
  mcc/avatars/*.png     Pictures MCC's Discord posts show (one per agent). Not part of the site's pages:
                        Discord downloads them from https://elikesbikes.com/mcc/avatars/<slug>.png, so they
                        must stay at these paths. Source SVGs and the export command live in the MCC repo
                        (shared/discord_avatars/, docs/discord.md); MCC's registry check `discord-avatars`
                        alerts if one stops loading. Added 2026-11-09.
scripts/                fetch_youtube.ym, fetch_github_repos.py
```

Blowfish is loaded as a Hugo module only (`config/_default/module.toml` + `go.mod` pinning v2.90.0).
There is no `themes/` directory and no `theme =` line in `config.toml`; keep it that way. A stale
`themes/blowfish` submodule pointer without `.gitmodules` broke every Cloudflare build until 2026-10-25
("error occurred while updating repository submodules" at clone time).
Do not run bare `hugo mod get` — it upgrades Blowfish past what Hugo 0.151 supports. Pin with
`hugo mod get github.com/nunocoracao/blowfish/v2@v2.90.0` if it drifts.

---

## Content Conventions

- **Headline** lives once in `languages.en.toml` (`params.author.headline`) and is used on home + about.
- **Videos**: thumbnails and titles open YouTube; the small "details →" opens the on-site page.
  Tags link to `/tags/<tag>/`. Video titles come from YouTube (fix bad titles there, then re-sync).
- **Resources**: `type: "repo"` + `folders:` list. External `url` → "Open in GitHub ↗", internal → "View details →".
- **Recent project**: `recent_project` in `content/_index.md`; thumbnail SVG in `static/images/projects/`.
- **Social links**: edit `data/social.yaml`, never the layouts. New icon → drop the Simple Icons SVG in `assets/icons/`.

---

## Local Development

```bash
# In a scratch COPY of the repo, never in this folder (see "Every commit here is a production deploy"):
hugo server --renderToMemory   # http://localhost:1313  (Hugo 0.151.0 ext in ~/.local/bin, Go via mise)
./build.sh                     # what Cloudflare runs: installs Hugo EXTENDED 0.151.0, hugo --gc --minify → ./public/
```

Open the preview as `localhost:1313`, not `127.0.0.1:1313`: search loads its index from the base URL and
the browser blocks it across the two names.

Deploy is automatic: a push to GitHub `main` triggers Cloudflare Workers Builds, which runs
`npx wrangler deploy`; wrangler runs `./build.sh` (`[build] command` in `wrangler.toml`) and uploads
`./public`. Hugo **extended** is required because `profile-image.html` writes WebP; the standard binary
fails with "error calling Fill: this feature is not available in your current Hugo version". A local
build can hide that behind the `resources/_gen/` cache, so verify in a fresh clone. Build status: the
"Workers Builds: elikesbikes" check on the GitHub commit; logs via the Cloudflare builds API (see the
elikesbikes-website skill).

Hugo server must be restarted after adding a new top-level directory (e.g. `assets/`) — the
watcher only follows directories that existed at startup.

---

## Known Gaps / Backlog

- No Open Graph image yet (`static/images/cover.jpg` referenced historically but missing).
- `public/` is tracked in git from the old setup; the CSS bundles and processed images are now
  ignored, the rest could be `git rm --cached` (confirmed 2026-10-25: Cloudflare builds from source).
- Mobile layout verified in headless Chromium at 390, 500, 700, 820 and 900px (2026-11-18), not on a real
  phone; Safari and Firefox not checked.
- Every build logs `WARN Module "github.com/nunocoracao/blowfish/v2" is not compatible with this Hugo
  version: 0.141.0/0.150.0 extended`: Blowfish v2.90.0 declares Hugo 0.150.0 as its newest, the site builds
  with 0.151.0. Blowfish v2.91.0 declares 0.151.0 (its `config.toml`), untested here. In the Findings Backlog.

---

## Revision history

| Date | Commit | Change |
|---|---|---|
| 2026-10-25 | b825b35 | Interstellar restyle; repo moved to `~/devops/projects`; GitLab mirror. |
| 2026-11-09 | b4bc5e3 | `static/mcc/avatars`: MCC Discord post pictures. |
| 2026-11-18 | (this commit) | Elegance pass, theme unchanged: glow layer without seams, header on the content column, current section marked in the nav, section labels with a rule, home project card with the picture beside the words and the n8n picture redrawn in the palette (its labels no longer overlap the icons), about page with a label column and a single row of social tiles, headline that wraps by phrase, video cards with tags on one line across a row, amber search focus, own 404 page, entrance motion. Tested: production build (61 pages, same single Blowfish warning as before); headless Chromium screenshots of every page type at 1440px plus 390-900px; dropdown, search, phone menu, card hover, scrolled header; no horizontal scroll and no script errors. Not tested: real phones, Safari, Firefox. |
