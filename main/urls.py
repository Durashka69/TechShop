from django.urls import path
from .views import *

urlpatterns = [
    path('create_list/category', CategoryListCreateView.as_view()),
    path('update_destroy/category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/product', ProductListCreateView.as_view()),
    path('update_destroy/product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/cart', CartListCreateView.as_view()),
    path('update_destroy/cart/<int:pk>', CartRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/cartproduct', CartProductListCreateView.as_view()),
    path('update_destroy/cartproduct/<int:pk>', CartProductRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/customer', CustomerListCreateView.as_view()),
    path('update_destroy/customer/<int:pk>', CustomerRetrieveUpdateDestroyAPIView.as_view()),
]
