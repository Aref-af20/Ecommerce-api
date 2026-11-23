from django.contrib import admin
from .models import Campaign, Coupon
# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):

    list_display = (
        'discount_type',
        'discount_rate',
        'discount_amount',
        'min_purchased_items',
        'apply_to',
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)



@admin.register(Coupon)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['minimum_cart_amount', 'discount_rate', 'created_at', 'updated_at']
    ordering = ['-created_at']    