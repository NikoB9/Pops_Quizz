# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def getType(libelle):
    at = AnswerType.objects.get(type=libelle)
    return at