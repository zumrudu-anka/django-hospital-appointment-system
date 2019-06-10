from django.contrib import admin
from .models import *

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
	fields=('city_name',)
	list_display=('city_name',)
	list_filter=('city_name',)
	search_fields=['city_name']
	ordering=('city_name',)
@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
	fields=('county_name','city_of_county')
	list_display=('county_name','city_of_county')
	list_filter=('city_of_county',)
	search_fields=['county_name','city_of_county__city_name']
	ordering=('city_of_county',)

@admin.register(Hospitals)
class HospitalAdmin(admin.ModelAdmin):
	fields=('hospital_name','county_of_hospital','hospital_telephone','begin_time','end_time','hospital_address')
	list_display=['hospital_name','county_of_hospital','hospital_telephone']
	list_filter=('county_of_hospital__city_of_county',)
	search_fields=['hospital_name','county_of_hospital__city_of_county__city_name','hospital_telephone']
    
@admin.register(Polyclinics)
class PolyclinicsAdmin(admin.ModelAdmin):
	fields=('polyclinic_name','hospital_of_polyclinic')
	list_display=('polyclinic_name','hospital_of_polyclinic')
	list_filter=('polyclinic_name','hospital_of_polyclinic')
	search_fields=('polyclinic_name','hospital_of_polyclinic')

@admin.register(Doctors)
class DoctorsAdmin(admin.ModelAdmin):
	fields=('dr_tc_no','dr_name','dr_surname','expertise_of_dr','polyclinic_of_doctor',
			'gender_of_dr','dr_date_of_birth','dr_place_of_birth','telephone_of_dr')
	list_display=('dr_tc_no','dr_name','dr_surname','expertise_of_dr','polyclinic_of_doctor','telephone_of_dr')
	list_filter=('dr_tc_no','dr_name','dr_surname','expertise_of_dr','polyclinic_of_doctor','telephone_of_dr')
	search_fields=('dr_tc_no','dr_name','dr_surname','expertise_of_dr','polyclinic_of_doctor','telephone_of_dr')

@admin.register(Patients)
class PatientAdmin(admin.ModelAdmin):
	fields=('patient_tc_no','patient_name','patient_surname','blood_group_of_patient',
		'mother_name_of_patient','father_name_of_patient','patient_date_of_birth','patient_place_of_birth',
		'gender_of_patient','telephone_of_patient','e_mail_of_patient')
	list_display=('patient_tc_no','patient_name','patient_surname','telephone_of_patient','e_mail_of_patient')
	list_filter=('patient_tc_no','patient_name','patient_surname','telephone_of_patient','e_mail_of_patient')
	search_fields=('patient_tc_no','patient_name','patient_surname','telephone_of_patient','e_mail_of_patient')

@admin.register(Appointments)
class AppointmentAdmin(admin.ModelAdmin):
	fields=('date_of_appointment','dr_of_appointment','patient_of_appointment','begin_time_of_appointment')
	list_display=('date_of_appointment','dr_of_appointment','patient_of_appointment')
	list_filter=('date_of_appointment','dr_of_appointment','patient_of_appointment')
	search_fields=('date_of_appointment','dr_of_appointment','patient_of_appointment')