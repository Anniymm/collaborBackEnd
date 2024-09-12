from rest_framework import viewsets
from rest_framework import permissions
from .models import Category, Feature, Collection, Product, Featured
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FeaturedViewSet(viewsets.ModelViewSet):
    queryset = Featured.objects.all()
    serializer_class = FeaturedSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)  
    filterset_class = ProductFilter