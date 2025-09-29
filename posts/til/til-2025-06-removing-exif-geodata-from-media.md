---
date: '2025-06-23T20:56:49.362878'
description: How to remove revealing data from your images and videos
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
title: 'TIL: Removing exif geodata from media'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

To do this you'll need [exiftool](https://exiftool.org/). On Mac it can be installed with `brew install exiftool`.

How to remove the geodata:

```sh
exiftool "-gps*=" beach-video.mp4
```