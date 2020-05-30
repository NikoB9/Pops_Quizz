# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *
from Quizz.requests.request_access_form import *


def getAllForms(user=None):
    if user is None:
        return Form.objects.all()
    return list(filter(lambda form: is_a_user_allowed_to_access_a_form(user, form), Form.objects.all()))


def getFormById(id):
    return Form.objects.get(id=id)


def nbQuizzByCat(cat, user):
    return len(getQuizzByCat(cat, user))


def getQuizzByCat(cat, user):
    if user is None:
        return getAllForms.filter(categories=cat)
    return list(filter(lambda form: is_a_user_allowed_to_access_a_form(user, form), Form.objects.filter(categories=cat)))


def addQuizzForm(name, author, description):
    f = Form()
    f.name = name
    f.author = author
    f.description = description
    f.save()
    set_access_form_for_a_user(author, f, "CREATOR")
    return f
