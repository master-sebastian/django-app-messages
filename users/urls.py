from django.urls import path
from . import views

#Views
urlpatterns = [
    path(
        route="profile/<str:slug_username>/",
        view=views.UserDetailView.as_view(),
        name="detail"
    ),
    path(
        "login/", 
        views.loginApp, 
        name="login"
    ),
    path(
        "logout/", 
        views.logoutApp, 
        name="logout"
    ),
    path(
        "signup/", 
        views.signupApp, 
        name="signup"
    ),
]