from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer

class ProductListSerializer(serializers.ModelSerializer):
   
    class Meta:
        model= Product
        fields= ['id','name','price','stock']# Essential fields for list view


class ProductDetailSerializer(serializers.ModelSerializer):
    category= CategorySerializer()
    class Meta:
        model= Product
        # fields= '__all__'
        exclude= ['is_home','created_at','updated_at']  # Exclude less relevant fields for detail view