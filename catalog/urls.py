from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import IndexListView, ProductDetailsView, ContactsListView, AddProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
    path('add/', AddProductCreateView.as_view(), name='add_product'),
]