from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

import datetime

GENDERS=(
    ('Man','Erkek'),
	('Woman','Kadın')
)

BLOOD_GROUPS=(
    ('0 Rh-','0 Rh-'),
	('0 Rh+','0 Rh+'),
	('A Rh-','A Rh-'),
	('A Rh+','A Rh+'),
	('B Rh-','B Rh-'),
	('B Rh+','B Rh+'),
	('AB Rh-','AB Rh-'),
	('AB Rh+','AB Rh+'),
)

class City(models.Model):
	name = models.CharField(max_length = 75, unique = True)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		verbose_name = 'City'
		verbose_name_plural='Cities'

class County(models.Model):
	name = models.CharField(max_length = 75)
	city = models.ForeignKey(
        City,
        on_delete = models.CASCADE,
        related_name = "counties"
    )

	def __str__(self):
		return '{}'.format(self.name)

	def clean(self):
		if County.objects.filter(name=self.name, city = self.city).count() > 0:
			raise ValidationError({
                "name": "County Already Exists"
            })

	class Meta:
		verbose_name='County'
		verbose_name_plural='Counties'

class Hospital(models.Model):
	county = models.ForeignKey(
        County,
        on_delete = models.CASCADE,
        related_name = "hospitals"
    )
	name = models.CharField(
        max_length=75,
    )
	start_time = models.TimeField()
	end_time = models.TimeField()
	phone_number = models.CharField(max_length = 20)
	address = models.CharField(max_length = 200)
	
	def __str__(self):
		return '{}'.format(self.name)

	def clean(self):
		if Hospital.objects.filter(name = self.name, county = self.county).count() > 0:
			raise ValidationError({
				"name":"Hospital Already Exists"
			})

	class Meta:
		verbose_name='Hospital'
		verbose_name_plural='Hospitals'

class Polyclinic(models.Model):
	hospital = models.ForeignKey(
        Hospital,
        on_delete=models.CASCADE,
        related_name = "polyclinics"
    )
	name = models.CharField(max_length=50)

	def __str__(self):
		return '{}'.format(self.name)

	def clean(self):
		if Polyclinic.objects.filter(name=self.name,hospital = self.hospital):
			raise ValidationError({
				"name":"Polyclinic Already Exists"
			})

	class Meta:
		verbose_name='Polyclinic'
		verbose_name_plural='Polyclinics'

class Doctor(models.Model):
	polyclinic = models.ForeignKey(
		Polyclinic,
		on_delete = models.CASCADE,
		related_name = "doctors"
	)
	identification_number = models.CharField(
		max_length = 11,
		primary_key = True,
	)
	first_name = models.CharField(max_length = 25)
	last_name = models.CharField(max_length = 25)
	phone_number = models.CharField(max_length = 20, unique = True)
	expertise = models.CharField(max_length = 25)
	birth_place = models.CharField(
		max_length = 15,
		blank = True,
		null = True
	)
	birth_date = models.DateField(
		blank = True,
		null = True
	)
	gender = models.CharField(
		max_length=5,
		choices = GENDERS,
		blank = True,
		null = True
	)
	
	def __str__(self):
		return 'Uzmanlık Alanı: {} - {} {} - Cinsiyet: {}'.format(self.expertise, self.first_name, self.last_name, self.gender)

	def clean(self):
		if Doctor.objects.filter(phone_number = self.phone_number).count() > 0:
			raise ValidationError({
				"phone_number":"Already Exists"
			})

	class Meta:
		verbose_name='Doctor'
		verbose_name_plural='Doctors'

class Patient(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE
	)
	identification_number = models.CharField(
		max_length = 11,
		primary_key = True
	)
	blood_group = models.CharField(
		max_length = 7,
		choices = BLOOD_GROUPS,
		blank = True,
		null = True
	)
	mother_name=models.CharField(
		max_length=15,
		blank = True,
		null = True
	)
	father_name=models.CharField(
		max_length=15,
		blank = True,
		null = True
	)
	phone_number = models.CharField(
		max_length=20,
		unique = True
	)
	birth_place = models.ForeignKey(
		City,
		on_delete = models.CASCADE,
		blank = True,
		null = True,
	)
	birth_date = models.DateField(
		blank = True,
		null = True
	)
	gender = models.CharField(
		max_length=5,
		choices = GENDERS,
		blank = True,
		null = True
	)

	def first_name(self):
		return self.user.first_name

	def last_name(self):
		return self.user.last_name

	def email(self):
		return self.user.email

	def __str__(self):
		return '{}'.format(self.identification_number)

	class Meta:
		verbose_name = 'Patient'
		verbose_name_plural = 'Patients'

class Appointment(models.Model):
	doctor = models.ForeignKey(
		Doctor,
		on_delete = models.CASCADE,
		related_name = "appointments"
	)
	patient = models.ForeignKey(
		Patient,
		on_delete = models.CASCADE,
		related_name = "appointments"
	)
	date = models.DateTimeField()

	def __str__(self):
		return '{} - {} - {}'.format(self.doctor.first_name, self.patient.user.first_name, self.date)

	def clean(self):
		temp = Appointment.objects.filter(date=self.date)
		if temp:
			for i in temp:
				if i.begin_time_of_appointment == self.begin_time_of_appointment:
					if i.dr_of_appointment == self.dr_of_appointment or i.patient_of_appointment == self.patient_of_appointment:
						raise ValidationError({
							"date":"Already Exists"
						})

	class Meta:
		verbose_name='Appointment'
		verbose_name_plural='Appointments'
