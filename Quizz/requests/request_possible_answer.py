# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def addPossibleAnswer(question, correct, value):
    a = PossibleAnswer()
    a.question = question
    a.correct = correct
    a.value = value
    a.save()
    return a