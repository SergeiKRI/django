from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Products, BlogRecord


class ProductsListView(ListView):
    model = Products


class ProductsDetailView(DetailView):
    model = Products


class ProductsCreateView(CreateView):
    model = Products
    fields = ('name', 'description', 'price', 'category', 'image')
    success_url = reverse_lazy('catalog:products_list')


class ProductsUpdateView(UpdateView):
    model = Products
    fields = ('name', 'description', 'price', 'category', 'image')
    success_url = reverse_lazy('catalog:products_list')


class ProductsDeleteView(DeleteView):
    model = Products
    success_url = reverse_lazy('catalog:products_list')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        # print(f'You have new message from {name}({phone}): {message}')
        with open('list_contacts.txt', mode='a', encoding='utf-8') as file:
            file.write(f'You have new message from {name}({phone}): {message}\n')
    return render(request, 'catalog/contact.html')


class BlogRecordListView(ListView):
    model = BlogRecord

    def get_queryset(self, *args, **kwargs):
        self.queryset = super().get_queryset(*args, **kwargs)
        self.queryset = self.queryset.filter(is_active=True)
        return self.queryset


class BlogRecordDetailView(DetailView):
    model = BlogRecord

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogRecordCreateView(CreateView):
    model = BlogRecord
    fields = ('title', 'text', 'is_active', 'image')
    success_url = reverse_lazy('catalog:record_list')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)


class BlogRecordUpdateView(UpdateView):
    model = BlogRecord
    fields = ('title', 'text', 'is_active', 'image')

    def form_valid(self, form):
        if form.is_valid():
            new_record = form.save()
            new_record.slug = slugify(new_record.title)
            new_record.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:record_detail', kwargs={'pk': self.object.pk})


class BlogRecordDeleteView(DeleteView):
    model = BlogRecord
    success_url = reverse_lazy('catalog:record_list')

