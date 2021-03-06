# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-06 05:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('description', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435')),
                ('image', models.ImageField(upload_to='images/advantages', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u041e\u0431\u044a\u0435\u043a\u0442',
                'verbose_name_plural': '\u041f\u0440\u0435\u043c\u0443\u0449\u0435\u0441\u0442\u0432\u0430',
            },
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': '\u041e\u0442\u0437\u044b\u0432', 'verbose_name_plural': '\u041e\u0442\u0437\u044b\u0432\u044b'},
        ),
    ]
