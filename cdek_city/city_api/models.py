from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=200, unique = True)
	code = models.IntegerField()

	def __str__(self):
		return self.name


class Region(models.Model):
	name = models.CharField(max_length=200, unique = True)
	country = models.CharField(max_length=150) 

	def __str__(self):
		return self.name


class City(models.Model):
	ID = models.IntegerField(unique=True)
	full_name = models.CharField(max_length=250)
	city_name = models.CharField(max_length=150)
	region = models.ForeignKey(Region,  on_delete=models.CASCADE)
	center = models.CharField(max_length=2, null=True)
	nal_sum_limit = models.CharField(max_length=30)
	eng_name = models.CharField(max_length=250)
	post_code_list = models.IntegerField()
	country = models.ForeignKey(Country, on_delete=models.CASCADE)

	def __str__(self):
		return self.city_name

