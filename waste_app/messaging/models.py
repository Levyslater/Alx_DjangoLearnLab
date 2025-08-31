from django.db import models
from django.conf import settings
from trading.models import WastePost 

class Message(models.Model):
    """Model to handle messages between users, optionally linked to a WastePost."""
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
    waste_post = models.ForeignKey(
        WastePost,
        related_name="messages",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def receiver_phone(self):
        """Return the receiver's phone number if available, else 'N/A'."""
        return getattr(self.receiver.profile, "phone_number", "N/A")

    def receiver_location(self):
        """Return the receiver's location if available, else 'N/A'."""
        return getattr(self.receiver.profile, "location", "N/A")

    def __str__(self):
        """String representation of the message."""
        if self.waste_post:
            return f"Message (waste-related) from {self.sender} to {self.receiver}"
        return f"Message (general) from {self.sender} to {self.receiver}"
