---
date: '2025-09-24T00:45:00.884329+00:00'
description: A retrospective of over twenty years worth of writing tools that I've used to write online.
published: true
tags:
- blog
- python
- flask
- Vue.js
- react
- air
title: Over Twenty Years of Writing Tools
---

On my [articles page](/articles), you can read near the top that I've been writing for the past 20 years (plus a little more). It's not all my online public writing, but it's a majority of it. The primary reason parts are missing is that over time, I've used a variety of tools to publish my thoughts. Some of those tools were hosted services, and material that was lost was because of services being shut down. Hence, why I prefer markdown files in a git repository over a database solution. 

Here's the story of my writing tools over the years.

## Geocities 1997-2010

In 1997, I first remember writing something for general publication on the web. Until then, my writings had been transmitted by printing paper, hand-copying onto disks, sending by email, or posting to usenet. I think it was in 1997 that I made my first essay-style writing on [GeoCities](https://en.wikipedia.org/wiki/GeoCities) site I put together. Geocities is gone, but periodically I've thought of digging through GeoCities archives to find my writing from that time between 1997 and 2004. Otherwise, those articles are gone.

Even though there's nothing from that time on this site, as Geocities overlaps with the first entry on this site, I've included it for the sake of posterity.

## Livejournal 2004-2009

From 2004 to 2009, I used LiveJournal to put down my thoughts, and there I wrote on a regular basis about life, activities, fitness, coding, and general work stuff. When I revisit those posts, I see some fun things, some hard challenges, and between the lines a lot carefully hidden despair. The few articles that made it onto this site capture extended family memories.

[Some of the articles from LiveJournal exist here](https://daniel.feldroy.com/tags/legacy-livejournal).

## Blogger 2007-2012

In 2007, blogs had taken off, and it was clear that professionally having my own blog was important. I decided to keep things simple and use Blogger to host my [first professional blog](https://pydanny.blogspot.com/). I opened a few other blogger sites for other purposes, but the main one was [PyDanny](https://pydanny.blogspot.com/. 

This was my formative years of Python (and Django). Everything was bright and shiny and new. I met [Audrey](https://audrey.feldroy.com) and fell in love with her.

A few years ago, I migrated that content [here on this page](https://daniel.feldroy.com/tags/legacy-blogger).

## Pelican 2012-2018

In 2012, I started writing content on a [Pelican](https://docs.getpelican.com/en/latest/) static site. I liked not having to set up a database for content. What I didn't like was having to work through the abstraction of Pelican to do anything.

## Mountain 2018-2019

Frustrated with the lack of control of Pelican in 2018, I wrote [my own Flask-powered blog engine](https://daniel.feldroy.com/posts/writing-new-blog-engine), which I called Mountain. The challenge there was that I had some crazy ideas for a feature that caused too much complexity. The result was a very slow rendering of the static site. It was too much trouble to fix, so I stuck with it.

[Uma](https://daniel.feldroy.com/tags/uma) was born in early 2019. I was too busy being a new father to do much writing, only getting in 5 articles for the whole of 2019.

## Vuepress 2019-2021

By 2019, I was in the Jamstack world. I've since left it, but for a while my site was on [Vuepress](https://vuepress.vuejs.org/). The speed of compilation was nice compared to Mountain, and I could stick in special pages as needed. However, there were a few too many layers of abstraction, and that made extending it to work outside the default behaviors of Vuepress too difficult.

## Next.js 2021-2024

In early 2021, for work, I needed to learn [Next.js](https://nextjs.org/) quickly. I used the official Next.js tutorial that existed at the time to learn the framework and React over a weekend. This was still the early days of Next.js, and I found it to be tons of fun. It reminded me of the best features of Flask combined with tons of frontend power. 

Next.js has changed rapidly. I believe Next.js went in an uncomfortable direction in terms of complexity and decreasing quality of documentation for new or changed features. Bitrot happened frequently, and I felt like I was fighting version upgrades rather than working with the Framework.

## FastHTML 2024-2025

I tried out [FastHTML](https://pypi.org/project/python-fasthtml/) in the summer of 2024. Keeping the features spec in my head, tiny, I coded up the kernel of a cached markdown content site in 45 minutes. This was a vast improvement in terms of speed and complexity over the unnecessarily complex Mountain project of 2018. It was nice to return to Python, but it chafed to use a framework that wasn't PEP8 nor fully type-annotated. 

## Air 2025+

For a few years now, I've wanted to create my own web framework. This year I did so, launching [AIR](https://github.com/feldroy/air) with my wife and coding partner Audrey. Air is a shallow layer over FastAPI, adding features to expedite authoring of dynamic HTML pages. One of the early projects I did with it was to convert this site to use Air. It was nice to return to a PEP8-formatted codebase that is fully type-annotated. I also like the smaller dependency tree.

## The Future

Perhaps I'll grow restless again in a few years and try something new. Or perhaps I'll stick with Air for a long time. What I do know is that I enjoy writing and sharing my thoughts. So there will be posts going into the future. 