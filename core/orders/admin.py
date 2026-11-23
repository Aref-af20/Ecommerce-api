from django.contrib import admin
from .models import Order, OrderItem




class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = (
        'product_title',
        'unit_price',
        'quantity',
        'total_price',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'status',
        'subtotal',
        'delivery_cost',
        'discount',
        'total_price',
        'created_at',
    )

    list_filter = ('status', 'created_at')

    search_fields = (
        'user__username',
        'user__email',
    )

    readonly_fields = (
        'user',
        'subtotal',
        'delivery_cost',
        'discount',
        'total_price',
        'created_at',
        'updated_at',
    )

    ordering = ('-created_at',)
    list_per_page = 20

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'product_title',
        'unit_price',
        'quantity',
        'total_price',
        'created_at',
    )

    search_fields = (
        'product_title',
        'order__id',
    )

    readonly_fields = (
        'order',
        'product',
        'product_title',
        'unit_price',
        'quantity',
        'total_price',
        'created_at',
    )

    list_filter = ('created_at',)
    ordering = ('-created_at',)