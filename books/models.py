from django.conf import settings
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class LanguageType(models.TextChoices):
        UZ = 'uzbek', 'Uzbek'
        EN = 'english', 'English'
        RU = 'russia', 'Russia'

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    slug = models.SlugField(unique=True, null=True)
    sales_price = models.PositiveIntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    pub_year = models.PositiveIntegerField(null=True)
    page_size = models.PositiveIntegerField()
    file = models.FileField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    lang = models.CharField(max_length=50, choices=LanguageType.choices, default=LanguageType.UZ)
    author = models.ForeignKey('BookAuthor', on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} - {self.category}"


class BookAuthor(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
