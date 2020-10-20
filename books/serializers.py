from rest_framework import serializers
from .models import Customer, Book
# required for the google books api call
import urllib.request, json

def google_book_exists(title, author, isbn):
    url = 'https://www.googleapis.com/books/v1/volumes?q=isbn:' + isbn + '+intitle:' + title + '+inauthor:' + author
    url = url.replace(' ', '%20')
    contents = urllib.request.urlopen(url).read()
    res = json.loads(contents.decode("UTF-8"))
    return res['totalItems']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('customer', 'title', 'author', 'created_at', 'isbn')

    def validate(self, data):
        """
        Check that the book can be found in the google book api
        """
        if google_book_exists(data['title'], data['author'], data['isbn']) == 0:
            raise serializers.ValidationError("Book can't be found. Please review inputs.")
        return data
