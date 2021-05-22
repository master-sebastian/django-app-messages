"""basic_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from basic_project import views

urlpatterns = [
#    path('admin/', admin.site.urls),
    path("api/v1/message", views.getMessageIndexV1),
    path("api/v2/message", views.getMessageIndexV2),
    path("api/v3/message", views.getMessageIndexV3),
    path("api/v4/message/<str:name>/<int:age>", views.getMessageIndexV4)
]
