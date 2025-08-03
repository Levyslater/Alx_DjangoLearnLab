# updates the first Book insatance attribute value

book = Book.objects.get(id=1)
book.title = 'Nineteen Eighty-Four'
book.save()

#Expected output: Object title is now Nineteen Eighty-Four