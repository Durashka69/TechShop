from django.urls import path
from .views import *

urlpatterns = [
    path('create_list/category', CategoryListCreateView.as_view()),
    path('update_destroy/category/<int:pk>', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/user', UserListCreateAPIView.as_view()),
    path('update_destroy/user/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('create_list/product', ProductListCreateView.as_view()),
    path('update_destroy/product/<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()),
]