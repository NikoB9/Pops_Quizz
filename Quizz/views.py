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
    allforms = getAllForms()
    return render(request, "home/index.html", {'allforms' : allforms})

def openform(request, idform):

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
    
	login = request.POST.get('loginco', None)
	email = request.POST.get('emailco', None)
	password = request.POST.get('passwordco', None)
	password_validation = request.POST.get('passwordco2', None)

	if loginExist(login) :

		data = {
    	'is_valid':  False,
    	'error_message': "Le pseudo existe déjà."   
    	}

	elif emailExist(email) :

		data = {
    	'is_valid':  False,
    	'error_message': "L'email existe déjà."   
    	}

	elif password != password_validation :

		data = {
    	'is_valid':  False,
    	'error_message': "Le mot de passe de confirmation est différent."   
    	}

	else :
        
		createUserBD(login, email, password)
        
		data = {
    	'is_valid':  True,
    	}

	return JsonResponse(data)

def connectUser(request):
    
	login = request.POST.get('login', None)
	password = request.POST.get('password', None)

	if loginExist(login) :

		if valideUser(login, password):
    		
			data = {
		    	'is_valid':  True,
		    	}

			request.session['login'] = login

		else :

			data = {
	    	'is_valid':  False,
	    	'error_message': "Le mot de passe est incorrect."   
	    	}

	else :

		data = {
    	'is_valid':  False,
    	'error_message': "Le pseudo n'existe pas."   
    	}


	return JsonResponse(data)



def creation(request):
    
    return render(request, "home/creation.html")

def categories(request):
    
    return render(request, "home/categories.html")

def resultats(request):
    
    return render(request, "home/resultats.html")




