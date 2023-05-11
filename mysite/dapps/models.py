from django.db import models

# Create your models here.

class NewMember(models.Model):
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	id_number = models.IntegerField()
	AUTHORITY_TYPE = (
		('P', 'President'),
		('Vp', 'Vice_President'),
		('S', 'Secretary'),
		('Fs', 'Financial_Secretary'),
		('T', 'Treasurer'),
		('Ss', 'Social Secretary'),
		('Cw', 'Chief Whip'),
		('M', 'Member'),
	)
	authority = models.CharField(max_length=20, choices=AUTHORITY_TYPE, default='M')
	email = models.EmailField(max_length=200, blank=False)
	phone = models.IntegerField(blank=False)
	MOB = (
		('January','January'), 
		('February','February'), 
		('March','March'), 
		('April' ,'April'), 
		('May','May'), 
		('June','June'), 
		('July','July'), 
		('August','August'), 
		('September','September'), 
		('October','October'), 
		('November','November'), 
		('December','December'), 
		)
	monthofbenefit = models.CharField(max_length=20, choices=MOB)

	def __str__(self):
		return self.firstname 
	
class SavingTab(models.Model):
	name = models.ForeignKey(NewMember, on_delete=models.CASCADE)
	TRANSACTION_TYPE = (
		('Deposit', 'Deposit'),
		('Cashout', 'Cashout'),
	)
	transaction_type = models.CharField(max_length=8, choices=TRANSACTION_TYPE)
	deposit_amount = models.IntegerField()
	deposit_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.transaction_type, self.name, self.deposit_date, 
		
	   
class LoanTab(models.Model):
	names = models.ForeignKey(NewMember, on_delete=models.CASCADE)
	loanamount = models.IntegerField()
	issue_date = models.DateField(auto_now=True)
	return_date = models.DateField(auto_now=False, auto_now_add=False)
	remarks = models.TextField(max_length=500)

	def __str__(self):
		return self.names  

class MonthContrib(models.Model):
	name = models.ForeignKey(NewMember, on_delete=models.CASCADE)
	monthly_contribution  = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.name	



