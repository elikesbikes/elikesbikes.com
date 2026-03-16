---
title: "linux_dotfiles"
description: "My personal Linux config files — modular, explicit, and built for people who want to understand their own setup."
date: 2025-11-04T00:00:00-08:00
type: "repo"
github_url: "https://github.com/elikesbikes/linux_dotfiles"
tech: ["Shell", "Bash", "Lua", "Neovim"]
---

A curated set of Linux configuration files built around one principle: explicit over clever. No automated installers — clone it, read it, and copy what makes sense for your setup.

## What's Configured

- **Shell** — modular Bash config split across `.bash/`, with clean separation of aliases, functions, and env vars
- **Neovim** — Lua-based config using Lazy.nvim for plugin management
- **Terminal** — consistent look and feel across Kitty, Alacritty, and Starship prompt
- **Environment** — documented `.env` structure for managing environment variables across machines

## How to Use

1. Clone the repo
2. Browse the files — don't copy blindly
3. Symlink or copy the configs you want into your home directory

The repo is organized by tool, so it's easy to grab just the pieces you need without pulling in everything else.

## Who It's For

Linux power users, systems engineers, and homelab nerds who value understanding their tools. If you want a one-click install script, this isn't it. If you want configs you can actually read and modify, start here.
