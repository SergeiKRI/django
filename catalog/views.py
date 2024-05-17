from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(f'You have new message from {name}({phone}): {message}')
        with open('list_contacts.txt', mode='a', encoding='utf-8') as file:
            file.write(f'You have new message from {name}({phone}): {message}\n')
    return render(request, 'contact/contact.html')

