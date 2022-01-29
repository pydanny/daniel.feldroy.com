---
date: '2011-12-17T15:10:00.000-08:00'
description: ''
published: true
slug: 2011-12-evaluating-which-package-to-use
tags:
- rant
- python
- legacy
time_to_read: 5
title: Evaluating which package to use
---

In November of 2009 I wrote about which <a href="http://pydanny.blogspot.com/2009/11/code-ill-reuse.html">third-party Python Packages I'll use</a>. Here is my modern take on it - much of it inspired by personal experience and the advice of peers and mentors:<br /><br /><h3>Tag and release on PyPI</h3><br />I really don't like pulling from tags on <a href="https://github.com">Github</a>, <a href="https://bitbucket.org">BitBucket</a>, or whatever. Or being told to pull from a specific commit. That works in early development, but it certainly doesn't fly in production. <br /><br />I also get frustrated when people release on <a href="http://pypi.python.org/pypi">PyPI</a> but then insist on hosting the release themselves. That is because invariably at some critical point in development when PyPI is up, the host provider is down. <br /><br />A <b>huge</b> point of frustration is that I shouldn't have to leave the canonical source of <a href="http://python.org">Python</a> package versions to hunt down what I should be using. I've seen too many beginning Python developers fall into the trap of using 3 year old packages because they didn't know they should be using trunk. I was guilty of doing it for a 6+ month old release in 2010, and for that I apologize and promise I won't do it again.<br /><br />This also means your package needs to be <a href="http://pypi.python.org/pypi/pip">pip</a> installable. If you don't know how to do it, please read the <a href="http://guide.python-distribute.org/">The Hitchhiker’s Guide to Packaging</a>. <br /><br /><h3>Documentation</h3><br />2011 is closing, which means your package needs to have <a href="http://sphinx.pocoo.org/">Sphinx Documentation</a>. And those Sphinx Docs should be on <a href="http://readthedocs.org/">Read the Docs</a>. Read the Docs is great because it doesn't just host the rendered HTML, it also lets you easily push to it from a DVCS push - and implements nice search and handy PDFs too.<br /><br />Yes, I know there is <a href="http://packages.python.org">packages.python.org</a> but I don't trust it. It doesn't have the easy <strong>push/deploy</strong> workflow of Read the Docs, which means often the docs are dated because it's yet another step for developers. Plus, the lack of search outside of Sphinx makes it hard to discover documentation.<br /><br />The same goes for hosting docs yourself. In fact, that's usually worse because when someone goes on vacation and the docs go down... ARGH!<br /><br />Please don't mention <strike>easy_install</strike> in your docs. We are nearly in 2012 and ought to be unified on our package installer, which is <a href="http://pypi.python.org/pypi/pip"><b>pip</b></a>. <br /><br /><h3>Tests</h3><br />You should have them. Otherwise any update you put on PyPI puts the rest of us at risk. We can't be sure your updates to the project won't break our stuff. So please write some tests! If you add in coverage.py and some kind of lint checker, it can even be fun! It certainly does earn you bragging rights having a high coverage rating.<br /><br /><h3>Code Quality</h3><br />Are you using new-style classes or old-style classes? Do you follow PEP-8? Do you keep meta-classes to the absolute minimum? Is the code on an available DVCS so others can fork and contribute? These are things that weigh in my judgement, and certainly the judgement of others.