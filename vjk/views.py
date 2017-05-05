from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.core import mail

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
	connection = mail.get_connection()
	connection.open()
	receiver_list = request.POST["emails"]
	sender_email = "win981026@gmail.com"
	title = request.POST["title"]
	body = request.POST["body"]
	email = mail.EmailMessage(title, body, sender_email, receiver_list, connection=connection)
	email.send()

	template = loader.get_template("email.html")
	context = {
		"length" : receiver_list.size
	}
	return HttpResponse(template.render(context,request))

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
