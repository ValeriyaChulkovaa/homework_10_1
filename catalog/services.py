from django.core.cache import cache

from config.settings import CACHE_ENABLE
from catalog.models import Product, Category


def get_products_by_category(category_name):
    '''Получаем все продукты в указанной категории (если категория существует) '''
    category = Category.objects.filter(name=category_name).first()
    if category:
        return Product.objects.filter(category=category, is_published=True)
    return None


def get_product_list_cache():
    '''Низкоуровневое кеширование для главной страницы'''
    if not CACHE_ENABLE:
        return Product.objects.all()
    key = 'product_list_cache'
    product = cache.get(key)
    if product is not None:
        return product
    product = Product.objects.all()
    cache.set(key, product, 60 * 5)
    return product