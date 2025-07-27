from django.urls import path
from .views import view_all_books, LibraryDetailView

urlpatterns = [
    path('books/', view_all_books, name='all_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
