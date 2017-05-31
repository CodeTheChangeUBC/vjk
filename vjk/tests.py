from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse
from django.apps import apps
from django.http import HttpResponse

password = 'password'
models = apps.get_app_config('vjk').get_models()

class SecurityTests(TestCase):
	"""
	Tests to ensure two-level authentication structure of app
	"""

	def setUp(self):
		User.objects.create_superuser('admin', 'admin@vjk.com', password)
		User.objects.create_user('user', 'staff@vjk.com', password)


	def test_admin_sign_in(self):
		"""
		Admin should access admin panel
		"""
		c = Client()
		response = c.post('/admin/login/', {'username':'admin', 'password':password}, follow=True)
		for model in models:
			model_name = model._meta.db_table.split('vjk_')[1] + 's'
			model_name = model_name.capitalize()
			if model_name != 'Students':
				self.assertContains(response, model_name)

	
	def test_regular_user_sign_in(self):
		"""
		Regular users should not be able to sign via admin portal (they should not exist
		in this appplication whatsoever)
		"""
		c = Client()
		response = c.post('/admin/login/', {'username':'user', 'password':password}, follow=True)
		self.assertContains(response, 'Please enter the correct username and password')




