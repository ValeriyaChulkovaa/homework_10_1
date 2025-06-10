from django import forms
from .models import Product
from PIL import Image


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


class ProductFormValidator(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'images', 'category', 'purchase_price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название продукта'})
        self.fields['description'].widget.attrs.update(
            {'rows': '2', 'class': 'form-control', 'placeholder': 'Введите описание продукта'})
        self.fields['images'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['purchase_price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите цену'})


    def clean_purchase_price(self):
        price = self.cleaned_data.get('purchase_price')
        if price is not None and price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной.')
        return price

    def clean(self):
        cleaned_data = super().clean()
        DANGER_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        description = cleaned_data.get('description', '').lower()
        name = cleaned_data.get('name', '').lower()

        for word in DANGER_WORDS:
            if word in description:
                self.add_error('description', f'Описание не должно содержать слово "{word}".')
            if word in name:
                self.add_error('name', f'Название не должно содержать слово "{word}".')