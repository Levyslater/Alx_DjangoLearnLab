# deletes the first Book instance
x = Book.objects.all()[0]
x.delete()

# Expected output after deletion: NO error