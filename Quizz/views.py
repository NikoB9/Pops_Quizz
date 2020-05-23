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

# regex
import re
# FOR JSON RESPONSE
from django.http import JsonResponse
from django.core import serializers
# JSON
import json
# OS lib
import os
# settings
from django.conf import settings
# date
import datetime


def index(request):
    allforms = getAllForms()
    return render(request, "home/index.html", {'allforms': allforms})


def openform(request, idform):
    game_name = request.POST.get('game_name', None)
    slot_max = request.POST.get('slot_max', None)
    is_public = True if request.POST.get('is_public', None) == "on" else False
    login = request.session['login']
    game = create_gameBD(idform, login, game_name, is_public, slot_max)

    user = getUserByLogin(login)

    player = Player()
    player.user = user
    player.game = game
    player.score = 0
    player.save()

    f = getFormsById(idform)
    questions = getQuestionsByForm(f)
    f.questions = getPossibleAnswersByQuestions(questions)

    return render(request, "home/forms.html", {'form': f, 'player': player})


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
    f = getFormsById(id_form)
    questions = getQuestionsByForm(f)
    f.questions = getPossibleAnswersByQuestions(questions)
    #print(f)

    return render(request, "home/create-game.html", {'form': f})


def disconnect(request):
    del request.session['login']

    data = {
        'is_valid': True
    }

    return JsonResponse(data)


def creation(request):

	if request.method == 'POST' :
		print(request.POST)
		title = request.POST.get('form_title')
		description = request.POST.get('form_description')
		author = request.session['login']

		nbQuestion = request.POST.get('nbQuestions')

		for i in range(nbQuestions):
			numq = i+1
			q_title = request.POST.get('qst_'+numq+'_title')
			q_answerType = request.POST.get('qst_'+numq+'_answerType')
			q_order = request.POST.get('qst_'+numq+'_order')

			q_nbAnswers = request.POST.get('qst_'+numq+'_nbAnswers')

			for j in range(q_nbAnswers):
				print(j)

	return render(request, "home/creation.html")


def categories(request):
    return render(request, "home/categories.html")


def resultats(request):
    return render(request, "home/resultats.html")


def saveUserAnswers(request):
	idplayer = request.POST.get('idplayer')
	player = Player.objects.get(id=idplayer)

	idPA = request.POST.get('idPA')
	valueUser = request.POST.get('value')

	print(idplayer)
	print(idPA)
	print(valueUser)

	pa = PossibleAnswer.objects.get(id=idPA)
	if pa.question.answer_type.type == "QCM" or pa.question.answer_type.type == "INPUT" :
		ua = UserAnswers.objects.filter(player=player, possible_answer=pa)
		if ua.count() >= 1 :
			ua = UserAnswers.objects.get(player=player, possible_answer=pa)			
			ua.value = valueUser
		else :
			ua = UserAnswers()
			ua.player = player
			ua.possible_answer = pa
			ua.value = valueUser

		ua.save()


	elif pa.question.answer_type.type == "UNIQUE_ANSWER":

		answers = PossibleAnswer.objects.filter(question=pa.question)

		for a in answers :
			ua = UserAnswers.objects.filter(player=player, possible_answer=a)
			if ua.count() >= 1 :
				ua = UserAnswers.objects.get(player=player, possible_answer=a)		
				ua.delete()


		ua = UserAnswers()
		ua.player = player
		ua.possible_answer = pa
		ua.value = valueUser
		ua.save()


	data = {
	'is_valid' : True
	}

	return JsonResponse(data)