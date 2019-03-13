from django.conf.urls import url
from .views import *
app_name='randevu'

urlpatterns=[
	url(r'^$',homepage_view,name='anasayfa'),
	url(r'^login/$',login_view,name='login_view'),
	url(r'^signin/$',sign_in_view,name='sign_in_view'),
	url(r'^randevu_al/$',get_appointment,name='get_appointment'),
]