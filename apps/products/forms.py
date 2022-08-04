from django.db import models
from django.forms import fields, widgets
from apps.products.models import *
from django import forms

# class ProductImageForm(forms.ModelForm):
#
#     class Meta:
#         model = ProductImage
#         fields = ['image']
#         widgets = {
#             'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
#         }

class ProductForm(forms.ModelForm):


    class Meta:
        model = Product
        exclude = ['is_stock','slug']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }



# class Form_user(forms.ModelForm):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'product_user':
#             return UserChoiceField(User.objects.filter(slug = 'Isa_kov17'))
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)