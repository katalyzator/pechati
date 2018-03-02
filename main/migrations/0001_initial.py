# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438')),
                ('image', models.ImageField(upload_to='slider/images', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0443',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
            },
        ),
    ]
