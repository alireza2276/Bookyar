from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from books.forms import CommentForm
from books.models import Book, Category
from django.utils.translation import gettext_lazy as _
from django.contrib import messages


class BooksListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'books/books_list.html'
    paginate_by = 4


#
# class BooksDetailView(DetailView):
#     model = Book
#     template_name = 'books/books_detail.html'
#     context_object_name = 'book'
#
@login_required
def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book_comment = book.comments.all()

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, _('Your comment successfully added'))
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(request, 'books/books_detail.html',
                  {'book': book, 'comments': book_comment, 'comment_form': comment_form})


class BooksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Book
    fields = ['title', 'author', 'translation', 'publication', 'price', 'discount', 'image', 'description']
    template_name = 'books/books_create.html'
    success_message = _('Your book successfully added')

    def form_valid(self, form):
        book = form.save(commit=False)
        book.user = self.request.user
        book.save()
        return super().form_valid(form)


class BooksUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'translation', 'publication', 'price', 'discount', 'image', 'description']
    template_name = 'books/books_update.html'
    success_message = _('Your book successfully updated')

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


def category(request, pk=None):
    categories = get_object_or_404(Category, id=pk)
    books = categories.categories.all()
    return render(request, 'books/books_list.html', {'categories': categories, 'books': books})



