# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class SliderImage(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название картинки')
    image = models.ImageField(upload_to='slider/images', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Слайдер'
        verbose_name = 'Картинку'

    def __unicode__(self):
        return smart_unicode(self.title)
