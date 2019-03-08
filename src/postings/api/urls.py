from django.conf.urls import url

from .views import QuestionRudView, QuestionAPIView, ChoiceRudView, ChoiceAPIView, CategoryAPIView, CategoryRudView, EnonceAPIView, EnonceRudView, TestAPIView, TestRudView, SessionAPIView, SessionRudView, CandidatAPIView, CandidatRudView,login, sample_api
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^question/$', QuestionAPIView.as_view(), name='post-create'),
    url(r'^question/(?P<pk>\d+)/$', QuestionRudView.as_view(), name='post-rud'),
    url(r'^choice/$', ChoiceAPIView.as_view(), name='post-create'),
    url(r'^choice/(?P<pk>\d+)/$', ChoiceRudView.as_view(), name='post-rud'),
    url(r'^enonce/$', EnonceAPIView.as_view(), name='post-create'),
    url(r'^enonce/(?P<pk>\d+)/$', EnonceRudView.as_view(), name='post-rud'),
    url(r'^category/$', CategoryAPIView.as_view(), name='post-create'),
    url(r'^category/(?P<pk>\d+)/$', CategoryRudView.as_view(), name='post-rud'),
    url(r'^session/$', SessionAPIView.as_view(), name='post-create'),
    url(r'^session/(?P<pk>\d+)/$', SessionRudView.as_view(), name='post-rud'),
    url(r'^test/$', TestAPIView.as_view(), name='post-create'),
    url(r'^test/(?P<pk>\d+)/$', TestRudView.as_view(), name='post-rud'),
    url(r'^candidat/$', CandidatAPIView.as_view(), name='post-create'),
    url(r'^candidat/(?P<pk>\d+)/$', CandidatRudView.as_view(), name='post-rud'),
    url(r'login/$', login),
    url(r'sampleapi/$', sample_api),
    url(r'auth/$', obtain_auth_token, name='api_token_auth'),
]
