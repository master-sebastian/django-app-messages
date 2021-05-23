from django.db import models
from django.contrib.auth.models import User as UserBase

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Profile(models.Model):
    """Profile model"""
    #user_id
    user = models.OneToOneField(UserBase, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bibliography = models.TextField(blank=True)
    """
        models.DateField(blank=True, null=True)
        ________________________________________
        Vuelve nullable el campo y el valor del vacio es null
    """
    birthdate = models.DateField(blank=True, null=True)
    picture = models.ImageField(upload_to="users/pictures", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name+" "+self.last_name

# Create your models here.
class Message(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.message