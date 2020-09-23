from django.core.management.base import BaseCommand
from appointment.models import City, County
import json

class Command(BaseCommand):
	def handle(self,*args,**kwargs):
		with open('appointment/management/jsonFilesForCommands/counties.json') as countiesFile:
			countiesJson=json.load(countiesFile)
			for cityPk, counties in countiesJson.items():
				city = City.objects.get(pk = cityPk)
				for county in counties:
					County.objects.get_or_create(
						city = city,
						name = county["name"]
					)