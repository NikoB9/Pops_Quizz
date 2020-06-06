# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

from django.contrib.auth import hashers

from Quizz.requests.request_friends import *


def get_users_friends(user):
    friends = get_friends_relationship_of_user(user)
    return get_users_from_friends_list_not_user_param(friends, user)


def get_waiting_sent_users_friend(user):
    relationships = get_waiting_friends_relationship_of_user(user)
    friends = list(filter(lambda relationship: relationship.source.login == user.login, relationships))
    return get_users_from_friends_list_not_user_param(friends, user)


def get_waiting_received_users_friend(user):
    relationships = get_waiting_friends_relationship_of_user(user)
    friends = list(filter(lambda relationship: relationship.target.login == user.login, relationships))
    return get_users_from_friends_list_not_user_param(friends, user)


def get_users_from_friends_list_not_user_param(friends, user_to_exclude):
    user_friends = []
    for relationship in friends:
        if relationship.source.login != user_to_exclude.login:
            user_friends.append(relationship.source)
        else:
            user_friends.append(relationship.target)
    return user_friends


def get_n_first_users_like_with_a_user_to_exclude(regex, user, number_of_user=5):
    return User.objects.exclude(login=user.login).filter(login__icontains=regex)[:number_of_user]


def createUserBD(login, mail, password):
    user = User()
    user.login = login
    user.mail = mail
    user.good_answer = 0
    user.bad_answer = 0
    user.password = hashers.make_password(password)
    user.save()


def user_add_good_answer(user):
    user.good_answer += 1
    user.save()


def user_add_bad_answer(user):
    user.bad_answer += 1
    user.save()


def editUserBD(id, login, mail, password):
    user = User.objects.get(id=id)
    user.login = login
    user.mail = mail
    if password is not None:
        user.password = hashers.make_password(password)
    user.save()
    return user


def editUserWithoutPwd(id, login, mail):
    return editUserBD(id, login, mail, None)


def getUserByLogin(login):
    return User.objects.get(login=login)


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
