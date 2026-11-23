from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.



class Order(models.Model):

    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        PAID = 'Paid', 'Paid'
        PROCESSING = 'Processing', 'Processing'
        SHIPPED = 'Shipped', 'Shipped'
        DELIVERED = 'Delivered', 'Delivered'
        CANCELED = 'Canceled', 'Canceled'


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name= 'orders'

    )    


    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0    

    )

    delivery_cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    discount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.user}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items'
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='order_items'
    )

    product_title = models.CharField(max_length=255)

    unit_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    quantity = models.PositiveIntegerField(default=1)

    total_price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_title} - {self.quantity}"