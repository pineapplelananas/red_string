from django.contrib import admin

from .models import Candidat, CandidatSession,Category, Choice, Enonce, Question, Session, Test

admin.site.register(Candidat)
admin.site.register(CandidatSession)
admin.site.register(Category)
admin.site.register(Choice)
admin.site.register(Enonce)
admin.site.register(Question)
admin.site.register(Session)
admin.site.register(Test)
