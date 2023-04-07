from django.contrib import admin

from .models import BookAuthor, Book, Category

# Register your models here.

admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(Category)
