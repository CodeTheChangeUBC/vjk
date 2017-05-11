from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
<<<<<<< HEAD
from django.core import mail
=======
from django.views import generic
from django.contrib.auth.decorators import login_required
>>>>>>> master

from .models import Contact, Donor, Sponsor, Student, Volunteer

@login_required(login_url='/login/', redirect_field_name='redirect')
def index(request):
    contacts = Contact.objects.all()
    donors = Donor.objects.all()
    sponsors = Sponsor.objects.all()
    students = Student.objects.all()
    volunteers = Volunteer.objects.all()
    context = Context({
        'contacts': contacts,
        'donors': donors,
        'spnsors': sponsors,
        'students': students,
        'volunteers': volunteers
        })
    return render(request, 'vjk/index.html', context)

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
