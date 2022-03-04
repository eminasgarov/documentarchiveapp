from django.contrib import admin
from .models import SupportTeam, Email, AccessRequest

# Register your models here.

class SupportTeamAdmin(admin.ModelAdmin):
    list_display        = ('support_title', 'first_name', 'last_name', 'email', 'phone', 'created_date')
    list_display_links  = ('first_name', 'last_name')
    
admin.site.register(SupportTeam, SupportTeamAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display        = ('first_name', 'last_name', 'email', 'subject', 'created_date')
    list_display_links  = ('subject',)
    
admin.site.register(Email, EmailAdmin)

class AccessRequestAdmin(admin.ModelAdmin):
    list_display        = ('employee_first_name', 'employee_last_name', 'employee_email', 'employee_department', 'employee_position', 'employee_is_management', 'employee_access_to_request', 'employee_is_admin', 'created_date')
    list_display_links  = ('employee_first_name', 'employee_last_name', 'employee_email')
    
admin.site.register(AccessRequest, AccessRequestAdmin)