# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 17:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20160905_0046'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='_book',
            new_name='fk_book',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='_user',
            new_name='fk_user',
        ),
    ]
