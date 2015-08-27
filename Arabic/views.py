# coding=utf-8
from django.shortcuts import render
from django.utils import translation
from django.utils.translation import ugettext as _

# Create your views here.
from Arabic.models import TransModel


def view_arabic(request):
    text_ar = _(u'نعم')
    text_en = _(u'Yes')

    context = {}
    context['text_arabic'] = text_ar
    context['text_english'] = text_en

    language = translation.get_language_from_request(request)
    context['lang'] = language

    return render(request, 'a.html', context)


def list_view(request):
    context = {}
    language = translation.get_language_from_request(request)
    context['lang'] = language

    context['list'] = TransModel.objects.all()

    return render(request, 'list.html', context)

