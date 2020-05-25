# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

from django.contrib.auth import hashers

def createUserBD(login, mail, password):
    user = User()
    user.login = login
    user.mail = mail
    user.password = hashers.make_password(password)
    user.save()

def editUserBD(id, login, mail, password):
    user = User.objects.get(id=id)
    user.login = login
    user.mail = mail
    user.password = hashers.make_password(password)
    user.save()
    return user

def editUserWithoutPwd(id, login, mail):
    user = User.objects.get(id=id)
    user.login = login
    user.mail = mail
    user.save()
    return user

def getUserByLogin(login):
    return User.objects.get(login = login)

def getAllUsers():
    return User.objects.all()

def loginExist(login):
	user = User.objects.filter(login=login)
	user_valid = user.count() >= 1
	return user_valid

def emailExist(mail):
	user = User.objects.filter(mail=mail)
	user_valid = user.count() >= 1
	return user_valid


def valideUser(login, pwd):
	user = User.objects.get(login=login)
	user_valid = hashers.check_password(pwd, user.password)
	return user_valid