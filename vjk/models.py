from django.db import models

# Create your models here.
class Contacts(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	phone = models.CharField(max_length  = 20)
	donor = models.BooleanField()
	sponsor = models.BooleanField()
	student = models.BooleanField()
	volunteer = models.BooleanField()

class Donors(models.Model):
	org_name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	year_donation = models.IntegerField()
	amount_donation = models.IntegerField()
	primary_contact = models.ForeignKey('Contacts', on_delete=models.PROTECT, related_name="+", default=-1)
	secondary_contact = models.ForeignKey('Contacts', on_delete=models.PROTECT, related_name="+", default=-1)

class Sponsors(models.Model):
<<<<<<< HEAD
	name = models.CharField(max_length = 30)
=======
	name = models.CharField(max_length = 50)
>>>>>>> master
	service_provided = models.CharField(max_length = 50)
	primary_contact = models.ForeignKey('Contacts', on_delete=models.PROTECT, related_name="+", default=-1)
	secondary_contact = models.ForeignKey('Contacts', on_delete=models.PROTECT, related_name="+", default=-1)

class Students(models.Model):
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
<<<<<<< HEAD
	years_helped = models.CharField(max_length=75,default="")
=======
	years_helped = models.CharField(max_length=75,default="") 
>>>>>>> master
