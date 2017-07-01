from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core import mail
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Contact, Donor, Sponsor, Student, Volunteer, Contribution

@login_required(login_url='/admin/login/', redirect_field_name='redirect')
def index(request):
	contacts	 		= Contact.objects.values();
	contact_fields 		= Contact._meta.get_fields()[5:]
	donors 				= Donor.objects.values();
	donor_fields 		= Donor._meta.get_fields()[1:]
	sponsors 			= Sponsor.objects.values();
	sponsor_fields 		= Sponsor._meta.get_fields()[1:]
	students 			= Student.objects.values()
	student_fields 		= Student._meta.get_fields()[1:]
	volunteers 			= Volunteer.objects.values()
	volunteer_fields	= Volunteer._meta.get_fields()[1:]
	contributions 		= Contribution.objects.values()
	contribution_fields = Contribution._meta.get_fields()[1:]

	context = {
            "request": request,
	        "contacts": contacts,
	        "contact_fields" : contact_fields,
			"donors": donors,
			"donor_fields": donor_fields,
			"sponsors": sponsors,
			"sponsor_fields": sponsor_fields,
			"students": students,
			"student_fields": student_fields,
			"volunteers": volunteers,
			"volunteer_fields": volunteer_fields,
			"contributions": contributions,
			"contribution_fields": contribution_fields
	 }
	return render(request, 'vjk/index.html', context)
