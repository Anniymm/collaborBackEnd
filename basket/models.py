from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class BasketItem(models.Model): 
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('basket', 'product') # ramdenjerme rom ar gamochndes konkjretuli product

