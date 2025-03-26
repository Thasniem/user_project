from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, ActivityLog

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_active', 'created_at')
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('phone_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'phone_number'),
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'updated_at')
    search_fields = ('user__username', 'user__email', 'location')
    list_filter = ('updated_at',)
    readonly_fields = ('updated_at',)

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'activity_timestamp')
    search_fields = ('user__username', 'activity_type', 'details')
    list_filter = ('activity_type', 'activity_timestamp')
    ordering = ('-activity_timestamp',)
    readonly_fields = ('activity_timestamp',)