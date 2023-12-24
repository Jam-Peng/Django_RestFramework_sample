from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product_detail', lookup_field='pk', read_only=True
    )


class UserPublicSerializers(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        print(obj)
        user = obj
        my_product_qs = user.product_set.all()[:5]
        return UserProductInlineSerializer(my_product_qs, many=True, context=self.context).data
