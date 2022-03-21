from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .views import ProfileDetailView

urlpatterns = [
    path("", views.register),
    path("<int:pk>/details", ProfileDetailView.as_view(), name="profile-detail"),
    path("register", views.register, name="register"),
    path("login", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", auth_views.LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("profile/", views.ProfileDetailView.as_view()),
]