        Week3 
start by creating a custom User model that inherits from AbstractUser
create role choice (waste_generator and waste_recyclers).
change the project auth model to use our custom model.
Create waste post model
register the models to our admin panel and test waste posting.
make migrations and create a superuser.
NB: Do not make migrations before setting up the custom user model to avoid complications which can only be solved by deleting the database.
Change database to Postgre in week 5
To use just email and password for authentication, create a custom UserManager.

        Week4
Use Django's built-in Login and Logout View which provide secure sessions, password hashing and redirects.
Create a custom user registration form with roles which extends the CustomUser Model.
Create a registartion view that handles POST request and saves user data upon registration. For GET request, it renders the registration template for data input.
Create a user dashboard that requires login for both users.
Use Django's signal to automatically create a user profile after registration.
Create a base template where all styling will be done using bootstrap in future.
