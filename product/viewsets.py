from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status


class ProductsViewSet(viewsets.ModelViewSet):
    """
    APIView & viewsets 的相對函式
    get -> list 這個不需要寫函式
    get -> retrieve 這個不需要寫函式,只需要加 lookup_field = 'pk',路由就可以取得該ㄧ筆的資料 
    post -> create
    put -> Update
    patch -> partial_update
    delete -> destroy
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
