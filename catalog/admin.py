from django.contrib import admin

from catalog.models import Category, Products


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)