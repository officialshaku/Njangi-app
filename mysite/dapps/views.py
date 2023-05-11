from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import NewMemberForm, SavingForm, LoanForm
from .models import NewMember, SavingTab, LoanTab
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(response):
	return render(response, "dapps/base.html", {})

class MemberDetailView(DetailView):
	model = NewMember

	def get_object(self, queryset = None):
		obj = super().get_object(queryset=queryset)
		obj.loans = LoanTab.objects.filter(names=obj)
		obj.savings = SavingTab.objects.filter(name=obj)

		return obj
	

def members(response):
	return render(response, "dapps/home.html", {
		'member_list': NewMember.objects.all()
	})

def newmember(response):
	form = NewMemberForm()
	if response.method == "POST":
		form = NewMemberForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect(members)
		else:
			print(form.errors)
	else:
		form = NewMemberForm()
	return render(response, "dapps/newmember.html", {'form':form})
		
		



def savings(response):
	form = SavingForm()
	if response.method == "POST":
		form = SavingForm(response.POST)
		if form.is_valid():
			form.save()
			
		return redirect(members)
	else:
		form = SavingForm()
	return render(response, 'dapps/savings.html', {'form': form})

def loans(response):
	form = LoanForm()
	
	if response.method == "POST":
		form = LoanForm(response.POST)
		if form.is_valid():
			 form.save()
				
		return redirect(members)
	else:
		form = LoanForm()		
	return render(response, "dapps/loans.html", {'form':form})	


def Login_user(response):
	if response.method == 'POST':
  
		# AuthenticationForm_can_also_be_used__
  
		username = response.POST['username']
		password = response.POST['password']
		user = authenticate(response, username = username, password = password)
		if user is not None:
			login(response, user)
			messages.success(response, f' welcome {username} !!')
			return render(response, 'dapps/home.html')
		else:
			messages.info(response, f'account done not exit plz sign in')
			return redirect(members)

	else:
		return render(response, 'dapps/login.html', {})

