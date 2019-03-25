from django.core.management.base import BaseCommand
from randevu.models import City
import json

class Command(BaseCommand):
	def handle(self,*args,**kwarg):
		with open('randevu/static/js/iller.json',encoding='utf-8') as file3:
			json_data3=json.load(file3)
		for i in range(1,82):
			City.objects.get_or_create(pk=i,city_name=json_data3['{}'.format(i)])
