# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.requests.request_game import change_game_status
from Quizz.requests.request_game_status import get_game_status
from Quizz.requests.request_question import *
from Quizz.requests.request_user_answers import *
from Quizz.requests.request_possible_answer import *
from django.db.models import Avg, Count, Min, Sum

def get_player_by_id(id):
    return Player.objects.get(id=id)


def create_player(game, user):
    player = Player()
    player.game = game
    player.user = user
    player.score = 0
    player.has_answered = False
    player.save()


def user_leave_game(user, game):
    Player.objects.get(user=user, game=game).delete()
    if len(Player.objects.filter(game=game)) == 0:
        change_game_status(game, "CANCELLED")


def is_user_in_game(user, game):
    print(Player.objects.filter(user=user, game=game))
    return len(Player.objects.filter(user=user, game=game)) > 0

def get_players_by_game(game):
    return Player.objects.filter(game=game)


def get_players_number_of_game(players):
    for player in players:
        player.parties = len(Player.objects.filter(user=player.user, has_answered=True))
    return players


def get_player_by_game_by_login(game, login):
    user = User.objects.get(login=login)
    return Player.objects.get(game=game, user=user)


def get_nb_player_by_game(game):
    return len(Player.objects.filter(game=game))


def get_players_by_game_order_by_score_desc(game):
    return Player.objects.filter(game=game).order_by('-score')


def get_players_by_user_desc_date_game(user):
    return Player.objects.filter(user=user).filter(game__game_status__type="DONE").order_by('-game__created_at')

def get_average_score_player_by_user_and_quizz(user,quizz):
    return Player.objects.filter(user=user, game__form=quizz, game__game_status__type="DONE").aggregate(average_user_score=Avg('score'))
def get_average_score_player_by_quizz(quizz):
    return Player.objects.filter(game__form=quizz, game__game_status__type="DONE").aggregate(average_score=Avg('score'))

def get_average_score_player_by_user_and_category(user,cat):
    return Player.objects.filter(user=user, game__form__categories=cat, game__game_status__type="DONE").aggregate(average_user_score=Avg('score'))
def get_average_score_player_by_category(cat):
    return Player.objects.filter(game__form__categories=cat, game__game_status__type="DONE").aggregate(average_score=Avg('score'))

def get_average_total_score_by_user(user):
    return Player.objects.filter(user=user, game__game_status__type="DONE").aggregate(average_user_score=Avg('score'))
def get_average_total_score():
    return Player.objects.filter(game__game_status__type="DONE").aggregate(average_score=Avg('score'))

def all_player_have_answered_a_game(game):
    return len(Player.objects.filter(game=game).exclude(has_answered=True)) == 0


def player_waiting_game(user):
    return Player.objects.filter(user=user, game__game_status__type="WAITING")


def calculate_score(player):
    questions = getPossibleAnswersByQuestions(getQuestionsByForm(player.game.form))
    score = 0
    for q in questions:
        if q['question'].answer_type.type == "UNIQUE_ANSWER":
            for possible_answer in q["answers"]:
                if len(user_selected_possible_answer(possible_answer, player)) > 0:
                    if possible_answer.correct:
                        score += 1
        elif q['question'].answer_type.type == "QCM":
            for possible_answer in q['answers']:
                uas = user_selected_possible_answer(possible_answer, player)
                if len(uas) > 0 and uas[0].value == "1":
                    if possible_answer.correct:
                        score += 1
                    else:
                        # decrease score by one if wrong
                        score -= 1
        elif q['question'].answer_type.type == "INPUT":
            possible_input_values = []
            for possible_answer in q['answers']:
                possible_input_values.append(possible_answer.value.strip())
            user_answer_input = get_input_response_by_question_by_player(q['question'], player)
            if user_answer_input.value.strip() in possible_input_values:
                score += 1
    player.score = score
    player.has_answered = True
    player.save()

    if all_player_have_answered_a_game(player.game):
        change_game_status(player.game, "DONE")
