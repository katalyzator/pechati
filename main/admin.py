# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import SliderImage, Product, Application, Review, Advantage

admin.site.register(SliderImage)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'timestamp']

    class Meta:
        model = Product


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'timestamp']

    class Meta:
        model = Application


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'description']

    class Meta:
        model = Review


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'timestamp']

    class Meta:
        model = Advantage


admin.site.register(Advantage, AdvantageAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Product, ProductAdmin)
