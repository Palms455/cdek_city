from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer
from rest_framework.pagination import PageNumberPagination
from .paginator import PaginationHandlerMixin

# Create your views here.
class BasicPagination(PageNumberPagination):
	#сколько элементов на странице
	page_size = 10
	page_size_query_param = 'page_size'


class CityView(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = CitySerializer
	def get(self, request, format=None, *args, **kwargs):
		country = request.GET.get('country', None)
		region = request.GET.get('region', None)
		cities = City.objects.all()
		if country:
			cities = cities.filter(country=country)
		if region:
			cities = cities.filter(region__name__icontains=region)
		page = self.paginate_queryset(cities)
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
		else:
			serializer = self.serializer_class(cities, many=True)
		return Response(serializer.data)