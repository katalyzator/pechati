# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import SliderImage, Product

admin.site.register(SliderImage)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'timestamp']

    class Meta:
        model = Product
