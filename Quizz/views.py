# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
from django.http import HttpResponse

#ACCES MODEL
from .models import *
from .forms import *

# Import request
from .request_user import *
from .request_form import *
from .request_question import *

#regex
import re

#FOR JSON RESPONSE
from django.http import JsonResponse
from django.core import serializers
import json

#OS lib
import os
#settings
from django.conf import settings
#date
import datetime

def index(request):
    """return HttpResponse("<h1 style="text-align:center">Page principal</h1>")"""
    """Liste pour créer le menu"""
    functionalities = [
    {'name':'Création de quizz','desc':''},
    {'name':'Jouer','desc':''},
    {'name':'Historique','desc':''},
    {'name':'Amis','desc':''},
    ]
    return render(request, "home/index.html", {'functionalities': functionalities})

def getforms(request):

	allforms = getAllForms()

	return render(request, "home/forms.html", {'allforms' : allforms})

def openform(request):

	idform = request.POST.get('idform')
	f = getFormsById(idform)
	questions = getQuestionsByForm(f)
	f.questions = getPossibleAnswersByQuestions(questions)
	print(f)

	return render(request, "home/forms.html", {'form' : f})

def users(request):
    """return HttpResponse("<h1 style="text-align:center">Page principal</h1>")"""
    """Liste pour créer le menu"""
    users = getAllUsers()

    return render(request, "home/users.html", {'users': users})

def createUser(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            createUser(form.cleaned_data['login'], form.cleaned_data['mail'], form.cleaned_data['password'])
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, "home/createUser.html", {"form" : form})
