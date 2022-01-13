from rest_framework.viewsets import ModelViewSet
from .serializers import FamilySerializer
from .models import Family


class FamilyModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]

    serializer_class = FamilySerializer
    queryset = Family.objects.all()


