# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import enum
import uuid as uuid
from datetime import timedelta, datetime

from django.db import models
from django.core import validators


# Class qui hérite directement du modele et qui permet de tracer les données
class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# classe exemple qui herite du timestamp pour un suivi des données
class Functionnalities(TimestampModel):
    name = models.CharField(max_length=255, null=False, blank=False, unique=False)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class User(models.Model):
    login = models.CharField(max_length=255, null=False, blank=False, unique=True)
    mail = models.EmailField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False, unique=False)
    friends = models.ManyToManyField("self", through='Friends', symmetrical=False)
    good_answer = models.IntegerField(null=False,  default=0)
    bad_answer = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.login


class Friends(TimestampModel):
    source = models.ForeignKey(User, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='target')
    accepted = models.BooleanField(default=False)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.source.login + " to " + self.target.login + " is " + ("not" if not self.accepted else "") + " accepted"


class Category(models.Model):
    label = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True, unique=False)

    def __str__(self):
        return self.label + " " + self.description


class Form(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    description = models.TextField(unique=False)
    is_public = models.BooleanField(default=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


# AccessType = [PUBLISHER, EDITOR, CREATOR]
class AccessFormType(models.Model):
    type = models.CharField(max_length=255, null=False, blank=False, unique=False)

    def __str__(self):
        return self.type


class AccessForm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    access_form_type = models.ForeignKey(AccessFormType, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.login + " access to " + self.form.name + " with right " + self.access_form_type.type


# Answer_type = [UNIQUE_ANSWER, QCM, INPUT]
class AnswerType(models.Model):
    type = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.type


class Question(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.CASCADE)
    label = models.TextField(null=False, blank=False, unique=False)
    order = models.IntegerField(null=False, blank=False, unique=False)
    need_correction = models.BooleanField(default=True)

    def __str__(self):
        return self.label


class PossibleAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    value = models.CharField(max_length=255, null=False, blank=False, unique=False)

    def __str__(self):
        return self.value


# GameStatus = [DRAFT, WAITING, IN_PROGRESS, DONE, CANCELLED]
class GameStatus(models.Model):
    type = models.CharField(max_length=255, null=False, blank=False, unique=True)

    def __str__(self):
        return self.type


class Game(models.Model):
    uuid = models.CharField(max_length=255, default="48D67F91", editable=False, unique=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    game_status = models.ForeignKey(GameStatus, on_delete=models.SET_DEFAULT, default=1)
    slot_max = models.IntegerField(blank=False, unique=False, default=0)
    name = models.CharField(max_length=255, null=False, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_real_time = models.BooleanField(default=False)
    is_limited_time = models.BooleanField(default=False)
    is_random_form = models.BooleanField(default=False)
    timer = models.DurationField(default=timedelta())
    time_launched = models.DateTimeField(default=None, null=True)

    def __str__(self):
        return "Game " + self.name


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(null=True, blank=False, unique=False)
    has_answered = models.BooleanField(default=False)
    is_invited = models.BooleanField(default=False)

    def __str__(self):
        return "Player " + self.user.login + " of game " + self.game.name


class UserAnswers(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    possible_answer = models.ForeignKey(PossibleAnswer, on_delete=models.CASCADE)
    value = models.CharField(max_length=255, null=False, blank=False, unique=False)

    def __str__(self):
        return self.value

# class Users(TimestampModel):
# 	role = models.ForeignKey(UserRights, on_delete=models.PROTECT)
# 	first_name = models.CharField(max_length=255, null=False, blank=False, unique=False)
# 	last_name = models.CharField(max_length=255, null=False, blank=False, unique=False)
# 	email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
# 	phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{8,18}$',
# 	 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
# 	phone_number = models.CharField(validators=[phone_regex],
# 		max_length=18, null=True, blank=True, unique=False)
# 	login = models.CharField(max_length=255, null=False, blank=False, unique=False)
# 	password = models.CharField(max_length=1000, null=False, blank=False, unique=False)
#
# 	def __str__(self):
# 		return self.first_name+" "+self.last_name
