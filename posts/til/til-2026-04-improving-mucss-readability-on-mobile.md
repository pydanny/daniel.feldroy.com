---
date: '2026-04-06T02:45:46.176600+00:00'
description: How to get an otherwise responsive framework to look good on mobile devices.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
title: "TIL: Improving \xB5CSS readability on mobile"
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

With [µCSS](https://mucss.org), the typography can be hard to read, and media queries appear to be the right approach to fixing it. Adding this bit of CSS below makes text more easy to read on mobile devices. I'm now using this on both this site and my [author site](https://grimdaniel.com/).

```css
@media (max-width: 768px) {
  body {
    font-size: 18px;
    line-height: 1.7;
    padding: 0 14px;
  }

  h1, h2, h3 {
    line-height: 1.25;
  }

  pre, code {
    font-size: 0.9em;
    overflow-x: auto;
  }
}
```
