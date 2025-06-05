from django.contrib import admin

from catalog.models import Product, Category, ContactInfo


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Админка продукта '''
    list_display = ('id', 'name', 'purchase_price', 'category', 'owner')
    list_filter = ('category', 'owner')
    search_fields = ('name', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Админка категории '''
    list_display = ('id', 'name')
    search_fields = ('name', 'description')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    '''Админка Контактов '''
    list_display = ('name', 'phone', 'email', 'address')
    list_filter = ('name',)
    search_fields = ('name',)