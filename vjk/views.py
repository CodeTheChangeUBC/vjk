from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from django.views import generic
from django.contrib.auth.decorators import login_required

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
	return HttpResponse("send email to different people.")

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
