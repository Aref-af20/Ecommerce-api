
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404
from cart.models import Cart, CartItem, DeliveryCost
from .serializers import (
    CartSerializer,
    CartItemSerializer,
    DeliveryCostSerializer
)


# Cart Views

class CartListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


# CartItem Views

class CartItemListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(
            cart__user=self.request.user
        ).select_related('cart', 'product')

    def perform_create(self, serializer):
        cart_id = self.request.data.get('cart')

        cart = get_object_or_404(
            Cart,
            id=cart_id,
            user=self.request.user
        )

        serializer.save(cart=cart)


class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(
            cart__user=self.request.user
        ).select_related('cart', 'product')


# DeliveryCost Views

class DeliveryCostListAPIView(generics.ListAPIView):

    serializer_class = DeliveryCostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DeliveryCost.objects.filter(
            status=DeliveryCost.Status.ACTIVE
        )


class DeliveryCostAdminListCreateAPIView(generics.ListCreateAPIView):

    queryset = DeliveryCost.objects.all()
    serializer_class = DeliveryCostSerializer
    permission_classes = [IsAdminUser]


class DeliveryCostAdminDetailAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = DeliveryCost.objects.all()
    serializer_class = DeliveryCostSerializer
    permission_classes = [IsAdminUser]
