from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from books.models import Book


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books-list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'books/books_detail.html'
    context_object_name = 'book'

