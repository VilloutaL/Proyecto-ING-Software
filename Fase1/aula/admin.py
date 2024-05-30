from django.contrib import admin
from aula.models import usuario

class usuario_admin(admin.ModelAdmin):
    list_display=("email","contraseña")
    search_fields = ("email","contraseña")
admin.site.register(usuario,usuario_admin)

# Register your models here.
