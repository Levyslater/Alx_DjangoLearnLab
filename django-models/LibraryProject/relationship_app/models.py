from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

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
    
    class Meta:
        permissions = (
            ("can_add_book", "Can add a book"),
            ("can_delete_book", "Can delete a book"),
            ("can_view_book", "Can view books"),
            ("can_change_book", "Can change a book"),
        )

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


@receiver(post_save, sender=UserProfile)
def assign_permissions_based_on_role(sender, instance, **kwargs):
    """Assign permissions dynamically based on user role once a user profile is created."""
    user = instance.user
    content_type = ContentType.objects.get_for_model(Book)

    # Get all custom permissions
    # Permissions for Book model
    add_perm = Permission.objects.get(codename='can_add_book', content_type=content_type)
    delete_perm = Permission.objects.get(codename='can_delete_book', content_type=content_type)
    view_perm = Permission.objects.get(codename='can_view_book', content_type=content_type)
    update_perm = Permission.objects.get(codename='can_change_book', content_type=content_type)

    # Clear old permissions
    user.user_permissions.clear()

    if instance.role == 'Admin':
        # Admin gets all permissions
        user.user_permissions.add(add_perm, delete_perm, view_perm, update_perm)

    elif instance.role == 'Librarian':
        # Librarian gets all except delete
        user.user_permissions.add(add_perm, view_perm, update_perm)

    elif instance.role == 'Member':
        # Member only gets view
        user.user_permissions.add(view_perm)