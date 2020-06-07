# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.requests.request_user import *
from Quizz.requests.request_game_status import get_game_status
from Quizz.requests.request_form import *


def get_games_invited_of_user(user):
    games = []
    for player in Player.objects.filter(user=user, is_invited=True):
        games.append(player.game)
    return games


def get_waiting_games(user):
    games = []
    for player in Player.objects.filter(user=user, game__game_status__type="WAITING"):
        games.append(player.game)
    return games


def get_games_in_progress_of_user(user):
    games = []
    for player in Player.objects.filter(user=user, is_invited=False, game__game_status__type="IN_PROGRESS"):
        player.game.player_playing = len(Player.objects.filter(game=player.game, is_invited=False, has_answered=True))
        player.game.player_max = len(Player.objects.filter(game=player.game, is_invited=False))
        player.game.not_answered = len(Player.objects.filter(user=user, game=player.game, has_answered=False)) > 0
        games.append(player.game)
    return games


def get_game_waiting_of_user(user):
    return Player.objects.get(user=user, game__game_status__type="WAITING", is_invited=False).game


def get_all_game():
    return Game.objects.all()


def get_game_by_uuid(uuid):
    return Game.objects.get(uuid=uuid)


def get_game_by_id(id):
    return Game.objects.get(id=id)


def change_game_status(game, status):
    new_status = get_game_status(status)
    game.game_status = new_status
    game.save()
    return game


def getGamesToJoinByForm(form):
    return Game.objects.filter(form=form, is_public=True, game_status__type="WAITING")


def edit_game(game_uuid, game_name, slot_max, is_public, is_real_time, game_status_libelle=None):
    game = get_game_by_uuid(game_uuid)
    game.name = game_name
    game.slot_max = slot_max
    game.is_public = is_public
    game.is_real_time = is_real_time
    game.save()
    if game_status_libelle is not None:
        game = change_game_status(game, game_status_libelle)
    return game


def create_gameBD(form_id, user_name, name, is_public, max_player, is_real_time, is_random_form=False,
                  game_status="WAITING"):
    author = getUserByLogin(user_name)
    form = getFormById(form_id)
    game_status = get_game_status(game_status)

    new_game = Game()
    new_game.form = form
    new_game.name = name
    new_game.author = author
    new_game.is_public = is_public
    new_game.slot_max = max_player
    new_game.is_real_time = is_real_time
    new_game.game_status = game_status
    new_game.uuid = str(uuid.uuid4())[:8].upper()
    new_game.is_random_form = is_random_form
    new_game.save()
    return new_game
