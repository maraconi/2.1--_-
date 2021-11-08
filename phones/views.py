from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    model = request.GET.get('sort')
    if model == 'name':
        phone = phones.order_by('name')
    elif model == 'min_price':
        phone = phones.order_by('price')
    elif model == 'max_price':
        phone = phones.order_by('price').reverse()
    else:
        phone = phones
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
