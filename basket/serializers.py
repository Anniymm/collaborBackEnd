from rest_framework import serializers
from .models import BasketItem, Basket

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ['id', 'basket', 'product', 'quantity']
        

class BasketSerializer(serializers.ModelSerializer):
    items = BasketItemSerializer(many=True, read_only=True)  #es unda gadavamowmo mere requestis dros 

    class Meta:
        model = Basket
        fields = ['id', 'user', 'created_at']
