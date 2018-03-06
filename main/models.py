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


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    image = models.ImageField(upload_to='images/products', verbose_name='Картинка')
    price = models.CharField(max_length=255, verbose_name='Цена')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Продукты'
        verbose_name = 'Продукт'

    def __unicode__(self):
        return smart_unicode(self.title)


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя', blank=True, null=True)
    surname = models.CharField(max_length=255, verbose_name='Фамилия', blank=True, null=True)
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='E-mail')
    text = models.TextField(verbose_name='Text')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Заявки с сайта'
        verbose_name = 'Заявка'

    def __unicode__(self):
        return smart_unicode(self.phone)


class Review(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    description = models.TextField(max_length=1000, verbose_name='Текст отзыва')
    image = models.ImageField(upload_to='images/reviews', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'

    def __unicode__(self):
        return smart_unicode(self.full_name)


class Advantage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/advantages', verbose_name='Картинка')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = 'Премущества'
        verbose_name = 'Объект'

    def __unicode__(self):
        return smart_unicode(self.title)
