# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#ACCES MODEL
from .models import User, Form, Question, PossibleAnswer

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

	allforms = Form.objects.all()

	return render(request, "home/forms.html", {'allforms' : allforms})

def openform(request):

	idform = request.POST.get('idform')

	f = Form.objects.get(id=idform)
	questions = Question.objects.filter(form=f).order_by('order')

	Tquestion = []
	for q in questions:
		pa = PossibleAnswer.objects.filter(question=q)
		Tquestion.append({'question':q, 'answers':pa})

	f.questions = Tquestion

	return render(request, "home/forms.html", {'form' : f})
 
def users(request):
    """return HttpResponse("<h1 style="text-align:center">Page principal</h1>")"""
    """Liste pour créer le menu"""
    users = User.objects.all()
    
    return render(request, "home/users.html", {'users': users})