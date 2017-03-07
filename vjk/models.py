from django.db import models

# Create your models here.
class Student(models.Model):
	first_name = models.CharField(max_length = 30)
	last_name = models.CharField(max_length = 30)
	email = models.EmailField()
	location = models.CharField(max_length = 100)
	school = models.CharField(max_length = 50)
	year_attended = models.IntegerField()