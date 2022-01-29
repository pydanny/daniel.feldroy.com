---
date: '2009-11-11T18:15:00.002-08:00'
description: ''
published: true
slug: 2009-11-picking-django-powered-cms
tags:
- november
- django
- review
- blog
- legacy
time_to_read: 5
title: Picking a Django powered CMS
---

<h3>Note as of October 2011</h3><br />The CMS options have changed greatly since I wrote this blog post in 2009. I might write a more current post. In the meantime, instead of FeinCMS, use <a href="http://django-cms.org/">Django CMS</a>, <a href="http://mezzanine.jupo.org/">Mezzanine</a>, or use the <a href="http://djangopackages.com/grids/g/cms/">CMS grid on Django Packages</a> to make your own decision.<br /><br /><h3>Back to the old blog post...</h3><br />A few months ago I asked the community to help us (<a href="http://nasascience.nasa.gov/">NASA SMD</a>) <a href="http://pydanny.blogspot.com/2009/09/show-me-your-open-source-django-cms.html">pick a Django powered CMS</a>.<br /><br />The response of the community was awesome. We were provided a decent sized list of CMS candidates to evaluate. We got a lot of responses, both in comments on my blog, twitter messages, and even direct emails. We compiled the list and got to work.<br /><br />Now it was time for evaluation. As much as I wanted to do it myself, this was given to the capable hands of my co-worker, <a href="http://improbable.org/chris/">Chris Adams</a>. I was a bit jealous because I like to explore, but that's how it worked out.<br /><br />First Chris used a process of elimination to weed out the ones that were unusable based on my published requirements:<br /><ul><li> Was it actually open source?<br /></li><li> Was it 508 compliant or easy to make so?</li><li> Runs on PostGreSQL and MySQL?</li><li> Is there an active community?</li></ul>That narrowed things down a bit. Now Chris added some more filters:<br /><ul><li> Could you show pages nested inside of pages? In order words, could you rely on Tree Traversal for display of content?</li><li> Was there documentation? In English?</li></ul>That reduced things to an even smaller list. Chris took the revised list of candidates, downloaded the code, and started them up. During this process he removed candidates that required patching to get working at the most basic level. He also looked at the code and made a few judgments there as well.<br /><br />Day by day it was a sad to see the list get smaller and smaller. Each project was the labor of many hours by talented people who cared about their work. Yet Chris had a job to do, and while he didn't drop candidates easily, he did drop them.<br /><br />Chris now added our sample content to each surviving candidate and invited the rest of the team to look at the code and the results. It was now up to our subjective evaluation. Two finalists stood out as winners, <a href="http://spinlock.ch/pub/feincms/html/">FeinCMS</a> and <a href="http://www.django-cms.org/en/">Django CMS 2</a>. They were so close that one might consider the results to be a tie. Both met all our needs, their code bases smelled pretty nice, documentation felt complete, code had test coverage, and the community active. They even shared a lot of the same dependencies!<br /><br />The call was very close but in the end we picked FeinCMS.<br /><br />Django CMS 2 was a very, very close second. I cannot say that enough.<br /><br />In a few months we'll announce the front facing site we are building. We'll contribute the work we can to the open source community, which will either be work done on FeinCMS or stand alone applications.<br /><br />Finally, I want to make clear the amount of effort and clarity of work Chris Adams put into these evaluations. He did the hard work and he did it well.<br /><br />20 more posts to go!