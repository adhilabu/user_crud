from rest_framework import serializers
from .models import Category, SubCategory

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('id', 'name')

class CategorySerializer(serializers.ModelSerializer):
    subcategory_set = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategory_set')


