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
    Render the dashboard with user posts, available posts, and inbox.
    """
    user = request.user

    # Posts created by the logged-in user
    my_posts = WastePost.objects.filter(posted_by=user)

    # Posts available from other users
    available_posts = WastePost.objects.filter(is_sold=False).exclude(posted_by=user)

    # Inbox for the logged-in user
    inbox = Message.objects.filter(receiver=user).order_by("-timestamp")

    context = {
        "user": user,
        "my_posts": my_posts,
        "available_posts": available_posts,
        "inbox": inbox,
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