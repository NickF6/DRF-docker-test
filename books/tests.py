from django.test import TestCase
from .models import Customer, Book
from .serializers import CustomerSerializer, BookSerializer
import datetime
from django.utils.timezone import make_aware
# two things you want to test are the 7, 14 day lists, and the google api
# check that a valid coutry been selected.

# Create your tests here.
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create a customer
        Customer.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            country="AU"
        )
        Customer.objects.create(
            first_name="John",
            last_name="Smith",
            email="john.smith@example.com",
            country="QQ"
        )
        # Set up non-modified objects used by all test methods
        Book.objects.create(
            customer=Customer.objects.get(id=1),
            title='Moby Dick',
            author = 'Herman Melville',
            isbn = '9780553213119',
        )
        # set up second book
        Book.objects.create(
            customer=Customer.objects.get(id=1),
            title = "A Room of One's Own",
            author = "Virginia Woolf",
            isbn = "9780156787338",
        )
        # set up third book
        Book.objects.create(
            customer=Customer.objects.get(id=1),
            title = "War and Peace",
            author = "Leo Tolstoy",
            isbn = "9780241265543",
        )

    def setUp(self):
        self.valid_book_entry = {
            "customer": 1,
            "title": "Ulysses",
            "author": "James Joyce",
            "isbn": "9780192834645"
        }
        self.invalid_book_entry = {
            'customer': 1,
            'title': 'The White Whale',
            'author': 'Herman Melville',
            'isbn': '9780553213119'
        }
        self.valid_country = {
            "first_name": "Jason",
            "last_name": "Smith",
            "email": "jason.smith@example.com",
            "country": "AU"
        }
        self.invalid_country = {
            "first_name": "John",
            "last_name": "Smith",
            "email": "john.smith@example.com",
            "country": "FAKE_PLACE"
        }


    def test_customer_email(self):
        customer = Customer.objects.get(id=1)
        field_label = customer._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_count_of_books_saved(self):
        response = self.client.get('/book/')
        self.assertEqual(3, len(response.data))

    def test_books_last_week(self):
        # force update one book to be added 10 days ago
        lastweek = datetime.datetime.now() - datetime.timedelta(days=10)
        Book.objects.filter(pk=1).update(created_at=make_aware(lastweek))
        # get the response of books from last week.
        response = self.client.get('/book/last_week/')
        # should be two books now from last week
        self.assertEqual(2, len(response.data))

    def test_all_books_last_week(self):
        # force update one book to be added 10 days ago
        lastweek = datetime.datetime.now() - datetime.timedelta(days=10)
        # for all books to be updated last week
        for i in range(1, Book.objects.all().count()+1):
            # force update the date of all books.
            Book.objects.filter(pk=i).update(created_at=make_aware(lastweek))
        # get the response of books from last week.
        response = self.client.get('/book/last_week/')
        # should be two books now from last week
        self.assertEqual(0, len(response.data))

    def test_books_last_fornight(self):
        # force update one book to be added 10 days ago
        last_fornight = datetime.datetime.now() - datetime.timedelta(days=20)
        Book.objects.filter(pk=1).update(created_at=make_aware(last_fornight))
        # get the response of books from last week.
        response = self.client.get('/book/last_fornight/')
        # should be two books now from last week
        self.assertEqual(2, len(response.data))

    def test_all_books_last_(self):
        # force update one book to be added 10 days ago
        lastweek = datetime.datetime.now() - datetime.timedelta(days=10)
        Book.objects.filter(pk=1).update(created_at=make_aware(lastweek))
        last_fornight = datetime.datetime.now() - datetime.timedelta(days=20)
        Book.objects.filter(pk=2).update(created_at=make_aware(last_fornight))
        # get the response of books from last week.
        response = self.client.get('/book/last_fornight/')
        # should be two books now from last week
        self.assertEqual(2, len(response.data))

    def test_google_api_for_valid_book(self):
        response = self.client.post('/book/', self.valid_book_entry)
        self.assertTrue(201, response.status_code)

    def test_valid_country(self):
        response = self.client.post('/customer/', self.valid_country)
        self.assertTrue(200, response.status_code)

    def test_invalid_country(self):
        response = self.client.post('/customer/', self.invalid_country)
        self.assertTrue(400, response.status_code)

    # def test_valid_country


# print(self.valid_book_one)
# print("HERE J")
# print(response)
# print(response.status_code)
# self.book = Book.objects.create(**self.invalid_book_one)
# print("HERE F")
# print(self.book)
# print(self.book.__dict__)
# print("HERE Y")
# self.client.post('/book/last_fornight/')
# self.serializer = BookSerializer(data=Book.objects.get(id=1))
# print(self.serializer)
# print(type(self.serializer))
# self.data = self.serializer.is_valid()
# print(self.data)
# self.assertTrue(self.serializer.is_valid())


# print("HERE W")
# print(response.data)
# print(len(response.data))
# def test_view_url_exists_at_desired_location(self):
#     response = self.client.get('/book/')
#     print("HERE W")
#     print(response.data)
#     print(len(response.data))
#     self.assertEqual(response.status_code, 200)

#     def test_books_add_last_week(self):
#         # force update the create_at date of one book
#          = datetime.datetime.now() - datetime.timedelta(days=10)
# FooBar.objects.filter(pk=foo.pk).update(updated_at=lastweek)


# def test_false_is_false(self):
#     print("Method: test_false_is_false.")
#     self.assertFalse(False)
#
# def test_false_is_true(self):
#     print("Method: test_false_is_true.")
#     self.assertTrue(False)
#
# def test_one_plus_one_equals_two(self):
#     print("Method: test_one_plus_one_equals_two.")
#     self.assertEqual(1 + 1, 2)
