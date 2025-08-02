from django.urls import path
from . import views as user_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('books/', user_views.list_books, name='all_books'),
    path('library/<int:pk>/', user_views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', user_views.SignUpView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('admin/', user_views.admin_view, name='admin_view'),
    path('librarian/', user_views.librarian_view, name='librarian_view'),
    path('member/', user_views.member_view, name='member_view'),
    path('add_book/', user_views.add_book, name='add_book'),
    path('update_book/<int:book_id>/', user_views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', user_views.delete_book, name='delete_book'),

]