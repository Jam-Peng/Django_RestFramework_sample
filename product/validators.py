from rest_framework import serializers
from .models import Product


def validate_title(value):
    """ 例外處理 - 驗證 title 屬性是否存在 """
    queryset = Product.objects.filter(title__exact=value)
    if queryset.exists():
        raise serializers.ValidationError(f'{value} 已經有這項產品名稱')
    return value
