# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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

# Droits utilisateur
class UserRights(TimestampModel):
	rule = models.IntegerField(null=False, blank=False, unique=False)
	libelle = models.CharField(max_length=255, null=False, blank=False, unique=True)
	def __str__(self):
		return self.libelle

# utilisateur (pas mal d'exemple avec ça)
#exemple relation clé étrangère	

class Users(TimestampModel):
	role = models.ForeignKey(UserRights, on_delete=models.PROTECT)
	first_name = models.CharField(max_length=255, null=False, blank=False, unique=False)
	last_name = models.CharField(max_length=255, null=False, blank=False, unique=False)
	email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
	phone_regex = validators.RegexValidator(regex=r'^\+?1?\d{8,18}$',
	 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.") 
	phone_number = models.CharField(validators=[phone_regex], 
		max_length=18, null=True, blank=True, unique=False)
	login = models.CharField(max_length=255, null=False, blank=False, unique=False)
	password = models.CharField(max_length=1000, null=False, blank=False, unique=False)


	def __str__(self):
		return self.first_name+" "+self.last_name
	
