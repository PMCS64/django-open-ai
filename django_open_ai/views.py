from django.shortcuts import render
from django.http import JsonResponse
from django import views
from . import helper, forms


# Create your views here.


class DjangoOpenAI(views.View):

    database = "default"
    connection = helper.Connect(database=database)
    connection.engage()
    data = connection.data()
    ai = helper.DjangoAI(data)
    template = "form.html"
    form = forms.AIMessage()

    def post(self, req):
        response = self.ai.think(req.POST["message"])
        return JsonResponse(data={"response": response})

    def get(self, req):
        return render(request=req, template_name=self.template, context={"form": self.form})