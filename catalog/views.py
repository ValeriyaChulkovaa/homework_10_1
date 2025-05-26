

from django.shortcuts import render, redirect

from catalog.forms import ProductForm
from catalog.models import Product, ContactInfo
from django.contrib import messages



def index(request):

    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'catalog/index.html', context)


def contacts(request):

    contact_info = ContactInfo.objects.all()

    context = {
        'contact_info': contact_info,
    }

    return render(request, 'catalog/contacts.html', context)


def product_details(request, pk):

    products = Product.objects.get(pk=pk)

    context = {'products': products}

    return render(request, 'catalog/product_details.html', context)



# def add_product(request):
#     return render(request, 'catalog/add_product.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Успешно добавлено! Переходим на главную страницу.')

    else:
        form = ProductForm()
    return render(request, 'catalog/add_product.html', {'form': form})