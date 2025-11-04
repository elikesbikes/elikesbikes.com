#!/usr/bin/env python3
"""
scripts/fetch_github_repos.py
Writes a small markdown list of repositories to content/resources/_repos.md
"""
import os, requests, pathlib, time

USER = "elikesbikes"  # from config or change here
OUTFILE = pathlib.Path("content/resources/_repos.md")
OUTFILE.parent.mkdir(parents=True, exist_ok=True)

headers = {}
token = os.environ.get("GITHUB_TOKEN")
if token:
    headers["Authorization"] = f"token {token}"

repos = []
page = 1
while True:
    r = requests.get(f"https://api.github.com/users/{USER}/repos", params={"per_page":100, "page":page}, headers=headers)
    r.raise_for_status()
    data = r.json()
    if not data:
        break
    repos.extend(data)
    page += 1
    time.sleep(0.1)

repos_sorted = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)
md = "# Repositories\n\n"
for r in repos_sorted:
    md += f"- [{r['name']}]({r['html_url']}) — {r.get('description') or ''}\n"

OUTFILE.write_text(md, encoding="utf-8")
print("Wrote", OUTFILE)
