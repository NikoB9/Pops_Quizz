# Create your views here.
# -*- coding: utf-8 -*-
from itertools import chain

from Quizz.models import *

from django.contrib.auth import hashers


def remove_friendship(user_1, user_2):
    get_relationship_between_users(user_1, user_2).delete()


def answer_friendship_request(is_accepted, user_1, user_2):
    if is_accepted:
        relationship = get_relationship_between_users(user_1, user_2)
        relationship.accepted = True
        relationship.save()
        print("relationship ok")
    else:
        remove_friendship(user_1, user_2)
        print("relationship nok")


def two_users_have_relationship(user_1, user_2):
    return len(Friends.objects.filter(source=user_1, target=user_2)) + len(Friends.objects.filter(source=user_2, target=user_1)) > 0


def get_relationship_between_users(user_1, user_2):
    relationship = Friends()
    if len(Friends.objects.filter(source=user_1, target=user_2)) > 0:
        relationship = Friends.objects.get(source=user_1, target=user_2)
    else:
        relationship = Friends.objects.get(source=user_2, target=user_1)
    return relationship


def relationship_accepted(user_1, user_2):
    if not two_users_have_relationship(user_1, user_2):
        return False
    return get_relationship_between_users(user_1, user_2).accepted


def add_friend_request(user_source, user_target):
    relationship = Friends()
    relationship.source = user_source
    relationship.target = user_target
    relationship.accepted = False
    return relationship.save()


def get_friends_relationship_of_user(user):
    friends_source = Friends.objects.filter(source=user, accepted=True)
    friend_target = Friends.objects.filter(target=user, accepted=True)
    return list(chain(friends_source, friend_target))


def get_waiting_friends_relationship_of_user(user):
    friends_source = Friends.objects.filter(source=user, accepted=False)
    friend_target = Friends.objects.filter(target=user, accepted=False)
    return list(chain(friends_source, friend_target))
