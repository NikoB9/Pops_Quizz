# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

#ACCES MODEL
#from .models import nomTable

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