# Create your views here.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

# ACCES MODEL
from .forms import *

# Import requests
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *
from Quizz.requests.request_question import *
from Quizz.requests.request_game import *

#regex
import re
#FOR JSON RESPONSE
from django.http import JsonResponse
from django.core import serializers
#JSON
import json
#OS lib
import os
#settings
from django.conf import settings
#date
import datetime

def index(request):
    allforms = getAllForms()
    return render(request, "home/index.html", {'allforms': allforms})


def openform(request, idform):
    game_name = request.POST.get('game_name', None)
    slot_max = request.POST.get('slot_max', None)
    is_public = request.POST.get('is_public', None)
    login = request.session['login']

    game = create_game(idform, login, game_name, is_public, slot_max)

    user = getUserByLogin(login)

    player = Player()
    player.user = user
    player.game = game
    player.score = 0
    player.save()

    f = getFormsById(idform)
    questions = getQuestionsByForm(f)
    f.questions = getPossibleAnswersByQuestions(questions)

    return render(request, "home/forms.html", {'form': f})


def users(request):
    users = getAllUsers()

    return render(request, "home/users.html", {'users': users})


def create_user(request):
    login = request.POST.get('loginco', None)
    email = request.POST.get('emailco', None)
    password = request.POST.get('passwordco', None)
    password_validation = request.POST.get('passwordco2', None)

    if loginExist(login):

        data = {
            'is_valid': False,
            'error_message': "Le pseudo existe déjà."
        }

    elif emailExist(email):

        data = {
            'is_valid': False,
            'error_message': "L'email existe déjà."
        }

    elif password != password_validation:

        data = {
            'is_valid': False,
            'error_message': "Le mot de passe de confirmation est différent."
        }

    else:

        createUserBD(login, email, password)

        data = {
            'is_valid': True,
        }

    return JsonResponse(data)


def connectUser(request):
    login = request.POST.get('login', None)
    password = request.POST.get('password', None)

    if loginExist(login):

        if valideUser(login, password):

            data = {
                'is_valid': True,
            }

            request.session['login'] = login

        else:

            data = {
                'is_valid': False,
                'error_message': "Le mot de passe est incorrect."
            }

    else:

        data = {
            'is_valid': False,
            'error_message': "Le pseudo n'existe pas."
        }

    return JsonResponse(data)

def create_game(request, id_form):

def disconnect(request) :

	del request.session['login']

	data = {
        'is_valid': True
    }

	return JsonResponse(data)

    return render(request, "home/create-game.html", {'form': f})

def creation(request):
    return render(request, "home/creation.html")


def categories(request):
    return render(request, "home/categories.html")


def resultats(request):
    return render(request, "home/resultats.html")
