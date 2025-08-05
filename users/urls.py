from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet  # yoki UserViewSet, agar oddiy user ishlatsangiz

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)  # Bu yerda API endpoint 'users/' bo'ladi

urlpatterns = [
    path('', include(router.urls)),
]
