from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .filters import KindFilter
from .models import Kind
from .serializers import KindSerializer


class KindQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = KindSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Kind.objects.all()

    def get_queryset(self):
        return Kind.objects.filter(name__contains='ур')
        # return Kind.objects.filter(user=self.request.user)


class KindKwargsFilterView(ListAPIView):
    serializer_class = KindSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Kind.objects.filter(name__contains=name)


class KindParamFilterViewSet(viewsets.ModelViewSet):
    # http://127.0.0.1:8000/filters/param/?name=ур
    queryset = Kind.objects.all()
    serializer_class = KindSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        kinds = Kind.objects.all()
        if name:
            kinds = kinds.filter(name__contains=name)
        return kinds


class KindDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    filterset_fields = ['name', 'family']


class KindCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    filterset_class = KindFilter
