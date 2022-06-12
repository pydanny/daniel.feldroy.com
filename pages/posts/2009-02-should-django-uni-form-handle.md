---
date: "2009-02-10T17:17:00.005-08:00"
description: ""
published: true
slug: 2009-02-should-django-uni-form-handle
tags:
  - django
  - forms
  - pinax
  - legacy-blogger
time_to_read: 5
title: Should django-uni-form handle boilerplate HTML?
---

_This was originally posted on blogger [here](https://pydanny.blogspot.com/2009/02/should-django-uni-form-handle.html)_.

This is in regards to my [django-uni-form](https://code.google.com/p/django-uni-form/) project, which lets you do proper fieldset forms in Django, letting you do prettily formatted forms that meet the Section 508 specification, not to mention various accessibility and usability guidelines.

Basically, I think django-uni-form could be a little more helpful. So what do I mean?

Standard uni-form looks like:<pre><div class="highlight"><pre>
&lt;form class="login uniForm" method="POST" action=""&gt;
&lt;fieldset class="inlineLabels"&gt;
&lt;legend&gt;_ Required fields&lt;/legend&gt; 
 &lt;div class="ctrlHolder "&gt; 
 &lt;label for="id_username"&gt; _ User Name&lt;/label&gt;
 &lt;input id="id_username" type="text" name="username" maxlength="30" /&gt;
 &lt;/div&gt;
&lt;/legend&gt;
&lt;/fieldset&gt;
&lt;div class=&quot;buttonHolder&quot;&gt;
 &lt;button type=&quot;reset&quot; class=&quot;resetButton&quot;&gt;Reset&lt;/button&gt;
 &lt;button type=&quot;submit&quot; class=&quot;primaryAction&quot;&gt;Submit&lt;/button&gt;
 &lt;/div&gt;
&lt;/form&gt;
</pre></div></pre>django-uni-form gives just:<pre><div class="highlight"><pre>
 &lt;div class="ctrlHolder "&gt; 
 &lt;label for="id_username"&gt; _ User Name&lt;/label&gt;
 &lt;input id="id_username" type="text" name="username" maxlength="30" /&gt;
 &lt;/div&gt;
</pre></div></pre>Does it make sense for django-uni-form to provide the following?<pre><div class="highlight"><pre>
&lt;fieldset class="inlineLabels"&gt;
&lt;legend&gt;_ Required fields&lt;/legend&gt; 
 &lt;div class="ctrlHolder "&gt; 
 &lt;label for="id_username"&gt; \* User Name&lt;/label&gt;
 &lt;input id="id_username" type="text" name="username" maxlength="30" /&gt;
 &lt;/div&gt;
&lt;/legend&gt;
&lt;/fieldset&gt;
</pre></div></pre>With this, you can still add in buttons elegantly. Thoughts?

<span style="font-weight: bold;">Update:</span> I'm working with James Tauber and perhaps some others to figure out the best way to make this work.
