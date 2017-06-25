from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)

from .models import Contact, Donor, Sponsor, Student, Volunteer

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
		(None, 			{'fields': ['first_name', 'last_name']}),
		('Details', 	{'fields': ['email', 'location', 'year_attended', 'school']}),
		('References',	{'fields': ['reference_fname', 'reference_lname', 'reference_email']})
	]
	list_display 	= ('first_name','last_name','email',
					'location', 'school', 'year_attended',
					'reference_fname', 'reference_lname')
	list_filter 	= ['first_name']
	search_fields 	= ['first_name','last_name','email',
					'location', 'year_attended',
					'reference_fname', 'reference_lname']

class VolunteerAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 			{'fields': ['first_name', 'last_name']}),
		('Details', 	{'fields': ['email', 'phone', 'role', 'years_helped']}),
	]
	list_display 	= ('first_name','last_name','email',
						'phone', 'role', 'years_helped')
	list_filter 	= ['first_name']
	search_fields 	= ['first_name','last_name','email', 'phone']


class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 				{'fields': ['first_name', 'last_name']}),
		('Contact Details', {'fields': ['email', 'phone']}),
	]
	list_display  	= ('first_name', 'last_name', 'organization', 'email', 'phone')
	list_filter 	= ['first_name']
	search_fields 	= ['first_name', 'last_name', 'email']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Donor, DonorAdmin)
admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Volunteer, VolunteerAdmin)






