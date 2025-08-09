from django.shortcuts import render
from .models import Book
from rest_framework import generics
from .serializers import BookSerializer
from rest_framework import viewsets

# Create your views here.
class BooklistView(generics.ListAPIView):
    """
    A view to list all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer