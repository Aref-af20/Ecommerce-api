from django.urls import path, include

app_name = 'discounts'


urlpatterns = [
    path('api/', include('discounts.api.urls'))
]