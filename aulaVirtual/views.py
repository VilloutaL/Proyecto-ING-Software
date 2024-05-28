from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


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
            return redirect('home')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrecta.")

    return render(request, "aulaVirtual/index.html", data)

@login_required
def home(request):
    data = {}
    user = request.user
    users_group = user.groups.all()
    
    data["title"] = "Home - Aula virtual"
    data["user"] = user
    data["groups"] = users_group

    return render(request, "aulaVirtual/home.html", data)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['correo']
        email2 = request.POST['correo2']
        clave = request.POST['clave']
        clave2 = request.POST['clave2']

        if email != email2:
            messages.error(request, "Los correos no coinciden")
        elif clave != clave2:
            messages.error(request, "Las constraseñas no coinciden")
        else:
            user = User.objects.create_user(username, email, clave)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return redirect('home')
        
    return render(request, "aulaVirtual/registro.html", {})

def change_password(request):
    data = {}
    return HttpResponse("Esta es la página de cambio de contraseña")