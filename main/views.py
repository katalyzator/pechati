# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from main.models import SliderImage, Product


def index_view(request):
    sliders = SliderImage.objects.all()
    products = Product.objects.all()[:8]

    context = {"sliders": sliders, "products": products}
    template = 'index.html'

    return render(request, template, context)


def contacts_view(request):
    context = {}
    template = 'contacts.html'

    return render(request, template, context)


def goods_view(request):
    products = Product.objects.all()
    context = {"products": products}
    template = 'goods.html'

    return render(request, template, context)
