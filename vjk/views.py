from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from .models import Contacts
from .models import Donors
from .models import Sponsors
from .models import Students
from .models import Volunteers

# Create your views here.
def search(request):
	contacts_list = Contacts.objects.all()
	donors_list = Donors.objects.all()
	sponsors_list = Sponsors.objects.all()
	students_list = Students.objects.all()
	volunteers_list = Volunteers.objects.all()

    	template = loader.get_template("search.html")
    	context = {
	        "contacts_list": contacts_list,
			"donors_list": donors_list,
			"sponsors_list": sponsors_list,
			"students_list": students_list,
			"volunteers_list": volunteers_list
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
