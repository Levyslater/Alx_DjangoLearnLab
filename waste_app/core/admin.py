from django.contrib import admin
from .models import CustomUser
from trading.models import WastePost, WasteSale
from messaging.models import Message

"""
admin.site.register() provides basic CRUD operations and return ModelAdmin instances
For more control, we use a custom admin class with searches, filters, and other features.
"""
@admin.register(WastePost)
class WastePostAdmin(admin.ModelAdmin):
    # create columns to show
    list_display = ('title', 'posted_by', 'created_at', 'updated_at')
    # add a search bar 
    search_fields = ('title', 'waste_type')
    # add filters on the right
    list_filter = ('waste_type', 'created_at')
    ordering = ('-created_at',)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # create columns to show
    list_display = ('email', 'role', 'is_active', 'is_staff')
    # add a search bar
    search_fields = ('email', 'role')
    # add filters on the right
    list_filter = ('role', 'is_active', 'is_staff')
    ordering = ('-is_active',)

@admin.register(WasteSale)
class WasteSaleAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'seller', 'waste_post', 'created_at')
    search_fields = ('buyer__email', 'seller__email', 'waste_post__title')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__email', 'receiver__email', 'context')
    list_filter = ('timestamp',)
    ordering = ('-timestamp',)
