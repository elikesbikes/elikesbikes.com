# CLAUDE.md — elikesbikes.com

Project context and conventions for AI-assisted development on this site.
Revision: 2026-10-25 (Interstellar restyle, repo moved to ~/devops/projects, GitLab mirror).

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

---

## Look: Interstellar console theme (dark only)

The site uses the owner's "Interstellar" theme, shared with MCC/Cooper. Never invent a new look.

- Tokens: bg `#06080b` · panel `#161a21` · raised `#212731` · border `#2b313b` · accent amber `#f0a23b`
  (dim `#b87723`) · data blue `#9fc4e8` · teal `#5fb3a1` · text `#e6e8ec` · muted `#8a909c`.
- Type: **Inter** for prose; **IBM Plex Mono** uppercase + wide tracking for labels, dates, tags, nav, buttons.
- Wordmark `ELIKESBIKES` in amber mono with glow (site title, styled by CSS).
- Faint amber/blue radial glows on body; blurred fixed header; cards lift + amber border on hover.

Where it lives:

| File | Purpose |
|---|---|
| `assets/css/schemes/interstellar.css` | Blowfish color scheme (neutral/primary/secondary ladders → Interstellar) |
| `assets/css/custom.css` | Everything else: tokens, fonts, Blowfish overrides, all component classes |
| `layouts/partials/extend-head.html` | Google Fonts (Inter, IBM Plex Mono), theme-color, forces `dark` class |
| `config/_default/params.toml` | `colorScheme = "interstellar"`, `defaultAppearance = "dark"`, switcher off |

**No inline styles in layouts.** Use the classes in `custom.css` (`.page`, `.page-head`, `.card`,
`.card-title`, `.pill`, `.btn`, `.section-head`, `.mono`, `.when`, grids `.grid-videos` etc.).

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
  index.html            Home: hero (avatar, name, headline, stats), bio, social chips, recent project, latest 3 videos
  videos/list.html      Header + video grid
  videos/single.html    Embedded player (youtube-nocookie), tags link to /tags/
  repo/list.html        Repo header, tech pills, GitHub button, folder grid
  resources/list.html   Repo cards
  about/list.html       Hero + bio sections + social cards
  _default/list.html    Generic list (rows)
  _default/terms.html   /tags/ as pill cloud with counts
  _default/term.html    /tags/<tag>/ reuses the video grid
  partials/
    video-card.html     One video card (maxresdefault thumb with hqdefault fallback)
    social-links.html   Renders data/social.yaml ("chips" or "cards" variant)
    brand-icon.html     Inlines assets/icons/<name>.svg with optional color/size
    profile-image.html  Processed avatar (Fill, webp, 1x/2x)
    favicons.html       Favicon override (Blowfish checks for this partial first)
    extend-head.html    Fonts + dark lock

static/                 favicons, images/projects/*.svg (recent project thumbnails)
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
hugo server -D            # http://localhost:1313  (Hugo 0.151.0 ext in ~/.local/bin, Go via mise)
./build.sh                # what Cloudflare runs: hugo --gc --minify → ./public/
wrangler deploy           # Cloudflare Workers (wrangler.toml)
```

Hugo server must be restarted after adding a new top-level directory (e.g. `assets/`) — the
watcher only follows directories that existed at startup.

---

## Known Gaps / Backlog

- No Open Graph image yet (`static/images/cover.jpg` referenced historically but missing).
- `public/` is tracked in git from the old setup; the CSS bundles and processed images are now
  ignored, the rest could be `git rm --cached` once confirmed Cloudflare builds from source.
- Mobile layout verified only via CSS breakpoints, not on a device.
