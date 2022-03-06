from django.db import models
from django.contrib.auth.models import User
from category.models import Department

# Create your models here.

class UserProfile(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo  = models.ImageField(upload_to='userprofile', blank=True)
    company        = models.CharField(max_length=100, blank=True)
    department     = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True, null=True)
    position       = models.CharField(max_length=100, blank=True)
    is_management  = models.BooleanField(default=False)
    request_access = models.BooleanField(default=False)
    is_online      = models.BooleanField(default=False)
    last_logout    = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    

    