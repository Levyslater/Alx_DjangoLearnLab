from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from .models import Library, Book, Author
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required, user_passes_test
from .utils import is_admin, is_librarian, is_member



class LibraryDetailView(DetailView):
    """Displays details of a specific library and lists all its books."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        """Adds the list of books in the library to the context."""
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(libraries=self.object)
        return context

# def register_user(request):
#     """Handles user registration."""
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('all_books')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})


# def user_login(request):
#     """Handles user login."""
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, f"Welcome back, {username}!")
#                 return redirect('all_books')  # Redirect to a page after login
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     else:
#         form = AuthenticationForm()
    
#     return render(request, 'relationship_app/login.html', {'form': form})

# def user_logout(request):
#     """Logs out the user and shows a logout confirmation page."""
#     logout(request)  # Ends the session
#     messages.info(request, "You have successfully logged out.")
#     return render(request, 'relationship_app/logout.html')

class SignUpView(CreateView):
    
    """Handles user registration."""
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after successful registration

@login_required(login_url='/login/')
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required(login_url='/login/')
@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required(login_url='/login/')
@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# View Books (all roles with view permission)
@permission_required('relationship_app.can_view_book', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/display_books.html', {'books': books})


# Add Book (Admin & Librarian)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
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
    return render(request, 'relationship_app/add_book.html', {'authors': authors})


# Update Book (Admin & Librarian)
@permission_required('relationship_app.can_change_book', raise_exception=True)
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
    return render(request, 'relationship_app/update_book.html', {'book': book, 'authors': authors})


# Delete Book (Admin only)
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    """Handles the deletion of a book."""
    """Fetches the book by ID and deletes it."""
    """Requires permission to delete a book."""
    """If the book does not exist, it raises a 404 error."""
    """Redirects to the list of all books after deletion."""
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('all_books')

def custom_permission_denied_view(request, exception=None):
    return render(request, '403.html', status=403)
