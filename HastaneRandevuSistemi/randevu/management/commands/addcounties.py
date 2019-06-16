from django.core.management.base import BaseCommand
from randevu.models import City,County
import json

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		with open('randevu/static/js/ilceler.json') as file2:
			json_data2=json.load(file2)
		for i in range(1,82):
			for j in (json_data2['{}'.format(i)]):
				city=City.objects.get(pk=i)
				County.objects.get_or_create(city_of_county=city,county_name=j['name'])