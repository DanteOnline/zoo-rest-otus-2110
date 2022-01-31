from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import generics, serializers, mixins, viewsets

from animals.models import Family


@login_required
def index_view(request):
    return render(request, 'animals_with_tests/index.html', {'title': 'Главная страница'})


class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ('name',)


#
# class FamilyViewSet(generics.ListCreateAPIView):
#     permission_classes = [permissions.AllowAny]
#     queryset = Family.objects.all()
#     serializer_class = FamilySerializer


class FamilyViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Family.objects.all()
    serializer_class = FamilySerializer


class FamilyPermissionViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.UpdateModelMixin,
                                viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Family.objects.all()
    serializer_class = FamilySerializer