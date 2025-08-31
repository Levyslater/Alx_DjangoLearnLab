from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request, receiver_id):
    if request.method == "POST":
        content = request.POST.get("content")
        Message.objects.create(
            sender=request.user,
            receiver_id=receiver_id,
            content=content
        )
        return redirect("inbox")
    return render(request, "messaging/send_message.html", {"receiver_id": receiver_id})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by("-timestamp")
    return render(request, "messaging/inbox.html", {"messages": messages})
