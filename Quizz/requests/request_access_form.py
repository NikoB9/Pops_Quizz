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
    return AccessForm.objects.filter(user=user, form=form)[0]


def user_form_right(user, form, exclude_author=True):
    if not len(AccessForm.objects.filter(user=user, form=form)) > 0:
        return "NONE"
    return return_highest_user_acces_to_form(user, form)


def remove_access_form_for_a_user(user, form):
    access = user_form_right(user, form)
    if access != "NONE":
        access.delete()


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


def transfer_old_form_right_to_another(old_form, new_form):
    old_access = AccessForm.objects.filter(form=old_form)
    AccessForm.objects.filter(form=new_form).delete()
    for access in old_access:
        set_access_form_for_a_user(access.user, new_form, access.access_form_type.type)
