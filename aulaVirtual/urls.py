from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("change_password", views.change_password, name="change_password"),
    path("register", views.register, name="register"),
]