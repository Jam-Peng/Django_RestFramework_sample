from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def getRouts(request):
    routes = [
        'GET | api/v1/',
        'GET | api/v1/products',

        " ======================   generics APIView  =========================== ",
        'POST | api/v1/productCreated/',
        'GET | api/v1/ProductDetail/:id/',
        'POST | api/v1/productCreatedAPIView/',
        'GET | api/v1/productListAPIView/',
        'PUT | api/v1/productUpdateAPIView/:id/',
        'DELETE | api/v1/productDestroyAPIView/:id/',

        "POST | api/v1/auth/",  # 發送 token

        " ========================  ViewSets  ================================== ",
        'GET | api/v1/getProducts',
        'GET | api/v1/getProducts/:id/',

    ]

    return Response(routes)
