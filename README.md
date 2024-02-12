# django-open-ai

This app enables you to use OpenAI requests over the Django database. 

## Installation

```
pip install django-open-ai
```

## Getting started

Please include your OpenAI API key in the settings.py file as follows. Please also include your target database (generally "default" but could be different if you have more databases):

```python
OPENAI_API_TYPE = "standard"
OPENAI_API_KEY = "<YOUR_API_KEY>"
OPENAI_TARGET_DATABASE = "default"
```

Also make sure that the package is in the installed apps list in the settings.py file:

```python
INSTALLED_APPS = [
    'django_open_ai',
    ...
]
```

Now, make sure that your database is not sqlite3, as this is not supported. Similarly, the each database in the DATABASES list in the settings.py file must include the following keys: HOST, NAME, USER, PASSWORD, ENGINE, PORT. The current version only allows for when the host is the server.

## Simple reproducible example

You now simply have to include the urls of the project into your urls.py file:

```python 
from django.urls import path, include

urlpatterns = [
    path("openai/", include("django_open_ai.urls")),
    ...
]
```

That's it! You can now simply make requests using `openai/<str:message>` for example `openai/how many people voted?`.
