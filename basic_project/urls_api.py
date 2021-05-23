

from django.urls import path
from basic_project import views

#APIs
urlpatterns = [

    path("api/v1/message", views.getMessageIndexV1),
    path("api/v2/message", views.getMessageIndexV2),
    path("api/v3/message", views.getMessageIndexV3),
    path("api/v4/message/<str:name>/<int:age>", views.getMessageIndexV4),
    path("api/v6/create_user_default", views.createUserAdminDefault)

]