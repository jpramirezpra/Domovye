from django.db import models
from django.contrib.auth.models import User

class Landlord(User):
	phonenumber = 
	email =
	website = 
	stripe_info = 

	def __unicode__(self):
		return "Lanlord: "+self.username

class Tenant(User):
	phonenumber = 
	email =
	website = 
	stripe_info = 

	def __unicode__(self):
		return "Tenant: "+self.username

class Property(models.Model):
	address = 
	renters = 
	owner = 
	work_orders
	expenses
	
	def __unicode__(self):
			return self.

	class Meta:
		verbose_name_plural = "properties"

class Lease(models.Model):
	BILL_CYCLE_CHOICES = (
		('D', 'Daily'),
		('W', 'Weekly'),
		('M', 'Monthly'),
		)
	landlord = 
	tennents = 
	prop = 
	sign_date = 
	end_date = 
	deposit_amt =
	bill_cylce = models.CharField(max_length=1,
								choices=BILL_CYCLE_CHOICES,
								default='D')
	premium =
	created_at =
	modifified_at =
	#photo or File of Contract



	def __unicode__(self):




