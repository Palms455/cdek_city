from peewee import *

db = PostgresqlDatabase(
	database = 'django',
	user = 'rustam',
	password = '3301344',
	host = 'localhost'
	)

class BaseModel(Model):
	class Meta:
		database = db

class city_api_country(BaseModel):
	name = CharField(max_length=200)
	code = CharField()

class city_api_region(BaseModel):
	name = CharField(max_length=250)
	country = ForeignKeyField(city_api_country, to_field='name')


class city_api_city(BaseModel):
	ID = IntegerField(unique=True)
	full_name = CharField(max_length=250)
	city_name = CharField(max_length=150)
	region = ForeignKeyField(city_api_region, to_field='name', backref='cities', on_delete='cascade', on_update='cascade')
	center = CharField(max_length=2, null=True)
	nal_sum_limit = CharField(max_length=30)
	eng_name = CharField(max_length=250)
	post_code_list = CharField()
	country = ForeignKeyField(city_api_country, to_field='name')

