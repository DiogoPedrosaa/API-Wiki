from rest_framework import serializers
from ..models import Category, Attribute, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    attributes = AttributeSerializer(many=True)

    class Meta:
        model = Item
        fields = ['name', 'category', 'attributes', 'description', 'weight']