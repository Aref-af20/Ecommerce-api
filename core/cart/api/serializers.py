from cart.models import Cart, CartItem, DeliveryCost
from rest_framework import serializers




class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields =  ['id', 'user', 'is_active', 'created_at', 'updated_at']

        read_only_fields = ['id', 'user', 'created_at', 'updated_at']



class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'created_at', 'updated_at']

        read_only_fields = ['id', 'cart', 'created_at', 'updated_at']

    def validate_quantity(self, value):
        if value < 1:
            raise serializers.ValidationError("Quantity must be at least 1.")

        return value    



class DeliveryCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCost
        fields = ['id','status', 'cost_per_delivery', 'cost_per_product', 'created_at', 'updated_at']

        read_only_fields = ['id', 'created_at', 'updated_at']
