# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def getQuestionsByForm(form):
    return Question.objects.filter(form=form).order_by('order')

def getPossibleAnswersByQuestions(questions):
    Tquestion = []
    for q in questions:
        pa = PossibleAnswer.objects.filter(question=q)
        Tquestion.append({'question':q, 'answers':pa})
    return Tquestion
