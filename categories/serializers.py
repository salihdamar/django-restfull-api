from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']  # Essential fields for list view


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['created_at', 'updated_at']  # Exclude less relevant fields for detail view
