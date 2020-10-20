from django.contrib import admin

from .models import Customer, Book

class Customerdmin(admin.ModelAdmin):
    model = Customer

class DesignInputAdmin(admin.ModelAdmin):
    model = Book
