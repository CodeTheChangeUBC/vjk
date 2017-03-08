from django.db import models

# Create your models here.

class Donor(models.Model):
	org_name = models.CharField(max_length = 50)
	location = models.CharField(max_length = 100)
	year_donation = models.IntegerField()
	amount_donation = models.IntegerField()
	contact_ID1 = models.IntegerField()
	contact_ID2 = models.IntegerField()