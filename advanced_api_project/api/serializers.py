from rest_framework import serializers
import datetime
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    """Serialize the Author Model.
    This serializer is used to represent the Author model in the BookSerializer.
    """
    class Meta:
        model = Author
        fields = ['name']


class BookSerializer(serializers.ModelSerializer):
    """Serialize the Book Model.
    This serializer is used to represent the Book model, including its related authors.
    The related_name here is irrelevant since we are using the AuthorSerializer to handle author data.
    The create method allows for nested author data to be passed in when creating a new book.
    """
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    def create(self, validated_data):
        """Create a new Book instance with nested author data.
        This method extracts the author data from the validated_data,
        gets or creates the author instance, and then creates the book instance.
        """
        # Extract nested author data (dictionary)
        author_data = validated_data.pop('author')
        
        # Get or create that author
        author, _ = Author.objects.get_or_create(**author_data)
        
        # Create the book linked to that author
        book = Book.objects.create(author=author, **validated_data)
        return book
