# Create your views here.
# -*- coding: utf-8 -*-
from .models import *

def getAllForms():
    return Form.objects.all()

def getFormsById(id):
    return Form.objects.get(id=id)