# deletes the first Book instance
from bookshelf.models import Book


book = Book.objects.get(id=1)
book.delete()

# Expected output: Empty QuerySet[]