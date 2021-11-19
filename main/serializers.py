from rest_framework import serializers
from .models import User, Product, Category


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        field = ('full_name', 'age', 'email', 'phone', 'password')


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        field = '__all__'


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = '__all__'
