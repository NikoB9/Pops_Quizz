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

def addQuestion(form, at, label, order):
    q = Question()
    q.form = form
    q.answer_type = at
    q.label = label
    q.order = order
    q.save()
    return q