from django import forms


class AIMessage(forms.Form):
    message = forms.CharField(max_length=10000)
