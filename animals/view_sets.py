from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from .models import Kind
from .serializers import KindSerializer


class KindViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    # extra action
    # http://127.0.0.1:8000/viewsets/base/1/kind_text_only/
    @action(detail=True, methods=['get'])
    def kind_text_only(self, request, pk=None):
        kind = get_object_or_404(Kind, pk=pk)
        return Response({'kind.full_name': kind.full_name})

    def list(self, request):
        kinds = Kind.objects.all()
        serializer = KindSerializer(kinds, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        kind = get_object_or_404(Kind, pk=pk)
        serializer = KindSerializer(kind)
        return Response(serializer.data)


class KindModelViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = KindSerializer


class KindCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
