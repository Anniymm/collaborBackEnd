from django.urls import path
from .views import AddToBasketView, RemoveFromBasketView,BasketDetailView

urlpatterns = [
    path('add/<int:product_id>/', AddToBasketView.as_view(), name='add-to-basket'),
    path('remove/<int:product_id>/', RemoveFromBasketView.as_view(), name='remove-from-basket'),
    path('basket/', BasketDetailView.as_view(), name='basket-detail'),
]
