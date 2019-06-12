from django import forms
from .models import *
from django.contrib.auth import authenticate
import datetime

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self):
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz!')
		return super(LoginForm,self).clean()

class SigninForm(forms.ModelForm):
	
	class Meta:
		model=Patients
		exclude=[]

	def __init__(self,*args,**kwargs):
		super(SigninForm, self).__init__(*args,**kwargs)
		CHOICES=[('Bay','Bay'),('Bayan','Bayan')]
		BloodGroups=[
					('0 Rh-','0 Rh-'),('0 Rh+','0 Rh+'),
					('A Rh-','A Rh-'),('A Rh+','A Rh+'),
					('B Rh-','B Rh-'),('B Rh+','B Rh+'),
					('AB Rh-','AB Rh-'),('AB Rh+','AB Rh+'),
					]
		self.fields['gender_of_patient'].widget = forms.widgets.RadioSelect(choices=CHOICES)
		self.fields['patient_tc_no'] = forms.CharField(max_length=11)
		self.fields['patient_name'] = forms.CharField(max_length=25)
		self.fields['patient_surname'] = forms.CharField(max_length=25)
		self.fields['blood_group_of_patient']=forms.ChoiceField(choices=BloodGroups)
		self.fields['mother_name_of_patient'] = forms.CharField(max_length=15)
		self.fields['father_name_of_patient'] = forms.CharField(max_length=15)
		self.fields['telephone_of_patient'] = forms.CharField(max_length=15)
		self.fields['e_mail_of_patient'] = forms.CharField(max_length=25)
		self.fields['patient_place_of_birth'] = forms.CharField(max_length=15)
		self.fields['patient_date_of_birth'] = forms.DateField(initial=datetime.date.today)
		self.fields['password_of_patient'] = forms.CharField(max_length=25)

class GetAppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointments
		fields=[
				'dr_of_appointment','date_of_appointment',
				'begin_time_of_appointment',
			]

