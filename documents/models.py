from django.db import models
from category.models import Document, Department

# Create your models here.

class Procedure(models.Model):
    procedure_id           = models.CharField(max_length=20, unique=True)
    procedure_name         = models.CharField(max_length=200)
    document_type          = models.ForeignKey(Document, on_delete=models.CASCADE)
    department             = models.ForeignKey(Department, on_delete=models.CASCADE)
    procedure_file         = models.FileField(upload_to='procedures/%Y/%m/%d/')
    procedure_date         = models.CharField(max_length=20)
    is_featured            = models.BooleanField(default=False)
    created_date           = models.DateTimeField(auto_now_add=True)
    modified_date          = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.procedure_id
    
    

    