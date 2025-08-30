from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import WastePost, WasteSale
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class WastePostListView(LoginRequiredMixin, ListView):
    model = WastePost
    template_name = "trading/waste_list.html"
    context_object_name = "waste_posts"
    ordering = ["-created_at"]

class WastePostDetailView(LoginRequiredMixin, DetailView):
    model = WastePost
    template_name = "trading/waste_detail.html"
    context_object_name = "waste_posts"

class WastePostCreateView(LoginRequiredMixin, CreateView):
    model = WastePost
    fields = ["title", "description", "quantity", "waste_type", "price"]
    template_name = "trading/waste_form.html"
    success_url = reverse_lazy("waste-list")

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

class WastePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WastePost
    fields = ["title", "description", "quantity", "waste_type", "price"]
    template_name = "trading/waste_form.html"
    success_url = reverse_lazy("waste-list")

    def test_func(self):
        post = self.get_object()
        return post.posted_by == self.request.user

class WastePostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WastePost
    template_name = "trading/waste_confirm_delete.html"
    success_url = reverse_lazy("waste-list")

    def test_func(self):
        post = self.get_object()
        return post.posted_by == self.request.user

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        messages.success(request, f'Your post "{post.title}" was deleted successfully.')
        return super().delete(request, *args, **kwargs)



@login_required
def buy_waste(request, pk):
    """Allow a logged-in recycler to buy a waste post."""
    waste_post = get_object_or_404(WastePost, pk=pk)

    # Prevent the seller from buying their own waste
    if waste_post.posted_by == request.user:
        messages.error(request, "You cannot buy your own waste post.")
        return redirect("waste-list")

    # Check if already purchased
    if WasteSale.objects.filter(
        waste_post=waste_post, buyer=request.user
    ).exists():
        messages.warning(request, "You have already purchased this waste.")
        return redirect("post-detail", pk=waste_post.pk)

    # Create the WasteSale record
    WasteSale.objects.create(
        waste_post=waste_post,
        buyer=request.user,
        seller=waste_post.user
    )

    messages.success(request, "You successfully purchased this waste!")
    return redirect("waste-list")