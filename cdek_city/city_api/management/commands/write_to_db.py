from city_api.models import City, Region
from django.core.management.base import BaseCommand, CommandError
import json
import os
import pyexcel as pe
os.environ.setdefault('DJANGO_SETTING_MODULE', 'settings')


class Command(BaseCommand):

	def handle(self,*args, **options):
		Region.objects.all().delete()
		for file in os.listdir():
			if file.endswith('.ods'):
				print('file')
				for record in pe.iget_records(file_name=file):
					if record.get('OblName', None) and record.get('CityName', None) and record.get('ID', None):
						region, created = Region.objects.get_or_create(name = record['OblName'], country=record['CountryName'])
						if created:
							print(f'Created Region {region}')
						if isinstance(record['CityName'], str):
							name = record['CityName'].split(',')[0]
							if not City.objects.filter(city_name=name, region=region).exists():
								city = City.objects.create(city_name=name, region=region, cdek_code=record['ID'])
