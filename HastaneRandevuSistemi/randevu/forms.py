from django import forms
from .models import *
from django.contrib.auth import authenticate

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
		fields=[
		'patient_tc_no','patient_name','patient_surname',
		'blood_group_of_patient','mother_name_of_patient','father_name_of_patient',
		'telephone_of_patient','e_mail_of_patient','patient_place_of_birth',
		'patient_date_of_birth','gender_of_patient','password_of_patient'
		]

class GetAppointmentForm(forms.ModelForm):
	class Meta:
		model=Appointments
		fields=[
				'dr_of_appointment','patient_of_appointment','date_of_appointment',
				'begin_time_of_appointment','end_time_of_appointment'
			]