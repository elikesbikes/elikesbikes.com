---
title: "tutorials"
description: "Working Docker Compose stacks, the Traefik edge, and the scripts and pipeline that deploy them across my homelab."
date: 2025-11-04T00:00:00-08:00
type: "repo"
github_url: "https://github.com/elikesbikes/tutorials"
tech: ["Docker", "Traefik", "GitLab CI", "Shell", "Python"]
folders:
  - name: "docker-compose"
    description: "51 production-ready Docker Compose stacks — Nextcloud, Graylog, n8n, Jellyfin, Wazuh, GitLab, Immich, and more."
    url: "/resources/tutorials/docker-compose/"
  - name: "infra"
    description: "The Traefik reverse-proxy project: env-driven, multi-host (tars, rocky, hailmary), Cloudflare DNS-01 TLS."
    url: "https://github.com/elikesbikes/tutorials/tree/main/infra"
  - name: "infra-snapshots"
    description: "Captured Traefik snapshots used to verify a host before and after a deploy."
    url: "https://github.com/elikesbikes/tutorials/tree/main/infra-snapshots"
  - name: "scripts"
    description: "Deploy, sync, snapshot and validate helpers — validate-compose.sh, sync-traefik.sh, traefik_smoke.py, deploy-endurance.sh."
    url: "https://github.com/elikesbikes/tutorials/tree/main/scripts"
  - name: "PIPELINE.md"
    description: "How the GitLab CI pipeline validates and deploys stacks: tars edits → rocky (dev) → hailmary (prod)."
    url: "https://github.com/elikesbikes/tutorials/blob/main/PIPELINE.md"
---

A growing collection of working configs and reference templates I use across my homelab and projects. Organized by topic — grab the folder you need and adapt it.
