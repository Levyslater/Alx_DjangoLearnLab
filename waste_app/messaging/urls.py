from django.urls import path
from . import views

urlpatterns = [
    # Inbox
    path("inbox/", views.inbox, name="inbox"),

    # General messaging (choose a receiver manually or use the CreateView)
    path("send/", views.GeneralMessageCreateView.as_view(), name="send_general_message"),

    # Send a message to a specific user (general one-to-one messaging)
    path("send/<int:receiver_id>/", views.send_message, name="send_message"),

    # Send a message tied to a waste post
    path("send/waste/<int:waste_id>/", views.send_message, name="send_waste_message"),
]
