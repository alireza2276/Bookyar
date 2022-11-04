from books.models import Book, Category


def show_book_list(request):
    new_book = Book.objects.order_by('-datetime_created')[:4]

    return {'new_book': new_book}


def show_category(request):
    category = Category.objects.order_by('-datetime_created')

    return {'category': category}


def show_discount_book(request):
    discount = Book.objects.filter(fantastic_discount=True)[:4]

    return {'discount': discount}
