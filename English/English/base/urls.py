from django.contrib import admin
from django.urls import path, include
from base.views import IndexView, StartTest, StartTestVerbs

app_name = 'base'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('start/', StartTest.as_view(), name='start'),
    path('start-verbs/', StartTestVerbs.as_view(), name='start-verbs'),
]