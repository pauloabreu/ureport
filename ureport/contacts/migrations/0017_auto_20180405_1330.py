# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 13:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("contacts", "0016_auto_20180314_1317")]

    operations = [
        migrations.RemoveField(model_name="contact", name="backend"),
        migrations.RemoveField(model_name="contactfield", name="backend"),
    ]
