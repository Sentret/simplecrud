# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170913_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='monitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='app.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Group'),
        ),
    ]
