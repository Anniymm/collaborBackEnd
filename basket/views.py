from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Basket, BasketItem, Product
from .serializers import BasketItemSerializer, BasketSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class BasketDetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def get_object(self):
        # Ensure to get the basket for the current user
        return Basket.objects.get(user=self.request.user)

class AddToBasketView(APIView):  #damatebistvis
    permission_classes = [IsAuthenticated]
    def post(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id)
        quantity = request.data.get('quantity', 1) 
        basket, created = Basket.objects.get_or_create(user=user)
        basket_item, created = BasketItem.objects.get_or_create(
            basket=basket,
            product=product
        )

        if not created:
            # tu ukve kalatashia odenobis updatestvis
            basket_item.quantity = quantity
            basket_item.save()
        else:
            basket_item.quantity = quantity
            basket_item.save()

        serializer = BasketItemSerializer(basket_item)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RemoveFromBasketView(APIView): # washlistvis
    permission_classes = [IsAuthenticated]
    def delete(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id)

        basket = Basket.objects.get(user=user)
        basket_item = BasketItem.objects.filter(basket=basket, product=product).first()

        if basket_item:
            basket_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Item not found in the basket.'}, status=status.HTTP_404_NOT_FOUND)
