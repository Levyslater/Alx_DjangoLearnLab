from django.db import models

# Create your models here.

"""This module defines the models for a library management system.
It includes models for Author, Book, Library, and Librarian."""


class Author(models.Model):
    """This model represents an author in the library management system."""
    name = models.CharField(max_length=100)

    def __str__(self):
        """Returns the name of the author."""
        return self.name


class Book(models.Model):
    """This model represents a book in the library management system."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        """Returns the title of the book."""
        return self.title


class Library(models.Model):
    """This model represents a library in the library management system."""
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        """Returns the name of the library."""
        return self.name


class Librarian(models.Model):
    """This model represents a librarian in the library management system."""
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the name of the librarian."""
        return self.name