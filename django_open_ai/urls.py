from django.urls import path
from . import views

urlpatterns = [
    path("<str:message>", views.OpenAIView.as_view(), name="open_ai")
]
