# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def get_game_status(libelle):
    game_status = GameStatus.objects.get(type=libelle)
    return game_status