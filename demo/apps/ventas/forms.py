from django import forms
from models import Producto

# Form para el producto 
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Producto
    