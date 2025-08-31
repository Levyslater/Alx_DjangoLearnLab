from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from .models import Message
from trading.models import WastePost

User = get_user_model()


@login_required
def send_message(request, receiver_id=None, waste_id=None):
    """
    Handles both general and waste-specific messages:
    - If waste_id is provided, send a message to the waste post creator.
    - If receiver_id is provided, send a direct message to that user.
    """
    receiver = None
    waste_post = None

    if waste_id:  # waste-specific messaging
        waste_post = get_object_or_404(WastePost, pk=waste_id)
        receiver = waste_post.user  # WastePost creator

    elif receiver_id:  # general messaging
        receiver = get_object_or_404(User, pk=receiver_id)

    if request.method == "POST":
        content = request.POST.get("content")
        if not receiver and not waste_post:  
            # General message dropdown case
            receiver_id = request.POST.get("receiver_id")
            if receiver_id:
                receiver = get_object_or_404(User, pk=receiver_id)

        if receiver and content.strip():
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                waste_post=waste_post,
                content=content
            )
        return redirect("inbox")


@login_required
def inbox(request):
    """Show all messages received by the logged-in user"""
    messages = Message.objects.filter(receiver=request.user).select_related("sender").order_by("-timestamp")
    return render(request, "messaging/inbox.html", {"messages": messages})


class GeneralMessageCreateView(LoginRequiredMixin, CreateView):
    """For general messages only (not tied to a waste post)."""
    model = Message
    fields = ["receiver", "content"]
    template_name = "messaging/send_message.html"
    success_url = reverse_lazy("inbox")

    def form_valid(self, form):
        form.instance.sender = self.request.user
        form.instance.waste_post = None  # Ensure it's a general message
        return super().form_valid(form)
