from django.urls import path
from . import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', user_views.list_books, name='all_books'),
    path('library/<int:pk>/', user_views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', user_views.register_user, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]