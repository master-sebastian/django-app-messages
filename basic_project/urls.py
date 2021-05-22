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
from basic_project import views as local_views
from manager_messages import views as manager_messages_views
urlpatterns = [
#    path('admin/', admin.site.urls),
    path("api/v1/message", local_views.getMessageIndexV1),
    path("api/v2/message", local_views.getMessageIndexV2),
    path("api/v3/message", local_views.getMessageIndexV3),
    path("api/v4/message/<str:name>/<int:age>", local_views.getMessageIndexV4),
    path("v1/message", manager_messages_views.listMessagesV1),
    path("v2/message", manager_messages_views.listMessagesV2)
]
