from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Family, Kind


class FamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


class KindSerializer(ModelSerializer):
    class Meta:
        model = Kind
        fields = '__all__'


class KindHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    family = HyperlinkedRelatedField(
        many=False,
        read_only=True,
        view_name='animals:family-detail'
    )

    class Meta:
        model = Kind
        fields = '__all__'


class KindSerializerBase(ModelSerializer):
    class Meta:
        model = Kind
        fields = ('name',)
