from django.shortcuts import render
from django.http import JsonResponse
from django import views
from . import helper, forms


# Create your views here.


class OpenAIView(views.View):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.database = "default"
        self.connection = helper.Connect(database=database)
        self.connection.engage()
        self.data = connection.data()
        self.ai = helper.DjangoAI(data)
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        super().dispatch(request, *args, **kwargs)

    @property
    def message(self):
        return self.kwargs["message"] if "message" in self.kwargs else None

    def get(self):
        return JsonResponse(data={"response": self.ai.think(self.message)})
