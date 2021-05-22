from django.db import models

# Create your models here.
class Message(models.Model):
    author_name = models.CharField(max_length=255)
    message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.author_name


class User(models.Model):
    """User model"""
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bibliography = models.TextField(blank=True)
    """
        models.DateField(blank=True, null=True)
        ________________________________________
        Vuelve nullable el campo y el valor del vacio es null
    """
    birthdate = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Role(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)