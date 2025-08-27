from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserRegistrationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

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
    Render the dashboard page upon login.
    """
    return render(request, "core/dashboard.html")