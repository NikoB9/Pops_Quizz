# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *
from Quizz.requests.request_game_status import get_game_status
from Quizz.requests.request_user import *
from Quizz.requests.request_form import *


def get_all_game():
    return Game.objects.all()

def get_game_by_uuid(uuid):
    return Game.objects.get(uuid=uuid)

def create_gameBD(form_id, user_name, name, is_public, max_player, game_status="WAITING"):
    author = getUserByLogin(user_name)
    form = getFormsById(form_id)
    game_status = get_game_status(game_status)

    new_game = Game()
    new_game.form = form
    new_game.name = name
    new_game.author = author
    new_game.is_public = is_public
    new_game.slot_max = max_player
    new_game.game_status = game_status
    new_game.uuid = str(uuid.uuid4())[:8].upper()
    new_game.save()
    return new_game
