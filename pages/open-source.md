---
title: "Open Source"
description: "My open-source efforts: tools, libraries, and infrastructure I build and maintain."
og_url: https://daniel.feldroy.com/open-source
---

_My open-source efforts: tools, libraries, and infrastructure I have created and/or maintain._

## Current Projects

### [Air](https://github.com/feldroy/air) 💨

I'm the lead on a new Python web framework that breathes fresh air into Python web development. Built with FastAPI, Starlette, and Pydantic. Inline docstrings and long form documentation given all the attention we give to our tech books, so great for both humans and LLMs.

- **Powered by FastAPI** - Designed to work with FastAPI so you can serve your API and web pages from one app
- **Fast to code** - Tons of intuitive shortcuts and optimizations designed to expedite coding HTML with FastAPI
- **Air Tags** - Easy to write and performant HTML content generation using Python classes to render HTML
- **Jinja Friendly** - No need to write `response_class=HtmlResponse` and `templates.TemplateResponse` for every HTML view
- **Mix Jinja and Air Tags** - Jinja and Air Tags both are first class citizens. Use either or both in the same view!
- **HTMX friendly** - We love HTMX and provide utilities to use it with Air
- **HTML form validation powered by pydantic** - We love using pydantic to validate incoming data. Air Forms provide two ways to use pydantic with HTML forms (dependency injection or from within views)
- **Easy to learn yet well documented** - Hopefully Air is so intuitive and well-typed you'll barely need to use the documentation. In case you do need to look something up we're taking our experience writing technical books and using it to make documentation worth boasting about.

### [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 🍪

I'm one of the leads of Cookiecutter, a cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects, and more.

## Previous Projects

These are some of the projects I have started or co-created over the years. All of these have had successful handoffs. 

- [djangopackages.org](https://djangopackages.org/) - The comparison site for Django packages.
- [dj-stripe](https://github.com/dj-stripe/dj-stripe) - The official Django connector to Stripe
- [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django) - Far and away the most popular open source Django starter template
- [dj-notebook](https://github.com/pydanny/dj-notebook) - Easy integration of Jupyter notebooks with Django
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - I started the predecessor library and helped get this library off the ground. The API design is mine
- [cached-property](https://github.com/pydanny/cached-property) - A decorator for caching properties in classes. This library's discovery of challenges with caching properties and theads directly affected the implementation of `functools.cached_property` into core Python.
- [dj-ango](https://github.com/pydanny/dj-ango) - Not everyone has my talent at memorizing long import paths. This project was an experiment in flattening the Django namespace similar to Flask's approach. Air's mostly flat namespace follows the same theme.
- [django-wysiwyg](https://github.com/pydanny/django-wysiwyg) - A Django app for making textareas in Django rich text editors, modern techniques rendered this abstraction moot.
- [cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage) - A Cookiecutter template for creating installable Django packages.