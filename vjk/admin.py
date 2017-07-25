from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

from .models import Contact, Donor, Sponsor, Student, Volunteer, Contribution

class DonorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['org_name']}),
		('Details', 	{'fields': ['location', 'amount_donation', 'year_donation']}),
		('Contacts', 	{'fields': ['primary_contact', 'secondary_contact']})
	]
	list_display 	= ('org_name',
					'amount_donation',
					'year_donation',
					'primary_contact',
					'secondary_contact')
	list_filter 	= ['org_name']
	search_fields 	= ['org_name',
					'amount_donation',
					'primary_contact',
					'secondary_contact']


class SponsorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['name', 'service_provided']}),
		('Contacts', 	{'fields': ['primary_contact', 'secondary_contact']}),
	]
	list_display 	= ('name', 'primary_contact', 'secondary_contact')
	list_filter 	= ['name']
	search_fields 	= ['name', 'primary_contact', 'secondary_contact']

class StudentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Personal Info', 	{'fields': ['first_name', 'last_name', 'gender', 'birth_date', 'aboriginal_group']}),
		('Contact Info', 	{'fields': ['email', 'home_phone' ,'cell_phone', 'school', 'address_line1',
								'address_line2', 'city', 'province', 'postal_code']}),
		('Guardian Info', {'fields': ['guardian_fname','guardian_lname','guardian_email','guardian_phone']}),
		('Teacher Info', {'fields': ['teacher_fname','teacher_lname','teacher_email','teacher_phone']}),
		('Program Details', {'fields': ['program_city','year_attended','program_institution','mentor',
										'room_assignment','chaperone_fname','chaperone_lname']}),
		('Reference Info',		{'fields': ['reference_fname', 'reference_lname', 'reference_email',
											'reference_address_line1','reference_address_line2', 
											'reference_city', 'reference_province','reference_postal_code']})
	]
	list_display = [f.name for f in Student._meta.get_fields()]
	# list_display 	= ('first_name','last_name','email',
	# 				'program_city', 'year_attended',
	# 				'reference_fname', 'reference_lname')
	list_filter 	= ['gender', 'aboriginal_group', 'program_city', 'year_attended', 'city']
	search_fields 	= list_display

class VolunteerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				{'fields': ['first_name', 'last_name']}),
		('Contact Info', 	{'fields': ['email', 'phone_number', 'address_line1',
								'address_line2', 'city', 'province', 'postal_code']}),
		('Details', 		{'fields': ['role', 'years_helped']})
	]
	list_display 	= ('first_name','last_name','email',
						'phone_number', 'role', 'years_helped')
	list_filter 	= ['first_name']
	search_fields 	= ['first_name','last_name','email', 'phone_number']


class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				{'fields': ['first_name', 'last_name']}),
		('Contact Info', {'fields': ['email', 'phone_number','address_line1',
							'address_line2', 'city', 'province', 'postal_code']}),
	]
	list_display  	= ('first_name', 'last_name', 'organization', 'email', 'phone_number')
	list_filter 	= ['first_name']
	search_fields 	= ['first_name', 'last_name', 'email']

class ContributionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['year', 'sponsor', 'donor', 'volunteer',
						'amount_contributed','service_provided', 'volunteer_hours']})
	]

	list_display 	= ('year', 'sponsor', 'donor', 'volunteer',
					'amount_contributed','service_provided', 'volunteer_hours')
	list_filter 	= ['year']
	search_fields 	= ['year', 'sponsor', 'donor', 'volunteer']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Contribution, ContributionAdmin)
