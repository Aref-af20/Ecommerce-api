from django.urls import path, include

app_name = 'discounts'


urlpatterns = [
    path('api/v1/', include('discounts.api.urls'))
]