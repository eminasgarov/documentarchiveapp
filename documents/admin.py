from django.contrib import admin
from documents.models import Document
# Register your models here.
class DocumentAdmin(admin.ModelAdmin):
    list_display        = ('document_section', 'document_type', 'document_id', 'document_name', 'department', 'access_for_all', 'document_date', 'is_featured', 'created_date', 'modified_date')
    list_display_links  = ('document_id', 'document_name')
    list_editable       = ('is_featured', 'access_for_all')
    search_fields       = ('document_name', 'department')
    list_filter         = ('document_section', 'department', 'document_type', 'access_for_all')

admin.site.register(Document, DocumentAdmin)

