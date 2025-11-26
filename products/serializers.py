from rest_framework import serializers
from .models import Product
from categories.serializers import  CategoryDetailSerializer

class ProductSerializer(serializers.ModelSerializer):   
    class Meta:
        model= Product
        fields= ['id','name','price','stock']# Essential fields for list view


class ProductDetailSerializer(serializers.ModelSerializer):

    # category= serializers.StringRelatedField(source='category.name')# Display only the category name
    category= CategoryDetailSerializer(read_only=True) # Nested serializer for detailed category info 

    class Meta:
        model= Product
        # fields= '__all__'
        exclude= ['is_home','created_at','updated_at']  # Exclude less relevant fields for detail view