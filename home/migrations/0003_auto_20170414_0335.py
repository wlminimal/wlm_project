# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-14 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='main_image',
            field=models.ForeignKey(help_text='main image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='main_title',
            field=models.TextField(default='Hello World'),
        ),
    ]
