from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'preview', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Введите загаловок',
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Введите содержание',
                'class': 'form-control'
            }),
            'preview': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'is_published': forms.CheckboxInput(attrs={})
        }