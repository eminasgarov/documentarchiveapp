from django.contrib import admin
from documents.models import Procedure

# Register your models here.
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('document_type', 'procedure_id', 'procedure_name', 'department', 'procedure_date', 'is_featured', 'created_date', 'modified_date')
    list_display_links = ('procedure_id', 'procedure_name')
    list_editable = ('is_featured',)
    search_fields = ('procedure_name', 'department')
    list_filter = ('department',)

admin.site.register(Procedure, ProcedureAdmin)
