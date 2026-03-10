---
date: '2026-03-10T05:54:45.072695+00:00'
description: Should we call mistakes made by humans slop?
published: true
tags:
- rant
title: Stupid human coding mistakes
---

This bug was created by me without the assistance of any AI. Does that make this "human slop"?

```python
description=content["attributes"].get("description", "slug"),
```

What this snippet does is that if the content attributes doesn't include a description field, then the description provided will be "slug". It's a stupid bug that's been in my personal site for about 18 months. I should have a test around it (but was lazy) and I shouldn't have made the mistake in the first place (I was overconfident). It is, in a word, "sloppy".

So does that mean I generated "human slop"?