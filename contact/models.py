from django.db import models
from datetime import datetime


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
    user_id         = models.IntegerField(blank=True, default=0)
    first_name      = models.CharField(max_length=20)
    last_name       = models.CharField(max_length=20)
    email           = models.EmailField(max_length=100)
    subject         = models.CharField(max_length=20)
    message         = models.TextField(blank=True)
    created_date    = models.DateField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email


class AccessRequest(models.Model):
    user_id                    = models.IntegerField(blank=True, default=0)
    first_name                 = models.CharField(max_length=20)
    last_name                  = models.CharField(max_length=20)
    email                      = models.EmailField(max_length=100)
    employee_last_name         = models.CharField(max_length=20)
    employee_first_name        = models.CharField(max_length=20)
    employee_email             = models.EmailField(max_length=100)
    employee_department        = models.CharField(max_length=100)
    employee_position          = models.CharField(max_length=100)
    employee_is_management     = models.CharField(max_length=20)
    employee_access_to_request = models.CharField(max_length=20)
    employee_is_admin          = models.CharField(max_length=20)
    employee_admin_descr       = models.TextField(blank=True)
    created_date               = models.DateField(blank=True, default=datetime.now)
    
    def __str__(self):
        return self.employee_email
