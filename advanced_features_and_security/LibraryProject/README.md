
The Bookshelf App is a Django-based application for managing a collection of books. It demonstrates how to implement custom permissions on a model (Book) and protect views using these permissions.

                Features
    Custom User Permissions on the Book model:

        bookshelf.can_view – Allows viewing books.

        bookshelf.can_add – Allows adding new books.

        bookshelf.can_edit – Allows editing existing books.

        bookshelf.can_delete – Allows deleting books.

     Permission-Based Access Control using Django’s @permission_required decorator.

    Simple CRUD interface protected by relevant permissions.