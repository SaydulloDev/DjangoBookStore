from django.urls import path

from .views import HomePageView, CategoriesView

urlpatterns = [
    path('', HomePageView.as_view(), name='homePage'),
    path('category/', CategoriesView.as_view(), name='categoryPage')
]
