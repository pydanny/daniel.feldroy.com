---
date: '2008-07-07T19:20:00.003-07:00'
description: ''
published: true
slug: 2008-07-me-grok-generate-add-and-edit-forms
tags:
- grok
- python
- zope
- legacy
time_to_read: 5
title: Me Grok generate Add and Edit forms!
---

So the first bit of documentation in the grok docs didn't work.  Grok has evolved a lot so this is understandable.  My thought when I dropped the effort in frustration was that my knowing of where the URLs for the add and edit forms were off.  Since the docs I was first working on lacked the URL of what I where I was supposed to go that answer seemed to make sense.<br /><br />My co-worker suggested I go to the explicit name of the view, which in the Zope 3 world is '@@' this or that.  A good suggestion but that didn't work.  More on that in a bit.<br /><br />Examining the <a href="http://grok.zope.org/documentation/developers-notes/">Developer Notes</a> I discovered that the docs I was using were out of date.  I changed my code to fit the notes, pointed Firefox at the URL named after the form classes, and it just plain worked.  Code changes were minimal.  And I'm posting to the Grok folks that the form docs are out of date.<br /><br />Anyway, you can go to /myview or /@@myview in Grok.  Which is good.  For some reasons that others explain quite well, Zope 3 has this whole big thing with '@@' and '++' in URL bars to explicitly name views, adapters, utilities, oversized SUVs, bad American food, et al.   I'm sure some people can't live without them but honestly since Grok avoids them it makes things feel more... pythonic.<br /><br />Anyway, the add &amp; edit forms, now that I can make them work, are wonderful.  Pretty HTML forms with validation done in moments off a little python code.