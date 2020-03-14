from db_settings import *
from pyexcel_ods3 import get_data
import os
from peewee import *
db.connect
#db.create_tables([cdek_city_region, cdek_city_city])
collect = {}
for file in os.listdir(): 
	if file.endswith('.ods'):
		data = get_data(file)
		print(f'Downloading {file}')
		for i in data:
		#for i in data['Part_1'][1::]:
		#	print(i)
			try:
				print('pfuheprf')
				country = city_api_country.create(name = data[i][11], code = data[i][10] )
				print('2')
				region = city_api_region.create(name = data[i][3], country = country)
				city_api_city.create(
					ID = data[i][0],
					full_name = data[i][1],
					city_name = data[i][2],
					region = region,
					center = data[i][4],
					nal_sum_limit = data[i][5],
					eng_name = data[i][6],
					post_code_list = data[i][7],
					country = country
						)
			except IndexError:
				print(f'{file} now is done!')
				break
	
