from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from .models import Sponsors
from .models import Donor
from .models import Student
from .models import Volunteers
from .models import Contacts

# Create your views here.
def search(request):
	latest_sponsor_list = Sponsors.objects.all()
	latest_donor_list = Donor.objects.all()
    	template = loader.get_template("search.html")
    	context = {
	        'latest_sponsor_list': latest_sponsor_list,
			'latest_donor_list': latest_donor_list
	    }
	return HttpResponse(template.render(context, request))

def home(request):
	return HttpResponse("you can choose what you want to do.")

def email(request):
	return HttpResponse("send email to different people.")

def edit(request):
	return HttpResponse("edit entries in tables.")

def add(request):

	return HttpResponse("add entries in tables.")

def delete(request):
	return HttpResponse("delete entries in tables.")
