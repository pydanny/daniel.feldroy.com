---
date: '2011-07-12T15:41:00.000-07:00'
description: ''
published: true
slug: 2011-07-normalization-noitazilamron
tags:
- mongodb
- sql
- legacy
time_to_read: 5
title: Normalization noitazilamroN
---

Since pretty much the start of my career as a developer back in the 1990s one skill I've carried from job-to-job has been an understanding of relational databases. Over the years I've worked with <a href="http://en.wikipedia.org/wiki/Foxpro">Foxpro</a>, <a href="http://en.wikipedia.org/wiki/Microsoft_Access">Access</a>, <a href="http://en.wikipedia.org/wiki/Oracle_Database">Oracle</a>, <a href="http://en.wikipedia.org/wiki/Microsoft_SQL_Server">SQL Server</a>, <a href="http://en.wikipedia.org/wiki/MySQL">MySQL</a>, <a href="http://en.wikipedia.org/wiki/Sqlite">Sqlite</a>, and now&nbsp;<a href="http://en.wikipedia.org/wiki/Postgresql">PostGreSQL</a>.<br /><br />Interestingly enough,&nbsp;<a href="http://en.wikipedia.org/wiki/Database_Normalization">database normalization</a> comes&nbsp;instinctively&nbsp;to me. I knew about complex SQL joins and unions and subqueries before I read anything about normalization. As I read up on normalization, it was rather exciting to discover that my natural instinct during database design was to hit the fourth or fifth normal form without thinking about it. &nbsp;And since for most of my pre-<a href="http://python.org/">Python</a> career the number of records I dealt with was measured in the tens of thousands, normalization was a great tool. I was aware that my record sets were smallish, and good database design kept my stuff running fast.<br /><br /><b>Relational Databases are not a panacea that lets you overcome bad code</b>.<br /><br />It surprises me how many developers I've encountered over the years who complained about the performance issues of normalized data but didn't understand normalization. Instead, they refused to follow any sort of standard and every table seemed to duplicate data and every query requires complex joins for trivial data calls. And usually with sets of records in the count of tens of thousands, not millions or billions. The end result are projects that were/are unmaintainable and slow, with or without normalization.<br /><br /><b>NoSQL is not a panacea that lets you overcome bad code</b>.<br /><br />Which brings me to the current state of things. NoSQL is a big thing, with advantages of NoSQL being touted in the arenas of speed, reliability, flexible architecture, avoidance of <a href="http://en.wikipedia.org/wiki/Object-relational_impedance_mismatch">Object relational&nbsp;impedance&nbsp;mismatch</a>, and just plain ease of development. I've spent a year spinning an <a href="http://en.wikipedia.org/wiki/XML">XML</a> database stapled on top of MS SQL Server, years using <a href="http://en.wikipedia.org/wiki/ZODB">ZODB</a>, and about a woefully short time working on <a href="http://en.wikipedia.org/wiki/MongoDB">MongoDB</a> projects. Like relational databases, the sad truth about XML, ZODB, and MongoDB is that there are problems. And just as with relational databases, the worst of it stemmed not from any issues with data systems, but developers and engineers.&nbsp;Like any other tool you can make terrible mistakes that lead to unmaintainable projects.<br /><br />So for now, like most of the developers I know, what I like to do is as follows:<br /><ol><li>Create a well-normalized database preferably using PostGreSQL.</li><li>Cache predicted slowdown areas in <a href="http://en.wikipedia.org/wiki/Redis_(data_store)">Redis</a>.&nbsp;</li><li>Use data analysis to spot database bottlenecks and <a href="http://en.wikipedia.org/wiki/Denormalization">break normalization</a> via specific non-normalized tables.</li><li>Use a queue system like <a href="http://celeryproject.org/">Celery</a> or even chronjobs to populate the&nbsp;non-normalized&nbsp;table so the user never sees anything slow.</li><li>Cache the results of queries against the specific&nbsp;non-normalized&nbsp;tables in Redis.</li></ol><div>The end result is something with the rigidity of a relational database but with the delivery speed of a key/value database.&nbsp; Since I work a lot in <a href="http://djangoproject.com/">Django</a> this means I get the advantage of most of the <a href="http://djangopackages.com/">Django Packages ecosystem</a> (at this time you lose much of the ecosphere if you go pure NoSQL). You can do the same in <a href="http://pylonsproject.org/projects/pyramid/about">Pyramid</a>, <a href="http://en.wikipedia.org/wiki/Ruby_on_Rails">Rails</a>, or whatever. Maybe its a bit conservative, but it works just fine.</div>