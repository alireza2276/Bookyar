from books.models import Book


def show_book_list(request):
    new_book = Book.objects.order_by('-datetime_created')[:4]

    return {'new_book': new_book}