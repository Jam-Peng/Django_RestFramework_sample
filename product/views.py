from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, authentication

# from rest_framework.permissions import AllowAny, IsAuthenticated  另一個寫法直接匯入“允許全部”或“需要token驗證”
from rest_framework import permissions


# class ProductLists(APIView):
#     def get(self, request):
#         """ DRF APIView """
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True).data
#         return Response(serializer, status=status.HTTP_200_OK)


# class ProductCreated(APIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(generics.RetrieveAPIView):
    """ 取得特定的一筆詳細資料 """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


# class ProductCreatedAPIView(generics.CreateAPIView):
#     """ 建立一筆資料 """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     # 驗證序列化後模型中屬性的值，若是空值就使用其他值補上
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         # print(content)
#         if content is '':
#             content = title
#         serializer.save(content=content)

# # 可以在路由中直接寫 views.product_created_view
# product_created_view = ProductCreatedAPIView.as_view()


# class ProductListAPIView(generics.ListAPIView):
#     """ 取得所有資料 (和基本取得所有資料一樣) """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """ 取得所有資料，並可以建立新資料 """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """ 驗證序列化後模型中屬性的值，若是空值就使用其他值補上 """
        # print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        # 建立原本不在 model 中的屬性
        # email = serializer.validated_data.pop('email')
        # print(email)

        if content == '':
            content = title
        serializer.save(content=content, user=self.request.user)

    def get_queryset(self, *args, **kwargs):
        """ 選擇使用者 """
        qs = super().get_queryset(*args, **kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        print(request.user)
        return qs.filter(user=request.user)


class ProductUpdateAPIView(generics.UpdateAPIView):
    """ 更新資料 """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        """ 序列化後模型中屬性的值，若是空值就使用其他值補上 (不驗證) """
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(generics.DestroyAPIView):
    """ 刪除資料 """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


# 使用 views.product_created_view 取代 views.ProductDestroyAPIView.as_view()
product_destroy_view = ProductDestroyAPIView.as_view()
