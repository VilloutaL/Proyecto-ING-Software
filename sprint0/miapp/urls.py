from django.urls import path, include
from .views import authView, home
urlpatterns = [
    path("",home, name="home"),
    path("singup/", authView, name = "authView"),

]
