
from django.db.models import Q
from django.db.models.query import QuerySet
from rest_framework import generics, mixins

from postings.models import Candidat, CandidatSession,Category, Choice, Enonce, Question, Session, Test

from .serializers import CandidatSerializer, CandidatSessionSerializer, ChoiceSerializer, EnonceSerializer, QuestionSerializer, CategorySerializer, SessionSerializer, TestSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Candidat - - - - - -- - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CandidatAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class =CandidatSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        qs = Candidat.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(email__icontains=query)) #|q() .distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CandidatRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = CandidatSerializer

    def get_queryset(self):
        return Candidat.objects.all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - CandidatSession - - - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CandidatSessionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = CandidatSessionSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        qs = CandidatSession.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(token__icontains=query)) #|q() .distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CandidatSessionRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = CandidatSessionSerializer

    def get_queryset(self):
        return CandidatSession.objects.all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Category - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class CategoryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = CategorySerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        qs = Category.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(label__icontains=query)) #|q() .distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Choice - - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class ChoiceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = ChoiceSerializer
    permission_classes = [IsOwnerOrReadOnly]

    #queryset = Choice.objects.all()

    def get_queryset(self):
        qs = Choice.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(statement__icontains=query)) #|q() .distinct
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def perform_create(self, serrializer):
    #     serrializer.save(user=self.request.user)


   
class ChoiceRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = ChoiceSerializer
    #queryset = Choice.objects.all()

    def get_queryset(self):
        return Choice.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Choice.objects.all(pk=pk)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Enonce - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class EnonceAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = EnonceSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Enonce.objects.all()

    def get_queryset(self):
        qs = Question.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(statement__icontains=query))
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

   
class EnonceRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = EnonceSerializer
    #queryset = Enonce.objects.all()

    def get_queryset(self):
        return Enonce.objects.all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - login - - - - - -- - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
@csrf_exempt
@api_view(["GET", "POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username)
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    login(request, user)
    return Response({'token': token.key}, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Question - - - - - - - - - - - - - - - -#
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class QuestionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]
    #queryset = Question.objects.all()

    def get_queryset(self):
        qs = Question.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(statement__icontains=query) | Q(question_type__icontains=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs): 
    #     return self.update(request, *args, **kwargs)
    
    # def patch(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def perform_create(self, serrializer):
    #     serrializer.save(user=self.request.user)


   
class QuestionRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = QuestionSerializer
    #queryset = Question.objects.all()

    def get_queryset(self):
        return Question.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Question.objects.all(pk=pk)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Session - - - - - -- - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class SessionAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = SessionSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        qs = Session.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(label__icontains=query)) #|q() .distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SessionRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = SessionSerializer

    def get_queryset(self):
        return Session.objects.all()

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# - - - - - - - - - - - - - - Test - - - - - -- - - - - - - - - - - #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
class TestAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = TestSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def get_queryset(self):
        qs = Test.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(label__icontains=query)| Q(time__icontains=query)).distinct() #|q() .distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TestRudView(generics.RetrieveUpdateDestroyAPIView):
    pass
    lookup_field =  'pk' # slug, id #url(r'?P<pk>\d+')
    serializer_class = TestSerializer

    def get_queryset(self):
        return Test.objects.all()
