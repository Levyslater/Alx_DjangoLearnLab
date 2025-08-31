from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Profile
from django import forms
from django.contrib.auth.models import User


class CustomUserRegistrationForm(UserCreationForm):
    """Creates a custom user registration form that extendes the default UserCreationForm
    to include additional fields like email, first_name, last_name, phone_number, and role
    """
    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "phone_number", "role", "password1", "password2"]
        
        

class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False, max_length=30)
    last_name = forms.CharField(required=False, max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = Profile
        fields = ["phone_number", "location", "bio"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)  # pass request.user when instantiating
        super().__init__(*args, **kwargs)

        if user:
            self.fields["first_name"].initial = user.first_name
            self.fields["last_name"].initial = user.last_name
            self.fields["email"].initial = user.email

    def save(self, commit=True):
        profile = super().save(commit=False)
        user = profile.user

        # Save User fields
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")
        user.email = self.cleaned_data.get("email")

        if commit:
            user.save()
            profile.save()
        return profile
