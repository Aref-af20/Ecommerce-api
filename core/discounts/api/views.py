from rest_framework.generics import ListAPIView
from discounts.models import Coupon , Campaign
from .serializers import CampaignSerializer, CouponSerializer




class CampaignView(ListAPIView):

    serializer_class = CampaignSerializer
    queryset = Campaign.objects.all().order_by('id')



class CouponView(ListAPIView):

    serializer_class = CouponSerializer
    quertset = Coupon.objects.all().order_by('id')
    