from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Email')
    phone = PhoneNumberField(unique=True, region='RU')
    avatar = models.ImageField(upload_to='user/avatar', blank=True, null=True, verbose_name='Аватар')
    country = models.CharField(max_length=200, blank=True, null=True, verbose_name='Страна')

    token = models.CharField(max_length=200, blank=True, null=True, verbose_name='Token')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['email']