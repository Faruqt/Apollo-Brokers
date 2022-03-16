from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# import XMLform serializer 
from .serializers import XMLSerializer

# import XML_to_json function from utils.py file
from .utils import XML_to_json

class ConverterViewSet(ViewSet):

    serializer_class = XMLSerializer
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        return Response({})
