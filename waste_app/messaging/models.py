from django.db import models
from django.conf import settings


# Create your models here.

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
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def receiver_phone(self):
        return getattr(self.receiver.profile, "phone_number", "N/A")

    def receiver_location(self):
        return getattr(self.receiver.profile, "location", "N/A")


    def __str__(self):
        """
        
        """
        return f"Message from {self.sender} to {self.receiver} at {self.timestamp}"