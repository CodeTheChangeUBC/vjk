from django.db import models

# Create your models here.

class Sponsors(models.Model):
	name = models.CharField(max_length = 30)
	service_provided = models.CharField(max_length = 50)
	personal_contact = models.IntegerField()
	sec_contact = models.IntegerField()