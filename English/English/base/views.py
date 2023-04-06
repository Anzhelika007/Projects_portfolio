from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from base.models import CategoryWord, Word, IrregularVerbs


class IndexView(TemplateView):
    template_name = 'base/index.html'
    title = 'Learn'


# class CategoryWordView(ListView):
#     model = CategoryWord
#     template_name = 'base/list.html'
#     paginate_by = 9
#     title = 'Store - Каталог'



