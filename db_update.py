from db_settings import *
from pyexcel_ods3 import get_data
import os



def write_to_db():
	db.connect
	for file in os.listdir(): 
		if file.endswith('.ods'):
			data = get_data(file)
			print(f'Downloading {file}')
			for i in data['Part 1'][1::]:
				try:
					city = i[2]
					try:
						if city.endswith('обл.'):
							city = city.split(',')[0]
					except AttributeError:
						city = i[2]
					region_id = None
					if i[3]:
						try:
							regi = city_api_region.get(name = i[3])
						except DoesNotExist:
							regi = city_api_region.create(name = i[3])
						region_id = regi.id	
						
					city_api_city.create(
						ID = i[0],
						city_name = city,
						region = region_id,
						country = i[11]
						)
				except IndexError:
					print(f'{file} now is done!')
					break
	
if __name__ == '__main__':
	write_to_db()
