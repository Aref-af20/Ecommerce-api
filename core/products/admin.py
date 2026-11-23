from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'parent_category_title',
        'created_at',
        'updated_at',
    )

    search_fields = ('title',)

    ordering = ('-created_at',)

    list_per_page = 4

    @admin.display(description="Parent Category")
    def parent_category_title(self, obj):
        return obj.parent_category_id.title if obj.parent_category_id else '-'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_at', 'updated_at']
    search_fields = ['title']
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']    