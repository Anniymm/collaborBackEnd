from rest_framework import serializers
from .models import contactsUs

class contactsUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = contactsUs
        fields = ['phone','email','time']
