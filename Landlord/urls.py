from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'Landlord.views.index'),
	url(r'^landlord/$', 'Landlord.views.hompage'),
)
