from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import CustomUserCreationForm
# Create your views here.

@login_required
def home(request):
    return render(request, "home.html",{}) 

def authView(request):
    if request.POST == 'POST':  
        form = UserCreationForm()  
        if form.is_valid():  
            form.save()
            login(request,form)
            return redirect('home')    
    else:
        form = CustomUserCreationForm()        
    context ={
        'form':form
    }
    return render(request, "registration/singup.html", context)
