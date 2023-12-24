from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'price',
                    'sale_price', 'updated', 'created')


admin.site.register(Product, ProductAdmin)
