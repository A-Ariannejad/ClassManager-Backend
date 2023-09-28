from django.urls import path
from .views import CustomUserViewSet, CreateCustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateCustomUser.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]