from django.urls import path
from .views import CustomUserViewSet, CreateCustomUser, MyCustomUser, ShowCustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('myshow/', MyCustomUser.as_view(), name='myshow'),
    path('show/<int:id>/', ShowCustomUser.as_view(), name='show'),
    path('list/', CustomUserViewSet.as_view({'get': 'list'}), name='list'),
    path('signup/', CreateCustomUser.as_view(), name='signup'),
    # path('update/<int:pk>/', UpdateCustomUser.as_view(), name='update'),
    # path('delete/<int:pk>/', DeleteCustomUser.as_view(), name='delete'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]