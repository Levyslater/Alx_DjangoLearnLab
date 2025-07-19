# deletes the first Book instance
book = Book.objects.get(id=1)
book.delete()

# Expected output: Empty QuerySet[]