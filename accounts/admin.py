from django.contrib import admin
from accounts.models import UserProfile, UserPermission
from django.utils.html import format_html


# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px" />'.format(object.profile_photo.url))
    
    list_display        = ('user', 'company', 'department', 'position')
    list_display_links  = ('user',)
    search_fields       = ('user', 'department', 'position')
    list_filter         = ('department',) 
    
    
class UserPermissionAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserPermission, UserPermissionAdmin)