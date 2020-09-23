from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import (
	authenticate,
	login,
	logout,
	update_session_auth_hash
)
from django.contrib.auth.models import User
from django.contrib.auth.forms import(
	AuthenticationForm,
	PasswordChangeForm,
	UserCreationForm

)
from django.contrib import messages

from .models import *
from .forms import *

def index(request):
	form = AuthenticationForm(data = request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get('username')
		password=form.cleaned_data.get('password')
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request, user)
			return redirect('appointment:profile')
	return render(request,'appointment/login.html',{'form':form})

@login_required(login_url = "appointment:index")
def profile(request):
	patient = Patient.objects.get(identification_number = request.user.username)
	appointments = Appointment.objects.filter(patient = patient)
	form = PasswordChangeForm(request.user, request.POST or None)
	context = {
		"patient" : patient,
		"appointments" : appointments,
		"form" : form
	}
	if form.is_valid():
		user = form.save()
		update_session_auth_hash(request, user)
		messages.success(request, 'Your password was successfully updated!')
		return redirect('appointment:profile')
	return render(request,'appointment/profile.html', context)

def logout_view(request):
	logout(request)
	return redirect('appointment:index')

def sign_up(request):
	form = PatientForm(request.POST or None)
	context = {
		"form" : form,
	}
	if form.is_valid():
		patient = form.save(commit = False)
		user = User.objects.create(
			username = patient.identification_number,
			first_name = form.cleaned_data.get("first_name"),
			last_name = form.cleaned_data.get("last_name"),
			email = form.cleaned_data.get("email")
		)
		user.set_password(form.cleaned_data.get("password"))
		user.save()
		patient.user = user
		patient.save()
		return redirect("appointment:index")
	return render(request, 'appointment/sign_up.html', context)

@login_required(login_url = "appointment:index")
def choose_city(request):
	form = CityForm(request.POST or None)
	context = {
		"form" : form
	}
	if form.is_valid():
		city = form.cleaned_data.get("city")
		return redirect('appointment:choose_county', cityPk = city.pk)
	return render(request,'appointment/choose_city.html', context)

@login_required(login_url = "appointment:index")
def choose_county(request, cityPk):
	city = City.objects.get(pk = cityPk)
	form = CountyForm(request.POST or None, city = city)
	context = {
		"form" : form,
		"city" : city,
	}
	if form.is_valid():
		county = form.cleaned_data.get('county')
		return redirect('appointment:choose_hospital', countyPk = county.pk)
	return render(request, 'appointment/choose_county.html', context)

@login_required(login_url = "appointment:index")
def choose_hospital(request, countyPk):
	county = County.objects.get(pk = countyPk)
	city = City.objects.get(pk = county.city.pk)
	form = HospitalForm(request.POST or None, county = county)
	context = {
		"form" : form,
		"city" : city,
		"county" : county,
	}
	if form.is_valid():
		hospital = form.cleaned_data.get('hospital')
		return redirect('appointment:choose_polyclinic', hospitalPk = hospital.pk)
	return render(request,'appointment/choose_hospital.html', context)

@login_required(login_url = "appointment:index")
def choose_polyclinic(request, hospitalPk):
	hospital = Hospital.objects.get(pk = hospitalPk)
	form = PolyclinicForm(request.POST or None, hospital = hospital)
	context = {
		"form" : form,
		"hospital" : hospital
	}
	if form.is_valid():
		polyclinic = form.cleaned_data.get('polyclinic')
		return redirect('appointment:choose_doctor', polyclinicPk = polyclinic.pk)
	return render(request, 'appointment/choose_polyclinic.html', context)

def choose_doctor(request, polyclinicPk):
	polyclinic = Polyclinic.objects.get(pk = polyclinicPk)
	form = DoctorForm(request.POST or None, polyclinic=polyclinic)
	context = {
		"form": form,
		"polyclinic" : polyclinic
	}
	if form.is_valid():
		doctor = form.cleaned_data.get('doctor')
		return redirect('appointment:make_an_appointment', doctorPk = doctor.pk)
	return render(request,'appointment/choose_doctor.html', context)

def make_an_appointment(request, doctorPk):
	doctor = Doctor.objects.get(pk = doctorPk)
	context = {
		"doctor" : doctor
	}
	if request.method == "POST":
		date = request.POST['date']
		time = request.POST['time']
		patient = Patient.objects.get(user = request.user)
		Appointment.objects.create(
			date = f"{date} {time}",
			doctor = doctor,
			patient = patient
		)
		messages.success(request, "Making Appointment Successfully Completed!")
		return redirect('appointment:profile')
	return render(request,'appointment/make_an_appointment.html', context)