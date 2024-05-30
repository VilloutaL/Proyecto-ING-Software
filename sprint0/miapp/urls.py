from django.urls import path
from .views import authView, home
from django.contrib.auth import views as auth_views
from .views import custom_logout
urlpatterns = [
    path("",home, name="home"),
    path("signup/", authView, name = "authView"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('logout/', custom_logout, name='custom_logout'),

]
