from rest_framework import serializers
from .models import City


class CitySerializer(serializers.ModelSerializer):
	region = serializers.CharField(source='region.name')

	class Meta:
		model = City
		fields = ('ID', 'city_name', 'region', 'country')
		
	