from django import forms

from cart.models import Order


class AddToCartBookForm(forms.Form):
    QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 30)]

    quantity = forms.TypedChoiceField(choices=QUANTITY_CHOICES, coerce=int)

    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'phone_number', 'email', 'description', ]
