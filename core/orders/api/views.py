
from decimal import Decimal

from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from cart.models import Cart, DeliveryCost
from orders.models import Order, OrderItem
from .serializers import OrderSerializer
from orders.tasks import send_order_confirmation_email




class CheckoutAPIView(APIView):

    permission_classes = [IsAuthenticated]

    @transaction.atomic
    def post(self, request):

        cart = (
            Cart.objects
            .filter(user=request.user, is_active=True)
            .prefetch_related('items__product')
            .order_by('-created_at')
            .first()
        )

        if cart is None:
            raise ValidationError("Active cart not found.")

        cart_items = list(cart.items.all())

        if not cart_items:
            raise ValidationError("Your cart is empty.")

        subtotal = Decimal('0.00')
        total_quantity = 0

        for item in cart_items:

            product_price = item.product.price

            subtotal += product_price * item.quantity
            total_quantity += item.quantity

        delivery = (
            DeliveryCost.objects
            .filter(status=DeliveryCost.Status.ACTIVE)
            .order_by('-created_at')
            .first()
        )

        delivery_cost = Decimal('0.00')

        if delivery:
            delivery_cost = (
                delivery.fixed_cost
                + delivery.cost_per_delivery
                + (delivery.cost_per_product * total_quantity)
            )

        discount = Decimal('0.00')

        total_price = subtotal + delivery_cost - discount

        order = Order.objects.create(
            user=request.user,
            subtotal=subtotal,
            delivery_cost=delivery_cost,
            discount=discount,
            total_price=total_price,
        )

        order_items = []

        for item in cart_items:

            product = item.product
            unit_price = product.price

            order_items.append(
                OrderItem(
                    order=order,
                    product=product,
                    product_title=str(product),
                    unit_price=unit_price,
                    quantity=item.quantity,
                    total_price=unit_price * item.quantity,
                )
            )

        OrderItem.objects.bulk_create(order_items)

        cart.is_active = False
        cart.save(update_fields=['is_active', 'updated_at'])

        transaction.on_commit(
            lambda: send_order_confirmation_email.delay(order.id)
        )

        serializer = OrderSerializer(order)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )
