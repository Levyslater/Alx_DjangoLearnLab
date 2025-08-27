from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    create a custom base manager that allows users to login with email and password
    """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a user with an email and password.
        """
        if not email:
            raise ValueError("The Email field must be set")
        # make email lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        # set default values for is_staff and is_superuser to True to enable admin access
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


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
    
    objects = CustomUserManager()

    def __str__(self):
        """whenever you define a choices field, 
        Django automatically creates a method called get_<fieldname>_display()
        that returns a human readable version of the field's value.
        """
        prefix = self.email.split('@')[0]
        role = self.get_role_display() if self.role else ""
        return f"{prefix} ({role})" if role else prefix

    def get_profile(self):
        """
        
        """
        return getattr(self, "profile", None)

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
        """
        create a pseudo username by splitting the email at the '@' symbol.
        Note if two users have the same prefix but different domains, they will have the same pseudo username.
        """
        return f"{self.title} by {self.posted_by.email.split('@')[0]}"

class Profile(models.Model):
    """
    User profile model to store additional information about the user.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        
        """
        return f"{self.user.email.split('@')[0]} Profile"
    

class WasteSale(models.Model):
    """
    
    """
    buyer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="purchases",
        on_delete=models.CASCADE
    )
    seller = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sales",
        on_delete=models.CASCADE
    )
    waste_post = models.ForeignKey(
        "WastePost",
        related_name="sales",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sale: {self.waste_post.title} from {self.seller} to {self.buyer}"
    
    
class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="sent_messages",
        on_delete=models.CASCADE
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="received_messages",
        on_delete=models.CASCADE
    )
    context = models.TextField()  # main message body
    timestamp = models.DateTimeField(auto_now_add=True)

    def receiver_phone(self):
        """
        fetches the user phone number if already exists
        """
        return self.receiver.phone_number if hasattr(self.receiver, "phone_number") else "N/A"

    def receiver_location(self):
        """
        fetches the user location if already exists
        """
        return self.receiver.location if hasattr(self.receiver, "location") else "N/A"

    def __str__(self):
        """
        
        """
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"