from django.urls import path
from .views import *

app_name='randevu'

urlpatterns=[
	path('', homepage_view, name='homepage'),
	path('user_profile',profilepage_view,name='profilepage'),
	path('logout',logout_view,name='logout'),
	path('signin/',sign_in_view,name='sign_in'),
	path('choose_city/',choose_city_view,name='choose_city'),
	path('choose_county/',choose_county_view,name='choose_county'),
	path('choose_hospital/',choose_hospital_view,name='choose_hospital'),
	path('choose_polyclinic/',choose_polyclinic_view,name='choose_polyclinic'),
	path('randevu_al/',get_appointment,name='get_appointment'),
]

