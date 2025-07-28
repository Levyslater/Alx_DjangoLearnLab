from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class UserProfile(models.Model):
    """Extends the built-in User model with a role field."""
    
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')
    
    def __str__(self):
        return f"{self.user.username} - {self.role}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile whenever a new User is created."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Ensure the profile is saved when the User is saved."""
    instance.profile.save()
