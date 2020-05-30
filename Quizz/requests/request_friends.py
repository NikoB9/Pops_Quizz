# Create your views here.
# -*- coding: utf-8 -*-
from itertools import chain

from Quizz.models import *

from django.contrib.auth import hashers


def get_friends_of_user(user):
    friends_source = Friends.objects.filter(source=user, accepted=True)
    friend_target  = Friends.objects.filter(target=user, accepted=True)
    return list(chain(friends_source,friend_target))

