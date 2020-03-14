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

class city_api_region(BaseModel):
	name = CharField(max_length=250)
	
class city_api_city(BaseModel):
	ID = CharField(unique=True)
	city_name = CharField(max_length=150, null=True)
	region = ForeignKeyField(city_api_region, to_field='name', backref='cities', on_delete='cascade', on_update='cascade', null=True)
	country = CharField(max_length = 150)