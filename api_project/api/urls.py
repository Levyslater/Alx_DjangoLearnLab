from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from .views import BooklistView
from rest_framework.authtoken.views import obtain_auth_token


# Create a router and register our viewset with it.
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BooklistView.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('token/', obtain_auth_token),
]