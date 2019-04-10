# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

QUESTION_TYPE_CHOICES = (
    (1, _("Choix multiple")),
    (2, _("Choix unique")),
    (3, _("Maybe relevant")),
    (4, _("Text à trou")),
)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Candidat - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Candidat(models.Model):
    email = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    token = models.CharField(max_length=500)
    session_id = models.ForeignKey('Session', blank=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.email)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - CandidatSession - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CandidatSession(models.Model):
    id_candidat = models.ForeignKey('Candidat', on_delete=models.CASCADE)
    status_session = models.BooleanField()
    token = models.CharField(max_length=500)

    def __str__(self):
            return str(self.id_candidat)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Category - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Category(models.Model):
    label = models.CharField(max_length=100)
    ponderation = models.IntegerField(default=1)

    def __str__(self):
        return str(self.label)
    
    @property
    def owner(self):
        return self.user

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Choice - - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Choice(models.Model):
    id_question = models.ForeignKey('Question', blank=True, on_delete=models.CASCADE, null=True,default=None)
    question_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES, default=1)   
    statement = models.CharField(max_length=500)
    is_answer = models.BooleanField()
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.statement)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Enonce - - - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Enonce(models.Model):
    statement = models.TextField()
    text = models.TextField( blank=True, null=True)
    image = models.TextField( blank=True, null=True)
    audio = models.TextField( blank=True, null=True)
    video = models.TextField( blank=True, null=True)
    ponderation = models.IntegerField(default=1)
    id_category = models.ForeignKey('Category', on_delete=models.CASCADE)
    id_test = models.ForeignKey('Test', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.statement)

    @property
    def owner(self):
        return self.user
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Question - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Question(models.Model):
    question_type = models.IntegerField(choices=QUESTION_TYPE_CHOICES, default=1)   
    text = models.TextField( blank=True, null=True)
    image = models.TextField( blank=True, null=True)
    audio = models.TextField( blank=True, null=True)
    video = models.TextField( blank=True, null=True)
    statement = models.TextField( blank=True, null=True)
    id_enonce = models.ForeignKey('Test', on_delete=models.CASCADE)
   
    def __str__(self):
        return str(self.statement)

    @property
    def owner(self):
        return self.user

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Session - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Session(models.Model):
    test_id = models.ForeignKey('Test', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    active = models.BooleanField()

    def __str__(self):
        return str(self.label)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Test - - - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class Test(models.Model):
    label = models.CharField(max_length=100)
    time = models.IntegerField(null=True)

    def __str__(self):
        return str(self.label)
    
    @property
    def owner(self):
        return self.user
