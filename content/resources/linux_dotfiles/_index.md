---
title: "linux_dotfiles"
description: "My personal Linux config files — modular, explicit, and built for people who want to understand their own setup."
date: 2025-11-04T00:00:00-08:00
type: "repo"
github_url: "https://github.com/elikesbikes/linux_dotfiles"
tech: ["Shell", "Bash", "Lua", "Neovim"]
folders:
  - name: ".bash"
    description: "Core Bash config split into focused files — aliases, functions, misc, and Starship shell prompt integration."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/.bash"
  - name: ".config"
    description: "App configs for Neovim, Alacritty, Kitty, Starship, Eza, Fastfetch, Neofetch, and VeraCrypt."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/.config"
  - name: "scripts"
    description: "Utility and automation scripts — Linux system tools, UniFi, Proxmox, TrueNAS, Restic, and onboarding."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/scripts"
  - name: "sudoers"
    description: "Modular sudoers configuration split by concern — defaults, admin, diagnostics, filesystem, and scripts."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/sudoers"
  - name: "exports"
    description: "Exported system configs including dconf settings for media keys and keyboard bindings."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/exports"
  - name: ".local"
    description: "Omakub framework bash defaults — aliases, functions, prompt, inputrc, and shell init files."
    url: "https://github.com/elikesbikes/linux_dotfiles/tree/main/.local"
---

A curated set of Linux configuration files built around one principle: explicit over clever. No automated installers — clone it, read it, and copy what makes sense for your setup.

## How to Use

1. Clone the repo
2. Browse the files — don't copy blindly
3. Symlink or copy the configs you want into your home directory (uses GNU Stow)

## Who It's For

Linux power users, systems engineers, and homelab nerds who value understanding their tools. If you want a one-click install script, this isn't it. If you want configs you can actually read and modify, start here.
