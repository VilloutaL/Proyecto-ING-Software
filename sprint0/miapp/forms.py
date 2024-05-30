from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError   
from django.forms.forms import Form  


class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Nombre usuario', min_length=5, max_length=150)  
    email = forms.EmailField(label='Email')  
    email2 = forms.EmailField(label='Confime su Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)  
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("El usuario ya existe")  
        return username  
  
    def email_clean(self):  
        if self.cleaned_data['email'].lower() == self.cleaned_data['email1'].lower() :
            email = self.cleaned_data['email'].lower()  
            new = User.objects.filter(email=email)  
            if new.count():  
                raise ValidationError("El correo ya esta en uso")  
            return email  
        else:
            raise ValidationError("Los correos no coinciden")  

  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(  
            self.cleaned_data['username'],  
            self.cleaned_data['email'],  
            self.cleaned_data['password1']
        )  
        return user  