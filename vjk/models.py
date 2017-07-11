from django.db import models
from django.core.validators import RegexValidator

province_choices = {
	('AB','Alberta'),
	('BC','British Columbia'),
	('SK','Saskatchewan'),
	('MB','Manitoba'),
	('ON','Ontario'),
	('QC','Quebec'),
	('PE','Prince Edward Island'),
	('NS','Nova Scotia'),
	('NL','Newfoundland and Labrador'),
	('NB','New Brunswick'),
	('NT','Northwest Territories'),
	('NU','Nunavut'),
	('YT','Yukon')
}

phone_regex = RegexValidator(regex=r'^\+?1?\d{10,12}$',
				message="Phone number must be entered in the format: '+16045555555'.")



# Create your models here.
class Contact(models.Model):
	first_name 		= models.CharField(max_length = 75, verbose_name="First Name")
	last_name 		= models.CharField(max_length = 75, verbose_name="Last Name")
	email 			= models.EmailField(verbose_name="E-mail")
	phone_number 	= models.CharField(validators=[phone_regex],max_length = 12, blank=True, null=True, verbose_name="Phone")

	address_line1 	= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address - Line 1")
	address_line2 	= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address - Line 2")
	city 			= models.CharField(max_length = 30, blank=True, null=True, verbose_name="City")
	province 		= models.CharField(max_length = 20, choices = province_choices, blank=True, null=True, verbose_name="Province")
	postal_code 	= models.CharField(max_length=6, blank=True, null=True, verbose_name="Postal Code")

	# Return name as identifier
	def __str__(self):
		return self.first_name + ' ' + self.last_name

	# Iterate over fields values. 
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				yield field.value_to_string(self)

	# Enforce that first name, last name and email form unique combination
	class meta:
		unique_together = (('first_name', 'last_name', 'email'),)
	
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
	org_name 			= models.CharField(max_length = 50, verbose_name="Organization Name")
	location 			= models.CharField(max_length = 100, blank=True, null=True, verbose_name="Location")
	year_donation 		= models.IntegerField(verbose_name="Year", blank=True, null=True)
	amount_donation 	= models.IntegerField(verbose_name="Amount Donated", blank=True, null=True)
	primary_contact 	= models.ForeignKey(Contact,
								on_delete=models.PROTECT,
								related_name="donor1",
								blank=True, null=True,
								verbose_name="Primary Contact")
	secondary_contact 	= models.ForeignKey(Contact,
								on_delete=models.PROTECT,
								related_name="donor2",
								blank=True, null=True,
								verbose_name="Secondary Contact")

	# Return name as identifier
	def __str__(self):
		return self.org_name

	# Iterate over fields values. If foreign key, produce name instead of id
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				val = field.value_to_string(self)
				if (val != 'None' 
					and (field.name == 'primary_contact' 
						or field.name == 'secondary_contact')):
					yield Contact.objects.get(pk=int(val))
				else:
					yield val

	# Organisation name is unique
	class meta:
		unique_together = (('org_name'),)


class Sponsor(models.Model):
	name 				= models.CharField(max_length = 50, verbose_name="Name")
	service_provided 	= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Service Provided")
	primary_contact 	= models.ForeignKey(Contact,
								on_delete=models.PROTECT,
								related_name="sponsor1",
								default=-1,
								blank=True, null=True,
								verbose_name="Primary Contact")
	secondary_contact 	= models.ForeignKey(Contact,
								on_delete=models.PROTECT,
								related_name="sponsor2",
								default=-1,
								blank=True, null=True,
								verbose_name="Secondary Contact")

	# Return name as identifier
	def __str__(self):
		return self.name

	# Iterate over fields values. If foreign key, produce name instead of id
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				val = field.value_to_string(self)
				if (val != 'None' 
					and (field.name == 'primary_contact' 
						or field.name == 'secondary_contact')):
					yield Contact.objects.get(pk=int(val))
				else:
					yield val

	# Name of sponsor is unique
	class meta:
		unique_together = (('name'),)



