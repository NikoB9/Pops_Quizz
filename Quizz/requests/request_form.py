# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def getAllForms():
    return Form.objects.all()

def getFormById(id):
    return Form.objects.get(id=id)

def addQuizzForm(name, author, description):
    f = Form()
    f.name = name
    f.author = author
    f.description = description
    f.save()
    return f
