from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from . forms import UserForm
from .models import Perfiles, PerfilesUsuario
from django.contrib.auth.models import User

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            usuario = User()
            perfil = PerfilesUsuario()
            perfil.usuario = user
            perfil.correo = form.cleaned_data['Correo']
            usuario.email = form.cleaned_data['Correo']
            perfil.perfil_id = form.cleaned_data['Perfil']
            usuario.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'usuarios/signup.html',{
        'form': form
    })