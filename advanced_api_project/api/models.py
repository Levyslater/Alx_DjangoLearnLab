from django.db import models

# Create your models here.

class Author(models.Model):
    """Django will create a reverse manager since the Book model has a foreign key to Author.
    This allows us to access all books related to an author using the related_name 'authors'.
    """
    name = models.CharField(max_length=50)
    
class Book(models.Model):
    """Model representing a book with a title, publication year, and related authors.
    Note that Django handles the One-to-Many relationship between Book and Author
    by setting  a foreign key on the model with 'many'.
    """
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE)