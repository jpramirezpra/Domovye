from django.db import models
from django.contrib.auth.models import User
class Landlord(User):
	phonenumber = models.CharField(max_length=11)
	stripe_info = models.CharField(max_length=11)

	def __unicode__(self):
		return "Lanlord: "+self.username

class Property(models.Model):
	STATES_LIST = (
	    ('AK', 'Alaska'),
	    ('AL', 'Alabama'),
	    ('AZ', 'Arizona'),
	    ('AR', 'Arkansas'),
	    ('CA', 'California'),
	    ('CO', 'Colorado'),
	    ('CT', 'Connecticut'),
	    ('DE', 'Delaware'),
	    ('FL', 'Florida'),
	    ('GA', 'Georgia'),
	    ('HI', 'Hawaii'),
	    ('ID', 'Idaho'),
	    ('IL', 'Illinois'),
	    ('IN', 'Indiana'),
	    ('IA', 'Iowa'),
	    ('KS', 'Kansas'),
	    ('KY', 'Kentucky'),
	    ('LA', 'Louisiana'),
	    ('ME', 'Maine'),
	    ('MD', 'Maryland'),
	    ('MA', 'Massachusetts'),
	    ('MI', 'Michigan'),
	    ('MN', 'Minnesota'),
	    ('MS', 'Mississippi'),
	    ('MO', 'Missouri'),
	    ('MT', 'Montana'),
	    ('NE', 'Nebraska'),
	    ('NV', 'Nevada'),
	    ('NH', 'New Hampshire'),
	    ('NJ', 'New Jersey'),
	    ('NM', 'New Mexico'),
	    ('NY', 'New York'),
	    ('NC', 'North Carolina'),
	    ('ND', 'North Dakota'),
	    ('OH', 'Ohio'),
	    ('OK', 'Oklahoma'),
	    ('OR', 'Oregon'),
	    ('PA', 'Pennsylvania'),
	    ('RI', 'Rhode Island'),
	    ('SC', 'South Carolina'),
	    ('SD', 'South Dakota'),
	    ('TN', 'Tennessee'),
	    ('TX', 'Texas'),
	    ('UT', 'Utah'),
	    ('VT', 'Vermont'),
	    ('VA', 'Virginia'),
	    ('WA', 'Washington'),
	    ('DC', 'Washington D.C.'),
	    ('WV', 'West Virginia'),
	    ('WI', 'Wisconsin'),
	    ('WY', 'Wyoming')
	   )
	
	street = models.CharField(max_length=50)
	city = models.CharField(max_length=2, choices=STATES_LIST) 
	owner = models.ForeignKey(Landlord)

	
	def __unicode__(self):
			return self.street

	class Meta:
		verbose_name_plural = "properties"

class Tenant(User):
	phonenumber = models.CharField(max_length=11)
	stripe_info = models.CharField(max_length=11)
	tenant_property = models.ForeignKey(Property)
	bgcheck = models.BooleanField()
	credit_check  = models.BooleanField()
	applicationFee = models.DecimalField(max_digits=250, decimal_places='2')


	def __unicode__(self):
		return "Tenant: "+self.username


class Lease(models.Model):
	lease_id = models.AutoField(primary_key=True)
	BILL_CYCLE_CHOICES = (
		('D', 'Daily'),
		('W', 'Weekly'),
		('M', 'Monthly'),
		)
	landlord = models.OneToOneField(Landlord)
	tennents = models.ForeignKey(Tenant)
	prop = models.OneToOneField(Property)
	sign_date = models.DateField()
	end_date = models.DateField()
	deposit_amt = models.DecimalField(max_digits=250, decimal_places='2')
	bill_cylce = models.CharField(max_length=1,
								choices=BILL_CYCLE_CHOICES,
								default='D')
	premium = models.DecimalField(max_digits=250, decimal_places='2')
	created_at = models.DateTimeField(auto_now_add=True)
	modifified_at = models.DateTimeField(auto_now=True)
	#photo or File of Contract

	def __unicode__(self):
		return self.lease_id



