from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, ServiceViewSet, ProjectViewSet, BlogViewSet, TeamMemberViewSet

router = DefaultRouter()
router.register(r'company', CompanyViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'blogs', BlogViewSet)
router.register(r'team', TeamMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
