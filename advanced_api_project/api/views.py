from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book if user is authenticated.
    This view uses the BookSerializer to validate and save the book data.
    
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class BookListView(generics.ListAPIView):
    """
    This view lists all available book instances even if the user is
    not logged in
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book instance.
    This view uses the BookSerializer to validate and save the updated book data.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete an existing book instance.
    This view uses the BookSerializer to validate and delete the book data.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book instance.
    This view uses the BookSerializer to serialize the book data.
    """
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [permissions.AllowAny]