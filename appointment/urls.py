from django.urls import path
from .views import (
	index,
	profile,
	sign_up,
	logout_view,
	choose_city,
	choose_county,
	choose_hospital,
	choose_polyclinic,
	choose_doctor,
	make_an_appointment
)

app_name = 'appointment'

urlpatterns=[
	path('', index, name='index'),
	path('profile', profile, name='profile'),
	path('signup/',sign_up,name='sign_up'),
	path('logout',logout_view,name='logout'),
	path('choose_city/', choose_city, name='choose_city'),
	path('<int:cityPk>/choose_county/', choose_county, name='choose_county'),
	path('<int:countyPk>/choose_hospital/', choose_hospital, name='choose_hospital'),
	path('<int:hospitalPk>/choose_polyclinic/', choose_polyclinic, name='choose_polyclinic'),
	path('<int:polyclinicPk>/choose_doctor/', choose_doctor, name='choose_doctor'),
	path('<int:doctorPk>/make_an_appointment/', make_an_appointment, name='make_an_appointment'),
]