import django
from django.urls import path
from . import views as views
from django.views.generic import TemplateView
#Views
urlpatterns = [
    path(
        route="profile/<str:username>/",
        view=TemplateView.as_view(template_name='users/detail.html'),
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