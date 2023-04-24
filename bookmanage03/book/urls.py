from django.urls import path
from book.views import add_book
urlpatterns = [
    path('add/book/', add_book)
]