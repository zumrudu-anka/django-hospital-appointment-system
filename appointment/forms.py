from django import forms
from .models import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import datetime

class PatientForm(forms.ModelForm):
	first_name = forms.CharField(
		max_length = 150,
		widget = forms.TextInput(
			attrs={
				"class" : "textbox",
				"placeholder" : "First Name",
			}
		)
	)
	last_name = forms.CharField(
		max_length = 150,
		widget = forms.TextInput(
			attrs={
				"class" : "textbox",
				"placeholder" : "Last Name",
			}
		)
	)

	email = forms.EmailField(
		widget = forms.EmailInput(
			attrs={
				"class" : "textbox",
				"placeholder" : "username@example.com",
			}
		)
	)

	password = forms.CharField(
		widget = forms.PasswordInput(
			attrs = {
				"class" : "textbox",
				"placeholder" : "Password",
			}
		)
	)

	class Meta:
		"""Meta definition for Patientform."""

		model = Patient
		exclude = (
			'user',
		)
		widgets = {
			"identification_number": forms.TextInput(
				attrs={
					"class" : "textbox",
					"placeholder" : "Identification Number",
					"max_length" : 11
				}
			),
			"birth_place": forms.Select(
				attrs={
					"class" : "textbox",
				}
			),
			"birth_date": forms.DateInput(
				attrs={
					"class" : "textbox",
					"type" : "date"
				}
			),
			"father_name": forms.TextInput(
				attrs={
					"class" : "textbox",
					"placeholder" : "Father Name",
					"max_length" : 15
				}
			),
			"mother_name": forms.TextInput(
				attrs={
					"class" : "textbox",
					"placeholder" : "Mother Name",
					"max_length" : 15
				}
			),
			"phone_number": forms.TextInput(
				attrs={
					"class" : "textbox",
					"placeholder" : "Phone Number",
					"max_length" : 20
				}
			),
			"blood_group": forms.Select(
				attrs={
					"class" : "textbox",
				}
			),
			"gender": forms.Select(
				attrs={
					"class" : "textbox",
				}
			),
		}


class CityForm(forms.Form):
	city = forms.ModelChoiceField(
		queryset=City.objects.all(),
		widget=forms.Select(
			attrs={
				"class" : "form-control"
			}
		)
	)

class CountyForm(forms.Form):
	
	def __init__(self,*args,**kwargs):
		city = kwargs.pop('city')
		counties = County.objects.filter(city = city)
		super(CountyForm, self).__init__(*args,**kwargs)
		self.fields['county'] = forms.ModelChoiceField(queryset = counties)
		self.fields['county'].widget.attrs.update({'class':'form-control'})


class HospitalForm(forms.Form):
	
	def __init__(self,*args,**kwargs):
		county = kwargs.pop('county')
		hospitals = Hospital.objects.filter(county = county)
		super(HospitalForm, self).__init__(*args,**kwargs)
		self.fields['hospital'] = forms.ModelChoiceField(queryset=hospitals)
		self.fields['hospital'].widget.attrs.update({'class':'form-control'})

class PolyclinicForm(forms.Form):
	
	def __init__(self,*args,**kwargs):
		hospital = kwargs.pop('hospital')
		polyclinics = Polyclinic.objects.filter(hospital = hospital)
		super(PolyclinicForm, self).__init__(*args,**kwargs)
		self.fields['polyclinic'] = forms.ModelChoiceField(queryset = polyclinics)
		self.fields['polyclinic'].widget.attrs.update({'class':'form-control'})

class DoctorForm(forms.Form):
	
	def __init__(self,*args,**kwargs):
		polyclinic = kwargs.pop('polyclinic')
		doctors = Doctor.objects.filter(polyclinic = polyclinic)
		super(DoctorForm, self).__init__(*args,**kwargs)
		self.fields['doctor'] = forms.ModelChoiceField(queryset=doctors)
		self.fields['doctor'].widget.attrs.update({'class':'form-control'})

# class AppointmentForm(forms.Form):
# 	date = forms.DateField(
# 		initial = datetime.date.today,
# 		label = "Appointment Date"
# 	)
# 	time = forms.TimeField(
# 		widget = forms.TimeInput(
# 			format = '%H:%M',
# 		),
# 		label = "Appointment Time",
# 		initial = datetime.datetime.now().strftime('%H:%M:%S')
# 	)


# class LoginForm(forms.Form):
# 	username = forms.CharField()
# 	password = forms.CharField(widget=forms.PasswordInput)

# 	def clean(self):
# 		username=self.cleaned_data.get('username')
# 		password=self.cleaned_data.get('password')
# 		if username and password:
# 			user = authenticate(username=username,password=password)
# 			if not user:
# 				raise forms.ValidationError('Kullanıcı adını veya parolayı yanlış girdiniz!')
# 		return super(LoginForm,self).clean()

# class ChangePassForm(forms.Form):
	
# 	old_password=forms.CharField()
# 	new_password=forms.CharField()
# 	again_new_pass=forms.CharField()

