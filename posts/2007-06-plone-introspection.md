---
date: '2007-06-04T09:17:00.000-07:00'
description: ''
published: true
slug: 2007-06-plone-introspection
tags:
- plone
- python
- interfaces
- zope
- five
- legacy
time_to_read: 5
title: Plone Introspection
---

So you have a Plone content type with some fields.  What are the properties of that content type?  Well, you can look it up by finding in your file system the product that content type comes from, then examining the schema and finding out your information.  Of course, if the product extends another product, then you have to look up that other product.<br /><br />Bleah.<br /><br />Introspection is what we really want.  Python has it in spades.  On pretty much any object in Python I can wrap it in dir() or help(), or check the __dict__ attribute.  But you can't do this easily in Plone.  Cooking up a universal instrospection view is something that ought to be done for my CMS of choice.  I know there are lots of various barely documented utility methods I can find.  I can wrap it up in a product and just use it by having a special introspection view that lays out some pretty HTML.<br /><br />Sigh.<br /><br />My coworker Reed pointed out that Zope 3, and the Five stuff in Zope 2 uses Interfaces that give some neat tricks you can do for introspection.  I think I'll give that method a try.  I think thats the right way to go because:<br /><ol><li>The Zope 3 specification handles introspection much more gracefully than Zope 2.  And the methods for doing it seem better documented.</li><li>The technology is going that way anyhow.<br /></li></ol>