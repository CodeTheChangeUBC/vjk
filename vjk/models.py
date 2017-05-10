from django.db import models

# Create your models here.
class ContactInfo(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	phone = models.CharField(max_length  = 20)
	donor = models.BooleanField()
	sponsor = models.BooleanField()
	student = models.BooleanField()
	volunteer = models.BooleanField()

	class Meta:
		abstract = True

	def type(self):
		if self.donor   	: return 'Donor'
		if self.sponsor 	: return 'Sponsor'
		if self.student 	: return 'Student'
		if self.volunteer 	: return 'volunteer'
		return 'None'

	def __str__(self):
		return self.first_name

class Donor(ContactInfo):
	org_name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	year_donation = models.IntegerField()
	amount_donation = models.IntegerField(verbose_name="Amount Donated")

class Sponsor(ContactInfo):
	name = models.CharField(max_length = 50)
	service_provided = models.CharField(max_length = 50)

class Student(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	location = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	year_attended = models.IntegerField()
	reference_fname = models.CharField(max_length=75,default="", 
										verbose_name="Reference First Name")
	reference_lname = models.CharField(max_length=75,default="", 
										verbose_name="Reference Last Name")
	reference_email = models.EmailField(default="")

class Volunteer(ContactInfo):
	role = models.CharField(max_length = 75)
	years_helped = models.CharField(max_length=75,default="") 
