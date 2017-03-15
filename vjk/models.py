from django.db import models

# Create your models here.

class Sponsors(models.Model):
	name = models.CharField(max_length = 30)
	service_provided = models.CharField(max_length = 50)
	personal_contact = models.IntegerField()
	sec_contact = models.IntegerField()

class Donor(models.Model):
	org_name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	year_donation = models.IntegerField()
	amount_donation = models.IntegerField()
	contact_ID1 = models.IntegerField()
	contact_ID2 = models.IntegerField()

class Student(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	location = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	year_attended = models.IntegerField()
	reference_fname = models.CharField(max_length=75,default="")
	reference_lname = models.CharField(max_length=75,default="")
	reference_email = models.EmailField(default="")

class Volunteers(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	phone = models.CharField(max_length  = 20)
	role = models.CharField(max_length = 75)
	years_helped = models.IntegerField()

class Contacts(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	phone = models.CharField(max_length  = 20)
	donor = models.BooleanField()
	sponsor = models.BooleanField()
	student = models.BooleanField()
	volunteer = models.BooleanField()
