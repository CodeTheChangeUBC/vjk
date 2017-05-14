from django.db import models

# Create your models here.
class Contact(models.Model):
	first_name 	= models.CharField(max_length = 75)
	last_name 	= models.CharField(max_length = 75)
	email 		= models.EmailField()
	phone 		= models.CharField(max_length = 20)


	def __str__(self):
		return self.first_name + ' ' + self.last_name

	def organization(self):
		""" 
		Return donor(s) or sponsor(s) for which contact is the contact
		"""
		result = ''
		d1,d2 = self.donor1.first(), self.donor2.first()
		s1,s2 = self.sponsor1.first(), self.sponsor2.first()

		if d1: 
			result += d1.org_name
		if d2:
			result += ' and ' + d2.org_name if d1 else d2.org_name
		if s1:
			result += ' and ' + s1.name if d1 or d2 else s1.name
		if s2: 
			result += ' and ' + s2.name if d1 or d2 or s1 else s2.name
		return result
		organization.short_description = "Contact For?"


class Donor(models.Model):
	org_name 			= models.CharField(max_length = 50)
	location 			= models.CharField(max_length = 100)
	year_donation 		= models.IntegerField(verbose_name="Year")
	amount_donation 	= models.IntegerField(verbose_name="Amount Donated")
	primary_contact 	= models.ForeignKey(Contact, 
								on_delete=models.PROTECT, 
								related_name="donor1",
								)
	secondary_contact 	= models.ForeignKey(Contact, 
								on_delete=models.PROTECT, 
								related_name="donor2")
	

	def __str__(self):
		return self.org_name 

class Sponsor(models.Model):
	name 				= models.CharField(max_length = 50)
	service_provided 	= models.CharField(max_length = 50)
	primary_contact 	= models.ForeignKey(Contact, 
								on_delete=models.PROTECT, 
								related_name="sponsor1", 
								default=-1)
	secondary_contact 	= models.ForeignKey(Contact, 
								on_delete=models.PROTECT, 
								related_name="sponsor2", 
								default=-1)

	def __str__(self):
		return self.name


class Student(models.Model):
	first_name 			= models.CharField(max_length = 75)
	last_name 			= models.CharField(max_length = 75)
	email 				= models.EmailField()
	location 			= models.CharField(max_length = 100)
	school 				= models.CharField(max_length = 75)
	year_attended 		= models.IntegerField()
	reference_fname 	= models.CharField(max_length=75,default="", 
										verbose_name="Reference First Name")
	reference_lname 	= models.CharField(max_length=75,default="", 
										verbose_name="Reference Last Name")
	reference_email 	= models.EmailField(default="")

	def __str__(self):
		return self.first_name + ' ' + self.last_name


class Volunteer(models.Model):
	first_name 			= models.CharField(max_length = 75)
	last_name 			= models.CharField(max_length = 75)
	email 				= models.EmailField()
	phone 				= models.CharField(max_length  = 20)
	role 				= models.CharField(max_length = 75)
	years_helped 		= models.CharField(max_length=75,default="") 

	def __str__(self):
		return self.first_name + ' ' + self.last_name

