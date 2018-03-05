# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import SliderImage, Product, Application

admin.site.register(SliderImage)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'timestamp']

    class Meta:
        model = Product


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'timestamp']

    class Meta:
        model = Application


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Product, ProductAdmin)
