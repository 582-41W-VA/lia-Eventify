from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "date_joined", "is_admin")
    list_filter = ("is_admin",)
    search_fields = ("username", "email")
    ordering = ("username",)
    
    readonly_fields = ("date_joined", "last_login")

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Profile Info', {'fields': ('bio', 'profile_picture')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    filter_horizontal = ()

    exclude = ("groups", "user_permissions")

admin.site.register(User, CustomUserAdmin)
