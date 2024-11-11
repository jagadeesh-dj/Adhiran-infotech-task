from rest_framework import serializers
from .models import Customer,Category,Products,Order


# creating serializer class for customer table
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','name','email','address','phone_number']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name','price','stock','category_id']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=['id','user_id','product_id','quantity','price']