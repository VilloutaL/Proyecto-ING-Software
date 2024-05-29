from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail

#==========================================================================

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

        email1_flag = True
        email2_flag = True
        pass_flag = True
        user_flag = True


        if email != email2:
            messages.error(request, "Los correos no coinciden")
            email1_flag = False
        if clave != clave2:
            messages.error(request, "Las contraseñas no coinciden")
            pass_flag = False
        if  User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso")
            user_flag = False
        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso")
            email2_flag = False
        if email1_flag and email2_flag and user_flag and pass_flag:
            user = User.objects.create_user(username, email, clave)
            user.first_name = first_name
            user.last_name = last_name
            user.is_active = False  # Desactivar la cuenta hasta que el usuario verifique su correo
            user.save()

            # Enviar correo de verificación
            subject = 'Verifica tu cuenta'
            message = f'Por favor, haz clic en el siguiente enlace para verificar tu cuenta: http://127.0.0.1:8000/verify/{user.id}/'
            from_email = 'tu_email@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "Registro exitoso. Por favor, revisa tu correo para verificar tu cuenta.")
            return redirect('registro')

    return render(request, "aulaVirtual/registro.html", {})

def verify(request, uid):
    try:
        user = User.objects.get(pk=uid)
        if user.is_active:
            messages.info(request, "Esta cuenta ya ha sido activada.")
        else:
            user.is_active = True
            user.save()
            messages.success(request, "Cuenta verificada exitosamente. Ahora puedes iniciar sesión.")
    except User.DoesNotExist:
        messages.error(request, "Usuario no encontrado.")

    return redirect('index')

def cambiar_clave(request):
    if request.method == 'POST':
        email = request.POST['correo']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            subject = 'Cambio de contraseña'
            message = f'Por favor, haz clic en el siguiente enlace para cambiar tu contraseña: http://127.0.0.1:8000/cambio-clave-verificado/{user.id}/ '
            from_email = 'saad11012002@gmail.com'
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, "Por favor, revisa tu correo para continuar el proceso.")
            return redirect('index')
        else:
            messages.error(request, "Correo invalido, por favor revisalo.")

    data = {}
    return render(request, 'aulaVirtual/cambiar-clave.html', data)

def cambiar_clave_verificado(request, uid):
    if request.method == 'POST':
        clave = request.POST['clave']
        clave2 = request.POST['clave2']

        if clave != clave2:
            messages.error(request, "Las contraseñas no coinciden")
        else:
            try:
                user = User.objects.get(pk=uid)
                user.set_password(clave)
                user.save()
                messages.info(request, "Contraseña actualizada con exito")
                return redirect("index")
            except User.DoesNotExist:
                messages.error(request, "Usuario no encontrado.")
    data = {}
    return render(request, 'aulaVirtual/cambiar-clave-verificado.html', data)