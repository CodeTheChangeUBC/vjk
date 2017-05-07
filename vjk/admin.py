from django.contrib import admin

from .models import Contact, Donor, Sponsor, Student, Volunteer

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['first_name', 'last_name']}),
		('Student', {'fields': ['student']}),
		('Sponsor', {'fields': ['sponsor']}),
		('Email', 	 {'fields': ['email']})
	]
	list_display = ('first_name', 'last_name', 'student', 'sponsor')
	list_filter = ['first_name']
	search_fields = ['first_name', 'last_name', 'email']



class DonorAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['org_name']}),
		('Amount', 	{'fields': ['amount_donation']}),
	]
	list_display = ('org_name', 'amount_donation')
	list_filter = ['org_name']
	search_fields = ['org_name', 'amount_donation', 'primary_contact', 'secondary_contact']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Donor, DonorAdmin)





