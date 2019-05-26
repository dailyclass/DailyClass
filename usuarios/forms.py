from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    Correo = forms.EmailField( required=True)
    Perfil = forms.CharField(max_length=255,required=True)

