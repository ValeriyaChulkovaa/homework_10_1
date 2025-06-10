from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductFormValidator
from catalog.models import Product, ContactInfo


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


class ContactsListView(ListView):
    model = ContactInfo
    template_name = 'catalog/contacts.html'
    context_object_name = 'contact_info'


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'catalog/product_details.html'
    context_object_name = 'products'


class AddProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductFormValidator
    template_name = 'catalog/add_product.html'

    def get_success_url(self):
        return f'/product_details/{self.object.pk}/'

    def form_valid(self, form):
        # Обработка при успешной валидации
        print("Форма валидна!")  # Отладка
        return super().form_valid(form)

    def form_invalid(self, form):
        # Обработка ошибок формы
        print("Ошибки формы:", form.errors)  # Отладка
        return super().form_invalid(form)


class EditProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductFormValidator
    context_object_name = 'products'
    template_name = 'catalog/edit_product.html'

    def get_success_url(self):
        return f'/product_details/{self.object.pk}/'


class DeleteProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/delete_product.html'
    success_url = '/'
    context_object_name = 'products'

