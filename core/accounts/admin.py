from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.




class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'first_name', 'is_staff', 'is_superuser']
    search_fields = ['email']
    ordering = ('-date_joined',)
    fieldsets = (
        ('Authentication', {"fields": ('email',)}),
        ("Permissions", {"fields": ('is_staff', 'is_active')}),
        ("Group Permission", {'fields':('groups', 'user_permission',)}),
        ("Important dates", {'fields':('last_login',)}),
        )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1', 
                    'password2',
                    'is_active',
                    'id_staff',
                ),
            },
        ),
    )
    
admin.site.register(User, CustomUserAdmin)    
