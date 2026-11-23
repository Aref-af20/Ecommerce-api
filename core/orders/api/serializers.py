from rest_framework import serializers

from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = [
            'id',
            'product',
            'product_title',
            'unit_price',
            'quantity',
            'total_price',
        ]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'items',
            'subtotal',
            'delivery_cost',
            'discount',
            'total_price',
            'status',
            'created_at',
        ]

        read_only_fields = fields
