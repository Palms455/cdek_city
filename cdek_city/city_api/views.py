from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer
from rest_framework.pagination import PageNumberPagination
from .paginator import PaginationHandlerMixin


# Create your views here.
class BasicPagination(PageNumberPagination):
	#сколько элементов на странице
	page_size = 100
	page_size_query_param = 'page_size'


class CityView(APIView, PaginationHandlerMixin):
	pagination_class = BasicPagination
	serializer_class = CitySerializer
	def get(self, request, format=None, *args, **kwargs):
		country = request.GET.get('country', '')
		region = request.GET.get('region', '')
		name = request.GET.get('name', '')
		cities = City.objects.filter(city_name__icontains=name,
									 region__country__icontains=country,
									 region__name__icontains=region).order_by('city_name', 'pk')
		
		page = self.paginate_queryset(cities[0:10])
		if page is not None:
			serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
		else:
			serializer = self.serializer_class(cities[0:10], many=True)
		return Response(serializer.data)
		