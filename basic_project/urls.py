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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = 'Administrador del proyecto'   # default: "Django Administration"
admin.site.index_title = 'Mi area de trabajo'           # default: "Site administration"
admin.site.site_title = 'Mi Proyecto'                   # default: "Django site admin"

urlpatterns = [

    #URLs views and APIs project_basic
    path("basic-project/", include(( "basic_project.urls_api", "basic_project"), namespace="basic_project")),
    #Urls Admin
    path('admin/', admin.site.urls),
    #URLs views and APIs messages
    path("", include( ("manager_messages.urls", "manager_messages"), namespace="manager_messages")),
    #URLs views and APIs users
    path("users/", include( ("users.urls", "users" ), namespace="users")),

]

#settings for files of the media 
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)