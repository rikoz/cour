from django.conf.urls import url, include
from app.views import *

urlpatterns = [
	url(r'^$', index, name='homepage'),
	url(r'^help/$', contact, name='contact'),
	url(r'^oya/', include([
    	url(r'^services/$', services, name='services'),
    	url(r'^contact/$', contact, name='oya-contact')
	])),
	
]

