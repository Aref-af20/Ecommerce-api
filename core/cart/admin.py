from django.contrib import admin
from .models import Cart, CartItem, DeliveryCost


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'is_active',
        'created_at',
        'updated_at',
    )

    list_filter = ('is_active', 'created_at')

    search_fields = (
        'user__username',
        'user__email',
    )

    readonly_fields = (
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)
    list_per_page = 20

    inlines = [CartItemInline]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cart',
        'product',
        'quantity',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'product__title',
        'cart__user__username',
    )

    list_filter = ('created_at',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(DeliveryCost)
class DeliveryCostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
        'cost_per_delivery',
        'cost_per_product',
        'fixed_cost',
        'created_at',
    )

    list_filter = ('status',)
    search_fields = ('status',)
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)