from django.urls import path
from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('product_details/<int:pk>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
]
