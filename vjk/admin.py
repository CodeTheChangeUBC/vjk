from django.contrib import admin

from .models import Contact, Donor, Sponsor, Student, Volunteer

class ContactAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['first_name', 'last_name']}),
		('Student?', {'fields': ['student']}),
		('Spondor?', {'fields': ['sponsor']}),
		('Email', 	 {'fields': ['email']})
	]
	list_display = ('first_name', 'last_name', 'student', 'sponsor')
	list_filter = ['first_name']
	search_fields = ['first_name', 'last_name', 'email']

admin.site.register(Contact, ContactAdmin)




