# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 05:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terapia',
            fields=[
                ('id_terapia', models.IntegerField(primary_key=True, serialize=False)),
                ('id_paciente', models.IntegerField()),
                ('id_cita', models.IntegerField()),
                ('recibida', models.CharField(max_length=2)),
            ],
        ),
    ]
