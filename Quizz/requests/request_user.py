# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

from django.contrib.auth import hashers

def createUser(login, mail, password):
    user = User()
    user.login = login
    user.mail = mail
    user.password = hashers.make_password(password)
    user.save()

def getUserByLogin(login):
    return User.objects.get(login = login)

def getAllUsers():
    return User.objects.all()
