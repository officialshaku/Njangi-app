from django.urls import path
from . import views
from .views import MemberDetailView

urlpatterns = [
path('index', views.index, name="index"),
path('members', views.members, name="members"),
path('newmember', views.newmember, name="newmember"),
path('savings', views.savings, name="savings"),
path('loans', views.loans, name="loans"),
path('<int:pk>/', MemberDetailView.as_view(), name="member_detail"),
path('login', views.Login_user, name="Login_user"),
]