from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

# import XMLform serializer 
from .serializers import XMLSerializer

# import XML_to_json function from utils.py file
from .utils import XML_to_json

class ConverterViewSet(ViewSet):

    # the serializer class will be used to validate 
    # and deserialize the custom XMLSerializer
    serializer_class = XMLSerializer

    #This allows for file uploads
    parser_classes = [MultiPartParser]


    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):

        xml_serializer = XMLSerializer(data=request.data)

        #confirm that input contains accurate data
        if xml_serializer.is_valid():

            #extract xml file from serialized data
            xml_doc = xml_serializer.validated_data['files']

            # pass xml file to xmltojson function in utils.py
            converted_XML = XML_to_json(xml_doc)
            
            return Response(converted_XML)
        
        return Response(xml_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

