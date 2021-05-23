from django.urls import path, re_path
from . import views as views

#Views
urlpatterns = [
    path(
        "v1/message", 
        views.listMessagesV1
    ),
    re_path(
        r"^$", 
        views.listMessagesV2, 
        name="index"
    ),
    path(
        "profile/edit", 
        views.updateProfile, 
        name="update_profile"
    ),
    path(
        "create/message", 
        views.createMessage, 
        name="create_message"
    )

]

#APIs
urlpatterns = urlpatterns + [
    path(
        "api/v5/seeder_message", 
        views.runSeederMessages
    ),
    path(
        "api/v5/list_message", 
        views.getListMessagesV1
    ),
    path(
        "api/v5/list_message/<int:id>", 
        views.getListMessagesByIdV1
    ),
]