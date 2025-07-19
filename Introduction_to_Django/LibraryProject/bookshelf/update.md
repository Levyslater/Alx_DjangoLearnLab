# updates the first Book insatance attribute value

Book.objects.filter(title='1984').update(title='Nineteen Eighty-Four)

#Expected output: Object title is now Nineteen Eighty-Four