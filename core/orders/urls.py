from django.urls import path, include



app_name = 'orders'

urlpatterns = [
    path('api/v1/', include('orders.api.urls'))
]