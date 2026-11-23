from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from products.models import Category, Product




class Campaign(models.Model):
    DISCOUNT_TYPE_CHOICES = (('Amount', 'amount'), ('Rate', 'rate'))
    APPLY_TO_CHOICES = (('Product', 'product'), ('Category', 'category'))

    discount_type = models.CharField(max_length=6, choices=DISCOUNT_TYPE_CHOICES, default='Rate')
    discount_rate = models.IntegerField(null=True, blank=True, help_text='percent discount(0 - 100)%')
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text = 'Fixed discount amount')
    min_purchased_items = models.IntegerField(default=1, help_text='Minimum quantity required for discount')
    apply_to = models.CharField(max_length=8, choices=APPLY_TO_CHOICES, default='Product')
    target_product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    target_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    valid_from = models.DateTimeField(default=timezone.now)
    valid_to = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.discount_type} - {self.discount_rate} - {self.discount_amount} - {self.min_purchased_items} - {self.apply_to} - {self.target_product} - {self.target_category} - {self.created_at} - {self.updated_at}"




class Coupon(models.Model):
    minimum_cart_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount_rate = models.PositiveSmallIntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.minimum_cart_amount} - {self.discount_rate} - {self.created_at} - {self.updated_at}"


