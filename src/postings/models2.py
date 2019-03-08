# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.urls import reverse

QUESTION_TYPE_CHOICES = (
    (1, _("Choix multiple")),
    (2, _("Choix unique")),
    (3, _("Maybe relevant")),
    (4, _("Text à trou")),
)

class Category(models.Model):
    label = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.label)


class Session(models.Model):
    test_id = models.OneToOneField('Test', blank=True, on_delete=models.CASCADE, null=True, default=None)
    label = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.label)

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    token = models.CharField(max_length=200)
    session_id = models.ForeignKey('Session', blank=True, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.email)


class Question(models.Model):
    question_type = models.ForeignKey('QuestionType', blank=True, on_delete=models.CASCADE,null=True, default=None)
    body = models.CharField(max_length=100)
    test_id = models.ManyToManyField('Test', blank=True, default=None)
    category_id = models.ForeignKey('Category', blank=True, on_delete=models.CASCADE,null=True, default=None)
    answer_ids = models.ManyToManyField('Answer', blank=True, default=None)

    def __str__(self):
        return str(self.body)

    @property
    def owner(self):
        return self.user

class Test(models.Model):
    session_id = models.OneToOneField('Session', blank=True, on_delete=models.CASCADE, null=True, default=None)
    label = models.CharField(max_length=100)
    question_ids = models.ManyToManyField('Question', blank=True, default=None)

    def __str__(self):
        return str(self.label)

class Answer(models.Model):
   question_type = models.ForeignKey('QuestionType', blank=True, on_delete=models.CASCADE, null=True,default=None)
   question_id = models.OneToOneField('Question', blank=True, on_delete=models.CASCADE, null=True,default=None)
   body = models.CharField(max_length=200)
   is_answer = models.BooleanField()
   orde = models.IntegerField(blank=True, null=True)

   def __str__(self):
       return str(self.body)

class QuestionType(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return str(self.label)
