from rest_framework import serializers
from .models import City
from collections import OrderedDict

class CitySerializer(serializers.ModelSerializer):
	region = serializers.CharField(source='region.name')
	country = serializers.CharField(source='region.country')

	class Meta:
		model = City
		fields = ('cdek_code', 'name', 'region', 'country')
		
