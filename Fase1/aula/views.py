from django.shortcuts import render, redirect
#from .forms import RegistroForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from aula.models import usuario
def inicio (request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')  # Obtén el valor del campo 'usuario' del formulario
        contraseña = request.POST.get('contraseña')  # Obtén el valor del campo 'contraseña' del formulario
        user = authenticate(request, username=usuario, password=contraseña)  # Autenticar usuario
        if user is not None:
            login(request, user)
            return redirect('aula')  # Redirige según el grupo del usuario
        else:
            messages.error(request, 'Credenciales inválidas')  # Mensaje de error
            return redirect('inicio')  # Redirige a la misma página de inicio de sesión en caso de error
    else:
        return render(request, 'aula/inicio.html')
    
    #return render(request,'aula/inicio.html')
def registro (request):
    
    return render(request,'aula/registro.html')
def recuperar_contraseña (request):
    return render(request,'aula/recuperar_contraseña.html')

def aula (request):
    '''
    if request.method== 'POST':
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

        #usuario = request.GET["prd"]
        #contraseña= request.GET["contraseña"]
        #verificar = usuario.objects.filter(email__icontains= email)
        #datos = {
            #"email":email,
            #"registros" : verificar
        
    else :
        email= "no ha introducido nada"

        datos = {
            "email":email
        }
        '''
    return render(request,'aula/aula.html')

# Create your views here.
