from django.db import models
from datetime import datetime
from category.models import Document


# Create your models here.

class SupportTeam(models.Model):
    support_title   = models.CharField(max_length=100)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    email           = models.EmailField(max_length=100)
    phone           = models.CharField(max_length=20)
    created_date    = models.DateField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.first_name

class Email(models.Model):
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    email           = models.EmailField(max_length=100)
    subject         = models.CharField(max_length=20)
    message         = models.TextField(blank=True)
    created_date    = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email

