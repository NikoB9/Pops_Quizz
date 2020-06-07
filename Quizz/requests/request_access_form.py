# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *
from Quizz.requests.request_access_type import *


def is_a_user_allowed_to_access_a_form(user, form):
    if form.is_public:
        return True
    return len(AccessForm.objects.filter(user=user, form=form)) > 0


def is_user_editor_of_a_form(user, form):
    return len(AccessForm.objects.filter(user=user, form=form, access_form_type__type="EDITOR")) > 0


def return_highest_user_acces_to_form(user, form):
    return AccessForm.objects.filter(user=user, form=form)[0].access_form_type.type


def set_access_form_for_a_user(user, form, access_form_type_libelle):
    access_form_type = get_access_form_type(access_form_type_libelle)
    AccessForm.objects.filter(user=user, form=form).delete()
    access_form = AccessForm()
    access_form.user = user
    access_form.form = form
    access_form.access_form_type = access_form_type
    access_form.save()

def get_users_access_form(user, form):
    return AccessForm.objects.select_related('access_form_type').exclude(user=user).filter(form=form)
