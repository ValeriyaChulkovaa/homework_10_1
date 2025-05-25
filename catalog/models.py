from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(verbose_name='Описание', blank=True, null=True, help_text='Введите описание')
    images = models.ImageField(upload_to='catalog/photo', verbose_name='Фото', blank=True, null=True,
                               help_text='Загрузите фото')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, max_length=100, verbose_name='Категория',
                                 help_text='Выберите категорию')
    purchase_price = models.IntegerField(verbose_name='Цена', help_text='Введите цену')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'created_at']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование', help_text='Введите наименование')
    description = models.TextField(blank=True, null=True, verbose_name='Описание', help_text='Введите описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name


class ContactInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя', help_text='Введите имя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', help_text='Введите номер телефона')
    email = models.EmailField(verbose_name='Email', help_text='Введите Email')
    address = models.TextField(verbose_name='Адресс', help_text='Введите адресс')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['name']

    def __str__(self):
        return self.name
