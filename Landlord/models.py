from django.db import models
from django.contrib.auth.models import User

class Landlord(User):

	__unicode__(self):
		return "Lanlord: "+self.username

class Tenant(User):

	__unicode__(self):
		return "Tenant: "+self.username

class Property(models.Model):
	
	 __unicode__(self):
			return self.titile

	class Meta:
		verbose_name_plural = "stories"

