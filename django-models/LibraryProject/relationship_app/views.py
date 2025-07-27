from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

def view_all_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/list_books.html', context)


class LibraryDetailView(DetailView):
    """Displays details of a specific library and lists all its books."""
    model = Library
    template_name = 'books/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(libraries=self.object)
        return context
