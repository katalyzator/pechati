# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from main.models import SliderImage


def index_view(request):
    sliders = SliderImage.objects.all()
    context = {"sliders": sliders}
    template = 'index.html'

    return render(request, template, context)


def contacts_view(request):
    context = {}
    template = 'contacts.html'

    return render(request, template, context)


def goods_view(request):
    context = {}
    template = 'goods.html'

    return render(request, template, context)
