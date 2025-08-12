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
    """Serialize the Book Model including its related Authors.
    This serializer includes validation to ensure that the publication year
    is not in the future.
    """
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']
        
    def validate(self, data):
        """ Validate the publication year of the book.
        Ensure that the publication year is not in the future.
        """
        if 'publication_year' in data and data['publication_year'] > datetime.date.today():
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data