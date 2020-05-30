# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *


def get_access_form_type(access_form_type):
    access_form_type = AccessFormType.objects.get(type=access_form_type)
    return access_form_type
