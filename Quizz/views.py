# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

#ACCES MODEL
from .forms import *

# Import requests
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *

#regex

#FOR JSON RESPONSE

#OS lib
#settings
#date

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
    # if this is a POST requests we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the requests:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            createUser(form.cleaned_data['login'], form.cleaned_data['mail'], form.cleaned_data['password'])
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, "home/createUser.html", {"form" : form})



def creation(request):
    
    return render(request, "home/creation.html")

def categories(request):
    
    return render(request, "home/categories.html")

def resultats(request):
    
    return render(request, "home/resultats.html")




