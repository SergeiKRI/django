from django.shortcuts import render, get_object_or_404

from catalog.models import Products


# def catalog(request):
#

def home(request):
    products = Products.objects.all()
    context = {'products': products}

    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {'product': product}

    return render(request, 'product_detail.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(f'You have new message from {name}({phone}): {message}')
        with open('list_contacts.txt', mode='a', encoding='utf-8') as file:
            file.write(f'You have new message from {name}({phone}): {message}\n')
    return render(request, 'contact.html')
