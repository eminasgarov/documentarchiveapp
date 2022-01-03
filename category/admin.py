from django.contrib import admin
from .models import Document, Department

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('document_type',)}
    list_display            = ('document_type', 'slug')
    
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('department',)}
    list_display            = ('department', 'slug')
    

admin.site.register(Document, DocumentAdmin)
admin.site.register(Department, DepartmentAdmin)