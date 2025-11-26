from rest_framework.response import Response
from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    try:
         products= Product.objects.all()
         serializer= ProductSerializer(products, many=True)
         return Response(serializer.data)       
    except:  
        return Response({'error':'An error occurred while fetching products'},status=500)

@api_view(['GET'])
def product_details(resquest, pk):
    try:
        product= Product.objects.get(pk=pk)
        serializer= ProductDetailSerializer(product)
        data= serializer.data
        return Response(data)
    
    except Product.DoesNotExist:
        return Response({'error':'Product not found'},status=404)
       