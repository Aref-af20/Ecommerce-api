from django.urls import path
from . import views




urlpatterns = [ 
    path('campaign/', views.CampaignView.as_view(), name='campaign'),
    path('coupon/', views.CouponView.as_view(), name='coupon'),
    
]   
