from django.urls import path
from .views import RegisterApiView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView




urlpatterns = [
    path('register/', RegisterApiView.as_view(), name='register'),
    path("token/login", ObtainAuthToken.as_view(), name="token_obtain"),
    path('jwt/token/', TokenObtainPairView.as_view(), name='jwt_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/token/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]


