from books.models import Book
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class Cart:
    def __init__(self, request):
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add(self, book, quantity=1, replace_current_quantity=False):
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': 0}

        if replace_current_quantity:
            self.cart[book_id]['quantity'] = quantity

        else:
            self.cart[book_id]['quantity'] += quantity
        messages.success(self.request, _('book added successfully'))

        self.save()

    def remove(self, book):
        book_id = str(book.id)

        del self.cart[book_id]
        messages.error(self.request, _('book removed successfully'))

        self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)

        cart = self.cart.copy()

        for book in books:
            cart[str(book.id)]['book_obj'] = book

        for item in cart.values():
            item['total_price'] = item['book_obj'].discount * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        book_ids = self.cart.keys()

        return sum(item['book_obj'].discount * item['quantity'] for item in self.cart.values())

















