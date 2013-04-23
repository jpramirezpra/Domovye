from django.db import models
from django.contrib.auth.models import User

class UserProfile(User):
	USER_ROLES = (
		('T', 'Tenant'),
		('L', 'Landlord'),
		)
	user_type = models.CharField(max_length=1, choices=USER_ROLES, default='T')
	stripe_info = models.CharField(max_length=200)
	lease_info = models.ForeignKey(Lease)

	def __unicode__(self):
		return "User Name: %s || User Type: %s" % (self.first_name, self.user_type)


class Property(models.Model):
	handle = models.CharField(max_length=15, null=False, default='My Property')
	street = models.CharField(max_length=50, null=False)
	city = models.CharField(max_length=25, null=False)
	state = models.CharField(max_length=2, null=False)
	zip_code = models.CharField(max_length=10, null=False)
	Bedrooms = models.IntegerField()
	Bathrooms = models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)
	#expenses = models.ForeignKey(Expense)
	#workorders = models.ForeignKey(WorkOrder)
	#Relationships
	owner  = models.ForeignKey(UserProfile)
	#tenants = models

	def __unicode__(self):
		return "Handle: %s"% self.handle



class Lease(models.Model):
	BILL_CYCLE_CHOICES = (
 		('D', 'Daily'),
 		('W', 'Weekly'),
 		('M', 'Monthly'),
 		)
	landlord = models.ForeignKey(UserProfile)
	prop = models.ForeignKey(Property)
	sign_date = models.DateTimeField()
	end_date = models.DateTimeField()
	bill_cylce = models.CharField(max_length=1, choices=BILL_CYCLE_CHOICES)
	premium_paid = models.DecimalField(max_digits=10, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)
	mod_at = models.DateTimeField(auto_now=True)
	active = models.BooleanField()

	def __unicode__(self):
		return "Lease For : %s"%(self.prop)



# class Property(models.Model):
# 	street = models.CharField(max_length=50)
# 	city = models.CharField(max_length=2, choices=STATES_LIST) 
# 	owner = models.ForeignKey(Landlord)

	
# 	def __unicode__(self):
# 			return self.street

# 	class Meta:
# 		verbose_name_plural = "properties"

# class Tenant(models.Model):
# 	user = models.OneToOneField(User)
# 	stripe_info = models.CharField(max_length=11)
# 	bgcheck = models.BooleanField()
# 	credit_check  = models.BooleanField()
# 	applicationFee = models.DecimalField(max_digits=250, decimal_places='2')


# 	def __unicode__(self):
# 		return "Tenant: %s " % self.user.first_name

# class Lease(models.Model):
# 	lease_id = models.AutoField(primary_key=True)
# 	BILL_CYCLE_CHOICES = (
# 		('D', 'Daily'),
# 		('W', 'Weekly'),
# 		('M', 'Monthly'),
# 		)
# 	landlord = models.OneToOneField(Landlord)
# 	tennents = models.ForeignKey(Tenant)
# 	prop = models.OneToOneField(Property)
# 	sign_date = models.DateField()
# 	end_date = models.DateField()
# 	deposit_amt = models.DecimalField(max_digits=250, decimal_places='2')
# 	bill_cylce = models.CharField(max_length=1,
# 								choices=BILL_CYCLE_CHOICES,
# 								default='D')
# 	premium = models.DecimalField(max_digits=250, decimal_places='2')
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	modifified_at = models.DateTimeField(auto_now=True)
# 	#photo or File of Contract

# 	def __unicode__(self):
# 		return self.lease_id


# class Expense(models.Model):
# 	EXPENSE_TYPE = (
# 		('Ren', 'renovation'),
# 		('Rep', 'repair'),
# 		)
# 	type_expense = models.CharField(max_length=10, choices=EXPENSE_TYPE)
# 	contractor = models.BooleanField()
# 	amount = models.DecimalField(max_digits=250, decimal_places=2)
