from django.urls import path

from .views import (
    CartListCreateAPIView,
    CartDetailAPIView,
    CartItemListCreateAPIView,
    CartItemDetailAPIView,
    DeliveryCostListAPIView,
    DeliveryCostAdminListCreateAPIView,
    DeliveryCostAdminDetailAPIView
)


urlpatterns = [

    # Cart
    path(
        'carts/',
        CartListCreateAPIView.as_view(),
        name='cart-list-create'
    ),

    path(
        'carts/<int:pk>/',
        CartDetailAPIView.as_view(),
        name='cart-detail'
    ),

    # Cart Items
    path(
        'cart-items/',
        CartItemListCreateAPIView.as_view(),
        name='cart-item-list-create'
    ),

    path(
        'cart-items/<int:pk>/',
        CartItemDetailAPIView.as_view(),
        name='cart-item-detail'
    ),

    # Delivery Cost
    path(
        'delivery-cost/',
        DeliveryCostListAPIView.as_view(),
        name='delivery-cost-list'
    ),

    path(
        'admin/delivery-cost/',
        DeliveryCostAdminListCreateAPIView.as_view(),
        name='delivery-cost-admin-list-create'
    ),

    path(
        'admin/delivery-cost/<int:pk>/',
        DeliveryCostAdminDetailAPIView.as_view(),
        name='delivery-cost-admin-detail'
    ),

]
