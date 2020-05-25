# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.requests.request_question import *
from Quizz.requests.request_user_answers import *
from Quizz.requests.request_possible_answer import *


def get_player_by_login(login):
    return Player.objects.get(login=login)


def get_players_by_game_order_by_score_desc(game):
    return Player.objects.filter(game=game).order_by('-score')


def calculate_score(login):
    player = get_player_by_login(login)
    questions = getQuestionsByForm(player.game.form)
    pa = getPossibleAnswersByQuestions(questions)
    score = 0

    for q in questions:
        if q.question.answer_type.type == "QCM" or q.question.answer_type.type == "UNIQUE_ANSWER":
            for possible_answer in q.answers:
                if(user_selected_possible_answer(possible_answer)):
                    if possible_answer.correct:
                        score += 1
                    else:
                        # decrease score by one if QCM
                        score -= 1 if q.question.answer_type.type == "QCM" else 0
        elif q.question.answer_type.type == "INPUT":
            possible_input_values = []
            for possible_answer in q.answers:
                possible_input_values.append(possible_answer.value.strip())
            if get_input_response_of_a_question(q.question) in possible_input_values:
                score += 1
    player.score = score
    player.save()
