from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

class CustomUser(AbstractUser):
    """Custom User Model that extends the default Django User model.
    This model can be used to add additional fields or methods in the future."""
      
    email = models.EmailField(unique=True,)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_photo = models.ImageField(upload_to='profile_pics/', blank=True, null=True, 
                                        default='profile_pics/default.jpg')
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        """Returns the username of the user."""
        return self.email or self.username