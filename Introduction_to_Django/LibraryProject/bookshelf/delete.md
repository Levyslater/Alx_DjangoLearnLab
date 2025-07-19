# deletes the first Book instance
Book.objects.filter(title='Ninetenn Eighty-Four').delete()

# Expected output after deletion: NO error