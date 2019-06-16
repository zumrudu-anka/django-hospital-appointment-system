from django.urls import path
from .views import *

app_name='randevu'

urlpatterns=[
	path('', homepage_view, name='homepage'),
	path('user_profile',profilepage_view,name='profilepage'),
	path('logout',logout_view,name='logout'),
	path('signin/',sign_in_view,name='sign_in'),
	path('choose_city/',choose_city_view,name='choose_city'),
	path('<int:city_id>/choose_county/',choose_county_view,name='choose_county'),
	path('<int:county_id>/choose_hospital/',choose_hospital_view,name='choose_hospital'),
	path('<int:hospital_id>/choose_polyclinic/',choose_polyclinic_view,name='choose_polyclinic'),
	path('<int:polyclinic_id>/choose_doctor/',choose_dr_view,name='choose_doctor'),
	path('<int:doctor_tc>/get_appointment/',get_appointment,name='get_appointment'),
]