from django.contrib import admin
from .models import SupportTeam, Email

# Register your models here.

class SupportTeamAdmin(admin.ModelAdmin):
    list_display        = ('support_title', 'first_name', 'last_name', 'email', 'phone', 'created_date')
    list_display_links  = ('first_name', 'last_name')
    
admin.site.register(SupportTeam, SupportTeamAdmin)

class EmailAdmin(admin.ModelAdmin):
    list_display        = ('first_name', 'last_name', 'email', 'subject', 'created_date')
    list_display_links  = ('subject',)
    
admin.site.register(Email, EmailAdmin)