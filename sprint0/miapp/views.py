from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from .forms import CustomUserCreationForm
# Create your views here.

@login_required
def home(request):
    return render(request, "home.html",{}) 

def authView(request):
    if request.method == 'POST':  
        form = CustomUserCreationForm(request.POST)  
        print(form)
        if form.is_valid():  
            user = form.save()
            login(request, user)
            return redirect("/")
            
    else:
        form = CustomUserCreationForm() 
        print("else")       
    context ={
        'form':form
    }
    return render(request, "registration/signup.html", context)
