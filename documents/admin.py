from django.contrib import admin
from documents.models import KISDocument
# Register your models here.
class KISDocumentAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'kis_document_id', 'kis_document_name', 'department', 'kis_document_date', 'is_featured', 'created_date', 'modified_date')
    list_display_links = ('kis_document_id', 'kis_document_name')
    list_editable = ('is_featured',)
    search_fields = ('kis_document_name', 'department')
    list_filter = ('department', 'document_type')

admin.site.register(KISDocument, KISDocumentAdmin)

