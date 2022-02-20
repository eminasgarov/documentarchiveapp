from pyexpat import model
from django.db import models
from django.urls import reverse
# Create your models here.

class DocumentSection(models.Model):
    document_section = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def get_url(self):
        return reverse('documents_by_section', args=[self.slug])
    
    def __str__(self):
        return self.document_section
    

class DocumentVariation(models.Model):
    document_type = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def get_url(self):
        return reverse('documents_by_type', args=[self.slug])
    
    def __str__(self):
        return self.document_type

class Department(models.Model):
    department = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def get_url(self):
        return reverse('documents_by_departments', args=[self.slug])
    
    def __str__(self):
        return self.department
    