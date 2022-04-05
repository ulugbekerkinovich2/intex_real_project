from django.contrib import admin
from basic_app import models
# Register your models here.
admin.site.register(models.Zakaz)
admin.site.register(models.Naduvnie)
admin.site.register(models.Kansultatsi)
admin.site.register(models.Karkas)
from django.contrib.auth.admin import UserAdmin




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