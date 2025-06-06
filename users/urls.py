from django.urls import path

from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("sign_up", views.sign_up, name="sign_up")
]