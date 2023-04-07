from django.views.generic import TemplateView, ListView

from books.models import Book, Category


# Create your views here.

class HomePageView(ListView):
    queryset = Book.objects.order_by('-id')
    template_name = 'home.html'
    context_object_name = 'books'


class CategoriesView(ListView):
    queryset = Category.objects.order_by('-id')
    template_name = 'books/category.html'
    context_object_name = 'categories'
