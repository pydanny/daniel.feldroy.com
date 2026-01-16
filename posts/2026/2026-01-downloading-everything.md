---
date: '2026-01-16T11:22:35.582258+00:00'
description: Using AI to help download photos so we can consolidate all our images into one place.
published: true
tags:
- python
title: Writing tools to download everything
---

Over the years, [Audrey](https://audrey.feldroy.com) and I have accumulated photos across a variety of services. Flickr, SmugMug, and others all have chunks of our memories sitting on their servers. Some of these services we haven't touched in years, others we pay for but rarely use. It was time to bring everything home.

## Why Bother?

Two reasons pushed me to finally tackle this.

First, money. Subscriptions add up. Paying for storage on services we barely use felt wasteful. As a backup even more so because there are services that are cheaper and easier to use for that purpose, like Backblaze.

Second, simplicity. Having photos scattered across multiple services means hunting through different interfaces when looking for a specific memory. Consolidating everything into one place makes our photo library actually usable.

## Using Claude to Write a Downloader

I decided to start with SmugMug since that had the largest collection. I could have written this script myself. I've done plenty of API work over the years. But I'm busy, and this felt like a perfect use case for AI assistance.

My approach was straightforward:

1. **Wrote a specification** for a Smugmug downloader. I linked to the docs for the service then told it to make a CLI for downloading things off that service. For the CLI I insist on `typer` but otherwise I didn't specify dependencies.

2. **Told Claude to generate code** based on the spec. I provided the specification and let Claude produce a working Python script.

3. **Tested** by running the scripts against real data. I started with small batches to verify the downloads worked correctly. Claude got everything right when iy came to downloads on the first go, which was impressive.

4. **Adjust for volume**. We had over 5,000 files on Smugmug. Downloading everything at once took longer than I expected. I asked Claude to track files so if the script was interrupted it could resume where it left off. Claude kept messing this up, and after the 5th or 6th attempt I gave up trying to use Claude to write this part.

## I Wrote Some Code

I wrote a super simple image ID cache using a plaintext file for storage. It was simple, effective, and worked on the first go. Sometimes it's easier to just write the code yourself than try to get an AI to do it for you.

## The SmugMug Downloader

The project is here at [SmugMug downloader](https://github.com/pydanny/smugmug-downloader). It authenticates, enumerates all albums, and downloads every photo while preserving the album structure. Nothing fancy, just practical.

I'll be working on the Flickr downloader soon, following the same pattern. There's a few other services on the list too; I'm scanning our bank statements to see what else we have accounts on that we've let linger for too long.

## Was It Worth It?

Absolutely. What would have taken me a day of focused coding took an hour of iterating with Claude. Our photos are off Smugmug and we're canceling a subscription we no longer need. I think this is what they mean by "vibe engineering".

## Summary

These are files which in some cases we thought we lost. Or had forgotten. So the emotional and financial investment in a vibe engineered effort was low. If this were something that was touching our finances or wedding/baby photos I would have been much more cautious. But for now, this is a fun experiment in using AI to handle the mundane parts of coding so I can focus on more critical tasks.
