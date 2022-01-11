from django.db import models
from category.models import Document, Department

# Create your models here.

class KISDocument(models.Model):
    kis_document_id        = models.CharField(max_length=100, unique=True)
    kis_document_name      = models.CharField(max_length=200)
    document_type          = models.ForeignKey(Document, on_delete=models.CASCADE)
    department             = models.ForeignKey(Department, on_delete=models.CASCADE)
    kis_document_file      = models.FileField(upload_to='kis_documents/%Y/%m/%d/')
    kis_document_date      = models.CharField(max_length=20)
    is_featured            = models.BooleanField(default=False)
    created_date           = models.DateTimeField(auto_now_add=True)
    modified_date          = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.kis_document_id
