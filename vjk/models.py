from django.db import models

# Create your models here.

class Student(models.Model):
	first_name = models.CharField(max_length = 75)
	last_name = models.CharField(max_length = 75)
	email = models.EmailField()
	location = models.CharField(max_length = 100)
	school = models.CharField(max_length = 75)
	year_attended = models.IntegerField()
	reference_fname = models.CharField(max_length=75,default="")
	reference_lname = models.CharField(max_length=75,default="")
	reference_email = models.EmailField(default="")