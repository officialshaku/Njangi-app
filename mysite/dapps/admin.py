from django.contrib import admin
from .models import NewMember, LoanTab, SavingTab

# Register your models here.


admin.site.register(NewMember)
admin.site.register(LoanTab)
admin.site.register(SavingTab)
