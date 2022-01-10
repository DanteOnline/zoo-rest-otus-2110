from rest_framework.routers import DefaultRouter
from .views import FamilyModelViewSet

family_router = DefaultRouter()
family_router.register(r'families', FamilyModelViewSet)
