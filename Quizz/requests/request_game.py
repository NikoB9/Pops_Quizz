# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *


def get_all_game():
    return Game.objects.all()

def create_game(form_id, user_name, name, is_public, max_player):
    author = getUserByLogin(user_name)
    form = getFormsById(form_id)
    new_game = Game()
    new_game.form = form
    new_game.name = name
    new_game.author = author
    new_game.is_public = is_public
    new_game.slot_max = max_player
    return new_game.save()
