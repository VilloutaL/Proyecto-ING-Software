from django import forms
from .models import Usuario

class RegistroForm(forms.ModelForm):
    # Definimos las opciones para el campo 'cargo'
    OPCIONES_CARGO = (
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
        ('apoderado', 'Apoderado'),
        ('administrador', 'Administrador'),
    )

    # Definimos el campo 'cargo' como un ChoiceField
    cargo = forms.ChoiceField(choices=OPCIONES_CARGO)

    class Meta:
        model = Usuario
        fields = ['usuario', 'correo_electronico', 'cargo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),  # Para ocultar la contraseña en el formulario
        }


