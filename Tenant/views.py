# Create your views here.
from django.http import HttpResponse
def hompage(request):
	return HttpResponse('HomePage for the Tenant')