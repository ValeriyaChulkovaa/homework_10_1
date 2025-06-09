from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Добавление данных тестовых продуктов'

    def handle(self, *args, **kwargs):

        Product.objects.all().delete()
        Category.objects.all().delete()

        call_command('loaddata', 'Category_fixture.json')
        call_command('loaddata', 'Product_fixture.json')

        self.stdout.write(self.style.SUCCESS('Данные из fixture успешно добавлены!'))
