from django.db import models
from django.conf import settings
from core.models import CustomUser


# Create your models here.

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
        return f"{self.waste_post.title} sold by {self.seller.email} to {self.buyer.email}"


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
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    waste_type = models.CharField(max_length=20, choices=WASTE_TYPE_CHOICES)
    image = models.ImageField(upload_to='waste_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="waste_posts")
    is_sold = models.BooleanField(default=False)


    def __str__(self):
        """
        create a pseudo username by splitting the email at the '@' symbol.
        Note if two users have the same prefix but different domains, they will have the same pseudo username.
        """
        return f"{self.title} by {self.posted_by.email.split('@')[0]}"
  