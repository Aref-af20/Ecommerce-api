from products.models import Category, Product
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ['id', 'parent_category_id', 'title', 'created_at', 'updated_at']
        read_only_fields = ['id', 'parent_category_id', 'created_at', 'updated_at']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'price', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
        