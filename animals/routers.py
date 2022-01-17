from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import FamilyModelViewSet, KindModelViewSet

router = DefaultRouter()
router.register(r'families', FamilyModelViewSet)
router.register(r'kinds', KindModelViewSet)
