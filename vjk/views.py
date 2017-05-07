from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

from .models import Contact, Donor, Sponsor, Student, Volunteer

# Create your views here.
def search(request):
	contacts_list = Contact.objects.all()
	donors_list = Donor.objects.all()
	sponsors_list = Sponsor.objects.all()
	students_list = Student.objects.all()
	volunteers_list = Volunteer.objects.all()
	template = loader.get_template("search.html")
	context = {
            "request": request,
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
    if request.POST:
        table = request.POST["table"]
        id = request.POST["id"]
        if table == "contacts":
            row = Contacts.objects.get(pk = id)
        elif table == "donors":
            row = Donors.objects.get(pk = id)
        elif table == "sponsors":
            row = Sponsors.objects.get(pk = id)
        elif table == "students":
            row = Students.objects.get(pk = id)
        elif table == "volunteers":
            row = Volunteers.objects.get(pk = id)
        row.delete()
    template = loader.get_template("delete.html")
    context = {
        "table" : table,
        "id" : id
    }
    return HttpResponse(template.render(context,request))
