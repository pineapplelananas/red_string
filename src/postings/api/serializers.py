from rest_framework import serializers
from django.core.exceptions import ValidationError

from postings.models import Candidat, CandidatSession, Category, Choice, Question, Enonce, Session, Test
from django.db.models import Q

from django.db import models


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Candidat - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CandidatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidat
        fields = [
            'pk',
            'session_id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'token',
        ]
        read_only_fields = ['']
    
    def validate_email(self, value):
        qs = Candidat.objects.filter(email__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The label of email must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - CandidatSession - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CandidatSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatSession
        fields = [
            'pk',
            'id_candidat',
            'status_session',
            'token',
        ]
        read_only_fields = ['']
    
    def validate_token(self, value):
        qs = CandidatSession.objects.filter(token__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The token of email must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Category - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'pk',
            'label',
            'ponderation',
        ]

        read_only_fields = ['']
    
    def validate_label(self, value):
        qs = Category.objects.filter(label__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The label of category must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Choice - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'pk',
            'id_question',
            'question_type',
            'statement',
            'is_answer',
            'order'
        ]
        read_only_fields = ['user']
    
    def validate_statement(self, value):
        qs = Choice.objects.filter(statement__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The statement of choice must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Enonce - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class EnonceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enonce
        fields = [
            'pk',
            'statement',
            'text',
            'image',
            'audio',
            'video',
            'ponderation',
            'id_category',
            'id_test',
        ]
        read_only_fields = ['']
    
    def validate_statement(self, value):
        qs = Enonce.objects.filter(statement__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The statement of enonce must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Question - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'pk',
            'question_type',
            'statement',
            'text',
            'image',
            'audio',
            'video',
            'id_enonce',
        ]
        read_only_fields = ['']
    
    def validate_statement(self, value):
        qs = Question.objects.filter(statement__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The statement of question must be unique")
        return value


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Session - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = [
            'pk',
            'test_id',
            'label',
            'active',
        ]
        read_only_fields = ['']
    
    def validate_label(self, value):
        qs = Session.objects.filter(label__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The label of Session must be unique")
        return value

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - test - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = [
            'pk',
            'label',
        ]

        read_only_fields = ['']
    
    def validate_label(self, value):
        qs = Test.objects.filter(label__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The label of test must be unique")
        return value

# class UserLoginSerializer(serializers.ModelSerializer):
#     token = models.CharField(blank=True)
#     username = models.CharField( blank=True)
#     email = models.EmailField(blank=True)
#     class Meta:
#         model = User
#         fields = [ 
#             'username',
#             'email',
#             'password',
#             'token',
#         ]
#         extra_kwargs = {"password":
#         {"write_only": True}}

    
#     def validate(self, data):
#         user_obj = None
#         email = data.get("email", None)
#         username = data.get("username", None)
#         password = data["password"]
#         if not email and not username:
#             raise ValidationError("A username or email is requiredto login.")
#         print(user)
#         user = User.objects.filter(
#             Q(email=email) |
#             Q(username=username)).distinct()
#         user = user.exclude(email__isnull=True).exclude(email__iexact='')
#         if user.exists() and user.count() == 1:
#             user_obj = user.first()
#         else:
#             raise ValidationError("This username/email is not valid.")
#         if user_obj:
#             if not user_obj.check_password(password):
#                 raise ValidationError("Incorrect credentials please try again.")
#         data["token"] = "SOME RAMDOM TOKEN"
#         return data
