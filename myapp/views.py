from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        user = authenticate(request, username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            return redirect('main')  # Redirige a la página "main" después de un inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
            return redirect('inicio_sesion')  # Redirige a la misma página de inicio de sesión en caso de error
    else:
        return render(request, 'inicio_sesion.html')
    
    
def main(request):
    return render(request, 'main.html')  # Renderiza la plantilla HTML "main.html"


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']
            user = User.objects.create_user(username=usuario, password=contraseña)
            messages.success(request, '¡Registro exitoso! Por favor inicia sesión.')
            return redirect('inicio_sesion')
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
            return redirect('main')  # Redirige a la página "main" después de un inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
            return redirect('inicio_sesion')  # Redirige a la misma página de inicio de sesión en caso de error
    else:
        return render(request, 'inicio_sesion.html')

