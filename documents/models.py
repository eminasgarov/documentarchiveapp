from django.db import models
from category.models import DocumentVariation, Department, DocumentSection

# Create your models here.

class Document(models.Model):
    document_section        = models.ForeignKey(DocumentSection, on_delete=models.CASCADE)
    document_id             = models.CharField(max_length=100, unique=True)
    document_name           = models.CharField(max_length=200)
    document_type           = models.ForeignKey(DocumentVariation, on_delete=models.CASCADE)
    department              = models.ForeignKey(Department, on_delete=models.CASCADE)
    document_file           = models.FileField(upload_to='documents/%Y/%m/%d/')
    document_date           = models.CharField(max_length=20)
    access_for_all          = models.BooleanField(default=False)
    is_featured             = models.BooleanField(default=False)
    created_date            = models.DateTimeField(auto_now_add=True)
    modified_date           = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.document_id
