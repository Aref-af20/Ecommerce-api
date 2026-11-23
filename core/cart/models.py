
from django.conf import settings
from django.db import models

from products.models import Product


class Cart(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='carts'
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart - {self.user}"


class CartItem(models.Model):

    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='cart_items'
    )

    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cart', 'product'],
                name='unique_product_per_cart'
            )
        ]

    def __str__(self):
        return f"{self.product} - {self.quantity}"


class DeliveryCost(models.Model):

    class Status(models.TextChoices):
        ACTIVE = 'Active', 'Active'
        PASSIVE = 'Passive', 'Passive'

    status = models.CharField(
        max_length=7,
        choices=Status.choices,
        default=Status.PASSIVE
    )

    cost_per_delivery = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    cost_per_product = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    fixed_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"{self.status} - "
            f"{self.cost_per_delivery} - "
            f"{self.cost_per_product} - "
            f"{self.fixed_cost}"
        )
