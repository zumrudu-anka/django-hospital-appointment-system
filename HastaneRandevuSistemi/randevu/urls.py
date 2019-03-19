from django.urls import path
from .views import *
app_name='randevu'

urlpatterns=[
	path('', homepage_view, name='homepage'),
	path('user_profile',profilepage_view,name='profilepage'),
	path('logout',logout_view,name='logout'),
	path('signin/',sign_in_view,name='sign_in'),
	path('randevu_al/',get_appointment,name='get_appointment'),
]