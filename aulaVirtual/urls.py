from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("cambio-clave", views.change_password, name="cambio-clave"),
    path("registro", views.register, name="registro"),
]