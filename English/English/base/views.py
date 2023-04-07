from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from base.models import CategoryWord, Word, IrregularVerbs, Themes


class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Learn'
        context['tremes'] = Themes.objects.all()
        print(context['tremes'])
        return context








