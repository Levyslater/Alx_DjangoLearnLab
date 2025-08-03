# retrieves all Book instance

book = Book.objects.get(title='1984')
# Expected Output: return the Book object titled 1984