from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import IndexListView, ProductDetailsView, ContactsListView, AddProductCreateView, \
    EditProductUpdateView, DeleteProductDeleteView, products_by_category

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('add/', AddProductCreateView.as_view(), name='add_product'),
    path('edit/<int:pk>/', EditProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', DeleteProductDeleteView.as_view(), name='delete_product'),
    path('category/<str:category_name>/', products_by_category, name='products_by_category'),
]