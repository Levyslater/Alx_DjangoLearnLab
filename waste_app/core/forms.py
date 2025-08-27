from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    """Creates a custom user registration form that extendes the default UserCreationForm
    to include additional fields like email, first_name, last_name, phone_number, and role
    """
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "phone_number", "role", "password1", "password2"]
