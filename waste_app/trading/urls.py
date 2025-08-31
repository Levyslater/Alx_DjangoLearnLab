from django.urls import path
from . import views

urlpatterns = [
    path("", views.WastePostListView.as_view(), name="waste-list"),
    path("post/new/", views.WastePostCreateView.as_view(), name="waste-create"),
    path("post/<int:pk>/", views.WastePostDetailView.as_view(), name="waste-detail"),
    path("post/<int:pk>/edit/", views.WastePostUpdateView.as_view(), name="waste-update"),
    path("post/<int:pk>/delete/", views.WastePostDeleteView.as_view(), name="waste-delete"),
    path("post/<int:pk>/buy/", views.buy_waste, name="buy-waste"),
]
