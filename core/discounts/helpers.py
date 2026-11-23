
from collections import defaultdict

from .models import Campaign, Coupon


class AvailableDiscount:
    """
    Standard structure for storing an available discount.
    """

    def __init__(self, discount_type, min_purchased_items, amount):
        self.discount_type = discount_type
        self.min_purchased_items = min_purchased_items
        self.amount = amount


class CouponHelper:
    """
    Finds coupons that are valid for the cart's total amount.
    """

    def __init__(self, cart_total_amount):
        self.cart_total_amount = cart_total_amount
        self.available_discounts = []

    def get_coupon_discounts(self):

        self.available_discounts = []

        coupons = Coupon.objects.filter(
            minimum_cart_amount__lte=self.cart_total_amount
        )

        for coupon in coupons:
            discount = AvailableDiscount(
                discount_type='Rate',
                min_purchased_items=0,
                amount={
                    'rate': coupon.discount_rate,
                    'amount': None
                }
            )

            self.available_discounts.append(discount)

        return self.available_discounts


class CampaignHelper:
    """
    Finds campaigns that apply to products or product categories
    in the shopping cart.
    """

    def __init__(self, cart_items):
        self.cart_items = cart_items
        self.available_discounts = []

    def get_campaign_discounts(self):

        self.available_discounts = []

        product_quantities = defaultdict(int)
        category_quantities = defaultdict(int)

        # Calculate total quantities for products and categories.
        for cart_item in self.cart_items:

            product = cart_item.item
            quantity = cart_item.quantity

            product_quantities[product.id] += quantity

            # Include the product's category and its parent categories.
            category = product.category
            visited_categories = set()

            while category is not None:

                if category.id in visited_categories:
                    break

                visited_categories.add(category.id)
                category_quantities[category.id] += quantity

                # Supports both parent_category and parent_category_id
                # when parent_category_id is a ForeignKey field.
                parent = getattr(category, 'parent_category', None)

                if parent is None:
                    parent = getattr(category, 'parent_category_id', None)

                category = parent

        self.get_product_discounts(product_quantities)
        self.get_category_discounts(category_quantities)

        return self.available_discounts

    def get_product_discounts(self, product_quantities):

        if not product_quantities:
            return

        campaigns = Campaign.objects.filter(
            apply_to='Product',
            target_product_id__in=product_quantities.keys()
        )

        for campaign in campaigns:

            purchased_quantity = product_quantities[campaign.target_product_id]

            if purchased_quantity >= campaign.min_purchased_items:
                self.add_discount(campaign)

    def get_category_discounts(self, category_quantities):

        if not category_quantities:
            return

        campaigns = Campaign.objects.filter(
            apply_to='Category',
            target_category_id__in=category_quantities.keys()
        )

        for campaign in campaigns:

            purchased_quantity = category_quantities[campaign.target_category_id]

            if purchased_quantity >= campaign.min_purchased_items:
                self.add_discount(campaign)

    def add_discount(self, campaign):

        discount = AvailableDiscount(
            discount_type=campaign.discount_type,
            min_purchased_items=campaign.min_purchased_items,
            amount={
                'rate': campaign.discount_rate,
                'amount': campaign.discount_amount
            }
        )

        self.available_discounts.append(discount)
