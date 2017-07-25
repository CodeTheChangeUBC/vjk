from django import forms
from django.forms import ModelForm
from .models import Student

class StudentForm(ModelForm):

	# Define the form with respect to Student Model
	class Meta:
		model = Student
		# Use all student fields in form
		fields = '__all__'