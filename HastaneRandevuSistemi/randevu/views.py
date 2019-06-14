from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render,render_to_response
from django.template import RequestContext

from .models import *
from .forms import *
from .urls import *
import json

def homepage_view(request):
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		if not user.is_superuser:
			login(request,user)
			return redirect('randevu:profilepage')
	return render(request,'randevu/login.html',{'form':form})

def profilepage_view(request):
	patient=Patients.objects.get(patient_tc_no=request.user.username)
	appoints=Appointments.objects.filter(patient_of_appointment=patient)
	form = ChangePassForm(request.POST or None, user=request.user)
	if form.is_valid():
		newpassword = form.cleaned_data.get('new_password')
		user=request.user
		user.set_password(newpassword)
		user.save()
		update_session_auth_hash(request,user)
		messages.success(request,"Şifreniz Başarıyla Güncellendi!")
		return redirect('randevu:profilepage')
	return render(request,'randevu/profile.html',{'patient':patient,'appoints':appoints,'form':form})

def logout_view(request):
	logout(request)
	return redirect('randevu:homepage')

def sign_in_view(request):
	form = SigninForm(request.POST or None)
	if form.is_valid():
		tc_no=form.cleaned_data.get('patient_tc_no')
		name=form.cleaned_data.get('patient_name')
		surname=form.cleaned_data.get('patient_surname')
		bloodgroup=form.cleaned_data.get('blood_group_of_patient')
		mothername=form.cleaned_data.get('mother_name_of_patient')
		fathername=form.cleaned_data.get('father_name_of_patient')
		telephone=form.cleaned_data.get('telephone_of_patient')
		e_mail=form.cleaned_data.get('e_mail_of_patient')
		birthdate=form.cleaned_data.get('patient_date_of_birth')
		birthplace=form.cleaned_data.get('patient_place_of_birth')
		gender=form.cleaned_data.get('gender_of_patient')
		newpassword=form.cleaned_data.get('password_of_patient')
		user=User.objects._create_user(username=tc_no,password=newpassword,email=e_mail,is_staff=True)
		user.save()
		Patients.objects.create(patient_tc_no=tc_no,patient_name=name,patient_surname=surname,blood_group_of_patient=bloodgroup,
								mother_name_of_patient=mothername,father_name_of_patient=fathername,telephone_of_patient=telephone,
								e_mail_of_patient=e_mail,patient_place_of_birth=birthplace,patient_date_of_birth=birthdate,gender_of_patient=gender,password_of_patient=newpassword)
		return redirect('randevu:homepage')
	return render(request,'randevu/sign_in.html',{'form':form})

def choose_city_view(request):
	patient = Patients.objects.get(patient_tc_no=request.user.username)
	form = ChooseCityForm(request.POST or None)
	if form.is_valid():
		city=form.cleaned_data.get('city_name')
		return redirect('randevu:choose_county',city_id = city.id)
	return render(request,'randevu/choose_city.html',{'form':form,'patient':patient})

def choose_county_view(request, city_id):
	city=City.objects.get(id=city_id)
	form = ChooseCountyForm(request.POST or None, city=city)
	if form.is_valid():
		county=form.cleaned_data.get('county_name')
		return redirect('randevu:choose_hospital',county_id=county.id)
	return render(request,'randevu/choose_county.html',{'form':form,'city':city})

def choose_hospital_view(request,county_id):
	county = County.objects.get(id=county_id)
	form = ChooseHospitalForm(request.POST or None, county=county)
	if form.is_valid():
		hospital = form.cleaned_data.get('hospital_name')
		return redirect('randevu:choose_polyclinic',hospital_id=hospital.id)
	return render(request,'randevu/choose_hospital.html',{'form':form,'county':county})

def choose_polyclinic_view(request,hospital_id):
	hospital=Hospitals.objects.get(id=hospital_id)
	form=ChoosePolyclinicForm(request.POST or None,hospital=hospital)
	if form.is_valid():
		polyclinic = form.cleaned_data.get('polyclinic_name')
		return redirect('randevu:choose_doctor',polyclinic_id=polyclinic.id)
	return render(request,'randevu/choose_polyclinic.html',{'form':form,'hospital':hospital})

def choose_dr_view(request,polyclinic_id):
	polyclinic=Polyclinics.objects.get(id=polyclinic_id)
	form=ChooseDrForm(request.POST or None,polyclinic=polyclinic)
	if form.is_valid():
		dr=form.cleaned_data.get('dr_name')
		return redirect('randevu:get_appointment',doctor_tc=dr.dr_tc_no)
	return render(request,'randevu/choose_doctor.html',{'form':form,'polyclinic':polyclinic})

def get_appointment(request,doctor_tc):
	form=GetAppointmentForm(request.POST or None)
	if form.is_valid():
		date=form.cleaned_data.get('date_of_appointment')
		dr=Doctors.objects.get(dr_tc_no=doctor_tc)
		patient=Patients.objects.get(patient_tc_no=request.user.username)
		begin_time=form.cleaned_data.get('begin_time_of_appointment')
		Appointments.objects.create(date_of_appointment=date,
									dr_of_appointment=dr,
									patient_of_appointment=patient,
									begin_time_of_appointment=begin_time)
		return redirect('randevu:profilepage')
	return render(request,'randevu/get_randevu.html',{'form':form})


