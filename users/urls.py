from django.urls import path
from . import views as views


#Views
urlpatterns = [

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