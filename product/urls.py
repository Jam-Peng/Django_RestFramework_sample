from django.urls import path, include
from . import views

from . import viewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('getProducts', viewsets.ProductsViewSet,
                basename='getProducts')


urlpatterns = [
    # path("products/", views.ProductLists.as_view()),  # 取得所有資料
    # path("productCreated/", views.ProductCreated.as_view()),  # 建立一筆資料

    path('productDetail/<int:pk>', views.ProductDetailAPIView.as_view(),
         name='product_detail'),  # 取得單筆資料

    # views.ProductCreatedAPIView.as_view() 基礎寫法
    # path('productCreatedAPIView/', views.product_created_view),  # 建立一筆資料

    # path('productListAPIView/', views.ProductListAPIView.as_view()),  # 取得所有資料
    path('productListCreateAPIView/',
         views.ProductListCreateAPIView.as_view(), name='product_list'),

    # 更新資料
    path('productUpdateAPIView/<int:pk>',
         views.ProductUpdateAPIView.as_view(), name='product_edit'),
    # 刪除資料
    path('productDestroyAPIView/<int:pk>',
         views.product_destroy_view, name='product_destroy'),

    # ========================  ViewSets  ================================== #
    path('', include(router.urls)),

]
