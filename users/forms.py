from .models import User
# from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields["password"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите пароль'})



class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'phone', 'avatar', 'country', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите email'})
        self.fields["phone"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите номер телефона'})
        self.fields["avatar"].widget.attrs.update({'class': 'form-control-file'})
        self.fields["country"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите страну'})
        self.fields["password1"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите пароль'})
        self.fields["password2"].widget.attrs.update({'class': 'form-control', 'placeholder': 'Повторите пароль'})