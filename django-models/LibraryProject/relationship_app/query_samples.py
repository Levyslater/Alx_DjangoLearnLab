"""This module contains sample queries for the library management system.
It demonstrates how to interact with the Author, Book, Library, and Librarian models."""

from .models import Author, Book, Library, Librarian

def get_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)


def get_librarian_for_library(library_name):
    """Returns the librarian responsible for a specific library."""
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)

def get_all_books_in_library(library_name):
    """Returns a list of all books in a specific library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()