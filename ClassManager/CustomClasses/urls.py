from django.urls import path
from .views import CustomClassViewSet, CreateCustomClass, ShowCustomClass, UpdateCustomClass, DeleteCustomClass


urlpatterns = [
    path('show/<int:id>/', ShowCustomClass.as_view(), name='show'),
    path('list/', CustomClassViewSet.as_view({'get': 'list'}), name='list'),
    path('create/', CreateCustomClass.as_view(), name='signup'),
    path('update/<int:pk>/', UpdateCustomClass.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCustomClass.as_view(), name='delete'),
]