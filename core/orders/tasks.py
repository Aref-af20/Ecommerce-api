from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

from .models import Order


@shared_task
def send_order_confirmation_email(order_id):

    order = Order.objects.select_related('user').get(
        id=order_id
    )

    user_email = order.user.email

    if not user_email:
        return "User has no email address"

    subject = f"Order #{order.id} Confirmation"

    message = f"""
Hello {order.user},

Your order has been successfully registered.

Order ID: {order.id}
Subtotal: {order.subtotal}
Delivery Cost: {order.delivery_cost}
Total Price: {order.total_price}

Thank you for shopping with us!
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user_email],
        fail_silently=False,
    )

    return f"Confirmation email sent for order #{order.id}"
