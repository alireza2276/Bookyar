from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from books.models import Book


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books-list.html'


class BooksDetailView(DetailView):
    model = Book
    template_name = 'books/books_detail.html'
    context_object_name = 'book'


class BooksCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'translation', 'publication', 'price', 'discount', 'image', 'description']
    template_name = 'books/books_create.html'

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super().form_valid(form)


class BooksUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'translation', 'publication', 'price', 'discount', 'image', 'description']
    template_name = 'books/books_update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class BooksDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/books_update.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user




