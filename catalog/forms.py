from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'images', 'category', 'purchase_price']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите название продукта',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Введите описание продукта',
                'class': 'form-control'
            }),
            'images': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'purchase_price': forms.NumberInput(attrs={
                'placeholder': 'Введите цену',
                'class': 'form-control'
            }),
        }