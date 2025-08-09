from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from .views import BooklistView

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BooklistView.as_view(), name='book-list'),
    path('', include(router.urls)),
]