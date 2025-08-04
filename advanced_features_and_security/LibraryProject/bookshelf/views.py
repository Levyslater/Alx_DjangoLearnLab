from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Author
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView



class SignUpView(CreateView):
    
    """Handles user registration."""
    form_class = UserCreationForm
    template_name = 'bookshelf/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/display_books.html', {'books': books})


# Add Book (Admin & Librarian)
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    """Handles the addition of a new book."""
    if request.method == 'POST':
        # Handle the form submission to add a new book
        title = request.POST['title']
        author = Author.objects.get(id=request.POST['author_id'])
        Book.objects.create(title=title, author=author)
        return redirect('all_books')

    # If GET request, render the form to add a new book
    # Assuming you have a form to select an author
    # For simplicity, we will just list all authors
    authors = Author.objects.all()
    return render(request, 'bookshelf/add_book.html', {'authors': authors})


# Update Book (Admin & Librarian)
@permission_required('bookshelf.can_edit', raise_exception=True)
def change_book(request, book_id):
    """Handles the update of an existing book."""
    """Fetches the book by ID and updates its details."""
    """Requires permission to update a book."""
    """If the book does not exist, it raises a 404 error."""
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = Author.objects.get(id=request.POST['author_id'])
        book.save()
        return redirect('all_books')
    # If GET request, render the form to update the book
    # Assuming you have a form to select an author
    # For simplicity, we will just list all authors
    authors = Author.objects.all()
    return render(request, 'bookshelf/update_book.html', {'book': book, 'authors': authors})


# Delete Book (Admin only)
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    """Handles the deletion of a book."""
    """Fetches the book by ID and deletes it."""
    """Requires permission to delete a book."""
    """If the book does not exist, it raises a 404 error."""
    """Redirects to the list of all books after deletion."""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('all_books')
