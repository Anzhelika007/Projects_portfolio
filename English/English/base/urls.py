from django.contrib import admin
from django.urls import path, include
from base.views import IndexView

app_name = 'base'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]