# 	def __init__(self,*args,**kwargs):
# 		user=kwargs.pop('user')
# 		super(ChangePassForm,self).__init__(*args,**kwargs)
# 		self.user=user
# 		self.fields['old_password'].widget = forms.PasswordInput()
# 		self.fields['new_password'].widget = forms.PasswordInput()
# 		self.fields['again_new_pass'].widget = forms.PasswordInput()
	
# 	def clean(self):
# 		old_password = self.cleaned_data.get('old_password')
# 		if not self.user.check_password(old_password):
# 			raise forms.ValidationError('Eski şifrenizi yanlış girdiniz!')
# 		return super(ChangePassForm,self).clean()

# class SigninForm(forms.ModelForm):
	
# 	class Meta:
# 		model=Patients
# 		exclude=[]

# 	def __init__(self,*args,**kwargs):
# 		super(SigninForm, self).__init__(*args,**kwargs)
# 		CHOICES=[('Bay','Bay'),('Bayan','Bayan')]
# 		BloodGroups=[
# 					('0 Rh-','0 Rh-'),('0 Rh+','0 Rh+'),
# 					('A Rh-','A Rh-'),('A Rh+','A Rh+'),
# 					('B Rh-','B Rh-'),('B Rh+','B Rh+'),
# 					('AB Rh-','AB Rh-'),('AB Rh+','AB Rh+'),
# 					]
# 		self.fields['gender_of_patient'].widget = forms.widgets.RadioSelect(choices=CHOICES)
# 		self.fields['patient_tc_no'] = forms.CharField(max_length=11)
# 		self.fields['patient_name'] = forms.CharField(max_length=25)
# 		self.fields['patient_surname'] = forms.CharField(max_length=25)
# 		self.fields['blood_group_of_patient']=forms.ChoiceField(choices=BloodGroups)
# 		self.fields['mother_name_of_patient'] = forms.CharField(max_length=15)
# 		self.fields['father_name_of_patient'] = forms.CharField(max_length=15)
# 		self.fields['telephone_of_patient'] = forms.CharField(max_length=15)
# 		self.fields['e_mail_of_patient'] = forms.CharField(max_length=25)
# 		self.fields['patient_place_of_birth'] = forms.CharField(max_length=15)
# 		self.fields['patient_date_of_birth'] = forms.DateField(initial=datetime.date.today)
# 		self.fields['password_of_patient'] = forms.CharField(max_length=25)

# class ChooseCityForm(forms.Form):
	
# 	def __init__(self,*args,**kwargs):
# 		super(ChooseCityForm, self).__init__(*args,**kwargs)
# 		self.fields['city_name'] = forms.ModelChoiceField(queryset=City.objects.annotate())
# 		self.fields['city_name'].widget.attrs.update({'class':'form-control'})

# class ChooseCountyForm(forms.Form):
	
# 	def __init__(self,*args,**kwargs):
# 		city = kwargs.pop('city')
# 		counties = County.objects.filter(city_of_county = city)
# 		super(ChooseCountyForm, self).__init__(*args,**kwargs)
# 		self.fields['county_name'] = forms.ModelChoiceField(queryset=counties.annotate())
# 		self.fields['county_name'].widget.attrs.update({'class':'form-control'})

# class ChooseHospitalForm(forms.Form):
	
# 	def __init__(self,*args,**kwargs):
# 		county = kwargs.pop('county')
# 		hospitals = Hospitals.objects.filter(county_of_hospital = county)
# 		super(ChooseHospitalForm, self).__init__(*args,**kwargs)
# 		self.fields['hospital_name'] = forms.ModelChoiceField(queryset=hospitals.annotate())
# 		self.fields['hospital_name'].widget.attrs.update({'class':'form-control'})


# class ChoosePolyclinicForm(forms.Form):
	
# 	def __init__(self,*args,**kwargs):
# 		hospital = kwargs.pop('hospital')
# 		polyclinics = Polyclinics.objects.filter(hospital_of_polyclinic = hospital)
# 		super(ChoosePolyclinicForm, self).__init__(*args,**kwargs)
# 		self.fields['polyclinic_name'] = forms.ModelChoiceField(queryset=polyclinics.annotate())
# 		self.fields['polyclinic_name'].widget.attrs.update({'class':'form-control'})


# class ChooseDrForm(forms.Form):
	
# 	def __init__(self,*args,**kwargs):
# 		polyclinic = kwargs.pop('polyclinic')
# 		doctors = Doctors.objects.filter(polyclinic_of_doctor = polyclinic)
# 		super(ChooseDrForm, self).__init__(*args,**kwargs)
# 		self.fields['dr_name'] = forms.ModelChoiceField(queryset=doctors.annotate())
# 		self.fields['dr_name'].widget.attrs.update({'class':'form-control'})


# class GetAppointmentForm(forms.Form):

# 	def __init__(self,*args,**kwargs):
# 		super(GetAppointmentForm,self).__init__(*args,**kwargs)
# 		self.fields['date_of_appointment'] = forms.DateField(initial=datetime.date.today,label="Randevu Tarihi")
# 		self.fields['begin_time_of_appointment'] = forms.TimeField(widget=forms.TimeInput(format='%H:%M'),label="Randevu Saati",initial=datetime.datetime.now().strftime('%H:%M:%S'))