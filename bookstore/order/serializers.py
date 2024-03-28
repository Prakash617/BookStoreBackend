from rest_framework import serializers
from .models import *
from user_accounts.serializers import CustomUserSerializer


class OrderQuantitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderQuantity
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_qty = OrderQuantitySerializer(many=True, read_only = True)
    customer = CustomUserSerializer( read_only = True)
    class Meta:
        model= Orders
        fields= '__all__'
