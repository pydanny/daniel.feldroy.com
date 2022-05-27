---
date: '2008-11-14T09:52:00.003-08:00'
description: ''
published: true
slug: 2008-11-subscribers-zope-3-style
tags:
- zope
- legacy-blogger
time_to_read: 5
title: Subscribers Zope 3 style
---

*This was originally posted on blogger [here](https://pydanny.blogspot.com/2008/11/subscribers-zope-3-style.html)*.

Vernon Chapman shared this with me.  Very elegant.

configure.zcml (brackets replacing XML open/close because Blogspot sucks!)
<blockquote>[subscriber for="<span style="color: rgb(0, 102, 0);">Products.CMFCore.interfaces.IActionSucceededEvent</span>"
    handler="<span style="color: rgb(0, 102, 0);">.handlers.</span><span style="color: rgb(0, 102, 0);">vernstuff_content_thing</span>" /]</blockquote>handlers module
<blockquote><span style="color: rgb(0, 0, 153);">def</span> <span style="color: rgb(0, 0, 102);">vernstuff_content_thing</span>(event):
<span style="color: rgb(0, 102, 0);">"""This will do all the work"""</span>
action_as_string = event.action
content = event.object
<span style="color: rgb(0, 102, 0);"># Do whatever you like here</span></blockquote>