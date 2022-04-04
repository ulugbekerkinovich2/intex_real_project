from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from basic_app import models


class CustomUserAdmin(UserAdmin):
    ordering = ('is_superuser',)
    search_fields = ('username',)
    list_filter = ('username',)
    list_display = ('username', 'is_superuser', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username',
                           'password', 'is_superuser', 'is_staff', 'is_active')}),
        ('Permissions', {'fields': ('groups',)}),
        # ('Group Permissions', {
        # 'classes': ('collapse',),
        # 'fields': ('groups', 'user_permissions',)
        # })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_superuser', 'is_staff', 'is_active')
        }
         ),
    )


admin.site.register(models.CustomUser, CustomUserAdmin)