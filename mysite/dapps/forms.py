from django import forms
from .models import NewMember, SavingTab, LoanTab


class NewMemberForm(forms.ModelForm):
	class Meta:
		model = NewMember
		fields = '__all__'

class SavingForm(forms.ModelForm):
	class Meta:
		model = SavingTab
		fields = ['name','transaction_type', 'deposit_amount']	

class LoanForm(forms.ModelForm):
	class Meta:
		model = LoanTab
		fields = ['names','loanamount','return_date','remarks']			