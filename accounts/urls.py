from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register",views.register, name="register"),
    path("login",auth_views.LoginView.as_view(template_name="Login.html"), name="login"),
    path("logout",auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("passwor-reset",auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name="reset_password"),
    path("passwor-reset/done",auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name="password_reset_done"),
    path("passwor-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path("passwor-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name="password_reset_complete"),
    path("profile",views.profile, name="profile")
]
