# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *
from Quizz.requests.request_game_status import get_game_status
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *


def get_players_by_game_order_by_score_desc(game):
    return Player.objects.filter(game=game).order_by('-score')

