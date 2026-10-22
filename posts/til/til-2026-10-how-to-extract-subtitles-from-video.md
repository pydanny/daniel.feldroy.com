---
date: '2026-10-22T03:35:27.008512+00:00'
description: How I use Python and ffmpeg to create a subtitle file.
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
published: true
tags:
- TIL
- python
title: 'TIL: How to extract subtitles from video'
twitter_image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/logos/til-1.png
---

Recently I've been making more and more videos for my [youtube channel](https://www.youtube.com/@DanielFeldroy). I like videos with subtitles, and decided to add them to my own efforts. This is what I do:

This command assumes you have uv and ffmpeg installed.


```sh
uvx --python 3.14 --from openai-whisper whisper "name-of-video.mp4" \
  --model small \
  --language English \
  --task transcribe \
  --output_format srt \
  --output_dir captions \
  --fp16 False
```