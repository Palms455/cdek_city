from django.db import models


class Region(models.Model):
	name = models.CharField(max_length=200, unique = True)

	def __str__(self):
		return self.name


class City(models.Model):
	ID = models.CharField(max_length=15, unique=True)
	city_name = models.CharField(max_length=150, null=True)
	region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
	country = models.CharField(max_length =50)


	def __str__(self):
		return self.city_name

