from turtle import position
from django.db import models
from django.contrib.auth.models import User
from category.models import Department

# Create your models here.

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    company     = models.CharField(max_length=100, blank=True)
    department  = models.ForeignKey(Department, on_delete=models.CASCADE)
    position    = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username
    