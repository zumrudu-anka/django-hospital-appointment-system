from django.urls import path
from .views import *
app_name='randevu'

urlpatterns=[
	path('', homepage_view, name='anasayfa'),
	path('user_profile',profilepage_view,name='profilepage'),
	path('login/',login_view,name='login_view'),
	path('logout',logout_view,name='logout_view'),
	path('signin/',sign_in_view,name='sign_in_view'),
	path('randevu_al/',get_appointment,name='get_appointment'),
]