from django.contrib import admin
from .models import *

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	fields = (
		'name',
	)

	list_display = (
		'name',
	)

	search_fields = [
		'name',
	]

	ordering = (
		'name',
	)

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
	
	list_display=(
		'name',
		'city'
	)

	list_filter=(
		'city',
	)

	search_fields=[
		'name',
		'city__name'
	]

	ordering=(
		'city',
		'name'
	)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):

	list_display=[
		'name',
		'county',
		'phone_number'
	]

	list_filter=(
		'county',
	)

	search_fields=[
		'name',
		'county',
		'phone_number'
	]
    
@admin.register(Polyclinic)
class PolyclinicsAdmin(admin.ModelAdmin):

	list_display=(
		'name',
		'hospital'
	)

	list_filter=(
		'name',
		'hospital'
	)

	search_fields=(
		'name',
		'hospital'
	)

@admin.register(Doctor)
class DoctorsAdmin(admin.ModelAdmin):

	list_display=(
		'identification_number',
		'first_name','last_name',
		'expertise',
		'polyclinic',
		'phone_number'
	)

	list_filter=(
		'expertise',
		'polyclinic'
	)

	search_fields=(
		'identification_number',
		'first_name',
		'last_name',
		'phone_number'
	)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

	list_display=(
		'identification_number',
		'first_name',
		'last_name',
		'email',
		'phone_number',
	)

	list_filter=(
		'birth_place',
		'gender',
		'blood_group'
	)

	search_fields=(
		'identification_number',
		'user__first_name',
		'user__last_name',
		'phone_number',
		'user__email'
	)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

	list_display=(
		'doctor',
		'patient',
		'date'
	)
	
	search_fields=(
		'doctor__first_name',
		'patient__user__first_name'
	)