from __future__ import unicode_literals
import bcrypt
import re
from django.db import models
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\+_-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z\-]*$')

# Create your models here.
class UserManager(models.Manager):
	def register(self, info):
		errors = {}
		if len(info['fname'])<2:
			errors['fname'] = "First name must be at least two characters"
		elif not NAME_REGEX.match(info['fname']):
			errors['fname'] = "First name field can only contain letters"
		if len(info['lname'])<2:
			errors['lname'] = "Last name must be at least two characters"
		elif not NAME_REGEX.match(info['lname']):
			errors['lname'] = "Last name field can only contain letters"
		if not EMAIL_REGEX.match(info['email']):
			errors['email'] = "E-mail must be a valid e-mail address"
		if len(info['password'])<8:
			errors['password'] = "Password must be a minimum of 8 characters"
		if info['password'] != info['confirmpass']:
			errors['confirmpass'] = "Confirm password entered does not match password"
		if errors:
			errors['success'] = False
			return errors
		else:
			success = {}
			password = info['password'].encode()
			hashedpw = bcrypt.hashpw(password, bcrypt.gensalt())
			User.objects.create(first_name=info['fname'], last_name=info['lname'], email=info['email'], password=hashedpw)
			success['success'] = True
			return success

	def login(self, info):
		email = info['email'].encode()
		try:
			user = User.objects.get(email=info['email'])
		except User.DoesNotExist:
			user = False
		response = {}
		if not user:
			response['success'] = False
			return response
		else:
			password = info['password'].encode()
			hashedpw = user.password.encode()
			if bcrypt.hashpw(password, hashedpw) == hashedpw:
				response['success'] = True
				response['user'] = user
				return response
			else:
				response['success'] = False
				return response



class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user_manager = UserManager()
	objects = models.Manager()
		