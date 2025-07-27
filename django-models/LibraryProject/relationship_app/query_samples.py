"""This module contains sample queries for the library management system.
It demonstrates how to interact with the Author, Book, Library, and Librarian models."""

from .models import Author, Book, Library, Librarian

def get_books_by_author(author_id):
    """Returns a list of books written by a specific author."""
    return Book.objects.get(author_id=author_id)


def get_librarian_for_library(library_id):
    """Returns the librarian for a specific library."""
    return Librarian.objects.get(library_id=library_id)

def get_all_books_in_library(library_name):
    """Returns a list of all books in a specific library."""
    library = Library.objects.get(name=library_name)
    return library.books.all()