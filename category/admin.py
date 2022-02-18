from django.contrib import admin
from .models import Document, Department, DocumentSection

# Register your models here.

class DocumentSectionAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('document_section',)}
    list_display            = ('document_section', 'slug')

class DocumentAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('document_type',)}
    list_display            = ('document_type', 'slug')
    
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields     = {'slug': ('department',)}
    list_display            = ('department', 'slug')
    

admin.site.register(Document, DocumentAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(DocumentSection, DocumentSectionAdmin)