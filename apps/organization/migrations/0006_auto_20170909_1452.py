# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-09 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_auto_20170909_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='\u8bfe\u7a0b\u6570'),
        ),
        migrations.AddField(
            model_name='courseorg',
            name='student_nums',
            field=models.IntegerField(default=0, verbose_name='\u5b66\u4e60\u4eba\u6570'),
        ),
    ]