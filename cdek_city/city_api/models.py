from django.db import models


class Region(models.Model):
	name = models.CharField(max_length=100, unique = True, verbose_name='Название')
	country = models.CharField(max_length=100, verbose_name='Страна')

	class Meta:
		verbose_name = 'Регион'
		verbose_name_plural = 'Регионы'

	def __str__(self):
		return self.name


class City(models.Model):
	cdek_code = models.PositiveIntegerField(verbose_name='CDEK ID', unique=True)
	name = models.CharField(max_length=150, verbose_name='Название')
	region = models.ForeignKey(Region, verbose_name='Регион', on_delete=models.CASCADE, null=True, related_name='cities')

	class Meta:
		verbose_name='Город'
		verbose_name_plural='Города'
		unique_together = ('region', 'name',)


	def __str__(self):
		return f'{self.name} {self.region}'

