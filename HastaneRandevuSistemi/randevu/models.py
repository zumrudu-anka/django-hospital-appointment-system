from django.db import models
from django.core.exceptions import ValidationError

import datetime

Genders=(('Erkek','Erkek'),
		('Kadın','Kadın')
	)

BloodGroups=(('0 Rh-','0 Rh-'),
	('0 Rh+','0 Rh+'),
	('A Rh-','A Rh-'),
	('A Rh+','A Rh+'),
	('B Rh-','B Rh-'),
	('B Rh+','B Rh+'),
	('AB Rh-','AB Rh-'),
	('AB Rh+','AB Rh+'),
	)

class City(models.Model):
	city_name = models.CharField(max_length = 75,verbose_name='Şehir Adı')

	def __str__(self):
		return '{}'.format(self.city_name)

	def clean(self):
		try:
			temp=City.objects.get(city_name=self.city_name)
		except City.DoesNotExist:
			pass
		else:
			raise ValidationError({"city_name":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name = 'Şehirler'
		verbose_name_plural='Şehirler'

class County(models.Model):
	county_name = models.CharField(max_length=75,verbose_name='İlçe')
	city_of_county = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name='Şehir')

	def __str__(self):
		return '{}'.format(self.county_name)

	def clean(self):
		try:
			temp=County.objects.get(county_name=self.county_name)
		except County.DoesNotExist:
			pass
		else:
			raise ValidationError({"county_name":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name='İlçeler'
		verbose_name_plural='İlçeler'

class Hospitals(models.Model):
	county_of_hospital=models.ForeignKey(County,on_delete=models.CASCADE,verbose_name='İlçe')
	hospital_name=models.CharField(max_length=75,verbose_name='Hastane Adı')
	begin_time=models.TimeField(verbose_name='Açılış Saati')
	end_time=models.TimeField(verbose_name='Kapanış Saati')
	hospital_telephone=models.CharField(max_length=20,verbose_name='Telefon No')
	hospital_address=models.TextField(max_length=200,verbose_name='Adres')
	
	def __str__(self):
		return '{} - {} - {}'.format(self.hospital_name,self.begin_time,self.end_time)

	def clean(self):
		try:
			temp=Hospitals.objects.get(hospital_name=self.hospital_name,county_of_hospital=self.county_of_hospital)
		except Hospitals.DoesNotExist:
			pass
		else:
			raise ValidationError({"hospital_name":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name='Hastaneler'
		verbose_name_plural='Hastaneler'

class Polyclinics(models.Model):
	hospital_of_polyclinic=models.ForeignKey(Hospitals,on_delete=models.CASCADE,verbose_name='Hastane')
	polyclinic_name=models.CharField(max_length=50,verbose_name='Poliklinik Adı')

	def __str__(self):
		return '{} - {}'.format(self.hospital_of_polyclinic,self.polyclinic_name)

	def clean(self):
		try:
			temp=Polyclinics.objects.get(polyclinic_name=self.polyclinic_name,hospital_of_polyclinic=self.hospital_of_polyclinic)
		except Polyclinics.DoesNotExist:
			pass
		else:
			raise ValidationError({"polyclinic_name":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name='Poliklinikler'
		verbose_name_plural='Poliklinikler'

class Doctors(models.Model):
	polyclinic_of_doctor=models.ForeignKey(Polyclinics,verbose_name='Poliklinik',on_delete=models.CASCADE)
	dr_tc_no=models.CharField(max_length=15,primary_key=True,verbose_name='Tc No')
	dr_name=models.CharField(max_length=25,verbose_name='Adı')
	dr_surname=models.CharField(max_length=25,verbose_name='Soyadı')
	telephone_of_dr=models.CharField(max_length=20,verbose_name='Telefon No')
	expertise_of_dr=models.CharField(max_length=25,verbose_name='Uzmanlık')
	dr_place_of_birth=models.CharField(max_length=15,verbose_name='Dogum Yeri')
	dr_date_of_birth=models.DateField(verbose_name='Doğum Tarihi')
	gender_of_dr=models.CharField(max_length=5,verbose_name='Cinsiyet',choices=Genders)
	
	def __str__(self):
		return '{} - {} - {} - {} - {}'.format(self.polyclinic_of_doctor.hospital_of_polyclinic.hospital_name,
											   self.polyclinic_of_doctor.polyclinic_name,
											   self.dr_name,self.dr_surname,self.gender_of_dr)

	def clean(self):
		try:
			temp =Doctors.objects.get(telephone_of_dr=self.telephone_of_dr)
		except Doctors.DoesNotExist:
			pass
		else:
			raise ValidationError({"telephone_of_dr":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name='Doktorlar'
		verbose_name_plural='Doktorlar'

class Patients(models.Model):
	patient_tc_no = models.CharField(max_length=15,primary_key=True, verbose_name='Tc No')
	patient_name = models.CharField(max_length=25, verbose_name='Adı')
	patient_surname = models.CharField(max_length=25, verbose_name='Soyadı')
	blood_group_of_patient=models.CharField(max_length=5,verbose_name='Kan Grubu',choices=BloodGroups)
	mother_name_of_patient=models.CharField(max_length=15,verbose_name='Anne Adı')
	father_name_of_patient=models.CharField(max_length=15,verbose_name='Baba Adı')
	telephone_of_patient = models.CharField(max_length=20,verbose_name='Telefonu')
	e_mail_of_patient=models.CharField(max_length=50,verbose_name='E-Mail')
	patient_place_of_birth=models.CharField(max_length=15,verbose_name='Doğum Yeri')
	patient_date_of_birth=models.DateField(verbose_name='Doğum Tarihi',default=datetime.date.today)
	gender_of_patient = models.CharField(max_length=5,verbose_name='Cinsiyet',choices=Genders)
	password_of_patient = models.CharField(max_length=16,verbose_name='Parola')

	def __str__(self):
		return '{} - {} - {}'.format(self.patient_name,self.patient_surname,self.gender_of_patient)

	def clean(self):
		try:
			temp = Patients.objects.get(telephone_of_patient=self.telephone_of_patient)
		except Patients.DoesNotExist:
			try:
				temp = Patients.objects.get(e_mail_of_patient=self.e_mail_of_patient)
			except Patients.DoesNotExist:
				pass
			else:
				raise ValidationError({"e_mail_of_patient":"Sistemde Kayıtlı."})
		else:
			raise ValidationError({"telephone_of_patient":"Sistemde Kayıtlı."})

	class Meta:
		verbose_name = 'Hastalar'
		verbose_name_plural = 'Hastalar'

class Appointments(models.Model):
	dr_of_appointment=models.ForeignKey(Doctors,verbose_name='Doktor',on_delete=models.CASCADE)
	patient_of_appointment=models.ForeignKey(Patients,verbose_name='Hasta',on_delete=models.CASCADE)
	date_of_appointment=models.DateField(verbose_name='Randevu Tarihi')
	begin_time_of_appointment=models.TimeField(verbose_name='Başlangıç Zamanı')

	def __str__(self):
		return '{} - {} - {}'.format(self.dr_of_appointment,self.patient_of_appointment,self.date_of_appointment)

	def clean(self):
		temp = Appointments.objects.filter(date_of_appointment=self.date_of_appointment)
		if temp:
			for i in temp:
				if i.begin_time_of_appointment == self.begin_time_of_appointment:
					if i.dr_of_appointment == self.dr_of_appointment or i.patient_of_appointment == self.patient_of_appointment:
						raise ValidationError({"begin_time_of_appointment":"Sistemde Kayıtlı."})
		print(self.begin_time_of_appointment)
		print(self.date_of_appointment)

	class Meta:
		verbose_name='Randevular'
		verbose_name_plural='Randevular'
