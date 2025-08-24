from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    """
    Create a custom user model that extends the Abstract user with
    extra fields
    """
    # Add any additional fields you want to include in your custom user model
    # create a tuple with user choices which are immutable
    ROLE_CHOICES = ( ('generator', 'Waste Generator'),
                    ('recycler', 'Recycler'),
                    )
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    # remove username to use email for login by making it None
    username = None
    # Now make email unique to authenticate users
    email = models.EmailField(unique=True)
    # Now use email for login instead of default username
    USERNAME_FIELD = 'email'
    # make username field not required
    REQUIRED_FIELDS = []

    def __str__(self):
        """whenever you define a choices field, 
        Django automatically creates a method called get_fieldname_display()
        that returns a human readable version of the field's value.
        """
        return f"{self.username} ({self.get_role_display()})"


class WastePost(models.Model):
    """
    This model handles creation of waste posts as instances
    """
    WASTE_TYPE_CHOICES = (
        ('plastic', 'Plastic'),
        ('metal', 'Metal'),
        ('paper', 'Paper'),
        ('organic', 'Organic'),
        ('electronic', 'Electronic'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES)
    image = models.ImageField(upload_to='waste_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.posted_by.username}"