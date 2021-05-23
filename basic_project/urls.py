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
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from basic_project import views as local_views
from manager_messages import views as manager_messages_views
from users import views as users_views


urlpatterns = []
"#URL APis"
urlpatterns = urlpatterns + [
    path("api/v1/message", local_views.getMessageIndexV1),
    path("api/v2/message", local_views.getMessageIndexV2),
    path("api/v3/message", local_views.getMessageIndexV3),
    path("api/v4/message/<str:name>/<int:age>", local_views.getMessageIndexV4),
    path("api/v5/seeder_message", manager_messages_views.runSeederMessages),
    path("api/v5/list_message", manager_messages_views.getListMessagesV1),
    path("api/v5/list_message/<int:id>", manager_messages_views.getListMessagesByIdV1),
    path("api/v6/create_user_default", local_views.createUserAdminDefault)
    
]

"URL views"
admin.site.site_header = 'Administrador del proyecto'   # default: "Django Administration"
admin.site.index_title = 'Mi area de trabajo'           # default: "Site administration"
admin.site.site_title = 'Mi Proyecto'                   # default: "Django site admin"

urlpatterns = urlpatterns + [
    path('admin/', admin.site.urls),
    path("v1/message", manager_messages_views.listMessagesV1),
    path("user/login/", users_views.loginApp, name="login"),
    path("user/logout/", users_views.logoutApp, name="logout"),
    path("user/signup/", users_views.signupApp, name="signup"),
    re_path(r"^$", manager_messages_views.listMessagesV2, name="index"),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)