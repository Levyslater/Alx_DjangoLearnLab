# updates the first Book insatance attribute value

x = Book.objects.all()[0]
x.title = 'Nineteen Eighty-Four'
x.save()

#Expected output: x.title 'Nineteen Eighty-Four'