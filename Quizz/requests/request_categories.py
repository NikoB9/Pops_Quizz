# Create your views here.
# -*- coding: utf-8 -*-
from Quizz.models import *

def get_category_by_id(idCat):
    cat = Category.objects.get(id=idCat)
    return cat

def get_category_by_label(label):
    return Category.objects.get(label=label)

def get_categories():
    cats = Category.objects.all().order_by('label')
    return cats