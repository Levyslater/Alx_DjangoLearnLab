from django.contrib import admin
from .models import Author, Book

# Register your models here.

admin.site.register(Author, list_display=['name'])
admin.site.register(Book, list_display=['title', 'publication_year', 'author'])