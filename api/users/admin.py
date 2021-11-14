from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import CustomUser

# Register your models here.

class CustomUserAdmin(ModelAdmin):
    readonly_fields = ('password', 'created_at', 'updated_at', 'agreed_on_terms')
    fieldsets = (
        ('Personal Information', {'fields': ('first_name','last_name', 'date_of_birth')}),
        ('Account Information', {'fields': ('email', 'password', 'created_at', 'updated_at', 'profile', 'agreed_on_terms')})
    )


admin.site.register(CustomUser, CustomUserAdmin)