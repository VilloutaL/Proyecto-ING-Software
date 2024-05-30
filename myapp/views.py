from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.db import IntegrityError

# Create your views here.
def index(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            return calificargrupo(user)  # Redirige según el grupo del usuario
        else:
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
            return redirect('inicio_sesion')  # Redirige a la misma página de inicio de sesión en caso de error
    else:
        return render(request, 'inicio_sesion.html')

def main(request):
    return render(request, 'main.html')  # Renderiza la plantilla HTML "main.html"

def Profesores(request):
    return render(request, 'profe.html')

def Administradores(request):
    return render(request, 'administrador.html')

def RecuperarContra(request):
    return render(request, 'contra.html')


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            correo_electronico = form.cleaned_data['correo_electronico']
            contraseña = form.cleaned_data['contraseña']
            cargo = form.cleaned_data['cargo']
            
            try:
                user = User.objects.create_user(username=usuario, email=correo_electronico, password=contraseña)
                group = Group.objects.get(name=cargo)
                user.groups.add(group)
                user.save()
                messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
                return redirect('inicio_sesion')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está en uso. Por favor, elige otro.')
                return redirect('registro')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')  # Obtén el valor del campo 'usuario' del formulario
        contraseña = request.POST.get('contraseña')  # Obtén el valor del campo 'contraseña' del formulario
        user = authenticate(request, username=usuario, password=contraseña)  # Autenticar usuario
        if user is not None:
            login(request, user)
            return calificargrupo(user)  # Redirige según el grupo del usuario
        else:
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
            return redirect('inicio_sesion')  # Redirige a la misma página de inicio de sesión en caso de error
    else:
        return render(request, 'inicio_sesion.html')

def calificargrupo(user):
    if user.groups.filter(name='administrador').exists():
        return redirect('administradores')  # Redirige a la página del administrador
    elif user.groups.filter(name='profesor').exists():
        return redirect('profesores')  # Redirige a la página del profesor
    elif user.groups.filter(name='estudiante').exists():
        return redirect('main')  # Redirige a la página del estudiante
    elif user.groups.filter(name='apoderado').exists():
        return redirect('main')  # Redirige a la página del apoderado
    else:
        return redirect('main')  # Redirige a la página principal si el usuario no pertenece a ningún grupo específico
    
def RecuperarContraseña(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Verificar si el correo electrónico existe en la base de datos
        try:
            user = User.objects.get(email=email)
            # Si el usuario existe, aquí puedes enviar el correo electrónico para recuperar la contraseña
            # Por ahora, vamos a mostrar un mensaje de éxito
            messages.success(request, f'Se ha enviado un correo electrónico a {email} con instrucciones para restablecer su contraseña.')
            return redirect('inicio_sesion')  # Redirige al inicio de sesión
        except User.DoesNotExist:
            messages.error(request, 'El correo electrónico proporcionado no está registrado en nuestro sistema.')
            return redirect('RecuperarContraseña')  # Redirige de vuelta al formulario de recuperación de contraseña
    else:
        return render(request, 'contra.html')