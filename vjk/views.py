from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Context
from django.core import mail
from django.views import generic
from django.contrib.auth.decorators import login_required
from .models import Contact, Donor, Sponsor, Student, Volunteer, Contribution
from .forms import StudentForm
from django.contrib import messages

@login_required(login_url='/admin/login/', redirect_field_name='redirect')
def index(request):
    contacts            = Contact.objects.all()
    contact_fields      = Contact._meta.get_fields()[5:]
    donors              = Donor.objects.all()
    donor_fields        = Donor._meta.get_fields()[2:]
    sponsors            = Sponsor.objects.all()
    sponsor_fields      = Sponsor._meta.get_fields()[2:]
    students            = Student.objects.all()
    student_fields      = Student._meta.get_fields()[1:]
    volunteers          = Volunteer.objects.all()
    volunteer_fields    = Volunteer._meta.get_fields()[2:]
    contributions       = Contribution.objects.all()
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
    return render(request, 'vjk/index_features.html', context)


def student_form(request):
    if request.method == 'POST':
        # create form instance and populate with data from request
        form = StudentForm(request.POST)
        if form.is_valid():
            # If valid form, create student model from data
            form.save() 
            return redirect('/')
            messages.success(request, 'Student Created!')
            
        else:
            messages.warning(request, 'Whoops, something went wrong.')

    else:
        form = StudentForm()

    return render(request, 'vjk/studentform.html', {'form': form})
