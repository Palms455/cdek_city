from db_settings import *
from pyexcel_ods3 import get_data
import os
from peewee import *
db.connect
collect = {}
for file in os.listdir(): 
	if file.endswith('.ods'):
		data = get_data(file)
		print(f'Downloading {file}')
		for i in data['Part 1'][1::]:
			try:
				regi = None
				if i[3]:
					try:
						regi = city_api_region.get(name = i[3])
					except DoesNotExist:
						regi = city_api_region.create(name = i[3])
					city = i[2]
					if city.endswith('обл.'):
						city = city.split(',')[0]
					city_api_city.create(
						ID = i[0],
						city_name = city,
						region = regi.id,
						country = i[11]
							)
				else:
					city = i[2]
					try:
						if city.endswith('обл.'):
							city = city.split(',')[0]
					except AttributeError:
						city = i[2]
					city_api_city.create(
						ID = i[0],
						city_name = city,
						region = None,
						country = i[11]
							)
			except IndexError:
				print(f'{file} now is done!')
				break
	
