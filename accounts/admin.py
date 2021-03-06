from django.contrib import admin
from accounts.models import UserProfile
from django.utils.html import format_html


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.profile_photo.url))
    
    list_display        = ('user', 'company', 'department', 'position', 'is_management', 'request_access')
    list_display_links  = ('user',)
    list_editable       = ('is_management',)
    search_fields       = ('user', 'department', 'position')
    list_filter         = ('department', 'is_management', 'request_access') 
    
    
admin.site.register(UserProfile, UserProfileAdmin)