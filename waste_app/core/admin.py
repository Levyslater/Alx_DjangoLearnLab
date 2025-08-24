from django.contrib import admin
from .models import CustomUser, WastePost
# Register your models here.

# admin.site.register() takes a list or tuple of models
admin.site.register(CustomUser)
admin.site.register(WastePost)
