from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import *
from .urls import *

def homepage_view(request):
	patient=Patients.objects.get(patient_tc_no=request.user.username)
	return render(request,'randevu/anasayfa.html',{'patient':patient})

def login_view(request):
	form=LoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		login(request,user)
		patient=Patients.objects.get(patient_tc_no=user.username)
		return redirect('/')
	return render(request,'randevu/login.html',{'form':form})

def logout_view(request):
	logout(request)
	return redirect('/login/')

def sign_in_view(request):
	form=SigninForm(request.POST or None)
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
		user=User.objects._create_user(username=tc_no,password=newpassword,email=e_mail)
		user.save()
		Patients.objects.create(patient_tc_no=tc_no,patient_name=name,patient_surname=surname,blood_group_of_patient=bloodgroup,
								mother_name_of_patient=mothername,father_name_of_patient=fathername,telephone_of_patient=telephone,
								e_mail_of_patient=e_mail,patient_place_of_birth=birthplace,patient_date_of_birth=birthdate,gender_of_patient=gender,password_of_patient=newpassword)
		return render(request,'randevu/anasayfa.html',{})
	return render(request,'randevu/sign_in.html',{'form':form})

def get_appointment(request):
	user=request.user
	form=GetAppointmentForm(request.POST or None)
	if form.is_valid():
		date=form.cleaned_data.get('date_of_appointment')
		dr=form.cleaned_data.get('dr_of_appointment')
		patient=form.cleaned_data.get('patient_of_appointment')
		begin_time=form.cleaned_data.get('begin_time_of_appointment')
		end_time=form.cleaned_data.get('end_time_of_appointment')
		Appointments.objects.create(date_of_appointment=date,dr_of_appointment=dr,patient_of_appointment=patient,begin_time_of_appointment=begin_time,end_time_of_appointment=end_time)
		return render(request,'randevu/anasayfa.html',{})
	return render(request,'randevu/get_randevu.html',{'form':form})


