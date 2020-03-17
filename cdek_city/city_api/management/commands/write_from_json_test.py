from city_api.models import City, Region
from django.core.management.base import BaseCommand, CommandError
import json
import os
os.environ.setdefault('DJANGO_SETTING_MODULE', 'settings')


class Command(BaseCommand):

	def handle(self,*args, **options):
		Region.objects.all().delete()
		with open('./data/city_ru.json', 'r', encoding='utf-8') as file:
			data = json.load(file)
			for item in data['items']:
				region, created = Region.objects.get_or_create(name = item['region_code'], country='Россия')
				if created:
					print(f'Created Region {region}')
				if not City.objects.filter(name=item['city'], region=region).exists():
					if not City.objects.filter(cdek_code=item['code']).exists():
						city = City.objects.create(name=item['city'], region=region, cdek_code=item['code'])
					else:
						print(item['city'], item['code'])
				else:
					print(item['city'], region, item['code'])
