from django.contrib import admin
from .models import Product, \
    CartProduct, Category, Customer, Cart
from django.utils.safestring import mark_safe


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'price', 'desc', 'category', 'get_html_photo', 'data_create', 'memory', 'is_published')
    list_display_link = ('title', 'id')
    search_fields = ('title', 'desc')
    list_editable = ('title', 'price', 'desc', 'category', 'data_create', 'is_published', 'memory')
    fields = ('title', 'price', 'desc', 'category', 'photo', 'data_create', 'is_published', 'memory')

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=100>")

    get_html_photo.short_description = "Изображение"


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
