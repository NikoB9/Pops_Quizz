# Create your views here.
# -*- coding: utf-8 -*-
import random

from Quizz.models import *
from Quizz.requests.request_access_form import *
from Quizz.requests.request_categories import *


def getAllForms(user=None):
    if user is None:
        return Form.objects.filter(is_public=True)
    forms = []
    for form in Form.objects.all():
        if form.author == user or is_user_editor_of_a_form(user, form):
            forms.append(form)
            form.is_author = form.author == user

    return forms


def getAllFormsAccessUser(user):
    forms = []
    for form in Form.objects.all():
        if form.author == user or form.is_public or is_user_editor_of_a_form(user, form):
            forms.append(form)
    return forms


def delete_form(form_id):
    Form.objects.get(id=form_id).delete()


def getFormById(id):
    return Form.objects.get(id=id)


def nbQuizzByCat(cat, user=None):
    return len(getQuizzByCat(cat, user))


def getQuizzByCat(cat, user):
    if user is None:
        return Form.objects.filter(is_public=True, categories=cat)
    return list(filter(lambda form: is_a_user_allowed_to_access_a_form(user, form), Form.objects.filter(categories=cat)))


def get_random_forms_by_cat(cat, user):
    forms = list(filter(lambda form: is_a_user_allowed_to_access_a_form(user, form), Form.objects.filter(categories=cat)))
    return random.choice(forms)


def addQuizzForm(name, author, description, categories_ids):
    f = Form()
    f.name = name
    f.author = author
    f.description = description
    f.is_older_version = False
    f.is_deleted = False
    f.save()
    for cat_id in categories_ids:
        f.categories.add(get_category_by_id(cat_id))
    f.save()
    set_access_form_for_a_user(author, f, "CREATOR")
    return f
