from django.db import models
from django_countries.fields import CountryField

# the customer model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    country = CountryField()

    def __str__(self):
        return self.first_name

# the book model
class Book(models.Model):
    customer = models.ForeignKey(Customer, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
