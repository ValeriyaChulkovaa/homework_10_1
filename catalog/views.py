from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductFormValidator
from catalog.models import Product, ContactInfo, Category
from catalog.services import get_product_list_cache, get_products_by_category


class IndexListView(ListView):
    ''' Главной страница, просмотр списка продуктов'''
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        return get_product_list_cache()


class ContactsListView(ListView):
    '''Страница Контактов '''
    model = ContactInfo
    template_name = 'catalog/contacts.html'
    context_object_name = 'contact_info'


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailsView(LoginRequiredMixin, DetailView):
    '''Страцина детальной информации продукта, с возможностью редактирования и удаления. Добавил кеширование '''
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'products'
    permission_required = 'catalog.view_product'


class AddProductCreateView(LoginRequiredMixin, CreateView):
    '''Страница добавления продукта '''
    model = Product
    template_name = 'catalog/add_product.html'
    permission_required = 'catalog.add_product'
    form_class = ProductFormValidator

    def get_success_url(self):
        return f'/product_details/{self.object.pk}/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        # Обработка ошибок формы
        print("Ошибки формы:", form.errors)  # Отладка
        return super().form_invalid(form)


class EditProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''Страница редактирования продукта, только для владельцев и суперюзеров'''
    model = Product
    form_class = ProductFormValidator
    context_object_name = 'products'
    template_name = 'catalog/edit_product.html'
    permission_required = 'catalog.change_product'

    def get_success_url(self):
        return f'/product_details/{self.object.pk}/'

    def test_func(self):
        """Проверка является ли пользователь владельцем продукта"""
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists() or user.is_superuser

    def handle_no_permission(self):
        """Обработка отказа в доступе"""
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Вы не являетесь владельцем этого продукта")

    # def get_queryset(self):
    #     """Фильтрует продукты только для текущего пользователя"""
    #     return Product.objects.filter(owner=self.request.user)

    # def get_queryset(self):
    #     if not self.request.user.has_perm('catalog.change_product'):
    #         return Product.objects.none()
    #     return Product.objects.all()


class DeleteProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    '''Страница удаления продукта, только для владельцев и суперюзеров'''
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = '/'
    context_object_name = 'products'
    permission_required = 'catalog.delete_product'

    def test_func(self):
        """Проверка является ли пользователь владельцем продукта"""
        product = self.get_object()
        user = self.request.user
        return user == product.owner or user.groups.filter(name='Модератор продуктов').exists() or user.is_superuser

    def handle_no_permission(self):
        """Обработка отказа в доступе"""
        from django.http import HttpResponseForbidden
        return HttpResponseForbidden("Вы не являетесь владельцем этого продукта")


def products_by_category(request, category_name):
    '''Страница всех продуктов определенной категории  '''
    products = get_products_by_category(category_name)

    if not products:
        raise Http404("Категория не найдена или в этой категории нет товаров.")

    category_exists = Category.objects.filter(name=category_name).exists()

    return render(request, 'catalog/products_by_category.html', {
        'products': products,
        'category_name': category_name,
        'category_exists': category_exists
    })