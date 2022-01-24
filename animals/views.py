from rest_framework.viewsets import ModelViewSet
from .serializers import FamilySerializer, KindHyperlinkedModelSerializer, KindSerializerBase
from .models import Family, Kind


class FamilyModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]

    serializer_class = FamilySerializer
    queryset = Family.objects.all()


class KindModelViewSet(ModelViewSet):
    serializer_class = KindHyperlinkedModelSerializer
    queryset = Kind.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return KindSerializerBase
        return KindHyperlinkedModelSerializer
