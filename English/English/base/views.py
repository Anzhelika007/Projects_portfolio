from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from base.models import Category, Word, IrregularVerbs, Themes, LinkRender


class IndexView(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Learn'
        context['tremes'] = Themes.objects.order_by('priority').all()
        context['link'] = LinkRender.objects.all()
        print(context['tremes'])
        return context


class StartTest(TemplateView):
    template_name = 'test/start_test.html'
    title = 'Start test'


class StartTestVerbs(TemplateView):
    template_name = 'test/start_test_irregular_verbs.html'
    title = 'Start test verbs'



