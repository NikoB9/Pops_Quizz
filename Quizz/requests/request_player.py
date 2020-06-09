# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.requests.request_game import *
from Quizz.requests.request_game_status import get_game_status
from Quizz.requests.request_question import *
from Quizz.requests.request_user import *
from Quizz.requests.request_user_answers import *
from Quizz.requests.request_possible_answer import *
from django.db.models import Avg, Count, Min, Sum


def get_player_by_id(id):
    return Player.objects.get(id=id)


def create_player(game, user, is_invited=False):
    player = Player()
    player.game = game
    player.user = user
    player.score = 0
    player.is_invited = is_invited
    player.has_answered = False
    return player.save()


def user_leave_game(user, game):
    Player.objects.get(user=user, game=game).delete()
    if user.login == game.author.login and get_nb_player_by_game(game) > 0:
        game.author = Player.objects.filter(is_invited=False)[0].user
        game.save()
    if len(Player.objects.filter(game=game)) == 0:
        change_game_status(game, "CANCELLED")


def kick_invited_players(game):
    Player.objects.filter(game=game, is_invited=True).delete()


def get_users_friends_not_in_game(user, game):
    friends = get_users_friends(user)
    return list(filter(lambda u: not is_user_in_game(u, game), friends))


def is_user_invited_in_game(user, game):
    return len(Player.objects.filter(is_invited=True)) > 0


def is_user_in_game(user, game):
    return len(get_players_by_game(game).filter(user=user)) > 0


def get_players_by_game(game):
    return Player.objects.filter(game=game, is_invited=False)

def get_players_waiting_by_game(game):
    return Player.objects.filter(game=game, is_invited=True, has_answered=False)

def get_players_answered_by_game(game):
    return Player.objects.filter(game=game, is_invited=False, has_answered=True)


def get_players_number_of_game(players):
    for player in players:
        player.parties = len(Player.objects.filter(user=player.user, has_answered=True, is_invited=False))
        player.is_author = player.user.login == player.game.author.login
    return players


def is_user_invited_in_game(user, game):
    return len(Player.objects.filter(game=game, user=user, is_invited=True))>0


def is_user_in_waiting_room(game, user):
    return len(Player.objects.filter(user=user, game=game, game__game_status__type="WAITING", is_invited=False)) > 0


def get_player_by_game_by_login(game, login):
    user = User.objects.get(login=login)
    return Player.objects.get(game=game, user=user)

def get_nb_player_invited_or_not_by_game(game):
    return len(Player.objects.filter(game=game))

def get_nb_player_by_game(game):
    return len(get_players_by_game(game))


def get_players_by_game_order_by_score_desc(game):
    return get_players_by_game(game).order_by('-score')


def get_players_by_user_desc_date_game(user):
    return Player.objects.filter(user=user).filter(game__game_status__type="DONE").order_by('-game__created_at')


def get_average_score_player_by_user_and_quizz(user, quizz):
    return Player.objects.filter(user=user, game__form=quizz, game__game_status__type="DONE").aggregate(
        average_user_score=Avg('score'))


def get_average_score_player_by_quizz(quizz):
    return Player.objects.filter(game__form=quizz, game__game_status__type="DONE").aggregate(average_score=Avg('score'))


def get_average_score_player_by_user_and_category(user, cat):
    return Player.objects.filter(user=user, game__form__categories=cat, game__game_status__type="DONE").aggregate(
        average_user_score=Avg('score'))


def get_average_score_player_by_category(cat):
    return Player.objects.filter(game__form__categories=cat, game__game_status__type="DONE").aggregate(
        average_score=Avg('score'))


def get_average_total_score_by_user(user):
    return Player.objects.filter(user=user, game__game_status__type="DONE").aggregate(average_user_score=Avg('score'))


def get_average_total_score():
    return Player.objects.filter(game__game_status__type="DONE").aggregate(average_score=Avg('score'))


def all_player_have_answered_a_game(game):
    return len(Player.objects.filter(game=game).exclude(has_answered=True, is_invited=False)) == 0


def player_waiting_game(user):
    return Player.objects.filter(user=user, game__game_status__type="WAITING", is_invited=False)


def calculate_score(player):
    questions = getPossibleAnswersByQuestions(getQuestionsByForm(player.game.form))
    score = 0
    for q in questions:
        if q['question'].answer_type.type == "UNIQUE_ANSWER":
            for possible_answer in q["answers"]:
                if len(user_selected_possible_answer(possible_answer, player)) > 0:
                    if possible_answer.correct:
                        score += 1
                        user_add_good_answer(player.user)
                    else:
                        user_add_bad_answer(player.user)
        elif q['question'].answer_type.type == "QCM":
            for possible_answer in q['answers']:
                uas = user_selected_possible_answer(possible_answer, player)
                if len(uas) > 0 and uas[0].value == "1":
                    if possible_answer.correct:
                        score += 1
                        user_add_good_answer(player.user)
                    else:
                        # decrease score by one if wrong
                        score -= 1
                        user_add_bad_answer(player.user)
        elif q['question'].answer_type.type == "INPUT":
            if is_input_response_have_user_answer(q['question'], player):
                possible_input_values = []
                for possible_answer in q['answers']:
                    possible_input_values.append(possible_answer.value.strip().upper())
                user_answer_input = get_input_response_by_question_by_player(q['question'], player)
                if user_answer_input.value.strip().upper() in possible_input_values:
                    score += 1
                    user_add_good_answer(player.user)
                else:
                    user_add_bad_answer(player.user)
    player.score = score
    player.has_answered = True
    player.save()

    if all_player_have_answered_a_game(player.game):
        change_game_status(player.game, "DONE")

def add_question_to_player(id_p, id_q):
    p = Player.objects.get(id=id_p)
    p.questions_answered.add(Question.objects.get(id=id_q))
    return True