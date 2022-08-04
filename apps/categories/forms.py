from django.db import models
from django.forms import fields, widgets
from apps.categories.models import Category
from django import forms

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
            'title','parent',
            )
        exclude = ['slug',]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }