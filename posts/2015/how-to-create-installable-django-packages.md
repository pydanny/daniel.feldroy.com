---
date: "2015-11-20"
published: true
slug: how-to-create-installable-django-packages
tags:
  - python
  - tech
  - python
  - tech3
  - django
  - cheatsheet
  - django packages
time_to_read: 2
title: How To Create Installable, Reusable Django Packages
image: https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/django-package-470x246.png
---

[![image](https://f004.backblazeb2.com/file/daniel-feldroy-com/public/images/django-package-470x246.png)](/how-to-create-installable-django-packages.html)

What I mean by an "installable Django package": a reusable component that can be shared across Django projects, allowing us to combine our own efforts with others. Some examples include:

- [django-test-plus](https://www.djangopackages.com/packages/p/django-test-plus/)
- [django-crispy-forms](https://www.djangopackages.com/packages/p/django-crispy-forms/)
- [dj-stripe](https://www.djangopackages.com/packages/p/dj-stripe/)
- [dj-spam](https://www.djangopackages.com/packages/p/dj-spam/)

Ever want to quickly create a similarly installable Django package to submit to [PyPI](pypi.python.org/pypi) and [Django Packages](https://wwww.djangopackages.com)? One that goes beyond the basics described in the [Django tutorial](https://docs.djangoproject.com/en/1.8/intro/reusable-apps/)? Specifically, a package that includes:

- Test runner so you don't need a example/test project (Although those can be useful).
- The important configuration in place: Travis, editorconfig, gitignore, etc.
- The important documentation in place: Readme, License, Read the Docs-ready Sphinx docs, etc.
- Static files ready to go.
- A base DTL/Jinja2 template ready to go.
- All those other fiddly bits not included in `django-admin.py startapp` that are hard to remember.

Well, here's how I do it.

# Introducing cookiecutter-djangopackage

[cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage) is a [Cookiecutter](https://github.com/audreyr/cookiecutter) template for creating reusable Django packages. Using it is easy:

First, get [Cookiecutter](https://github.com/audreyr/cookiecutter). Trust me, it's awesome:

```bash
$ pip install cookiecutter
```

Now run it against this repo:

```bash
$ cookiecutter https://github.com/pydanny/cookiecutter-djangopackage.git
```

You'll be prompted to enter some values. Enter them. Then an installable Django package will be built for you.

**Warning**: `app_name` must be a valid Python module name or you will have issues on imports.

Enter the new package (in my case, I called it 'newpackage') and look around. Open up the `AUTHORS.rst`, `setup.py`, or `README.rst` files and you'll see your input inserted into the appropriate locations.

Speaking of the `README.rst`, that file includes instructions for putting the new package on [PyPI](pypi.python.org/pypi) and [Django Packages](https://wwww.djangopackages.com).

```bash
newpackage
├── .editorconfig
├── .gitignore
├── .travis.yml
├── AUTHORS.rst
├── CONTRIBUTING.rst
├── HISTORY.rst
├── LICENSE
├── MANIFEST.in
├── Makefile
├── README.rst
├── newpackage
│   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── newpackage.css
│   │   ├── img
│   │   │   └── .gitignore
│   │   └── js
│   │       └── newpackage.js
│   └── templates
│       └── cheese
│           └── base.html
├── docs
│   ├── Makefile
│   ├── authors.rst
│   ├── conf.py
│   ├── contributing.rst
│   ├── history.rst
│   ├── index.rst
│   ├── installation.rst
│   ├── make.bat
│   ├── readme.rst
│   └── usage.rst
├── requirements-test.txt
├── requirements.txt
├── requirements_dev.txt
├── runtests.py
├── setup.cfg
├── setup.py
├── tests
│   ├── __init__.py
│   └── test_models.py
└── tox.ini
```

Now, instead of monkeying around for awhile doing copy/paste package setup, I'm immediately ready to write code.

# Summary

[cookiecutter-djangopackage](https://github.com/pydanny/cookiecutter-djangopackage) does a lot, but even with its tight focus on package creation it could do more. Some of the things I would love to see included in the future:

- Option for Appveyor CI support
- Option to replace `django.test` with `py.test`.
- Generation of model boilerplate, admin, and CRUD views.
- More in the [issue
  tracker](https://github.com/pydanny/cookiecutter-djangopackage/issues).

Try it out and let me know what you think. I'm open to new ideas and receiving pull requests.
