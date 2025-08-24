        Week3 
start by creating a custom User model that inherits from AbstractUser
create role choice (waste_generator and waste_recyclers).
change the project auth model to use our custom model.
Create waste post model
register the models to our admin panel and test waste posting.
make migrations and create a superuser.
NB: Do not make migrations before setting up the custom user model to avoid complications which can only be solved by deleting the database.
Change database to Postgre in week 5