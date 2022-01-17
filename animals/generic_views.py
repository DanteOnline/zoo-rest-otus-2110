from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, \
    DestroyAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
from .models import Kind
from .serializers import KindSerializer


class KindCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Kind.objects.all()
    serializer_class = KindSerializer

# Есть и другие, которые являются комбинацией этих
