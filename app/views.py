# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    users = User.objects.all()
    form1 = ContactForm(request.POST)
    return render(request, 'app/index.html', {'users': users, 'form': form1})

def contact(request):
    users = User.objects.all()
    return render(request, 'app/contact.html', {'users': users})

def services(request):
    users = User.objects.all()
    return render(request, 'app/contact.html', {'users': users})

def api(request):
	return render(request, 'app/contact.html', {'users': users})