---
date: '2026-03-05T07:30:50.970143+00:00'
description: The tools I use in my day-to-day coding efforts in early 2026.
published: true
tags:
- python
- tools 
- terminal
title: Top Terminal Tools
---

When I sit down to code, these are the tools I use at this time whenever I touch code. In alphabetical order:

## [Atuin](https://atuin.sh/)

Atuin is a replacement for the default shell history. It saves your history to a local, encrypted SQLite database. Then it allows for blazing fast searches. You can sync your history across devices, and is has a lot of other features. I can't imagine using a terminal without Atuin.

For OSX users, I recommend installing following [these instructions](https://docs.atuin.sh/cli/#quickstart).

## [bat](https://github.com/sharkdp/bat)

A Rust-based cat replacement. It has syntax highlighting, line numbers, and a lot of other features that make it a great tool for quickly looking at files in the terminal.


## [Ghostty](https://ghostty.org/)

Ghostty is a fast, feature-rich, and cross-platform terminal emulator that I believe works everywhere. Yes, TMUX (and competitors) are more configurable and have more features, but **Ghostty just works out of the box**. Ghostty eschews the arcane key combinations of its predecessors in favor of intuitive keybindings. A ghostty terminal can be split horizontally and vertically and copy/paste works as expected. It also doesn't appear to interfere with any other shell tool, something that annoyed me about TMUX.

Usually I have three vertical panels:

1. On the far left a panel for running general shell commands like git, uv, and whatever. [Atuin](https://atuin.sh) is a must for me, giving me shell history on steriods so I don't have to remember commands anymore
2. In the middle I run a CLI-based text editor, these days usually [pad](https://github.com/feldroy/pad)
3. On the righthand side a panel for running LLM CLI tools, usually AMP, Codex, and sometimes Claude

## [GitHub CLI](https://cli.github.com/)

Even though I use a fraction of the available commands, this is just a really useful tool for working on GitHub-hosted projects. 

## [Pad](https://github.com/feldroy/pad)

Pad is an easy-to-use terminal editor I created for those of us who aren't into vim. It's powered by [Will McGugan's Textual](https://textual.textualize.io/). I did what I can to make pad work with typical VS Code keybindings. 

Right now I'm not accepting general contributions to Pad. I am still recovering from a [head injury](https://daniel.feldroy.com/tags/concussion) and that unfortunately makes reviewing PRs challenging. As I get better I plan to put more features into the project and perhaps even accept contributions. For now it does what I need it to do and is a handy addition to my tool chain.

## Various LLM CLI tools

I have no loyalty to any particular LLM provider. I use whatever tool gets the job done and for which I have free or affordable credits. For now I use:

- Amp
- ChatGPT Codex
- Claude Code

For a while I was using gemini-cli, but it stopped working for me weeks ago. Rather than try to debug it I just used the competition.