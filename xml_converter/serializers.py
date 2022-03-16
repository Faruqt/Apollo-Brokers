# import serializer from rest_framework
from rest_framework import serializers
 
# XML DOcument form serializer
class XMLSerializer(serializers.Serializer):
	files = serializers.FileField()

	class Meta:
		fields = ['file_upload']
