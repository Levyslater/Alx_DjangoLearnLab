from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """ Form for creating a new user with email and password.
    """
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'username', 'date_of_birth', 'profile_photo')
    
    
class CustomUserChangeForm(UserChangeForm):
    """ Form for updating an existing user.
    """

    class Meta:
        model = CustomUser
        fields = ('email', 'username','date_of_birth', 'profile_photo')