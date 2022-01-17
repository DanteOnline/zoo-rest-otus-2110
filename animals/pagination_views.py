from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import Kind
from .serializers import KindSerializer


class KindPageNumberPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer


class KindLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class KindLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Kind.objects.all()
    serializer_class = KindSerializer
    pagination_class = KindLimitOffsetPagination
