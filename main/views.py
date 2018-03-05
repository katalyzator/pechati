# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from main.models import SliderImage, Product, Application


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


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {"product": product}
    template = 'item.html'

    return render(request, template, context)


@csrf_exempt
def application_view(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']

    Application.objects.create(name=name, phone=phone, email=email)

    return JsonResponse(dict(result=True))
