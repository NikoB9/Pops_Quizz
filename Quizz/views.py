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
from Quizz.requests.request_possible_answer import *
from Quizz.requests.request_answer_type import *
from Quizz.requests.request_player import *
from Quizz.requests.request_categories import *

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
    user = None
    if 'login' in request.session:
        user = getUserByLogin(request.session['login'])
    allforms = getAllForms(user)

    return render(request, "home/index.html", {'allforms': allforms})

def quizz_by_cat(request, cat_id):
    cat = get_category_by_id(cat_id)
    allforms = getQuizzByCat(cat)

    return render(request, "home/quizz_by_cat.html", {'allforms': allforms, 'cat': cat})

def create_game(request, id_form):
    f = getFormById(id_form)
    questions = getQuestionsByForm(f)
    f.questions = getPossibleAnswersByQuestions(questions)
    user = getUserByLogin(request.session['login'])
    game = create_gameBD(f.id, user.login, "Partie de "+user.login, False, 1, False, "EDITING")
    create_player(game, user)

    return render(request, "home/create-game.html", {'form': f, 'game':game})


def attente(request, game_uuid):
    user = getUserByLogin(request.session['login'])
    game_name = request.POST.get('game_name', None)
    slot_max = request.POST.get('slot_max', None)
    is_public = True if request.POST.get('is_public', None) == "on" else False
    game = get_game_by_uuid(game_uuid)
    if game.game_status.type=="WAITING":
        game = edit_game(game_uuid, game_name, slot_max, is_public, False, "IN_PROGRESS")

    friends = get_users_friends(user)
    players = get_players_number_of_game(get_players_by_game(game))
    is_author = game.author == user
    change_game_status(game, "WAITING")

    return render(request, "home/attente.html", {'game':game, 'is_author':is_author, 'players':players, 'friends':friends})


def openform(request, game_uuid):
    game = get_game_by_uuid(game_uuid)
    login = request.session['login']
    player = get_player_by_game_by_login(game, login)

    f = getFormById(game.form.id)
    questions = getQuestionsByForm(f)
    f.questions = getPossibleAnswersByQuestions(questions)
    change_game_status(game, "IN_PROGRESS")

    return render(request, "home/game.html", {'form': f, 'player': player, 'game': game})


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


def disconnect(request):
    del request.session['login']

    data = {
        'is_valid': True
    }

    return JsonResponse(data)


def creation(request):
    if request.method == 'POST':

        # print(request.POST)
        title = request.POST.get('form_title')
        description = request.POST.get('form_description')
        author = getUserByLogin(request.session['login'])

        form = addQuizzForm(title, author, description)

        nbQuestions = request.POST.get('nbQuestions')

        for i in range(int(nbQuestions)):
            numq = i + 1
            numq = str(numq)

            q_title = request.POST.get('qst_' + numq + '_title')
            q_answerType = request.POST.get('qst_' + numq + '_answerType')
            if q_answerType == "radio":
                q_answerType = "UNIQUE_ANSWER"
            elif q_answerType == "checkbox":
                q_answerType = "QCM"
            elif q_answerType == "text":
                q_answerType = "INPUT"
            q_order = request.POST.get('qst_' + numq + '_order')

            type = getType(q_answerType)
            question = addQuestion(form, type, q_title, q_order)

            q_nbAnswers = request.POST.get('qst_' + numq + '_nbAnswers')

            for j in range(int(q_nbAnswers)):
                numa = str(j + 1)
                numa = str(numa)

                a_value = request.POST.get('qst_' + numq + '_ans_' + numa + '_value')
                if q_answerType == "INPUT":
                    a_correct = True
                else:
                    a_correct = request.POST.get('qst_' + numq + '_ans_' + numa + '_correct')
                    a_correct = True if a_correct == 'on' else False

                addPossibleAnswer(question, a_correct, a_value)

    return render(request, "home/creation.html")


def categories(request):
    return render(request, "home/categories.html")


def resultats(request, game_uuid):
    game = get_game_by_uuid(game_uuid)
    players = get_players_by_game_order_by_score_desc(game)
    print(players)
    return render(request, "home/resultats.html", {'game': game, 'players': players})


def saveUserAnswers(request):
    idplayer = request.POST.get('idplayer')
    player = Player.objects.get(id=idplayer)

    idPA = request.POST.get('idPA')
    valueUser = request.POST.get('value')

    pa = PossibleAnswer.objects.get(id=idPA)
    if pa.question.answer_type.type == "QCM" or pa.question.answer_type.type == "INPUT":
        ua = UserAnswers.objects.filter(player=player, possible_answer=pa)
        if ua.count() >= 1:
            ua = UserAnswers.objects.get(player=player, possible_answer=pa)
            ua.value = valueUser
        else:
            ua = UserAnswers()
            ua.player = player
            ua.possible_answer = pa
            ua.value = valueUser

        ua.save()


    elif pa.question.answer_type.type == "UNIQUE_ANSWER":

        answers = PossibleAnswer.objects.filter(question=pa.question)

        for a in answers:
            ua = UserAnswers.objects.filter(player=player, possible_answer=a)
            if ua.count() >= 1:
                ua = UserAnswers.objects.get(player=player, possible_answer=a)
                ua.delete()

        ua = UserAnswers()
        ua.player = player
        ua.possible_answer = pa
        ua.value = valueUser
        ua.save()

    data = {
        'is_valid': True
    }

    return JsonResponse(data)


def user_profil(request):
    user = getUserByLogin(request.session['login'])

    return render(request, 'dashboard/profil.html', {'user': user})
    if request.method == "POST":

        if request.POST.get('newpwd') == '':

            user = editUserWithoutPwd(user.id, request.POST.get('loginedit'), request.POST.get('emailedit'))

        elif request.POST.get('newpwd') == request.POST.get('newpwd2'):

            if valideUser(user.login, request.POST.get('oldPwd')):

                user = editUserBD(user.id, request.POST.get('loginedit'), request.POST.get('emailedit'), request.POST.get('newpwd'))

            else :

                return render(request, 'dashboard/profil.html', {'user': user, 'active': 0, 'invalid_old_pwd': True, 'invalid_new_pwd': False})

        else :

            return render(request, 'dashboard/profil.html', {'user': user, 'active': 0, 'invalid_old_pwd': False, 'invalid_new_pwd': True})

    return render(request, 'dashboard/profil.html', {'user':user, 'active': 0, 'invalid_old_pwd': False, 'invalid_new_pwd': False})

def user_history(request):

    user = getUserByLogin(request.session['login'])

    players = get_players_by_user_desc_date_game(user)

    return render(request, 'dashboard/history.html', {'active': 1, 'players': players})

def correction(request, player_id):
    player = get_player_by_id(player_id)
    calculate_score(player)
    game = player.game
    questions = getUserAnswersByQuestions(getQuestionsByForm(game.form), player)

    return render(request, 'home/correction.html', {'game': game, 'player': player, 'questions':questions})


def menuCategories(request):
    cats = []
    categories = get_categories()
    for c in categories:
        cats.append({'id':c.id,'label':c.label,'nbQuizz':nbQuizzByCat(c)})

    data = {'cats':cats}
    return JsonResponse(data)