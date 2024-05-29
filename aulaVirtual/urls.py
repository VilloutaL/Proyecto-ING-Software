from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.home, name="home"),
    path("cambio-clave", views.cambiar_clave, name="cambio-clave"),
    path("cambio-clave-verificado/<int:uid>/", views.cambiar_clave_verificado, name="cambio-clave-verificado"),
    path("registro", views.register, name="registro"),
    path('verify/<int:uid>/', views.verify, name='verify'),
    
]