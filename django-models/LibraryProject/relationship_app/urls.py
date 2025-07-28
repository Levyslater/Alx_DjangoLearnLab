from django.urls import path
from . import views as user_views

urlpatterns = [
    path('books/', user_views.list_books, name='all_books'),
    path('library/<int:pk>/', user_views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', user_views.register_user, name='register'),
    path('login/', user_views.user_login, name='login'),
    path('logout/', user_views.user_logout, name='logout'),
]