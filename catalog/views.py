from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import Product, ContactInfo


def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]

    for product in latest_products:
        print(product)

    context = {'latest_products': latest_products}

    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        return HttpResponse('Данные успешно отправлены!')

    contact_info = ContactInfo.objects.all()

    context = {
        'contact_info': contact_info,
    }

    return render(request, 'catalog/contacts.html', context)
