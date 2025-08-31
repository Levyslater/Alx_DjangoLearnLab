from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm, ProfileUpdateForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from trading.models import WastePost
from messaging.models import Message

def register(request):
    """Handle user registration."""
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("dashboard")
    else:
        form = CustomUserRegistrationForm()
    return render(request, "core/register.html", {"form": form})


@login_required
def dashboard(request):
    """
    Render a simplified dashboard with links to key sections and awareness info.
    """
    user = request.user

    waste_tips = [
        "Separate your waste into recyclables, compostables, and general waste.",
        "Avoid burning plastic as it releases harmful chemicals.",
        "Use reusable bags instead of plastic bags.",
        "Compost organic kitchen waste to reduce landfill usage.",
    ]

    context = {
        "user": user,
        "waste_tips": waste_tips,
    }

    return render(request, "core/dashboard.html", context)



@login_required
def profile(request):
    """
    Render the profile page for the logged-in user.
    """
    context = {'user': request.user}
    return render(request, "core/profile.html", context)


User = get_user_model()

@login_required
def profile_update(request):
    """Allow users to update their profile and user info."""
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect("profile")
    else:
        form = ProfileUpdateForm(instance=profile, user=request.user)

    return render(request, "core/profile_form.html", {"form": form})