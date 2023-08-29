from django.shortcuts import render, redirect


def index(request):
    return redirect('catalog')

from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    sort_param = request.GET.get('sort', None)

    if sort_param == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.order_by('price')
    elif sort_param == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)

def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
