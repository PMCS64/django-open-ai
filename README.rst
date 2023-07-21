===============
django-open-ai
===============

Installation
----------------------------------------

You can install the package using pip::

    #pip install django-open-ai

Quick start
----------------------------------------

1. Add "django_open_ai" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "django_open_ai",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("open-ai/", include("django_open_ai.urls")),

