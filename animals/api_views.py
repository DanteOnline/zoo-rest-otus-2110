from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Kind
from .serializers import KindSerializer


class KindAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        kinds = Kind.objects.all()
        serializer = KindSerializer(kinds, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def kind_view(request):
    kinds = Kind.objects.all()
    serializer = KindSerializer(kinds, many=True)
    return Response(serializer.data)
