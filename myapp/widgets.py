from django import forms
from .models import Product


class ProductCheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    template_name = 'products/product_widget.html'

    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if isinstance(label, Product): # Проверяем, что label является объектом Product
            option['image_url'] = label.image.url
            option['name'] = label.name
        return option