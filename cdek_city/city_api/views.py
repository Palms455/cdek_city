from rest_framework.views import APIView
from rest_framework.response import Response
from .models import City
from .serializers import CitySerializer

# Create your views here.
class CityView(APIView):
	def get(self, request):
		cities = City.objects.all()
		serialize = CitySerializer(cities, many=True)
		return Response(serialize.data)