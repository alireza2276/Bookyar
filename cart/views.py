from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy

from books.models import Book
from .cart import Cart
from .forms import AddToCartBookForm, OrderForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Order


@login_required
def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['book_update_quantity_form'] = AddToCartBookForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    return render(request, 'cart/cart_detail.html', {'cart': cart})


@require_POST
def add_to_cart_view(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)

    form = AddToCartBookForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = cleaned_data['quantity']

        cart.add(book, quantity, replace_current_quantity=cleaned_data['inplace'])

    return redirect('cart:cart_detail')


def remove_cart_view(request, book_id):
    cart = Cart(request)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book)

    return redirect('cart:cart_detail')


class Checkout(CreateView):
    model = Order
    template_name = 'cart/checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('home')











