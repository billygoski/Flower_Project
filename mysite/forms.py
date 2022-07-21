from django import forms
from django.forms import ModelForm
from .models import Flowers


class MyForm(ModelForm):
    class Meta:
        model = Flowers
        fields = ['name','category','tag','description']