class Student(models.Model):
	first_name 			= models.CharField(max_length = 75, verbose_name="First Name")
	last_name 			= models.CharField(max_length = 75, verbose_name="Last Name")
	gender 				= models.CharField(max_length = 10, 
											choices = {
														('M','Male'),
														('F','Female'),
														('O','Other')
													}, 
											verbose_name="Gender", null = True, blank = True)
	
	bday_regex 			= RegexValidator(regex=r'^\d{2}/\d{2}/\d{4}', 
								message='Birth date must be entered in form MM/DD/YYYY')
	birth_date 			= models.CharField(max_length = 10, validators=[bday_regex], blank = True, null = True, verbose_name='Birth Date')
	
	aboriginal_group 	= models.CharField(max_length = 20, 
											choices = 	{
											('First Nations','First Nations'),
											('Metis','Metis'),
											('Inuit','Inuit')
											},
											blank = True, null = True, 
											verbose_name='Aboriginal Group')

	email 				= models.EmailField(verbose_name="E-mail")
	school 				= models.CharField(max_length = 75, blank=True, null=True, verbose_name="School")
	home_phone 			= models.CharField(max_length = 12, validators = [phone_regex], blank=True, null=True, verbose_name="Home Phone")
	cell_phone	 		= models.CharField(max_length = 12, validators = [phone_regex], blank=True, null=True, verbose_name="Cell Phone")

	guardian_fname		= models.CharField(max_length = 75, verbose_name="Guard. First Name", blank = True, null = True)
	guardian_lname		= models.CharField(max_length = 75, verbose_name="Guard. Last Name", blank = True, null = True)
	guardian_phone		= models.CharField(max_length = 12, validators = [phone_regex], blank=True, null=True, verbose_name="Guard. Phone")
	guardian_email		= models.EmailField(default="",verbose_name="Guard. Email",blank=True,null=True)

	teacher_fname		= models.CharField(max_length = 75, verbose_name="Teach. First Name", blank = True, null = True)
	teacher_lname		= models.CharField(max_length = 75, verbose_name="Teach. Last Name", blank = True, null = True)
	teacher_email		= models.EmailField(default="",verbose_name="Teach. Email",blank=True,null=True)
	teacher_phone		= models.CharField(max_length = 12, validators = [phone_regex], blank=True, null=True, verbose_name="Teach. Phone")
	
	program_city 		= models.CharField(max_length = 100, blank=True, null=True, verbose_name="Program City")
	year_attended 		= models.IntegerField(blank=True,null=True, verbose_name="Year Attended")
	program_institution = models.CharField(max_length = 75, blank=True, null=True, verbose_name="Institution")
	mentor				= models.CharField(max_length = 75, blank=True, null=True, verbose_name="Mentor")
	room_assignment		= models.CharField(max_length = 75, blank=True, null=True, verbose_name="Room Assign.")
	chaperone_fname		= models.CharField(max_length = 75, blank=True, null=True, verbose_name="Chaperone First Name")
	chaperone_lname		= models.CharField(max_length = 75, blank=True, null=True, verbose_name="Chaperone Last Name")

	address_line1 		= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address - Line 1")
	address_line2 		= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address - Line 2")
	city 				= models.CharField(max_length = 30, blank=True, null=True, verbose_name="City")
	province 			= models.CharField(max_length = 20, choices = province_choices, blank=True, null=True, verbose_name="Province")
	postal_code 		= models.CharField(max_length=6, blank=True, null=True, verbose_name="Postal Code")

	reference_fname 	= models.CharField(max_length=75,default="",
										verbose_name="Ref. First Name")
	reference_lname 	= models.CharField(max_length=75,default="",
										verbose_name="Ref. Last Name")
	reference_email 	= models.EmailField(default="", verbose_name='Ref. E-mail')
	reference_number 	= models.CharField(max_length = 12, validators = [phone_regex], blank=True, null=True, verbose_name="Ref. Number")

	reference_address_line1 = models.CharField(max_length = 50, blank=True, null=True, verbose_name="Ref. Addr - Line 1")
	reference_address_line2 = models.CharField(max_length = 50, blank=True, null=True, verbose_name="Ref. Addr - Line 2")
	reference_city 			= models.CharField(max_length = 30, blank=True, null=True, verbose_name="Ref. City")
	reference_province 		= models.CharField(max_length = 20, choices = province_choices, blank=True, null=True, verbose_name="Ref. Province")
	reference_postal_code 	= models.CharField(max_length=6, blank=True, null=True, verbose_name="Ref. Postal Code")

	# Return name as identifier
	def __str__(self):
		return self.first_name + ' ' + self.last_name

	# Iterate over field values
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				yield field.value_to_string(self)

	# Enforce that first name, last name and email form unique combination
	class meta:
		unique_together = (('first_name', 'last_name', 'email'),)

class Volunteer(models.Model):

	first_name 			= models.CharField(max_length = 75, verbose_name="First Name")
	last_name 			= models.CharField(max_length = 75, verbose_name="Last Name")
	email 				= models.EmailField(verbose_name="E-mail")
	phone_number 		= models.CharField(validators=[phone_regex],max_length = 12, blank=True, null=True, verbose_name="Number")

	address_line1 		= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address Line - 1")
	address_line2 		= models.CharField(max_length = 50, blank=True, null=True, verbose_name="Address Line - 2")
	city 				= models.CharField(max_length = 30, blank=True, null=True, verbose_name="City")
	province 			= models.CharField(max_length = 20, choices = province_choices, blank=True, null=True, verbose_name="Province")
	postal_code 		= models.CharField(max_length=6, blank=True, null=True, verbose_name="Postal Code")

	role 				= models.CharField(max_length = 75, blank=True, null=True, verbose_name="Role")
	years_helped 		= models.CharField(max_length=75,default="", blank=True, null=True, verbose_name="Years Helped")

	# Return name as identifier
	def __str__(self):
		return self.first_name + ' ' + self.last_name

	# Iterate over field values
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				yield field.value_to_string(self)

	# Enforce that first name, last name and email form unique combination
	class meta:
		unique_together = (('first_name', 'last_name', 'email'),)


class Contribution(models.Model):
	year				= models.IntegerField(blank=True, null=True, verbose_name="Year")
	sponsor				= models.ForeignKey(Sponsor, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Sponsor")
	donor				= models.ForeignKey(Donor, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Donor")
	volunteer			= models.ForeignKey(Volunteer, on_delete=models.PROTECT, blank=True, null=True, verbose_name="Volunteer")
	amount_contributed	= models.IntegerField(blank=True, null=True, verbose_name="Amount Contributed")
	service_provided	= models.TextField(blank=True, null=True, verbose_name="Service Provided")
	volunteer_hours		= models.IntegerField(blank=True, null=True, verbose_name="Volunteer Hours")

	# Iterate over fields values. If foreign key, produce name instead of id
	def __iter__(self):
		for field in self._meta.fields:
			if field.name != "id":
				val = field.value_to_string(self)
				if (field.name == 'sponsor' and val!='None'):
					yield Sponsor.objects.get(pk=int(val))
				elif (field.name == 'donor' and val!='None'):
					yield Donor.objects.get(pk=int(val))
				elif (field.name == 'volunteer' and val!='None'):
					yield Volunteer.objects.get(pk=int(val))
				else: 
					yield val
