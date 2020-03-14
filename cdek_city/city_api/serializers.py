from rest_framework import serializers
from .models import City
from collections import OrderedDict

class CitySerializer(serializers.ModelSerializer):
	region = serializers.CharField()

	class Meta:
		model = City
		fields = ('ID', 'city_name', 'region', 'country')
		

	def to_representation(self, instance):
		result = super().to_representation(instance)
		return OrderedDict([(key, result[key]) for key in result if result[key] not in ['0', None]])
	