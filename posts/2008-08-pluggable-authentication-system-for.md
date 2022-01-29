---
date: '2008-08-15T12:40:00.004-07:00'
description: ''
published: true
slug: 2008-08-pluggable-authentication-system-for
tags:
- plone conference
- plone
- review
- interfaces
- legacy
time_to_read: 5
title: Pluggable Authentication System for Plone
---

It took me a little to get started, because the paster template for Plone 3 Pluggable Authentication System (PAS) products doesn't work for me.  Not sure why, so I submitted a ticket.<br /><br />Anyway, once I figured out that it was the template, and not me, things went very fast.  PAS is rather straightforward when you get the hang of it.  The quick summary of how to do a PAS plugin as how I've done it:<br /><ul><li>Grab the gmail auth plugin and use that as your base.</li><li>In your 'content type', import and register the appropriate method and in the content type's class, create the appropriate method.</li><li>Follow the <a href="http://plone.org/documentation/manual/pas-reference-manual">PAS documentation</a> on <a href="http://plone.org/">Plone.org</a> for different actions you might need to do.<br /></li></ul>Yeah, very basic.  I also figured out how to detail properties that can be set via the ZMI.  Easy, but the documentation is not as easy to find as it should be.<br /><br />I might document things in more depth since in some ways this took much longer than it should have considering the simplicity of the end code.  I'm sure the Plone folks would love a detailed set of PAS examples to reinforce the current documentation, and I seem to enjoy doing that quite a bit. <br /><br />Heh, while I'm at it, maybe I should finish my KSS documentation that I left hanging since the Naples Plone Conference in 2007?<br /><br />Anyway, my quick review of PAS is that its really powerful.  That each element (Authentication, Authorization, Challenges, etc) is seperated into its own plugin/module means that you can switch out components without jeopordizing the security and role system that might already exist.  So, for example, if you want to use LDAP for authentication and SQL for authorization and a Smart Card to handle security challenges, you can do that without having do rewrite the core Plone engine.  Another big bonus is that to do the actual replacement of individual plugin/modules is really easy once you figure out how.  And that is pretty damned hot.