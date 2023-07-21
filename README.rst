===============
django-open-ai
===============

This app enables you to use OpenAI requests over the Django database.

Installation
----------------------------------------

You can install the package using pip::

    #pip install django-open-ai

Quick start
----------------------------------------

1. Please include your OpenAI API key in the settings.py file as follows. Please also include your target database (generally "default" but could be different if you have more databases):::

    OPENAI_API_TYPE = "standard"
    OPENAI_API_KEY = "<YOUR_API_KEY>"
    OPENAI_TARGET_DATABASE = "default"

2. Also make sure that the package is in the installed apps list in the settings.py file:::

    INSTALLED_APPS = [
    'django_open_ai',
    ...
    ]

Now, make sure that your database is not sqlite3, as this is not supported. Similarly, the each database in the DATABASES list in the settings.py file must include the following keys: HOST, NAME, USER, PASSWORD, ENGINE, PORT. The current version only allows for when the host is the server.


Simple example
----------------------------------------

Suppose that the Django app has an app called polls.py (as per the example https://docs.djangoproject.com/en/4.2/intro/tutorial01/). Then in the polls/views.py simply make::

    from django_open_ai import views

    class make_view(views.DjangoOpenAI):
        template = "YOUR OWN TEMPLATE.html"


Please make sure that your template includes a form as follows::

    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="Submit">
    </form>

Now set up your urls.py file inside polls::

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.make_view.as_view()),
        ...
    ]

and in your site urls.py::

    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path("ai/", include("polls.urls")),
        ...
    ]

That's it! Run your server::

    python manage.py runserver

The page http://127.0.0.1:8000/ai/ shows the form. Ask away about your data! For example "What is the most popular choice for question 1?". This will return a JsonResponse with the result.