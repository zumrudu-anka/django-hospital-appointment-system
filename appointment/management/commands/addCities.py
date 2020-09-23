from django.core.management.base import BaseCommand
from appointment.models import City
import json

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		with open('appointment/management/jsonFilesForCommands/cities.json',encoding='utf-8') as citiesFile:
			citiesJson=json.load(citiesFile)
		for key, value in citiesJson.items():
			City.objects.get_or_create(
				pk = key,
				name = value
			)