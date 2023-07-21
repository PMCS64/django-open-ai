from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("/", views.DjangoOpenAI.as_view(database=settings.OPENAI_TARGET_DATABASE)),
]
