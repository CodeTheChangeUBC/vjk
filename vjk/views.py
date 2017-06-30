from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core import mail
from django.views import generic
from django.contrib.auth.decorators import login_required

from .models import Contact, Donor, Sponsor, Student, Volunteer, Contribution

@login_required(login_url='/admin/login/', redirect_field_name='redirect')
def index(request):
	contacts_list = Contact.objects.all()
	donors_list = Donor.objects.all()
	sponsors_list = Sponsor.objects.all()
	students_list = Student.objects.all()
	volunteers_list = Volunteer.objects.all()
	contributions_list = Contribution.objects.all()
	context = {
            "request": request,
	        "contacts_list": contacts_list,
			"donors_list": donors_list,
			"sponsors_list": sponsors_list,
			"students_list": students_list,
			"volunteers_list": volunteers_list,
			"contributions_list" : contributions_list
	    	}
	return render(request, 'vjk/index.html', context)
