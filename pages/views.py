from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from books.models import Category,Book


class HomeView(TemplateView):
    template_name = 'pages/home.html'


def search(request):
    q = request.GET.get('q')
    books = Book.objects.filter(title__icontains=q)
    return render(request, 'books/books_list.html', {'books': books})

