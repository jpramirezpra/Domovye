from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
	return HttpResponse('This is the Index, Include the Log In and Sign Up')

def hompage(request):
	return HttpResponse('HomePage for the Landlord')

def myLogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = autheticate(username=username, password=password)
	









# def my_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#     else:
#         # Return an 'invalid login' error message.