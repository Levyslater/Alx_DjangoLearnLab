from . import views as userviews 
from django.urls import path


urlpatterns = [
    path('books/', userviews.BookListView.as_view(), name='book-list'),
    path('books/create/', userviews.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', userviews.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', userviews.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', userviews.BookDeleteView.as_view(), name='book-delete'),
]