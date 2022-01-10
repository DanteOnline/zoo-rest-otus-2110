from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import Family


class FamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'

# HyperlinkedModelSerializer
# class FamilySerializer(HyperlinkedModelSerializer):
#     class Meta:
#         model = Family
#         fields = '__all__'
