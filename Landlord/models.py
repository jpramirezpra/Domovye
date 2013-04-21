from django.db import models
from django.contrib.auth.models import User

class Landlord(User):


	def __unicode__(self):
		return "Lanlord: "+self.username

class Tenant(User):

	def __unicode__(self):
		return "Tenant: "+self.username

class Property(models.Model):

	
	def __unicode__(self):
			return self.title

	class Meta:
		verbose_name_plural = "stories"

class Address(models.Model):

	def __unicode__(self):
		return self.t

