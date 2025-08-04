from django.urls import path
from . import views as user_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', user_views.list_books, name='all_books'),
    path('add_book/', user_views.create_book, name='add_book'),
    path('edit_book/<int:book_id>/', user_views.change_book, name='update_book'),
    path('delete_book/<int:book_id>/', user_views.delete_book, name='delete_book'),
    path('login/', LoginView.as_view(template_name='bookshelf/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', user_views.SignUpView.as_view(), name='register'),
]
