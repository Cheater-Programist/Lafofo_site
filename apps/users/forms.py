from django.forms import fields, widgets
from apps.users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegistrateForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username','profile','age','gender'
            )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'profile':forms.FileInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
        }


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username','password'
            )
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),

        }

        def create(self, validated_data):
            user = super().create(validated_data)
            password = validated_data['password']
            user.set_password(password)
            user.save()
            return user

class UserChoiceField(forms.ModelChoiceField):
    pass



class Form_user(forms.ModelForm):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'product_user':
            return UserChoiceField(User.objects.filter(username = request.user.username))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)