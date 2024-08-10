from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'value']


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name', 'slug']


class FeaturedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Featured
        fields = ['id', 'name', 'slug']

class ProductSerializer(serializers.ModelSerializer):
    collections = serializers.PrimaryKeyRelatedField(queryset=Collection.objects.all(), many=True)
    features = serializers.PrimaryKeyRelatedField(queryset=Feature.objects.all(), many=True)
    # categories = CategorySerializer(many=True, read_only=True)
    # features = FeatureSerializer(many=True, read_only=True)
    # collections = CollectionSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 
            'available', 'categories', 
            'features', 'collections', 'image'
        ]