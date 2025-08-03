from .models import Book
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    """Custom admin for the CustomUser model."""
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    link_display = ['email', 'username', 'is_staff', 'is_active',]
    list_filter = ('is_staff', 'is_active', 'date_of_birth')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'username', 'profile_picture')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2', 'date_of_birth', 'profile_picture')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
admin.site.register(CustomUser, CustomUserAdmin)

def profile_picture_tag(obj):
    """Returns an HTML image tag for the profile picture."""
    if obj.profile_picture:
        return format_html('<img src="{}" width="50" height="50" />', obj.profile_picture.url)
    return 'No picture'