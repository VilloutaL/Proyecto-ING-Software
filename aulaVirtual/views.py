from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    data = {}
    data["titulo_de_pagina"] = "Inicio - Aula virtual"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        recordarme = request.POST.get('recordarme', False)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if not recordarme:
                request.session.set_expiry(0)
            messages.info(request, f'Has iniciado sesion como {username}.')
            return redirect('/')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrecta.")

    return render(request, "aulaVirtual/index.html", data)

@login_required
def home(request):
    data = {}
    
    return render(request, "aulaVirtual/home.html", data)
