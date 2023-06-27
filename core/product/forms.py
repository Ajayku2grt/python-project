from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
