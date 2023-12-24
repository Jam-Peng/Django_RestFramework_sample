from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from .validators import validate_title
from staff.serializers import UserPublicSerializers


class ProductSerializer(serializers.ModelSerializer):
    # source='user' 是對應 models 的 user 屬性
    ower = UserPublicSerializers(read_only=True, source='user')

    my_discount = serializers.SerializerMethodField(
        read_only=True)  # 自定義一個屬性名稱是取得模型中get_discount()

    url = serializers.SerializerMethodField(
        read_only=True)  # 自定義一個屬性名稱

    update_url = serializers.SerializerMethodField(
        read_only=True)  # 自定義一個屬性名稱

    # 第二種寫法 - 使用 HyperlinkedIdentityField 不需要寫函式
    url2 = serializers.HyperlinkedIdentityField(
        view_name='product_detail', lookup_field='pk'
    )

    # email = serializers.EmailField(write_only=True)

    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = ['ower', 'url', 'update_url', 'url2', 'id', 'title', 'content',
                  'price', 'sale_price', 'get_discount', 'my_discount']

    # def validate_title(self, value):
    #     """ 例外處理 - 驗證 title 屬性是否存在 """
    #     queryset = Product.objects.filter(title__exact=value)
    #     if queryset.exists():
    #         raise serializers.ValidationError(f'{value} 已經有這項產品名稱')
    #     return value

    def get_my_discount(self, obj):
        """ 
        obj 是指 model = Product 這個模型 
        在序列化中去取得 model 中的函式
        """
        return obj.get_discount()

    def get_url(self, obj):
        """ 回傳可以取得單筆資料的相對 Url """
        return f'api/v1/getProducts/{obj.id}'

        """ 回傳取得其他 URL 連結絕對路徑"""
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_detail", kwargs={'pk': obj.id}, request=request)

    # 加入“更新產品的路徑連結”
    def get_update_url(self, obj):
        """ 回傳取得其他 URL 連結絕對路徑"""
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product_edit", kwargs={'pk': obj.id}, request=request)

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     # print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)
