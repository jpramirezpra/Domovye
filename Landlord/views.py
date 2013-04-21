from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def hompage(request):
	return HttpResponse('HomePage for the Landlord')
