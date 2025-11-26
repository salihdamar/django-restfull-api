from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer

@api_view(['GET','POST'])
def category_list(request):
    try:   
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        if request.method == 'POST':
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': 'An error occurred while fetching categories'}, status=500)
    

@api_view(['GET'])
def category_details(request, pk):
    try:
        category = Category.objects.get(pk=pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=404)
    
