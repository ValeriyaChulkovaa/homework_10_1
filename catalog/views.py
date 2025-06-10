from django.views.generic import ListView, DetailView, CreateView

from catalog.forms import ProductForm
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


class AddProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/add_product.html'

    def get_success_url(self):
        return f'/product_details/{self.object.pk}/'