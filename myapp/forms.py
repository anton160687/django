from django import forms
from .models import Order, Product
from .widgets import ProductCheckboxSelectMultiple

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'products', 'total_price']
        widgets = {
            'products': ProductCheckboxSelectMultiple(),
        }