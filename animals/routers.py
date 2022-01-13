from rest_framework.routers import DefaultRouter, SimpleRouter
from .views import FamilyModelViewSet

router = DefaultRouter()
# router = SimpleRouter()
router.register(r'families', FamilyModelViewSet)

