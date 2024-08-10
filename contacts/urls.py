from django.urls import path
from .views import contactsUsView

urlpatterns = [
    path('contact/', contactsUsView.as_view(), name='contact-info'),
]
